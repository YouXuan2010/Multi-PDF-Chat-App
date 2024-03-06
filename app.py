import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS  # Saved in local directory not cloud
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from htmlTemplates import css, bot_template, user_template
from langchain_community.llms import HuggingFaceHub

def get_pdf_text(pdf_docs):
    raw_text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            raw_text += page.extract_text()
    return raw_text

def get_chunks_of_text(raw_text):
    # Chunk overlap to protect against splitting words in halfway
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
    text_chunks = text_splitter.split_text(raw_text)
    return text_chunks

def get_vector_store(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vector_store = FAISS.from_texts(text_chunks, embeddings)
    return vector_store

def get_conversation_chain(vector_store):
    # model_name="gpt-3.5-turbo"
    llm = ChatOpenAI()

    # Can be changed to other text-to-text generation models @ https://huggingface.co/models?pipeline_tag=text2text-generation&sort=trending
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever(), memory=memory)
    return conversation_chain

def handle_user_input(user_question):
    bot_response = st.session_state.conversation_chain({'question': user_question})
    st.session_state.chat_history = bot_response['chat_history']
    
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    load_dotenv()
    st.set_page_config(page_title='Chat with multiple PDFs', page_icon=':books:')

    st.write(css, unsafe_allow_html=True)

    # Initialize session state
    if "conversation_chain" not in st.session_state:
        st.session_state.conversation_chain = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    if "pdf_docs" not in st.session_state:
        st.session_state.pdf_docs = None

    st.header('Chat with multiple PDFs :books:')
    # user_question = st.text_input('Ask a question about your documents: ')

    with st.form("Question", clear_on_submit=True):
        user_question = st.text_input('Ask a question about your documents: ')
        submitted = st.form_submit_button("Submit")
        if submitted:
            pdf_docs = st.session_state.pdf_docs if "pdf_docs" in st.session_state else None
            if pdf_docs:
                handle_user_input(user_question)
            else:
                st.warning('Please upload your PDFs first in order to start the chat.')

    # with st.form("Question",clear_on_submit=True):
    #     user_question = st.text_input('Ask a question about your documents: ')
    #     submitted = st.form_submit_button("Submit")
    #     if submitted:
    #         handle_user_input(user_question)

    # if user_question:
    #     handle_user_input(user_question)

    with st.sidebar:
        st.subheader('Your documents')
        pdf_docs = st.file_uploader('Upload your PDFs here and click on "Process"', accept_multiple_files=True)
        if st.button('Process'):
            if pdf_docs:
                with st.spinner('Processing your documents...'):
                    # Get pdf text
                    raw_text = get_pdf_text(pdf_docs)

                    # Get text chunks in form of list
                    text_chunks = get_chunks_of_text(raw_text)

                    # Create vector store
                    vector_store = get_vector_store(text_chunks)
                    st.write('Done! Your documents are ready to be queried.')

                    st.session_state.pdf_docs = pdf_docs

                    # Create Conversation Chain (Session State to allow for multiple queries without reprocessing the documents)
                    st.session_state.conversation_chain = get_conversation_chain(vector_store)
            else:
                st.write('Please upload your PDFs first in order to start the chat.')

if __name__ == '__main__':
    main()
# Multi-PDF Chatbot

The Multi-PDF Chatbot is a Python application that allows user to chat with multiple PDF documents using LangChain and ChatGPT API. Users can ask questions about the PDFs in natural language and the application will provide relevant responses based on the content of the documents. This app utilizes a language model to generate accurate answers to your queries. Please note that the app will only respond to questions related to the loaded PDFs.

<img width="700" alt="image" src="https://github.com/YouXuan2010/Multi-PDF-Chat-App/assets/100280753/68ee9249-b48a-42f2-a593-fdc3c3948867">

## Features

- **PDF Text Extraction:** Efficiently extracts text from multiple PDF documents, providing a comprehensive source for information retrieval.
- **Text Chunking:** Divides the extracted text into manageable chunks, optimizing processing and ensuring efficient handling of large datasets.
- **Embeddings Generation:** Utilizes OpenAIEmbeddings to generate vector representations of text chunks, enhancing the semantic understanding of content. You can also use HuggingFaceInstructEmbeddings and search for your own embedding models in HuggingFace.
- **Vector Store Creation:** Creates a vector store using FAISS, enabling efficient storage and retrieval of text representations for improved performance.
- **Conversational Chain:** Establishes a Conversational Retrieval Chain using ChatOpenAI, facilitating dynamic interactions with the loaded PDF content.
- **Memory Management:** Implements a ConversationBufferMemory to store and retrieve chat history, enhancing context awareness for more coherent responses.
- **User-Defined Models:** Allows flexibility in choosing different text-to-text generation models in Huggingface (Need to configure your HUGGINGFACEHUB_API_TOKEN), enabling adaptation to specific project requirements.


## Getting Started

### Prerequisites

- Python 3.9

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YouXuan2010/Multi-PDF-Chat-App.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Obtain an API key from OpenAI and HuggingFace (If you want to use HuggingFace Models) and add it to the .env file under the project directory:
   ```bash
   OPENAI_API_KEY=sk-XXXXXXXXX
   HUGGINGFACEHUB_API_TOKEN=XXXXXXXXXXX
   ```

### Running the application
Run the main.py file using the Streamlit CLI:
   ```bash
   streamlit run app.py
   ```
## Example Demo

Answering user's queries based on the given pdf file:\
<img width="700" alt="image" src="https://github.com/YouXuan2010/Multi-PDF-Chat-App/assets/100280753/6df32cff-2ef5-469a-b26f-e2606d6590e7">

User interface to upload pdf:\
<img height="500" alt="image" src="https://github.com/YouXuan2010/Multi-PDF-Chat-App/assets/100280753/4e7b5ba3-1a3f-44d5-88d0-ce099299123b">


Basic error handling:\
<img width="700" alt="image" src="https://github.com/YouXuan2010/Multi-PDF-Chat-App/assets/100280753/1575e03a-c63e-4c51-9913-3e91d9704874">


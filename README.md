# Multi-PDF Chatbot

The Multi-PDF Chatbot is a Python application that allows user to chat with multiple PDF documents. Users can ask questions about the PDFs in natural language and the application will provide relevant responses based on the content of the documents. This app utilizes a language model to generate accurate answers to your queries. Please note that the app will only respond to questions related to the loaded PDFs.

## Features

- **PDF Loading:** Efficiently loads multiple PDF documents, extracting their text content for further processing.
- **Text Chunking:** Divides the extracted text into manageable chunks, optimizing the processing workflow.
- **Language Model Integration:** Utilizes a sophisticated language model to generate vector representations (embeddings) of the text chunks.
- **Similarity Matching:** Employs advanced similarity matching techniques to compare your queries with text chunks, identifying the most semantically similar content.
- **Dynamic Response Generation:** Selected text chunks are passed to the language model, dynamically generating responses based on the relevant content of the loaded PDFs.

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
   
3. Obtain an API key from OpenAI and add it to the .env file under the project directory:
   ```bash
   OPENAI_API_KEY=your_secret_api_key
   ```

### Running the application

1. Run the main.py file using the Streamlit CLI:
   ```bash
   streamlit run app.py
   ```
### Example Demo

1. Answering user's queries based on the given pdf file:
<img width="800" alt="image" src="https://github.com/YouXuan2010/Multi-PDF-Chat-App/assets/100280753/6df32cff-2ef5-469a-b26f-e2606d6590e7">

2. Nice and cool uploading user interface:
<img width="800" alt="image" src="https://github.com/YouXuan2010/Multi-PDF-Chat-App/assets/100280753/4e7b5ba3-1a3f-44d5-88d0-ce099299123b">

3. Basic error handling:
<img width="800" alt="image" src="https://github.com/YouXuan2010/Multi-PDF-Chat-App/assets/100280753/1575e03a-c63e-4c51-9913-3e91d9704874">


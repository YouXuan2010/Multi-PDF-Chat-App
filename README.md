# Multi-PDF Chatbot

This project is a 

## Features

- **Create:** Add new contacts with their first name, last name, and email.
- **Read:** View a list of contacts with their details.
- **Update:** Modify existing contact information.
- **Delete:** Remove unwanted contacts from the database.
- **Error Handling:**
  - Ensure non-empty entries for first name, last name, and email fields.
  - Prevent the creation of contacts with duplicate email addresses.

## Technologies Used

- **Backend:**
  - Flask: A lightweight web framework for building the backend.
  - SQLAlchemy: An ORM for working with databases in Flask applications.

- **Frontend:**
  - React: A JavaScript library for building user interfaces.

## Getting Started

### Prerequisites

- Python 3.x
- Node.js
- npm

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

<img width="458" alt="image" src="https://github.com/YouXuan2010/Multi-PDF-Chat-App/assets/100280753/6df32cff-2ef5-469a-b26f-e2606d6590e7">


# Multi-PDF Chatbot

This project is a 

<img width="458" alt="image" src="https://github.com/YouXuan2010/Multi-PDF-Chat-App/assets/100280753/6df32cff-2ef5-469a-b26f-e2606d6590e7">

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
   git clone https://github.com/YouXuan2010/My-Contact-App.git
   ```

2. Navigate to the backend directory and install Python dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
   
3. Navigate to the frontend directory and install npm packages:
   ```bash
   cd frontend
   npm install
   ```

### Running the application

1. Run the main.py file using the Streamlit CLI:
   ```bash
   streamlit run app.py
   ```


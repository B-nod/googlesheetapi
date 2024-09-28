# Django Google Sheets API Integration
This Django project demonstrates how to use the Google Sheets API to append data to a Google Sheet using a REST API. It includes functionality to add rows of data to a Google Sheet via a POST request, with the option to handle headers if they do not already exist.

## Features
Add new data to Google Sheets using a POST request.
Automatically add headers to the Google Sheet if they don't already exist.
Uses Google Sheets API for seamless integration.
Simple API endpoint to append data  name, address, contact, and email .

## Requirements
1. Python 3.x
2. Django 4.x
3. Django REST Framework
4. Google Sheets API
5. Google service account credentials

# Installation
### Clone the repository:
git clone https://github.com/B-nod/googlesheetapi

*cd googlesheetapi* 

### Create a virtual environment and activate it:

python3 -m venv venv
# On mac
source venv/bin/activate  
# On Windows: 
venv\Scripts\activate

# Install dependencies:
pip install -r requirements.txt
Set up your .env file with the necessary environment variables:

GOOGLE_CREDENTIALS_FILE=path/to/your/credentials.json
The GOOGLE_CREDENTIALS_FILE points to the Google service account credentials JSON file that allows access to the Google Sheets API.
Set up your Google Sheets API credentials by following the Google API Quickstart Guide to create a Google Service Account and enable Google Sheets API.

Update the SHEET_ID in your code with the actual ID of your Google Sheet:

python
Copy code
SHEET_ID = 'your_google_sheet_id'
Running the Project
Apply migrations:

bash
Copy code
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
Use an API testing tool like Postman or curl to test the API.

Example POST request:

bash
Copy code
curl -X POST http://127.0.0.1:8000/api/add-person/ \
-H "Content-Type: application/json" \
-d '{"name": "John Doe", "address": "123 Main St", "contact": "555-5555", "email": "johndoe@example.com"}'
The data will be appended to your Google Sheet.

API Endpoints
Add Person (POST /api/add-person/)
This endpoint accepts a POST request with the following JSON payload:

json
Copy code
{
    "name": "John Doe",
    "address": "123 Main St",
    "contact": "555-5555",
    "email": "johndoe@example.com"
}
Upon successful request, the data will be appended to the Google Sheet, and you will receive a response:

json
Copy code
{
    "message": "Your data was added successfully!"
}
Google Sheets Setup
Ensure your Google Sheet has headers such as "Name", "Address", "Contact", and "Email".
The system will automatically check for these headers and insert them if they are missing.
The new data will be appended below the headers.
Folder Structure
plaintext
Copy code
.
├── .env                  # Environment variables file
├── manage.py             # Django management file
├── requirements.txt      # Python dependencies
├── project/              # Django project directory
│   ├── settings.py       # Project settings
│   └── urls.py           # Project URLs
├── app/                  # Django app directory
│   ├── views.py          # API logic
│   └── urls.py           # App URLs
└── README.md             # Project README file
Environment Variables
Make sure to set the following environment variables in your .env file:

GOOGLE_CREDENTIALS_FILE: The path to your Google service account JSON file.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit and push your changes (git commit -m "Description of changes").
Create a pull request.
Resources
Django
Django REST Framework
Google Sheets API
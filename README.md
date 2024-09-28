# Django Google Sheets API Integration
This Django project demonstrates how to use the Google Sheets API to append data to a Google Sheet using a REST API. It includes functionality to add rows of data to a Google Sheet via a POST request .

# Features
Add new data to Google Sheets using a POST request.
Uses Google Sheets API for seamless integration.
Simple API endpoint to append data  name, address, contact, and email .

# Requirements
1. Python 3.x
2. Django 4.x
3. Django REST Framework
4. Google Sheets API
5. Google service account credentials

# Installation
### Clone the repository:
git clone https://github.com/B-nod/googlesheetapi

cd googlesheetapi

### Create a virtual environment and activate it:
python3 -m venv venv

### On mac
source venv/bin/activate  
# On Windows: 
venv\Scripts\activate

### Install dependencies:
pip install -r requirements.txt

### Set up your .env file with the necessary environment variables:

GOOGLE_CREDENTIALS_FILE=path/to/your/credentials.json

**The GOOGLE_CREDENTIALS_FILE points to the Google service account credentials JSON file that allows access to the Google Sheets API.**

Set up your Google Sheets API credentials by following the Google API Quickstart Guide to create a Google Service Account and enable Google Sheets API.

Update the SHEET_ID in your code with the actual ID of your Google Sheet:

SHEET_ID = 'your_google_sheet_id'

### Running the Project
##### Apply migrations:
python manage.py makemigrations

python manage.py migrate

### Start the development server:

python manage.py runserver
### Use an API testing tool like Postman or curl to test the API.

#### Example POST request:

API Endpoints

POST : http://127.0.0.1:8000/addDetail/

This endpoint accepts a POST request with the following JSON payload:

{
    "name": "Binod Tamang",
    "address": "Kathmandu",
    "contact": "9880898989",
    "email": "binod@example.com"
}

**Upon successful request, the data will be appended to the Google Sheet, and you will receive a response:**

{
    "message": "Your data was added successfully!"
}

### Google Sheets Setup
Ensure your Google Sheet has headers such as "Name", "Address", "Contact", and "Email".

The new data will be appended below the headers.

### POSTMAN DATA
Here, i have mentioned json file of postman. Visit File

Googlesheetsapi.postman_collection.json
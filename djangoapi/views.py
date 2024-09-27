import os
from django.http import JsonResponse
from rest_framework.decorators import api_view
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Google Sheets credentials file path from .env
GOOGLE_CREDENTIALS_FILE = os.getenv('GOOGLE_CREDENTIALS_FILE')

# Define the scope for accessing Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Replace with your Google Sheet ID and range
SHEET_ID = '1vwYRtY4f237CO0ZSeGiRiUZOY3RLuqCDLfsUrOh9RdQ'
SHEET_RANGE = 'Sheet1!A:D'  # Adjust the range as necessary

# Function to get Google Sheets API service
def get_google_sheets_service():
    creds = Credentials.from_service_account_file(GOOGLE_CREDENTIALS_FILE, scopes=SCOPES)
    return build('sheets', 'v4', credentials=creds)

@api_view(['POST'])
def add_person(request):
    try:
        # Get data from request
        name = request.data.get('name')
        address = request.data.get('address')
        contact = request.data.get('contact')
        email = request.data.get('email')

        if not all([name, address, contact, email]):
            return JsonResponse({'error': 'All fields are required.'}, status=400)

        # Get the Google Sheets service
        service = get_google_sheets_service()

        # Prepare the data to append
        values = [[name, address, contact, email]]
        body = {'values': values}

        # Append the data to Google Sheets
        result = service.spreadsheets().values().append(
            spreadsheetId=SHEET_ID,
            range=SHEET_RANGE,
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()

        return JsonResponse({'message': 'Data added successfully!'}, status=200)

    except HttpError as err:
        return JsonResponse({'error': f"Google Sheets API error: {err}"}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
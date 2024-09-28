from django.http import JsonResponse
from rest_framework.views import APIView
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import os

class GoogleSheetView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Extract data from request
            name = request.data.get('name')
            address = request.data.get('address')
            contact = request.data.get('contact')
            email = request.data.get('email')

            if not all([name, address, contact, email]):
                return JsonResponse({'error': 'All fields are required.'}, status=400)

            # Call method to append data to Google Sheets
            service = self.get_google_sheets_service()
            self.append_data_to_sheet(service, [name, address, contact, email])

            return JsonResponse({'message': 'Your data was added successfully!'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_google_sheets_service(self):
        creds = Credentials.from_service_account_file(os.getenv('GOOGLE_CREDENTIALS_FILE'), scopes=['https://www.googleapis.com/auth/spreadsheets'])
        return build('sheets', 'v4', credentials=creds)

    def append_data_to_sheet(self, service, data):
        sheet_id = '1vwYRtY4f237CO0ZSeGiRiUZOY3RLuqCDLfsUrOh9RdQ'
        sheet_range = 'Sheet1!A:D'
        body = {'values': [data]}
        service.spreadsheets().values().append(
            spreadsheetId=sheet_id,
            range=sheet_range,
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()

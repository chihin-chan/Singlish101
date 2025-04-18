import os
import json
import gspread
from google.oauth2.service_account import Credentials

# Load credentials from environment variable
credentials_info = json.loads(os.getenv('GOOGLE_SHEETS_CREDENTIALS'))

# Authenticate with Google Sheets API using the service account credentials
credentials = Credentials.from_service_account_info(credentials_info)

# Initialize gspread client with the credentials
client = gspread.authorize(credentials)

# Open the sheet by name
spreadsheet = client.open('Your Google Sheet Name')

# Access the first sheet
worksheet = spreadsheet.get_worksheet(0)

# Example: Print the data from the first column
data = worksheet.col_values(1)
print(data)

# Now, update your LaTeX file based on the fetched data

import os
import json
import gspread
from google.oauth2.service_account import Credentials
import re

# Outline scopes
SCOPES = ['https://www.googleapis.com/auth/spreadsheets',  # Access Google Sheets
          'https://www.googleapis.com/auth/drive']        # Access Google Drive (needed for accessing files)

# Load credentials from JSON file
with open('../../../../chihin/Downloads/opportune-balm-457323-u7-e2d9b8780653.json', 'r') as file:
   credentials_info = json.load(file)  # Use json.load to read the JSON file
# Load credentials from environment variable
# credentials_info = json.loads(os.getenv('GOOGLE_SHEETS_CREDENTIALS'))

# Authenticate with Google Sheets API using the service account credentials
credentials = Credentials.from_service_account_info(credentials_info, scopes=SCOPES)

# Initialize gspread client with the credentials
client = gspread.authorize(credentials)

# Open the sheet by name
spreadsheet = client.open('Singlish101Responses').sheet1
rows = spreadsheet.get_all_values()

# Get (Singlish, English, Contributor) 
gsheet_entries = gsheet_entries = [(row[1].strip(), row[2].strip(), row[3].strip()) for row in rows[1:] if len(row) >= 3 and row[1] and row[2] and row[3]]
print(gsheet_entries)

# Load the gsheets.tex
gsheets_tex = 'Chaptermate/gsheets.tex'
with open(gsheets_tex, 'r') as file:
    tex_content = file.read()

# Extract existing LaTeX items using regex
existing_items = re.findall(r'\\item\s+\\textit\{(.*?)\}\s*-\s*(.*?)(?:\s*\((.*?)\))?\s*$', tex_content, re.MULTILINE)

# Convert both lists to sets for comparison
gsheet_set = set(gsheet_entries)
tex_set = set(existing_items)

# Determine what entries are new
new_entries = list(gsheet_set - tex_set)

# If there are new entries, insert them before the first \item
if new_entries:

    insert_position = tex_content.find('\\item')
    new_tex = ""

    for sg, uk, author in new_entries:
        new_tex += f"    \\item \\textit{{{sg}}} - {uk} ({author})\n"
        tex_content = tex_content[:insert_position] + new_tex + tex_content[insert_position:]

    with open(gsheets_tex, 'w') as file:
        file.write(tex_content)

    print(f"Added {(new_entries)} new entries.")
else:
    print("No new entries to add.")


# Access the first sheet
# worksheet = spreadsheet.get_worksheet(0)
# 
# # Example: Print the data from the first column
# singlish_col = worksheet.col_values(2)
# ukenglish_col = worksheet.col_values(3)
# 
# # Example: Print the data from the first column
# if singlish_col and ukenglish_col:
#     latest_sg_gsheets = singlish_col[-1]
#     latest_uk_gsheets = ukenglish_col[-1]
#     print(f"Gsheets: {latest_sg_gsheets}, {latest_uk_gsheets}")
# else:
#     print("Either gsheets columns are empty.")
# 
# # Reading main.tex
# texfile = 'Chaptermate/gsheets.tex'
# with open(texfile, 'r') as texstream:
#     tex_content = texstream.read()
# 
# # Use regex to find first entry
# last_item_match = re.search(r'\\item\s+\\textit\{(.*?)\}\s*-\s*(.*)', tex_content)
# if last_item_match:
#     latest_sg_main = last_item_match.group(1)  # Get the last Singlish entry
#     latest_uk_main = last_item_match.group(2)  # Get the last UK English entry
#     print(f"Main.tex: {latest_sg_main}, {latest_uk_main}")
# else:
#     last_singlish = ""
#     last_uk_english = ""
# 
# 
# # Check if the latest Singlish entry exists in the LaTeX file
# if latest_sg_gsheets != latest_sg_main and latest_uk_gsheets != latest_uk_main:
# 
#     new_item = f"\\item \\textit{{{latest_sg_gsheets}}} - {latest_uk_gsheets}\n"
# 
#     # Find the position of the first \item and insert the new item before it
#     insert_position = tex_content.find('\\item')  # Find the first occurrence of \item
# 
#     # Insert the new item above the first \item (just before it)
#     tex_content = tex_content[:insert_position] + new_item + tex_content[insert_position:]
# 
#     # Write the updated content back to the LaTeX file
#     with open(texfile, 'w') as texstream:
#         texstream.write(tex_content)
# 
#     print(f"New entry added: {new_item.strip()}")
# 
# else:
# 
#     print("The latest entry already exists in the LaTeX file.")
# 

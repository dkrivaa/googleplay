import base64
import gspread
from google.oauth2.service_account import Credentials
import os
import json


credentials_json_string = os.environ.get('credentials_json_string')
credentials_json = json.loads(base64.b64decode(credentials_json_string))
sheet_id = os.environ.get('sheet_id')
creds = Credentials.from_service_account_info(credentials_json)
client = gspread.authorize(creds)

book = client.open_by_key(sheet_id)

# values_list = book.sheet1.row_values(1)
# print(values_list)


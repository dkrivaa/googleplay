import base64
import gspread
from google.oauth2.service_account import Credentials
import os
import json


credentials_json_string = os.environ.get('credentials_json_string')
credentials_json = json.loads(base64.b64decode(credentials_json_string))
sheet_id = os.environ.get('sheet_id')

scopes = ["https://www.googleapis.com/auth/spreadsheets"]

creds = Credentials.from_service_account_info(credentials_json, scopes=scopes)
client = gspread.authorize(creds)

book = client.open_by_key(sheet_id)

book.sheet1.update([[1, 2], [3, 4]], 'A1:B2')
# values_list = book.sheet1.row_values(1)
# print(values_list)


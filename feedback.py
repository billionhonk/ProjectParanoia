import gspread
from oauth2client.service_account import ServiceAccountCredentials

import _variables as v


#set scope of what we want to access
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

#store information from JSON file
credentials = ServiceAccountCredentials.from_json_keyfile_name('annular-moon-388406-3e02c59f1c64.json', scope)

#makes a variable interface with google sheets
googleSheet = gspread.authorize(credentials)

index = 0 #which sheet to use | 0 = sheet1
wks = googleSheet.open('IDP2023Feedback').get_worksheet(index)

#practice input
def update_data():
  name = v.username

  q1 = v.survey1
  q2 = v.survey2
  q3 = v.survey3
  q4 = v.survey4
  q5 = v.survey5
  q6 = v.survey6

  #add a new row to the google sheet
  wks.append_row([name, q1, q2, q3, q4, q5, q6])
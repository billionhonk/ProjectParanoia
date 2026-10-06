import gspread
from oauth2client.service_account import ServiceAccountCredentials

import _variables as v


#set scope of what we want to access
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

#store information from JSON file
credentials = ServiceAccountCredentials.from_json_keyfile_name('idp2023leaderboard-6998517295d0.json', scope)

#makes a variable interface with google sheets
googleSheet = gspread.authorize(credentials)

index = 0 #which sheet to use | 0 = sheet1
wks = googleSheet.open('IDP2023Leaderboard').get_worksheet(index)

#practice input
def update_data():
  global name, time, wks
  global p1, p2, p3, p4, p5, p6, p7, p8, p9, p10
  global h1, h2, h3, h4, h5, h6, h7, h8, h9, h10

  index = 0 #which sheet to use | 0 = sheet1
  wks = googleSheet.open('IDP2023Leaderboard').get_worksheet(index)

  name = v.username
  time = v.time
  p1 = v.time_puzzle1
  p2 = v.time_puzzle2
  p3 = v.time_puzzle3 
  p4 = v.time_puzzle4
  p5 = v.time_puzzle5
  p6 = v.time_puzzle6
  p7 = v.time_puzzle7
  p8 = v.time_puzzle8
  p9 = v.time_puzzle9
  p10 = v.time_puzzle10
  f1 = p1 + p2 + p3
  f2 = p4 + p5 + p6
  f3 = p7 + p8 + p9
  h1 = v.hints_puzzle1
  h2 = v.hints_puzzle2
  h3 = v.hints_puzzle3
  h4 = v.hints_puzzle4
  h5 = v.hints_puzzle5
  h6 = v.hints_puzzle6
  h7 = v.hints_puzzle7
  h8 = v.hints_puzzle8
  h9 = v.hints_puzzle9
  h10 = v.hints_puzzle10
  hints = h1 + h2 + h3 + h4 + h5 + h6 + h7 + h8 + h9 + h10

  #add a new row to the google sheet
  wks.append_row([name, time, hints, f1, f2, f3, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10])

def leaderboard_text():
  global wks
  #get data from google sheet
  index = 2
  wks = googleSheet.open('IDP2023Leaderboard').get_worksheet(index)

  leaderboard = []
  for i in range(2,7,1): #header and top 5 users
    leaderboard.append(wks.row_values(i))
  headers = wks.row_values(1)

  header1 = headers[0]
  header2 = headers[1]
  header3 = headers[2]

  usernames = []
  times_remaining = []
  hints_used = []
  
  for i in range(5):
    if len(leaderboard[i]) > 0:
      usernames.append(leaderboard[i][0])
  for i in range(5):
    if len(leaderboard[i]) > 0:
      times_remaining.append(leaderboard[i][1])
  for i in range(5):
    if len(leaderboard[i]) > 0:
      hints_used.append(leaderboard[i][2])

  return header1, usernames, header2, times_remaining, header3, hints_used
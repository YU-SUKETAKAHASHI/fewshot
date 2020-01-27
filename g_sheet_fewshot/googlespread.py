import gspread
from oauth2client.service_account import ServiceAccountCredentials


def setsheet():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('gspread-sample-06cdd678a479.json', scope)
    global worksheet    
    gc = gspread.authorize(credentials)
    gc = gc.open("mySheet")
    worksheet = gc.worksheet("fewshot")#管理シートを指定


def search_last_row(num):
        row_count = 1
        while worksheet.cell(row_count, num).value:
            row_count += 1
        return row_count


def record(info):
    worksheet.update_cell(search_last_row(1), 1, info)
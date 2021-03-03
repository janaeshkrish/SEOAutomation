import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def get_data():
    
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)

    # authorize the clientsheet
    client = gspread.authorize(creds)

    #get tje sheet instance
    sheet = client.open('Keywords')
    # get the first sheet of the Spreadsheet
    sheet_instance = sheet.worksheet('Sheet1')

    # get all the records of the data
    records_data = sheet_instance.get_all_records()

    #print(records_data)

    # convert the json to dataframe
    data = pd.DataFrame.from_dict(records_data)

    return data
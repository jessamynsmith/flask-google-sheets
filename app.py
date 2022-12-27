from flask import Flask, render_template
import googleapiclient.discovery
from google.oauth2 import service_account
import json



def get_credentials():
    
    '''
    app.config['SECRET_KEY'] = config.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.get('DEV_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.get('SQLALCHEMY_TRACK_MODIFICATIONS')  
    '''
    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    GOOGLE_PRIVATE_KEY = config.get('GOOGLE_PRIVATE_KEY')
    
    account_info = {
      "private_key": GOOGLE_PRIVATE_KEY,
      "client_email": config.get('GOOGLE_CLIENT_EMAIL'),
      "token_uri": "https://accounts.google.com/o/oauth2/token",
    }
    
    credentials = service_account.Credentials.from_service_account_info(account_info, scopes=scopes)
    return credentials

'''
def get_credentials():
    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    GOOGLE_PRIVATE_KEY = os.environ["GOOGLE_PRIVATE_KEY"]
    # The environment variable has escaped newlines, so remove the extra backslash
    GOOGLE_PRIVATE_KEY = GOOGLE_PRIVATE_KEY.replace('\\n', '\n')

    account_info = {
      "private_key": GOOGLE_PRIVATE_KEY,
      "client_email": os.environ["GOOGLE_CLIENT_EMAIL"],
      "token_uri": "https://accounts.google.com/o/oauth2/token",
    }

    credentials = service_account.Credentials.from_service_account_info(account_info, scopes=scopes)
    return credentials
'''

def get_service(service_name='sheets', api_version='v4'):
    credentials = get_credentials()
    service = googleapiclient.discovery.build(service_name, api_version, credentials=credentials)
    return service


app = Flask(__name__)

# Load configuration from JSON file
with open('config.json') as config_file:
    config = json.load(config_file)


@app.route('/', methods=['GET'])
def homepage():
    service = get_service()
    spreadsheet_id = config.get('GOOGLE_SPREADSHEET_ID')
    range_name = config.get('GOOGLE_CELL_RANGE')

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])

    return render_template('index.html', values=values)


if __name__ == '__main__':
    app.run(debug=True)

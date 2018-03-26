# flask-simple-example

Simple example of retrieving data from Google Sheets and displaying it in a Flask app.
https://flask-google-sheets.herokuapp.com/

Like my work? Tip me! https://www.paypal.me/jessamynsmith


### Development

## Setup

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/flask-google-sheets.git

Create a virtualenv using Python 3 and install dependencies. I recommend getting python3 using a package manager (homebrew on OSX), then installing [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation) to that python. NOTE! You must change 'path/to/python3'
to be the actual path to python3 on your system.

    mkvirtualenv flask-google-sheets --python=/path/to/python3
    pip install -r requirements.txt

Check code style:

    flake8

## Set up Google Sheets

1. Open https://console.developers.google.com/permissions/serviceaccounts

1. If you already have a Google API project, select it. Otherwise, create one.

1. Click "CREATE SERVICE ACCOUNT"

1. Enter a Service account name. Set Role to Owner. Ensure that "Furnish a new private key" is checked, and that Key type "JSON" is selected. Click "CREATE".

1. Open the automatically downloaded JSON credentials file. You will use the values to set the following environment variables:

    ```
    export GOOGLE_PRIVATE_KEY="<private_key_from_credentials_json>"
    export GOOGLE_CLIENT_EMAIL="<client_email_from_credentials_json>"
    ```

1. Set environment variables for the Google Sheet you want to retrieve data from:

    ```
    export GOOGLE_SPREADSHEET_ID="<spreadsheet_id_from_google_sheets>"
    export GOOGLE_CELL_RANGE='<sheetname>!<range>'  # e.g. 'Dogs!A1:C'
    ```

1. Ensure that your API Project has the Google Sheets API enabled. You can go to https://console.developers.google.com/apis/dashboard to select the project, then click "ENABLE APIS AND SERVICES" and look for sheets.

1. Log into Google Sheets and share your sheet with the service account user, as specified in client_email in the JSON credentials file.

## Run server

Run using flask:

    FLASK_APP=app.py flask run

Or run using gunicorn:

    gunicorn app:app

### Deployment

This project is already set up for deployment using Heroku.

Make a new Heroku app:

    heroku apps:create

Set environment variables

You can find the values in the downloaded JSON credentials file for your Google service account.

    heroku config:set GOOGLE_PRIVATE_KEY="<private_key_from_credentials_json>"
    heroku config:set GOOGLE_CLIENT_EMAIL="<client_email_from_credentials_json>"
    heroku config:set GOOGLE_SPREADSHEET_ID="<spreadsheet_id_from_google_sheets>"
    heroku config:set GOOGLE_CELL_RANGE='<sheetname>!<range>'  # e.g. 'Dogs!A1:C'

Push code to heroku:

    git push heroku master
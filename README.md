# flask-simple-example

Simple example of retrieving data from Google Sheets and displaying it in a Flask app.

## Setup

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/flask-google-sheets.git

Create a virtualenv using Python 3 and install dependencies. I recommend getting [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) using a package manager (homebrew on OSX), then using pyenv to install python. 

    pyenv install python 3.10.7
    pyenv virtualenv 3.10.7 fgs
    pyenv activate fgs
    pip install -r requirements.txt


## Set up Google Sheets

1. Open https://console.cloud.google.com/iam-admin/serviceaccounts

1. If you already have a Google API project, select it. Otherwise, create one.

1. Click "CREATE SERVICE ACCOUNT"

1. Enter a Service account name and Description. Click "CREATE AND CONTINUE".

1. Set Role to Owner. Click "CONTINUE".

1. Under "3. Grant users access to this service account", leave both boxes blank and click "DONE".

1. Once back on the "Service accounts for project <project_name>" screen, click the "⋮" menu in the "Actions" column of your new Service Account and select "Manage Keys".

1. Click the "ADD KEY" dropdown and select "Create new key". On the "Create Private key for <project_name>" modal, ensure that the JSON Key type is select, and then click "CREATE".

1. Create 



1. Add the appropriate values from the JSON file that automatically downloaded and from Google Sheets to a file called `config.json` that resides in the same directory as `app.py`:

    ```{JSON}
    {
        "FLASK_DEBUG": "True",
        "SECRET_KEY": "SuperSecretKey",
        "GOOGLE_PRIVATE_KEY": "<private_key_from_credentials_json>",
        "GOOGLE_CLIENT_EMAIL": "<client_email_from_credentials_json>",
        "GOOGLE_SPREADSHEET_ID": "<spreadsheet_id_from_google_sheets>",
        "GOOGLE_CELL_RANGE": "<sheetname>!<range>"  # e.g. "Dogs!A1:C"
    }
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

Set [Heroku environment variables](https://devcenter.heroku.com/articles/config-vars)

You can find the values in the downloaded JSON credentials file for your Google service account.

    heroku config:set GOOGLE_PRIVATE_KEY="<private_key_from_credentials_json>"
    heroku config:set GOOGLE_CLIENT_EMAIL="<client_email_from_credentials_json>"
    heroku config:set GOOGLE_SPREADSHEET_ID="<spreadsheet_id_from_google_sheets>"
    heroku config:set GOOGLE_CELL_RANGE='<sheetname>!<range>'  # e.g. 'Dogs!A1:C'

Push code to heroku:

    git push heroku master

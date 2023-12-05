import requests
import json

# Define the necessary information
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
tenant_id = 'YOUR_TENANT_ID'
recipient_email = 'recipient@example.com'
subject = 'Test Email'
body = 'This is a test email sent via Microsoft Graph API.'

# Get an access token from Azure Active Directory
token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
payload = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'https://graph.microsoft.com/.default'
}
token_response = requests.post(token_url, data=payload)
access_token = token_response.json()['access_token']

# Send the email
sendmail_url = 'https://graph.microsoft.com/v1.0/users/me/sendMail'
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}
email_data = {
    'message': {
        'subject': subject,
        'body': {
            'contentType': 'Text',
            'content': body
        },
        'toRecipients': [
            {
                'emailAddress': {
                    'address': recipient_email
                }
            }
        ]
    }
}
response = requests.post(sendmail_url, headers=headers, data=json.dumps(email_data))

# Check the response
if response.status_code == 202:
    print('Email sent successfully.')
else:
    print('Failed to send email. Status code:', response.status_code)
    print('Response:', response.text)
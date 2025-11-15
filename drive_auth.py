from time import time
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
import io

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def authenticate_drive(credentials_path, max_retries=3, retry_delay=2):
    retries = 0

    while retries < max_retries:
        try:
            print(f"Authenticating with Google Drive... Attempt {retries + 1}/{max_retries}")
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
            print("Authentication successful.")
            return build('drive', 'v3', credentials=creds)

        except Exception as e:
            print(f"Authentication failed: {e}")
            retries += 1
            if retries < max_retries:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Max retries reached. Could not authenticate with Google Drive.")
                raise

def download_pdf(service, file_id, dest_path):
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(dest_path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    return dest_path

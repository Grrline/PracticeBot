from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import aspose.pdf as pdf
import sqlite3
import os
import re

SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = 'client_secrets.json'
FOLDER_ID = '1C1gHs6jiXr-SGpQEJtNBvoWU9AIGwLul'
ADMIN_CHAT_ID = 5618617071

def contains_python_or_sql(file_path):
    pdfFile = pdf.Document(file_path)
    textAbsorder = pdf.text.TextAbsorber()
    pdfFile.pages.accept(textAbsorder)
    return bool(re.search(r"(Python|SQL)", textAbsorder.text, re.IGNORECASE))

def upload_to_google_drive(file_path, file_name):
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    drive_service = build('drive', 'v3', credentials=credentials)
    media = MediaFileUpload(file_path, resumable=True)
    file_metadata = {'name': file_name, 'parents': [FOLDER_ID]}
    response = drive_service.files().create(body=file_metadata, media_body=media).execute()
    return response.get('webViewLink')

def upload_resume_file_to_cloud(bot):
    @bot.message_handler(content_types=['document'])
    def handle_document(message):
        file_info = bot.get_file(message.document.file_id)
        file_name = message.document.file_name
        downloaded_file = bot.download_file(file_info.file_path)
        temp_file_path = f'./{file_name}'

        with open(temp_file_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        if contains_python_or_sql(temp_file_path):
            bot.send_message(ADMIN_CHAT_ID, f"Привет! Тут пришло интересное резюме: '{file_name}'\n"
                                            f"Телеграмм айди владельца резюме: {message.chat.id}\n")

        try:
            upload_to_google_drive(temp_file_path, file_name)
            bot.send_message(message.chat.id, "✅ Ваше резюме успешно загружено на Google Диск!")
        except Exception as e:
            bot.send_message(message.chat.id, f"❌ Произошла ошибка при загрузке: {str(e)}")
        finally:
            os.remove(temp_file_path)
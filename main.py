import telebot
import os

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from pydrive.auth import GoogleAuth

from data.functions.go_back import go_back
from data.functions.show_about import show_about
from data.functions.show_answer import show_answer
from data.functions.show_help import show_help
from data.functions.show_start_markup import show_start_markup
from data.functions.show_faq import show_faq
from data.functions.upload_resume_file_to_cloud import upload_resume_file_to_cloud

bot = telebot.TeleBot('7225986191:AAF_igRpxsmb4c-ThF9awq7NdcHABXhnQSU')
show_start_markup(bot)
upload_resume_file_to_cloud(bot)
show_help(bot)
show_about(bot)
show_faq(bot)
show_answer(bot)
go_back(bot)

bot.polling()
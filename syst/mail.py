import datetime
import imaplib
import email
import re
from email.header import decode_header
import webbrowser
import os
import copy


class ReadLettersFromGmail:
    def __init__(self):
        self.username = "zast0tsaz@gmail.com"
        self.password = "xzyzfmfuktumsfbd"
        self.server = "imap.gmail.com"
        self.mess = self.read_mess_from_email()

    def read_mess_from_email(self):
        imap = imaplib.IMAP4_SSL(self.server)
        imap.login(self.username, self.password)
        imap.select("INBOX")
        result, data = imap.search(None, "UNSEEN")
        ids = data[0]  # Получаем строку номеров писем
        id_list = ids.split()  # Разделяем ID писем
        latest_email_id = id_list[-1]  # Берем последний ID
        res, msg = imap.fetch(latest_email_id, '(RFC822)')
        msg = email.message_from_bytes(msg[0][1])
        letter_from = msg["Return-path"]  # e-mail отправителя
        letter_sub = decode_header(msg["Subject"])[0][0]
        letter_date = email.utils.parsedate_tz(msg["Date"])
        d = datetime.datetime(*(letter_date[0:6]))
        # dStr_1 = d.isoformat(' ')
        dStr = d.strftime('%Y-%m-%d %H:%M:%S')
        print(dStr)
        sender = '<filterdevreact@gmail.com>'
        reset_message = []
        for part in msg.walk():
            print(f"Запуск цикла чтения письма...")
            # extract content type of email
            if letter_from == sender:
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                # get the email body
                body = part.get_payload(decode=True)
                print(f"Проверка содержимого письма...")
                if content_type == "text/plain" and "attachment" not in content_disposition:
                    # print text/plain emails and skip attachments
                    body_of_message = copy.copy(body)
                    a = [letter_sub, body_of_message]
                    reset_message.append(a)
                    print(f"Возвращение данных...")
                    return reset_message
            else:
                raise Exception("Message from FilterBuy is not found!")

    def return_link_for_reset_password(self):
        letters = self.mess
        reset_title = "Reset your password."
        for letter in letters:
            print("Получение ссылки...")
            if reset_title in letter[0]:
                body = letter[1].split()
                body_link = body[-9]
                str_body = str(body_link)
                b_link = re.split(r'\'', str_body)
                old_link = b_link[1]
                new_link = old_link.replace('filterbuy.com', "react.test.filterbuytest.com")
                print(f'\n{new_link}\n{letter[0]}')
                return new_link
            else:
                raise Exception("Reset password message is not found!")

#!/usr/bin/env python3
import argparse
import smtplib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import base64
import sys
import os

# Load key from file
def load_key(file_path):
    try:
        with open(file_path, 'r') as file:
            key_string = file.read().strip()
        key = base64.b64decode(key_string)
        return key
    except Exception as e:
        print(f"Error loading key: {e}")
        sys.exit(1)

# Decrypt account and password
def decrypt_credentials(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            encrypted_data = base64.b64decode(file.readline().strip())
            iv = encrypted_data[:16]  # Extract initialization vector
            encrypted_email = encrypted_data[16:]  # Extract encrypted email
            encrypted_data = base64.b64decode(file.readline().strip())
            encrypted_password = encrypted_data[16:]  # Extract encrypted password
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_email = unpad(cipher.decrypt(encrypted_email), AES.block_size)
        decrypted_password = unpad(cipher.decrypt(encrypted_password), AES.block_size)
        email = decrypted_email.decode()
        password = decrypted_password.decode()
        return email, password
    except Exception as e:
        print(f"Error decrypting credentials: {e}")
        sys.exit(1)

# Send email
def send_email(subject, body, sender_filename, receiver_filename, key_file, attachment_path=None):
    key = load_key(key_file)
    sender_username, sender_password = decrypt_credentials(sender_filename,key)
    receiver_usernames = [line.strip() for line in open(receiver_filename)]
    
    # Select SMTP server and port based on sender's email address
    domain = sender_username.split('@')[-1]
    smtp_servers = {
        'gmail.com': ('smtp.gmail.com', 587),
        'outlook.com': ('smtp-mail.outlook.com', 587),
        'hotmail.com': ('smtp-mail.outlook.com', 587),
    }
    if domain not in smtp_servers:
        print(f"Error: Unsupported email provider {domain}")
        sys.exit(1)
    smtp_server, smtp_port = smtp_servers[domain]

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender_username
    msg['To'] = ', '.join(receiver_usernames)
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    if attachment_path is not None:
        with open(attachment_path, 'rb') as file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(os.path.basename(attachment_path)))
            msg.attach(part)
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(sender_username, sender_password)
    status = smtp.sendmail(sender_username, receiver_usernames, msg.as_string())
    if not status:
        print("Email sent successfully!")
    else:
        print("Email sent fail!")
    smtp.quit()

# Main function
def main():
    sender_filename = 'sender_info_encrypt.txt'
    receiver_filename = 'receiver.list'
    key_file = '.key.txt'
    subject = 'Subject'
    body = "Hi:\nThis is a auto send information. You don't need to reply. \nThx."
    # create a  argumentParser object
    parser = argparse.ArgumentParser(description='Send an email with optional attachment.')
    parser.add_argument('--subject', default = subject, help='The subject of the email.')
    parser.add_argument('--body', default = body, help='The body of the email.')
    parser.add_argument('--sender', default = sender_filename, help='The file containing the encrypted sender information. (default: sender_info_encrypt.txt)')
    parser.add_argument('--receiver', default = receiver_filename, help='The file containing the receiver information. (default: receiver.list)')
    parser.add_argument('--key', default = key_file, help='The file containing the encryption key. (default: .key.txt)')
    parser.add_argument('-a','--attachment', help='The file to be attached to the email.')

    args = parser.parse_args()
    send_email(args.subject, args.body, args.sender, args.receiver, args.key, args.attachment)

if __name__ == "__main__":
    main()


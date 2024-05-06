#!/usr/bin/env python3
import argparse
import smtplib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import base64
import sys
import os
import hashlib

def generate_and_save_key(key_file_path):
    try:
        key = hashlib.sha256(os.urandom(32)).digest()[:32]
        key_string = base64.b64encode(key).decode()
        with open(key_file_path, 'w') as file:
            file.write(key_string)
        return key
    except Exception as e:
        print(f"Error generating and saving key: {e}")
        sys.exit(1)

def encrypt_credentials(file_path, output_path, key):
    try:
        with open(file_path, 'r') as file:
            email = file.readline().strip()
            password = file.readline().strip()
        email_bytes = email.encode()
        password_bytes = password.encode()
        email_bytes_padded = pad(email_bytes, AES.block_size)
        password_bytes_padded = pad(password_bytes, AES.block_size)

        # generate the random initiate vector
        iv = os.urandom(16)

        cipher = AES.new(key, AES.MODE_CBC, iv)

        # encrypt the addrass and password
        encrypted_email = cipher.encrypt(email_bytes_padded)
        encrypted_password = cipher.encrypt(password_bytes_padded)

        # create the files for the encrypted address and password
        with open(output_path, 'wb') as file:
            file.write(base64.b64encode(iv + encrypted_email))
            file.write(b'\n')
            file.write(base64.b64encode(iv + encrypted_password))
    except Exception as e:
        print(f"Error encrypting credentials: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_file = "sender_info.txt";
    output_file = "sender_info_encrypt.txt";
    key_file = ".key.txt";
    
    parser = argparse.ArgumentParser(description='Encrypt email credentials.')
    parser.add_argument('-i', '--input',  default = input_file, help='The input file containing the email and password. (default: sender_info.txt)')
    parser.add_argument('-o', '--output', default = output_file, help='The output file to write the encrypted credentials. (default: sender_info_encrypt.txt)')
    parser.add_argument('-k', '--keyfile',default = key_file, help='The file to save the encryption key. (dafault: .key.txt)')
    args = parser.parse_args()
    key = generate_and_save_key(args.keyfile)
    encrypt_credentials(args.input, args.output, key)


# Auto Email Sender Project
auto_send_email_with_smtp

This project contains two Python scripts, `encrypt_sender_emailinfo.py` and `auto_send_email.py`, which are used to automate the process of sending emails. The email can use gmail.com or outlook.com (hotmail.com).

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.6 or later.
- You have installed the following Python package:
  - `pycryptodome==3.20.0` for cryptographic operations or `pycrypto`

You can install this package using pip:

```bash
pip install -r requirements.txt
```

## Enableing the SMTP service in your email account

### Enabling Gmail SMTP Service

1. Log into your Gmail account and click on the settings icon in the top right corner.
2. In the settings page, select 'See all settings'.
3. Click on 'Forwarding and POP/IMAP'.
4. In the 'IMAP Access' section, select 'Enable IMAP'.
5. Click on 'Save Changes'.

SMTP Server Address: `smtp.gmail.com`

For detailed steps, you can refer to the official Gmail support page [here](https://developers.google.com/gmail/imap/imap-smtp?hl=zh-tw).

### Enabling Hotmail SMTP Service

1. Log into your Hotmail account and click on the settings icon in the top right corner.
2. In the settings page, select 'View all Outlook settings'.
3. Click on 'Mail' and select 'Sync email'.

SMTP Server Address: `smtp-mail.outlook.com`

For detailed steps, you can refer to the official Hotmail support page [here](https://support.microsoft.com/zh-tw/office/outlook-com-%E7%9A%84-pop-imap-%E5%92%8C-smtp-%E8%A8%AD%E5%AE%9A-d088b986-291d-42b8-9564-9c414e2aa040).

### Enabling Outlook Mail SMTP Service

1. Open Outlook and go to 'File'.
2. Click on 'Account Settings' and again on 'Account Settings'.
3. Select your email account.
4. Click on 'Server Settings'.

SMTP Server Address: `smtp-mail.outlook.com`

For detailed steps, you can refer to the official Outlook support page [here](https://support.microsoft.com/zh-tw/office/outlook-com-%E7%9A%84-pop-imap-%E5%92%8C-smtp-%E8%A8%AD%E5%AE%9A-d088b986-291d-42b8-9564-9c414e2aa040).

Please note that these steps may change due to updates from the service providers. It is recommended to regularly check for the latest setup methods.

## encrypt_sender_emailinfo.py
This script encrypts the sender’s email address and password. The encrypted credentials are then used by the `auto_send_email.py` script to send the email.
You need to create the file`sender_info.txt` include your email address and password. This script will genereate the output file `sender_info_encrypt.txt`.

Usage:

```bash
./encrypt_sender_emailinfo.py [-h] [-i INPUT] [-o OUTPUT] [-k KEYFILE]
```

Optional arguments:
```bash
-h, --help: Show the help message and exit.
-i INPUT, --input INPUT: The input file containing the email and password. (default: sender_info.txt)
-o OUTPUT, --output OUTPUT: The output file to write the encrypted credentials. (default: sender_info_encrypt.txt)
-k KEYFILE, --keyfile KEYFILE: The file to save the encryption key. (default: .key.txt)
```

## auto_send_email.py
This script sends an email with an optional attachment. 
Attension: execute the `encrypt_sender_emailinfo.py` before this scropt!
You need to add the email of receivers into a file named `receiver.list`. 

Usage:
```bash
auto_send_email.py [-h] [--subject SUBJECT] [--body BODY]
                          [--sender SENDER] [--receiver RECEIVER] [--key KEY]
                          [-a ATTACHMENT]
```

Optional arguments:

```bash
-h, --help: Show the help message and exit.
--subject SUBJECT: The subject of the email.
--body BODY: The body of the email.
--sender SENDER: The file containing the encrypted sender information. (default: sender_info_encrypt.txt)
--receiver RECEIVER: The file containing the receiver information. (default: receiver.list)
--key KEY: The file containing the encryption key. (default: .key.txt)
-a ATTACHMENT, --attachment ATTACHMENT: The file to be attached to the email.
```

## Installation
1. Clone this repository.
2. Install the required Python package: `pip install -r requirements.txt`
3. Run the `encrypt_sender_emailinfo.py` script to encrypt your email credentials.
4. Run the `auto_send_email.py` script to send an email.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



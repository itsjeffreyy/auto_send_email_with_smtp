# Auto Email Sender Project
auto_send_email_with_smtp

This project contains two Python scripts, `encrypt_sender_emailinfo.py` and `auto_send_email.py`, which are used to automate the process of sending emails.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.6 or later.
- You have installed the following Python package:
  - `pycryptodome==3.20.0` for cryptographic operations or `pycrypto`

You can install this package using pip:

```bash
pip install -r requirements.txt
```

## encrypt_sender_emailinfo.py
This script encrypts the sender’s email address and password. The encrypted credentials are then used by the auto_send_email.py script to send the email.

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

Usage:
```bash
./auto_send_email.py [-h] [--subject SUBJECT] [--body BODY] --sender SENDER
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

Installation
1. Clone this repository.
2. Install the required Python package: `pip install -r requirements.txt`
3. Run the `encrypt_sender_emailinfo.py` script to encrypt your email credentials.
4. Run the `auto_send_email.py` script to send an email.
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



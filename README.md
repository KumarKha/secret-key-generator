# Secret Key Generator

A simple Python CLI tool to generate secure secret keys for Flask applications (or any other use), with support for:

* base64
* hex
* raw byte string

You can also:

* copy the key to your clipboard
* save it to a file (such as `.env`)

## Features

* Generate cryptographically secure keys
* Supports base64, hex, or raw formats
* Optional clipboard copy
* Optional save to file
* Simple CLI interface

## Usage

### Run the script

python secret\_key\_generator.py \[options]

### Options

\--length        Length of key in bytes (default: 32)
\--format        Output format: base64, hex, or raw
\--copy          Copy the generated key to clipboard
\--save FILENAME Save the key to a file (ex: .env)

## Example commands

Generate a 32-byte base64 key (default):

python secret\_key\_generator.py

Generate a 64-byte hex key:

python secret\_key\_generator.py --length 64 --format hex

Generate and copy to clipboard:

python secret\_key\_generator.py --copy

Generate and save to .env:

python secret\_key\_generator.py --save .env

## Example Output

Flask Secret Key Generated:
• Length : 32 bytes
• Format : base64
• Key    : QWxhZGRpbjpvcGVuIHNlc2FtZQ==

## Requirements

* Python 3.x
* pyperclip module

Install pyperclip if needed:

pip install pyperclip

## Notes

* Useful for Flask SECRET\_KEY or other API tokens
* Recommended key length >= 32 bytes for Flask

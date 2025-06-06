import secrets
import base64
import argparse
import pyperclip
from pathlib import Path


def generate_secret_key(key_len: int, fmt: str) -> str:
	raw = secrets.token_bytes(key_len)
	if  fmt == "base64":
		return base64.b64encode(raw).decode('utf-8')
	elif fmt == "hex":
		return raw.hex()
	elif fwt == "raw":
		return str(raw)
	else:
		raise ValueError("Unsupported format. Choose 'base64', 'hex', 'raw'.")

def main():
    parser = argparse.ArgumentParser(description="Secret Key Generator")
    parser.add_argument('--length', type=int, default=32, help='Length in bytes (default: 32)' )
    parser.add_argument('--format', choices=['base64', 'hex', 'raw'], default='base64', help='Output format (default: base64)')
    parser.add_argument('--copy', action='store_true', help='Copy key to clipboard')
    parser.add_argument('--save', metavar='FILENAME', help='Save key to a file (e.g., .env)')

    args = parser.parse_args()

    key = generate_secret_key(args.length, args.format)

    print("\nFlask Secret Key Generated:")
    print(f"  • Length : {args.length} bytes")
    print(f"  • Format : {args.format}")
    print(f"  • Key    : {key}\n")

    if args.copy:
        pyperclip.copy(key)
        print("Key copied to clipboard")

    if args.save:
        try:
            path = Path(args.save)
            with path.open('a') as f:
                f.write(f'SECRET_KEY="{key}"\n')
            print(f"Key saved to {args.save}")
        except Exception as e:
            print(f"Failed to save key: {e}")


  		
if __name__ == "__main__":

	main()		
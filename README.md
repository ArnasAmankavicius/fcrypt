# fcrypt
Nothing spectacular. Takes a key and a file path and encrypts/decrypts it.

## Dependancies
- setuptools
- cryptography
- click

You can install the script by running `python3 build && python3 install`.
Note : You need setuptools for this to work.

## Usage
```bash
usage: fcrypt [-h] [-k KEY_PATH] [-v] [-d] [-y] [--version] path

Encrypt/Decrypt specified files using Fernet

positional arguments:
  path                  File to encrypt/decrypt

optional arguments:
  -h, --help            show this help message and exit
  -k KEY_PATH, --key-path KEY_PATH
                        Path to the encryption key
  -v, --verbose         Enable verbose
  -d, --decrypt         Decrypt the file
  -y, --yes             By-pass safety check
  --version             Display app version
```

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

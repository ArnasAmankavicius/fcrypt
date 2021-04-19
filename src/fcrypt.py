from . import encryptor, logger
import os
import argparse
from platform import system, release
from pathlib import Path
from time import sleep

__version__ = '1.0.0'

system_os = system()
system_release = release()

current_dir = os.getcwd()
default_key_path = '\\default.key' if system_os == 'Windows' else '/default.key'

key = None

info = f"""
#===================================================#
        Crypto - File Encryptor/Decryptor
             App written by h4sh

           Detected OS : {system_os}
           OS Release  : {system_release}
#===================================================#
"""

epilog = """
Exit Codes:
    * 0 -> Success.
    * 1 -> Supplied an invalid path.
    * 2 -> Failure to load the key file.
    * 3 -> Failure to decrypt a specified file.
    * 4 -> Failure to encrypt a specified file.
    * 5 -> User stopped the action
"""

def setup_parser():
    parser = argparse.ArgumentParser(description="Encrypt/Decrypt specified files using Fernet", 
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=epilog)
    parser.add_argument('path', metavar='path', type=str, help='File to encrypt/decrypt')
    parser.add_argument('-k', '--key-path', default=current_dir + default_key_path, type=str, help='Path to the encryption key')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the file')
    parser.add_argument('-y', '--yes', action='store_true', help='By-pass safety check')
    parser.add_argument('--version', action='version', version=f'Crypto @ {__version__}', help='Display app version')
    return parser.parse_args()

def exec():
    args = setup_parser()

    print(info)

    decrypt = args.decrypt
    override = args.yes

    if not Path(args.path).exists():
        logger.error(f'Invalid path : {args.path}')
        return 1

    if not Path(args.key_path).exists():
        logger.warn(f'Key not found : {args.key_path} | Generating new key...')
        key = encryptor.key_create()
        logger.verbose(f'Key generated. Writing to {args.key_path}', args.verbose)
        encryptor.key_write(key, args.key_path)
        logger.success(f'New key has been written to: {args.key_path}')
    else:
        logger.verbose(f'Key found! Loading into memory...', args.verbose)
        key = encryptor.key_load(args.key_path)
        if key != None:
            logger.success(f'Key loaded into memory!')
        else:
            logger.error(f'Unable to load the key. Exiting...')
            return 2
    
    if not override and not decrypt:
        logger.warn(f'Are you sure you wish to encrypt "{args.path}"?')
        u = input('(y/n)> ').lower()
        if u not in ('y', 'ye', 'yes'):
            logger.info('Task stopped by the user')
            return 5

    if decrypt:
        logger.info(f'Decrypting -> {args.path}...')
        try:
            encryptor.file_decrypt(key, args.path, args.path)
            logger.success(f'Decryption complete!')
        except Exception as e:
            logger.error(f'Failed to decrypt -> {e}')
            return 3
    else:
        logger.info(f'Encrypting -> {args.path}...')
        try:
            encryptor.file_encrypt(key, args.path, args.path)
            logger.success(f'Encryption complete!')
        except Exception as e:
            logger.error(f'Failed to encrypt -> {e}')
            return 4
    return 0
    
if __name__ == '__main__':
    exec()
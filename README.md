# Hybrid Encryption with RSA and AES

## Overview

This project implements a hybrid encryption system in Python, combining the strengths of RSA and AES algorithms to securely encrypt and decrypt files. The system utilizes RSA for secure key exchange and AES for efficient data encryption, ensuring both security and performance.

## Features

- **RSA Key Generation**: Generate 2048-bit RSA public and private keys.
- **Hybrid Encryption**: Encrypt files using AES symmetric encryption, with the AES key securely encrypted using RSA.
- **Hybrid Decryption**: Decrypt files by first decrypting the AES key using RSA, then decrypting the file data using AES.

## Prerequisites

- Python 3.x
- [PyCryptodome library](https://pycryptodome.readthedocs.io/en/latest/)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/JatinGuptaCodeForge/Hybrid-Encryption-with-RSA-and-AES.git
   cd hybrid-encryption
   ```

2. **Install Dependencies**:
   Install the required Python libraries using pip:
   ```bash
   pip install pycryptodome
   ```

## Usage

1. **Generate RSA Keys**:
   Run the script to generate RSA public and private keys:
   ```bash
   python hybrid_encryption.py --generate-keys
   ```
   This will create `private.pem` and `public.pem` files in the current directory.

2. **Encrypt a File**:
   To encrypt a file, use the following command:
   ```bash
   python hybrid_encryption.py --encrypt --file <path_to_file>
   ```
   Replace `<path_to_file>` with the path to the file you wish to encrypt. The encrypted file will be saved with a `.enc` extension.

3. **Decrypt a File**:
   To decrypt a previously encrypted file, use:
   ```bash
   python hybrid_encryption.py --decrypt --file <path_to_encrypted_file>
   ```
   Replace `<path_to_encrypted_file>` with the path to the `.enc` file. The decrypted file will be saved with a `_decrypted` suffix.

## Code Structure

- `hybrid_encryption.py`: Main script containing functions for RSA key generation, encryption, and decryption.

## Security Considerations

- **Key Management**: Ensure that the `private.pem` file is stored securely and is not exposed to unauthorized users.
- **File Handling**: Be cautious with file permissions and ensure that sensitive data is handled appropriately during encryption and decryption processes.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [PyCryptodome Documentation](https://pycryptodome.readthedocs.io/en/latest/)
- [Hybrid Encryption in Python](https://medium.com/@igorfilatov/hybrid-encryption-in-python-3e408c73970c)

For a visual demonstration of hybrid encryption, you might find this video helpful:

videoImplementing Hybrid RSA-AES Encryption in Pythonturn0search3 

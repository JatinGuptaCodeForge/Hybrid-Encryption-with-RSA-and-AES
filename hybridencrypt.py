from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os

# Function to generate RSA keys
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

  
    with open("private.pem", "wb") as priv_file:
        priv_file.write(private_key)
    with open("public.pem", "wb") as pub_file:
        pub_file.write(public_key)

    print("RSA keys generated and saved.")

# Function to load RSA keys from files
def load_rsa_keys():
    try:
        with open("private.pem", "rb") as priv_file:
            private_key = RSA.import_key(priv_file.read())
        with open("public.pem", "rb") as pub_file:
            public_key = RSA.import_key(pub_file.read())
        return private_key, public_key
    except FileNotFoundError:
        print("RSA key files not found. Please generate keys first.")
        return None, None

def hybrid_encrypt(file_path, public_key):
    try:
       
        aes_key = get_random_bytes(32)  
        iv = get_random_bytes(16)       

       
        aes_cipher = AES.new(aes_key, AES.MODE_CBC, iv)

        with open(file_path, "rb") as f:
            file_data = f.read()

        encrypted_data = aes_cipher.encrypt(pad(file_data, AES.block_size))

        rsa_cipher = PKCS1_OAEP.new(public_key)
        encrypted_aes_key = rsa_cipher.encrypt(aes_key)

        enc_file_path = file_path + ".enc"

        with open(enc_file_path, "wb") as f_enc:
            f_enc.write(iv + encrypted_aes_key + encrypted_data)

        print(f"File '{file_path}' encrypted successfully as '{enc_file_path}'.")

    except FileNotFoundError:
        print(f"File '{file_path}' not found! Please check the file path.")

def hybrid_decrypt(enc_file_path, private_key):
    try:
        with open(enc_file_path, "rb") as f_enc:
            iv = f_enc.read(16) 
            encrypted_aes_key = f_enc.read(private_key.size_in_bytes()) 
            encrypted_data = f_enc.read()
        rsa_cipher = PKCS1_OAEP.new(private_key)
        aes_key = rsa_cipher.decrypt(encrypted_aes_key)

        aes_cipher = AES.new(aes_key, AES.MODE_CBC, iv)

        decrypted_data = unpad(aes_cipher.decrypt(encrypted_data), AES.block_size)

        original_file_name = enc_file_path.replace(".enc", "")
        
        base_name, ext = os.path.splitext(original_file_name)
        new_file_name = base_name + "_decrypted" + ext

        with open(new_file_name, "wb") as f_dec:
            f_dec.write(decrypted_data)

        print(f"File '{enc_file_path}' decrypted successfully as '{new_file_name}'.")

    except FileNotFoundError:
        print(f"File '{enc_file_path}' not found! Please check the file path.")
    except ValueError as e:
        print(f"Decryption failed: {str(e)}")

# Example usage of hybrid encryption and decryption system
if __name__ == "__main__":
    try:
        choice = input("Do you want to (G)enerate keys, (E)ncrypt or (D)ecrypt?: ").lower()

        if choice == 'g':
            generate_rsa_keys()

        elif choice == 'e':
            private_key, public_key = load_rsa_keys()
            if public_key is None:
                print("Cannot proceed without RSA keys.")
            else:
                file_to_encrypt = input("Enter the path of the file to encrypt: ")
                hybrid_encrypt(file_to_encrypt, public_key)

        elif choice == 'd':
            private_key, public_key = load_rsa_keys()
            if private_key is None:
                print("Cannot proceed without RSA keys.")
            else:
                file_to_decrypt = input("Enter the path of the encrypted file (.enc): ")
                hybrid_decrypt(file_to_decrypt, private_key)

        else:
            print("Invalid choice! Please enter 'G' for generating keys, 'E' for encryption or 'D' for decryption.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
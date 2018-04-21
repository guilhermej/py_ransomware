import pyaes

# Open file
file_name = "foto2.jpg"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# Decrypt
key = "0123456789abcdef"  # 16 bytes key - change for your key
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# Save file
new_file_name = "descriptografado.jpg"  # Path to drop file
new_file = open(new_file_name, 'wb')
new_file.write(decrypt_data)
new_file.close()
from Crypto.Cipher import AES
# passing the first 16 bytes from the decrypted AES_Encrypted_Key
key = bytes.fromhex()
#Empty space to apply cipher
emp = 16 * b'\x00'
#initialize the cipher
ciph = AES.new(key, AES.MODE_CBC, emp=emp)
#Reading the remaing part of t.wnry file(rem_large_chunk)
r = open("rem_large_chunk.bin", "rb").read()
d = ciph.decrypt(r)
#Write into another file (Rem_large_chunk.dec)
new_dec_file = open("rem_large_chunk.dec", "wb")
new_dec_file.write(d)
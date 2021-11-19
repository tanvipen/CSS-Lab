from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
plaintxt = b"This is a top secret."
ciphertxt = "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9"
result = []
file = open('words.txt', 'r')
lines = file.readlines()
words = [str.strip(line) for line in lines]
for word in words:
    if len(word) >= 16:
        continue
    word = word.lower()
    key = word.encode() + b' '*(16-len(word))
    cipher = AES.new(key, AES.MODE_CBC, iv=bytes.fromhex('0'*32))
    ciphertext = cipher.encrypt(pad(plaintxt, AES.block_size))
    match = "NO MATCH"
    if bytes.hex(ciphertext) == ciphertxt:
        match = "MATCH"
        result.append(word)
    bytes.hex(ciphertext)
    print(word,match)
print("\n\nResulting Key:",result)

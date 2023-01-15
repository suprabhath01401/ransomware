from Crypto.PublicKey import RSA

key = RSA.generate(2048)
privateKey = key.export_key()
publicKey = key.publickey().export_key()

# save private key to file
with open('private.pem', 'wb') as f:
    f.write(privateKey)

# save public key to file
with open('public.pem', 'wb') as f:
    f.write(publicKey)
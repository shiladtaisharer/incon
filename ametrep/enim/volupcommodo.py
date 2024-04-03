from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key

# Load your private key from a file
with open('private_key.pem', 'rb') as key_file:
    private_key = load_pem_private_key(key_file.read(), password=None, backend=default_backend())

# Data to sign
data = b"Data to sign"

# Sign the data
signature = private_key.sign(
    data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Save the signature to a file
with open('signature.sig', 'wb') as signature_file:
    signature_file.write(signature)

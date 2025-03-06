import zlib  # For compression
import base64  # For encoding

# 2️⃣ Presentation Layer (Encoding, Compression, Encryption)
class PresentationLayer:
    def send_data(self, data):
        print("[Presentation Layer] Encoding, Compressing, Encrypting data")
        compressed = zlib.compress(data.encode())
        encrypted = base64.b64encode(compressed).decode()
        return encrypted

    def receive_data(self, data):
        print("[Presentation Layer] Decrypting, Decompressing, Decoding data")
        compressed = base64.b64decode(data.encode())
        decompressed = zlib.decompress(compressed).decode()
        return decompressed
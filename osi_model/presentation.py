import zlib  # For compression
import base64  # For encoding

# Presentation Layer (Encoding, Compression, Encryption)
class PresentationLayer:
    def send_data(self, data):
        print("[Presentation Layer] Encoding, Compressing, Encrypting data")
        compressed = zlib.compress(data.encode())
        encrypted = base64.b64encode(compressed).decode()
        return encrypted

    def receive_data(self, data):
        print("[Presentation Layer] Decrypting, Decompressing, Decoding data")
        
        # ✅ Ensure data is bytes before decoding
        if isinstance(data, str):  
            data = data.encode()  # Convert str to bytes if needed

        compressed = base64.b64decode(data)  # ✅ Remove .encode()
        decompressed = zlib.decompress(compressed)
        return decompressed.decode()  # ✅ Convert back to string
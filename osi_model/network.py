# Network Layer (Handles IP addressing, routing)
class NetworkLayer:
    def send_data(self, data, ip="192.168.1.1"):
        print("[Network Layer] Adding IP header")
        ip = ip.encode()  # Convert IP to bytes
        return ip + b":" + data  # Everything remains bytes

    def receive_data(self, data):
        print("[Network Layer] Removing IP header")
        parts = data.split(b":", 1)  # Use b":" for bytes
        if len(parts) < 2:
            raise ValueError("Invalid IP header format")  # Handle errors properly
        
        ip, message = parts
        return message  # Message remains in bytes
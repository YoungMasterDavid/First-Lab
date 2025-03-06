import struct

# Transport Layer (Adds sequencing, error handling)
class TransportLayer:
    def send_data(self, data):
        print("[Transport Layer] Adding sequence number")
        seq_num = 1  # Simple example (in real TCP, this would increment)
        return struct.pack("I", seq_num) + data.encode()

    def receive_data(self, data):
        print("[Transport Layer] Validating sequence number")
        seq_num = struct.unpack("I", data[:4])[0]
        message = data[4:].decode()
        return message
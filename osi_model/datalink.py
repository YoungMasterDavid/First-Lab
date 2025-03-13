# Data Link Layer (Handles MAC addressing & frame transmission)
class DataLinkLayer:
    def send_data(self, data, mac="AA:BB:CC:DD:EE:FF"):
        print("[Data Link Layer] Adding MAC header")
        mac_bytes = mac.encode()  # Convert MAC address to bytes
        return mac_bytes + b":" + data  # Keep everything in bytes

    def receive_data(self, data):
        print("[Data Link Layer] Removing MAC header")
        
        # MAC address is always 17 characters (6 pairs of hex + 5 colons)
        mac_end_index = data.find(b":192.168")  # Find where IP starts
        if mac_end_index == -1:
            raise ValueError(f"Invalid MAC header format: {data}")  # Debugging
        
        # Extract and remove MAC header
        mac_header = data[:mac_end_index]  # Extract MAC (for debugging)
        remaining_data = data[mac_end_index + 1:]  # Remove MAC

        # print(f"[DEBUG] MAC Header: {mac_header}, Remaining Data: {remaining_data}")
        return remaining_data
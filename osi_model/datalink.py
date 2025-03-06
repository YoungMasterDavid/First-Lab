# 6️⃣ Data Link Layer (Handles MAC addressing & frame transmission)
class DataLinkLayer:
    def send_data(self, data, mac="AA:BB:CC:DD:EE:FF"):
        print("[Data Link Layer] Adding MAC header")
        return f"MAC:{mac}:{data}"

    def receive_data(self, data):
        print("[Data Link Layer] Removing MAC header")
        _, mac, message = data.split(":", 2)
        return message
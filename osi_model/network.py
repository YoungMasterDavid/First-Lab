# 5️⃣ Network Layer (Handles IP addressing, routing)
class NetworkLayer:
    def send_data(self, data, ip="192.168.1.1"):
        print("[Network Layer] Adding IP header")
        return f"IP:{ip}:{data}"

    def receive_data(self, data):
        print("[Network Layer] Removing IP header")
        _, ip, message = data.split(":", 2)
        return message
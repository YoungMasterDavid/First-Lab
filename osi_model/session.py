from hashlib import sha256  # For simple encryption

# 3️⃣ Session Layer (Manages sessions, connections)
class SessionLayer:
    def send_data(self, data):
        print("[Session Layer] Creating session ID and adding handshake")
        session_id = sha256(data.encode()).hexdigest()[:8]
        return f"SESSION:{session_id}:{data}"

    def receive_data(self, data):
        print("[Session Layer] Validating session")
        _, session_id, message = data.split(":", 2)
        return message
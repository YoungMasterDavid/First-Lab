import socket
import pickle

class PhysicalLayer:
    def __init__(self, mode="server"):
        self.mode = mode
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # ✅ Allows reuse of port
        self.host = "127.0.0.1"
        self.port = 5000

    def send_data(self, data):
        print("[Physical Layer] Converting to bits & sending over network. Mode:", self.mode)
        if self.mode == "server":
            self.sock.bind((self.host, self.port))
            self.sock.listen(1)
            print("[Server] Waiting for connection...")
            conn, addr = self.sock.accept()
            conn.sendall(pickle.dumps(data))
            conn.close()
            print("[Server] Data sent successfully")
        else:
            self.sock.connect((self.host, self.port))
            self.sock.sendall(pickle.dumps(data))
            self.sock.close()
            print("[Client] Data sent successfully")

    def receive_data(self):
        print("[Physical Layer] Receiving bits & converting back...")
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        conn, addr = self.sock.accept()
        data = pickle.loads(conn.recv(4096))  # Increased buffer size
        conn.close()
        return data

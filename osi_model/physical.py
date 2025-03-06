import socket
import pickle

# 7️⃣ Physical Layer (Simulates raw bit transmission over sockets)
class PhysicalLayer:
    def __init__(self, mode="server"):
        self.mode = mode
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "127.0.0.1"
        self.port = 5000

    def send_data(self, data):
        print("[Physical Layer] Converting to bits & sending over network")
        if self.mode == "server":
            self.sock.bind((self.host, self.port))
            self.sock.listen(1)
            conn, addr = self.sock.accept()
            conn.sendall(pickle.dumps(data))
            conn.close()
        else:
            self.sock.connect((self.host, self.port))
            self.sock.sendall(pickle.dumps(data))
            self.sock.close()
import sys
from osi_model.application import ApplicationLayer
from osi_model.presentation import PresentationLayer
from osi_model.session import SessionLayer
from osi_model.transport import TransportLayer
from osi_model.network import NetworkLayer
from osi_model.datalink import DataLinkLayer
from osi_model.physical import PhysicalLayer

def main(mode):
    message = "Hello, OSI Model!"

    app = ApplicationLayer()
    pres = PresentationLayer()
    sess = SessionLayer()
    trans = TransportLayer()
    net = NetworkLayer()
    link = DataLinkLayer()
    phys = PhysicalLayer(mode)

    if mode == "server":
        print("\n[Server is running...]")
        received_data = phys.receive_data()
        # print("\n[Server is receiving data... ], received_data:", received_data)
        received_data = link.receive_data(received_data)
        # print("\n[Server is receiving data... ], received_data:", received_data)
        received_data = net.receive_data(received_data)
        # print("\n[Server is receiving data... ], received_data:", received_data)
        received_data = trans.receive_data(received_data)
        # bprint("\n[Server is receiving data... ], received_data:", received_data)
        received_data = sess.receive_data(received_data)
        # print("\n[Server is receiving data... ], received_data:", received_data)
        received_data = pres.receive_data(received_data)
        # print("\n[Server is receiving data... ], received_data:", received_data)
        final_message = app.receive_data(received_data)
        # print("\n[Final Output] Received Message:", final_message)

    elif mode == "client":
        print("\n[Client is sending data...]")
        data = app.send_data(message)
        data = pres.send_data(data)
        data = sess.send_data(data)
        data = trans.send_data(data)
        data = net.send_data(data)
        data = link.send_data(data)
        phys.send_data(data)

    else:
        print("Invalid mode! Use 'server' or 'client'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m osi_model.main <server|client>")
        sys.exit(1)

    main(sys.argv[1])

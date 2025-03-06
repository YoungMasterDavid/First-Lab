from osi_model.application import ApplicationLayer
from osi_model.presentation import PresentationLayer
from osi_model.session import SessionLayer
from osi_model.transport import TransportLayer
from osi_model.network import NetworkLayer
from osi_model.datalink import DataLinkLayer
from osi_model.physical import PhysicalLayer

def main():
    message = "Hello, OSI Model!"

    app = ApplicationLayer()
    pres = PresentationLayer()
    sess = SessionLayer()
    trans = TransportLayer()
    net = NetworkLayer()
    link = DataLinkLayer()
    phys = PhysicalLayer()

    data = app.send_data(message)
    data = pres.send_data(data)
    data = sess.send_data(data)
    data = trans.send_data(data)
    data = net.send_data(data)
    data = link.send_data(data)
    phys.send_data(data)

    print("\n[Transmission complete]\n")

    received_data = phys.receive_data()
    received_data = link.receive_data(received_data)
    received_data = net.receive_data(received_data)
    received_data = trans.receive_data(received_data)
    received_data = sess.receive_data(received_data)
    received_data = pres.receive_data(received_data)
    final_message = app.receive_data(received_data)

    print("\n[Final Output] Received Message:", final_message)

if __name__ == "__main__":
    main()

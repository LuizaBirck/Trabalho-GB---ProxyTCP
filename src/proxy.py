import socket
import threading
import time
from metrics import init_log, log_metrics

LISTEN_HOST = '127.0.0.1'
LISTEN_PORT = 8000
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9000

init_log()

# Configurações de otimização
DELAYED_ACK_ENABLED = True
TCP_PACING_ENABLED = True
DELAYED_ACK_BASE = 0.05  # 50 ms de atraso base
TCP_PACING_DELAY = 0.01   # 10 ms entre pacotes

def handle_client(client_socket):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((SERVER_HOST, SERVER_PORT))

    def forward(source, destination, measure_rtt=False, pacing=False, delayed_ack=False):
        while True:
            data = source.recv(4096)
            if not data:
                break

            # Medir RTT
            if measure_rtt:
                start = time.time()

            # TCP pacing
            if pacing:
                time.sleep(TCP_PACING_DELAY)

            destination.sendall(data)

            # Delayed ACK
            if delayed_ack:
                time.sleep(DELAYED_ACK_BASE)

            if measure_rtt:
                end = time.time()
                rtt = (end - start) * 1000 
                log_metrics(rtt)

    # Thread cliente - servidor
    t1 = threading.Thread(
        target=forward,
        args=(client_socket, server_socket, True, TCP_PACING_ENABLED, False)
    )
    # Thread servidor - cliente
    t2 = threading.Thread(
        target=forward,
        args=(server_socket, client_socket, False, False, DELAYED_ACK_ENABLED)
    )

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    client_socket.close()
    server_socket.close()

# Inicializa proxy
proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy.bind((LISTEN_HOST, LISTEN_PORT))
proxy.listen()
print(f"Proxy rodando em {LISTEN_HOST}:{LISTEN_PORT}")

while True:
    client_conn, client_addr = proxy.accept()
    print(f"Conexão de {client_addr} recebida pelo proxy")
    threading.Thread(target=handle_client, args=(client_conn,)).start()

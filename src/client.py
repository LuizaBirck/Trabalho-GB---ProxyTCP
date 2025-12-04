import socket
import time
from metrics import init_log, log_metrics

HOST = '127.0.0.1'
PORT = 8000  
NUM_MENSAGENS = 20  

init_log()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    total_bytes = 0
    start_total = time.time()
    
    for i in range(NUM_MENSAGENS):
        mensagem = f"Mensagem {i}".encode()
        total_bytes += len(mensagem)
        
        start = time.time()
        s.sendall(mensagem)
        data = s.recv(1024)
        end = time.time()
        
        rtt = (end - start) * 1000  # RTT em ms
        print(f"Mensagem {i} recebida: {data.decode()}, RTT estimado: {rtt:.2f} ms")
        
        # Registrar RTT no CSV
        log_metrics(rtt)

    end_total = time.time()
    
    # Calcular throughput total
    duration_sec = end_total - start_total
    throughput_mbps = (total_bytes * 8) / (duration_sec * 1_000_000)
    print(f"\nThroughput total: {throughput_mbps:.4f} Mbps em {duration_sec:.2f} s")
    
    # Registrar throughput no CSV
    log_metrics(rtt=0, throughput=throughput_mbps, retransmissions=0)

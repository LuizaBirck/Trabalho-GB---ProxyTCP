import csv
import time
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), '../logs/metricas.csv')

def init_log():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'RTT_ms', 'throughput_Mbps', 'retransmissions'])

def log_metrics(rtt, throughput=0, retransmissions=0):
    timestamp = time.time()
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, rtt, throughput, retransmissions])


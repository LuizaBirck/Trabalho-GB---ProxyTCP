import pandas as pd
import matplotlib.pyplot as plt
import os

# Caminho do CSV gerado pelo proxy
csv_path = '../logs/metricas.csv'

# Verifica se o CSV existe
if not os.path.exists(csv_path):
    print(f"Erro: arquivo {csv_path} não encontrado!")
    exit()

# Lê o CSV
df = pd.read_csv(csv_path)

# Confere as colunas disponíveis
print("Colunas no CSV:", df.columns)

# Gráfico de RTT
plt.figure(figsize=(10,5))
plt.plot(df['timestamp'], df['RTT_ms'], marker='o', color='blue')
plt.title("RTT ao longo do tempo")
plt.xlabel("Timestamp")
plt.ylabel("RTT (ms)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../logs/RTT_graph.png')  
plt.show()

# Gráfico de Throughput
plt.figure(figsize=(10,5))
plt.plot(df['timestamp'], df['throughput_Mbps'], marker='o', color='orange')
plt.title("Throughput ao longo do tempo")
plt.xlabel("Timestamp")
plt.ylabel("Throughput (Mbps)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../logs/Throughput_graph.png') 
plt.show()

print("Gráficos salvos em ../logs/")


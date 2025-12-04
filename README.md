# Trabalho GB - Desenvolvimento de Proxy TCP para Monitoramento e Otimização de Conexões

## Descrição
Projeto de Proxy TCP que monitora e otimiza conexões, coletando métricas como RTT, throughput e retransmissões.  
Inclui políticas de otimização: TCP pacing e Delayed ACK.

## Estrutura do projeto
- src/
  - proxy.py → Proxy TCP principal
  - client.py → Programa cliente
  - server.py → Programa servidor
  - metrics.py → Coleta de métricas
  - plot_metrics.py → Geração de gráficos
- logs/ → Arquivo metricas.csv e gráficos
- README.md → Este arquivo
- relatório.docx → Relatório final com testes e análise

## Como usar
1. Preparar a pasta de logs:
```bash
mkdir -p logs
rm -f logs/metricas.csv
```

2. Rodar o servidor:
```bash
python3 src/server.py
```

3. Rodar o proxy:
```bash
python3 src/proxy.py
```
- Para desativar otimizações, configure no arquivo `proxy.py`:
```python
TCP_PACING_ENABLED = False
DELAYED_ACK_ENABLED = False
```

4. Rodar o cliente:
```bash
python3 src/client.py
```

## Testes de rede
- Exemplo: atraso de 50ms e 1% de perda:
```bash
sudo tc qdisc add dev enp0s3 root netem delay 50ms loss 1%
```
- Limpar regras após os testes:
```bash
sudo tc qdisc del dev enp0s3 root
```

## Gerar gráficos
```bash
pip3 install pandas matplotlib
python3 src/plot_metrics.py
```
- Os gráficos serão salvos em `logs/`: `RTT_graph.png` e `Throughput_graph.png`.


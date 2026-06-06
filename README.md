# Trabalho Final - Inteligência Artificial (MATA64) 🚦

**Status do Projeto:** Em desenvolvimento 

Repositório destinado ao Trabalho Final da disciplina MATA64 - Inteligência Artificial, da Universidade Federal da Bahia (UFBA). 

O objetivo deste projeto é construir e treinar um agente autônomo utilizando **Aprendizado por Reforço** (Reinforcement Learning) para solucionar um problema real de mobilidade urbana: **a otimização do tempo de semáforos em cruzamentos para minimizar o congestionamento**.

## Arquitetura do Projeto

O agente toma decisões (abrir/fechar o semáforo) com base no estado atual do cruzamento (número de carros nas vias). Para isso, utilizamos a seguinte stack de tecnologias:

* **Python 3**
* **Eclipse SUMO (Simulation of Urban MObility):** Simulador de tráfego de código aberto que lida com a física e o ambiente visual do trânsito.
* **SUMO-RL:** Biblioteca que converte o simulador SUMO em um ambiente padrão compatível com a interface do *Gymnasium*.
* **Gymnasium:** Interface padrão para comunicação entre o agente e o ambiente.
* **Stable-Baselines3 (SB3):** Biblioteca que fornece a implementação do algoritmo **PPO (Proximal Policy Optimization)**, que atua como o "cérebro" da nossa rede neural.

## Estrutura do Repositório

* `nets/`: Contém os arquivos XML gerados pelo NetEdit (SUMO) que modelam o ambiente físico.
  * `cruzamento.net.xml`: O mapa físico do cruzamento, vias e semáforos.
  * `fluxo.rou.xml`: As rotas e a taxa de geração contínua de veículos.
* `src/`: Scripts de treinamento e execução.
  * `train.py`: Script principal que instancia o ambiente, configura o algoritmo PPO e inicia o ciclo de aprendizado do agente.
* `outputs/`: (Gerado automaticamente) Onde o SUMO-RL salvará os logs e métricas em CSV do desempenho do agente.

## Como executar localmente

1. Certifique-se de ter o **Eclipse SUMO** instalado na sua máquina e a variável de ambiente `SUMO_HOME` configurada.
2. Instale o gerenciador de pacotes `uv`.
3. Crie e ative o ambiente virtual:
   ```bash
   uv venv
   # No Windows:
   .\.venv\Scripts\activate
   # No Linux/Mac:
   source .venv/bin/activate
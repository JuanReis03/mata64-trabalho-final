# Trabalho Final - Inteligência Artificial (MATA64) 🚦

**Status do Projeto:** Em desenvolvimento 

Repositório destinado ao Trabalho Final da disciplina MATA64 - Inteligência Artificial, da Universidade Federal da Bahia (UFBA). 

O objetivo deste projeto é construir e treinar um agente autônomo utilizando **Aprendizado por Reforço** (Reinforcement Learning) para solucionar um problema real de mobilidade urbana: **a otimização do tempo de semáforos em cruzamentos para minimizar o congestionamento**.

## Arquitetura do Projeto

O agente toma decisões (abrir/fechar o semáforo) com base no estado atual do cruzamento (número de carros nas vias e tamanho das filas). Para isso, utilizamos a seguinte stack de tecnologias:

* **Python 3**
* **Eclipse SUMO (Simulation of Urban MObility):** Simulador de tráfego de código aberto que lida com a física e o ambiente visual do trânsito.
* **SUMO-RL:** Biblioteca que converte o simulador SUMO em um ambiente padrão compatível com a interface do *Gymnasium*.
* **Gymnasium:** Interface padrão para comunicação entre o agente e o ambiente.
* **Stable-Baselines3 (SB3):** Biblioteca que fornece as implementações das Redes Neurais e dos algoritmos de aprendizado aplicados no projeto: **DQN (Deep Q-Network), A2C (Advantage Actor-Critic) e PPO (Proximal Policy Optimization)**.

## O Desafio do *Reward Hacking* (Inanição)
Durante a modelagem, enfrentamos o clássico problema de *Reward Hacking*: a IA percebeu que era "mais barato" penalizar os carros da via transversal para sempre do que fechar o sinal e parar o fluxo maior da via principal. Para solucionar essa "injustiça" matemática e forçar a alternância do semáforo, o ambiente foi aprimorado com:
* **Função de recompensa baseada em filas (`reward_fn='queue'`):** Punição severa pelo número absoluto de carros parados.
* **Trava de Segurança (`max_green=30`):** Tempo máximo permitido de sinal verde contínuo, simulando um controlador real.

## Estrutura do Repositório

* `nets/`: Contém os arquivos XML gerados pelo NetEdit (SUMO) que modelam o ambiente físico.
  * `cruzamento.net.xml`: O mapa físico do cruzamento, vias e a lógica do semáforo central.
  * `fluxo.rou.xml`: As rotas e a taxa de geração de veículos desbalanceada (para simular uma avenida principal vs. via transversal).
* `src/`: Scripts de treinamento e execução.
  * `treino.py` (DQN), `treino_a2c.py`, `treino_ppo.py`: Scripts independentes que instanciam o ambiente e treinam cada algoritmo específico.
  * `teste_modelo.py`: Script de avaliação para carregar um agente já treinado e rodar a simulação gráfica (ainda não implementado).
* `outputs/`: (Gerado automaticamente) Onde o SUMO-RL salvará os logs e métricas em CSV do desempenho do agente para a plotagem dos gráficos.

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
4. 
   ``` bash 
    uv pip install gymnasium stable-baselines3[extra] sumo-rl
5. Para treinar um modelo:
   ``` bash 
      python src/treino.py       # Treina usando o algoritmo DQN
      python src/treino_a2c.py   # Treina usando o algoritmo A2C
      python src/treino_ppo.py   # Treina usando o algoritmo PPO
6. Para treinar visualmente um modelo treinado(ainda não implementamos):
    ``` bash 
      python src/teste_modelo.py

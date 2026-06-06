import os
import gymnasium as gym
import sumo_rl
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import EvalCallback
from stable_baselines3.common.env_util import make_vec_env

def main():
    # 1. Definição dos caminhos para os arquivos do SUMO
    # (Estes arquivos representam o nosso ambiente físico)
    net_file = os.path.join('nets', 'cruzamento.net.xml')
    route_file = os.path.join('nets', 'fluxo.rou.xml')

    # 2. Configuração do Ambiente SUMO-RL
    # O sumo-rl registra o ambiente no Gymnasium automaticamente
    env = gym.make('sumo-rl-v0',
                   net_file=net_file,
                   route_file=route_file,
                   out_csv_name='outputs/ppo_results',
                   use_gui=True, # Mude para False para treinar mais rápido depois
                   num_seconds=3600) # Simular 1 hora de trânsito
    
    # Vetorizar o ambiente é uma boa prática para o PPO no SB3
    # env = make_vec_env(lambda: env, n_envs=1)

    print("Ambiente configurado. Iniciando a construção do modelo PPO...")

    # 3. Inicialização do Agente PPO
    # MlpPolicy indica que usaremos uma Rede Neural clássica para os Estados e Ações
    model = PPO("MlpPolicy", 
                env, 
                verbose=1, 
                learning_rate=0.0003, 
                gamma=0.99) # Fator de desconto: o quão o agente valoriza o futuro

    # 4. Treinamento do Agente
    # Timesteps é a quantidade total de ações que o agente vai tomar no simulador
    print("Iniciando o treinamento...")
    model.learn(total_timesteps=20000)

    # 5. Salvando o conhecimento (Os 'pesos' da rede neural)
    model.save("ppo_semaforo_model")
    print("Modelo salvo com sucesso!")

    env.close()

if __name__ == "__main__":
    main()
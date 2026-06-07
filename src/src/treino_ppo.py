import os
import gymnasium as gym
import sumo_rl
from stable_baselines3 import PPO

def main():
    # Definição dos caminhos para os arquivos do SUMO
    net_file = os.path.join('nets', 'cruzamento.net.xml')
    route_file = os.path.join('nets', 'fluxo.rou.xml')

    # Configuração do Ambiente SUMO-RL
    # out_csv_name configurado especificamente para o PPO
    env = gym.make('sumo-rl-v0',
                   net_file=net_file,
                   route_file=route_file,
                   out_csv_name='outputs/ppo_results',
                   use_gui=True, 
                   num_seconds=3600) 

    print("Ambiente configurado. Iniciando a construção do modelo PPO...")

    # Inicialização do Agente PPO (Proximal Policy Optimization)
    model = PPO("MlpPolicy", 
                env, 
                verbose=1, 
                learning_rate=0.0003, 
                gamma=0.99)

    print("Iniciando o treinamento do PPO...")
    model.learn(total_timesteps=20000)

    # Salvando o conhecimento
    model.save("ppo_semaforo_model")
    print("Modelo PPO salvo com sucesso!")

    env.close()

if __name__ == "__main__":
    main()
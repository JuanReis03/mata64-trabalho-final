import os
import gymnasium as gym
import sumo_rl
from stable_baselines3 import A2C

def main():
    # Definição dos caminhos para os arquivos do SUMO
    net_file = os.path.join('nets', 'cruzamento.net.xml')
    route_file = os.path.join('nets', 'fluxo.rou.xml')

    # Configuração do Ambiente SUMO-RL
    # out_csv_name configurado especificamente para o A2C
    env = gym.make('sumo-rl-v0',
                   net_file=net_file,
                   route_file=route_file,
                   out_csv_name='outputs/a2c_results',
                   use_gui=False, 
                   num_seconds=3600,
                   reward_fn='queue',
                   max_green=30)

    print("Ambiente configurado. Iniciando a construção do modelo A2C (Temporal Difference)...")

    # Inicialização do Agente A2C (Advantage Actor-Critic)
    model = A2C("MlpPolicy", 
                env, 
                verbose=1, 
                learning_rate=0.0007, 
                gamma=0.99)

    print("Iniciando o treinamento do A2C...")
    model.learn(total_timesteps=20000)

    # Salvando o conhecimento do Ator e do Crítico
    model.save("a2c_semaforo_model")
    print("Modelo A2C salvo com sucesso!")

    env.close()

if __name__ == "__main__":
    main()
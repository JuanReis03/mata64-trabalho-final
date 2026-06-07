import os
import gymnasium as gym
import sumo_rl
from stable_baselines3 import DQN

def main():
    # Definição dos caminhos para os arquivos do SUMO
    net_file = os.path.join('nets', 'cruzamento.net.xml')
    route_file = os.path.join('nets', 'fluxo.rou.xml')

    # 1. Ambiente configurado SEM o ts_id (ele achará o J14 automaticamente)
    env = gym.make('sumo-rl-v0',
                   net_file=net_file,
                   route_file=route_file,
                   out_csv_name='outputs/dqn_results',
                   use_gui=False, 
                   num_seconds=3600,
                   reward_fn='queue',
                   max_green=30) 
    
    print(f"🕵️ Semáforos encontrados e controlados pela IA: {env.unwrapped.ts_ids}")
    print("Ambiente configurado. Iniciando a construção do modelo DQN (Deep Q-Learning)...")

    # 2. Inicialização do Agente DQN (A Evolução do Q-Learning)
    # A política MlpPolicy aproxima a Tabela Q usando uma rede neural
    model = DQN("MlpPolicy", 
                env, 
                verbose=1, 
                learning_rate=0.001, 
                buffer_size=10000,
                exploration_fraction=0.1) # Q-Learning precisa de "exploração" no início

    print("Iniciando o treinamento...")
    model.learn(total_timesteps=20000)

    # 3. Salvando o conhecimento (A função Q aprendida)
    model.save("dqn_semaforo_model")
    print("Modelo salvo com sucesso!")

    env.close()

if __name__ == "__main__":
    main()
import random
import time

AÇÕES_VALIDAS = ("aspirar", "mover", "nada", "desviar")

def decidir_acao(percepcao: str) -> str:
    acao = "nada"  # Define uma ação padrão
    if percepcao == "sujo":
        acao = "aspirar"
    elif percepcao == "obstaculo":
        acao = "desviar"
    elif percepcao == "limpo":
        acao = "mover"
    elif percepcao == "sair":
        acao = "sair"
    
    return acao


def main():
    print("Iniciando o Agente Inteligente com Memória")
    print("Percepções possíveis: 'sujo', 'limpo', 'obstaculo'")
    print("Digite 'auto' para modo automático ou 'sair' para encerrar.\n")


    # Tarefa 1: Contadores de estatísticas
    total_passos = 0
    total_aspiracoes = 0

    # Tarefa 2: Adicionando memória ao agente
    agente_memoria = {
        "ultima_acao": None,
        "celulas_visitadas": {0},  # Usamos um conjunto (set) para evitar duplicatas. O agente começa na célula 0.
        "posicao_atual": 0,
        "direcao": 1  # 1 para "frente", -1 para "trás"
    }
    
    # ----------------------------------------

    modo_auto = False

    try:
        while True:
            percepcao_atual = ""
            if modo_auto:
                percepcao_atual = random.choice(["sujo", "limpo", "obstaculo"])
                print(f"Percepção automática: '{percepcao_atual}'")
                time.sleep(1)
            else:
                entrada = input("Digite a Percepção> ").strip().lower()
                if entrada == "auto":
                    modo_auto = True
                    print("\nModo automático ativado. Pressione Ctrl+C para interromper.")
                    continue
                percepcao_atual = entrada
            
            if percepcao_atual == "sair":
                print("Ação de encerramento solicitada pelo usuário.")
                break

            # 1. Decidindo uma ação
            acao_escolhida = decidir_acao(percepcao_atual)
            
            if acao_escolhida == "nada":
                print(f"Percepção '{percepcao_atual}' é inválida. Nenhuma ação foi tomada.")
                continue

            print(f"Ação decidida: '{acao_escolhida}'")

            # 2. Contabilizando as ações (Tarefa 1)
            total_passos += 1
            if acao_escolhida == "aspirar":
                total_aspiracoes += 1

            # 3. Atualizando a memória do agente (Tarefa 2)
            agente_memoria["ultima_acao"] = acao_escolhida
            
            # Atualiza a posição com base na ação
            if acao_escolhida == "mover":
                # Move o agente na direção atual
                agente_memoria["posicao_atual"] += agente_memoria["direcao"]
            elif acao_escolhida == "desviar":
                agente_memoria["direcao"] *= -1
                print(f"Agente desviou. Nova direção: {agente_memoria['direcao']}")

            agente_memoria["celulas_visitadas"].add(agente_memoria["posicao_atual"])

            print(f"Memória -> Última Ação: {agente_memoria['ultima_acao']} | Posição Atual: {agente_memoria['posicao_atual']} | Células Visitadas: {sorted(list(agente_memoria['celulas_visitadas']))}")
            print("-" * 30)


    except KeyboardInterrupt:
        print("\n\nExecução interrompida pelo usuário.")
    
    finally:
        print("\n--- ESTATÍSTICAS FINAIS ---")
        print(f"Total de passos executados: {total_passos}")
        print(f"Total de ações de 'aspirar': {total_aspiracoes}")
        print("-----------------------------\n")

if __name__ == "__main__":
    main()
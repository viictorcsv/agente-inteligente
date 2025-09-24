# Agente Inteligente Simples em Python

Este projeto implementa um agente reativo simples em Python, desenvolvido como uma solução para um exercício prático de Inteligência Artificial. O objetivo é demonstrar os conceitos básicos de um agente racional que interage com um ambiente, toma decisões baseadas em percepções e mantém um estado interno (memória) para registrar suas ações e locais visitados.

---

## ✨ Funcionalidades

-   **Agente Reativo Baseado em Regras:** O agente toma decisões simples e diretas com base na percepção atual do ambiente (ex: se o ambiente está 'sujo', a ação é 'aspirar').
-   **Memória Interna:** O agente é capaz de:
    -   Lembrar sua última ação executada.
    -   Manter um registro de todas as "células" visitadas em um ambiente 1D simulado.
-   **Estatísticas de Desempenho:** Ao final da execução, o programa exibe um resumo com o total de passos executados e o número de vezes que a ação 'aspirar' foi realizada.
-   **Modos de Execução:**
    -   **Modo Manual:** Permite que o usuário insira as percepções do ambiente manualmente.
    -   **Modo Automático:** O agente recebe percepções aleatórias (`sujo`, `limpo`, `obstaculo`) a cada segundo para simular uma interação contínua com o ambiente.

---

## 🛠️ Pré-requisitos

Para executar este projeto, você precisará ter o **Python 3** instalado em sua máquina. Nenhuma biblioteca externa é necessária.

---

## 🚀 Como Executar

Siga os passos abaixo para executar o agente em seu ambiente local:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/PittViic/agente-inteligente.git
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd agente-inteligente
    ```

3.  **Execute o script Python:**
    ```bash
    python agente-inteligente.py
    ```

---

## 🕹️ Como Usar

Após iniciar o script, você pode interagir com o agente diretamente no terminal:

-   **Para inserir uma percepção manualmente:**
    -   Digite uma das percepções válidas: `sujo`, `limpo` ou `obstaculo`.
    -   Pressione `Enter`.
    -   O agente exibirá a ação tomada e o estado atual de sua memória.

-   **Para ativar o modo automático:**
    -   Digite `auto` e pressione `Enter`.
    -   O agente começará a operar sozinho. Para interromper, pressione `Ctrl+C`.

-   **Para encerrar o programa:**
    -   No modo manual, digite `sair`.
    -   Em qualquer modo, pressione `Ctrl+C` para forçar o encerramento.
    -   Ao encerrar, as estatísticas finais de desempenho serão exibidas.

---

## ✍️ Autor

-   **[PittViic](https://github.com/PittViic)**

---

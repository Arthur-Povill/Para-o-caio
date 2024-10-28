# Jogo da Velha (Tic-Tac-Toe)

## Descrição

Este é um projeto simples de Jogo da Velha com interface gráfica utilizando **Pygame**. O jogo inclui uma inteligência artificial que utiliza o algoritmo **Minimax** otimizado com **poda alfa-beta**, tornando a experiência desafiadora para o jogador.

## Índice

- [Descrição](#descrição)
- [Como Jogar](#como-jogar)
- [Instalação](#instalação)
- [Como Executar](#como-executar)
- [Funcionalidades](#funcionalidades)
- [Ideias para Aprimoramento](#ideias-para-aprimoramento)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Como Jogar

- **Escolha seu símbolo**: Ao iniciar o jogo, você pode escolher jogar como **X** ou **O**.
- **Faça sua jogada**: Clique em uma célula vazia para fazer sua jogada.
- **Objetivo**: Alinhe três símbolos iguais em uma linha, coluna ou diagonal.
- **Desafio**: A inteligência artificial fará movimentos estratégicos, tornando o jogo desafiador.
- **Reiniciar**: Após o término da partida, você pode clicar em "Play Again" para jogar novamente.

## Instalação

### Pré-requisitos

- **Python 3.x** instalado em seu sistema.
- Biblioteca **Pygame** instalada.

### Passos para Instalação

1. **Clone o repositório** ou baixe os arquivos `tictactoe.py` e `runner.py` para um diretório local.

   ```bash
   git clone https://github.com/Arthur-Povill/Para-o-caio.git
   ```

2. **Instale as dependências**:

   ```bash
   pip install pygame
   ```

3. **Fonte opcional**: Para uma melhor experiência visual, você pode baixar e incluir a fonte **OpenSans-Regular.ttf** no diretório do projeto.

## Como Executar

1. **Navegue até o diretório do projeto**:

   ```bash
   cd caminho/para/o/projeto
   ```

2. **Execute o jogo**:

   ```bash
   python runner.py
   ```

3. **Divirta-se**: A janela do jogo será aberta e você poderá começar a jogar.

## Funcionalidades

- **Interface Gráfica Intuitiva**: Utiliza Pygame para uma experiência visual agradável.
- **Inteligência Artificial Avançada**: Implementação do algoritmo Minimax com poda alfa-beta para decisões otimizadas.
- **Detecção de Fim de Jogo**: Identifica vitórias, derrotas e empates corretamente.
- **Opção de Reinício**: Fácil reinicialização para jogar múltiplas partidas consecutivas.
- **Feedback Visual**: Indicação clara de turnos e movimentos.

## Ideias para Aprimoramento

Aqui estão algumas sugestões para futuras melhorias no projeto:

- **Níveis de Dificuldade**: Implementar modos Fácil, Médio e Difícil, ajustando a profundidade do algoritmo ou introduzindo movimentos aleatórios.
- **Modo Multijogador Online**: Permitir que jogadores desafiem amigos ou oponentes aleatórios pela internet.
- **Aprimoramentos Visuais**:
  - Animações ao fazer movimentos.
  - Temas personalizáveis para o tabuleiro e símbolos.
  - Efeitos sonoros para interações e notificações.
- **Histórico e Estatísticas**:
  - Registro de partidas jogadas.
  - Estatísticas de vitórias, derrotas e empates.
- **Aprendizado de Máquina**:
  - Implementar um agente que aprende com as partidas utilizando técnicas de aprendizado por reforço.
- **Portabilidade para Mobile**:
  - Adaptar o jogo para plataformas móveis, como Android e iOS.
- **Internacionalização (i18n)**:
  - Suporte a múltiplos idiomas com opção de seleção pelo usuário.
- **Tutorial Interativo**:
  - Incluir um guia passo a passo para novos jogadores aprenderem as regras e mecânicas do jogo.
- **Sistema de Pontuação**:
  - Atribuir pontos por vitória, empate e derrota, com um ranking local ou global.
- **Salvar e Carregar Partidas**:
  - Permitir que o jogador salve o estado atual do jogo e retome posteriormente.
- **Integração com Redes Sociais**:
  - Compartilhar resultados e convidar amigos para jogar.

## Contribuindo

Contribuições são bem-vindas! Se você tem ideias, encontrou bugs ou deseja melhorar o código, por favor:

1. **Faça um fork** do projeto.
2. **Crie uma branch** para sua modificação:

   ```bash
   git checkout -b minha-modificacao
   ```

3. **Commit suas mudanças**:

   ```bash
   git commit -m "Descrição da minha modificação"
   ```

4. **Envie para o repositório remoto**:

   ```bash
   git push origin minha-modificacao
   ```

5. **Abra um Pull Request** explicando suas alterações.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

Esperamos que você aproveite o jogo e sinta-se à vontade para contribuir com melhorias e novas ideias!
# chatbot-openai

# Chatbot OpenAI com PySimpleGUI

Este projeto implementa um chatbot usando a API da OpenAI e uma interface gráfica simples construída com PySimpleGUI. O chatbot permite que os usuários conversem com um modelo de linguagem da OpenAI através de uma interface gráfica fácil de usar.

## Funcionalidades

- Interface gráfica amigável para enviar e receber mensagens do chatbot.
- Integração com a API da OpenAI para processar e gerar respostas.

## Requisitos

- Python 3.6 ou superior
- Uma chave API da OpenAI

## Instalação

1. **Clone o repositório** para o seu ambiente local:
  
   git clone https://github.com/seu_usuario/chatbot-openai.git
   cd chatbot-openai

2. **Crie um ambiente virtual** (opcional, mas recomendado) para gerenciar as dependências:

    python -m venv venv
    
    source venv/bin/activate  # Para Linux/macOS
    
    venv\Scripts\activate  # Para Windows

3. Instale as dependências necessárias:

    pip install openai pysimplegui

4. Configure sua chave API da OpenAI:

    Substitua campo para inserir a chave api no script pelo valor da sua chave API da OpenAI.
   
    Alternativamente, você pode configurar a chave API como uma variável de ambiente:
        export OPENAI_API_KEY="sua-chave-api"

    E modifique o código para usar esta variável de ambiente:
        
        import os
        openai.api_key = os.getenv("OPENAI_API_KEY")

## Uso

1. Execute o script para iniciar o chatbot:

python nome_do_script.py

2. Interaja com o chatbot:

    Digite sua mensagem na caixa de entrada e clique em "Enviar".
    A resposta do chatbot aparecerá na área de saída.

3. Encerramento:

    Clique no botão "Sair" ou feche a janela para encerrar o programa.


## Problemas Conhecidos

    A API da OpenAI pode ocasionalmente retornar erros devido a problemas de conectividade ou uso excessivo. Tais erros são capturados e uma mensagem de erro amigável é exibida ao usuário.

## Contribuição
    
    Sinta-se à vontade para contribuir com este projeto enviando pull requests ou relatando problemas no GitHub Issues.

## Licença

    Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo LICENSE para mais detalhes.   

    Certifique-se de ajustar os placeholders como `seu_usuario`, `seu_repositorio` e `nome_do_script.py` para os valores reais do seu repositório e script. Adicionalmente, inclua um arquivo `LICENSE` no seu repositório se desejar especificar os termos de uso do código.
 
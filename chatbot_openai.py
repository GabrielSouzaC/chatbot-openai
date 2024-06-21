import openai
import PySimpleGUI as sg

chave_api = "campo para inserir a chave api"

openai.api_key = chave_api

def enviar_mensagem(mensagem, lista_mensagens=None):
    if lista_mensagens is None:
        lista_mensagens = []

    lista_mensagens.append({"role": "user", "content": mensagem})

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=lista_mensagens
        )
        return resposta["choices"][0]["message"]
    except openai.error.OpenAIError as e:
        print(f"Ocorreu um erro: {e}")
        return {"role": "system", "content": "Desculpe, ocorreu um erro ao processar sua mensagem."}

# interface gráfica
layout = [
    [sg.Text("Escreva sua mensagem:")],
    [sg.Input(key='-INPUT-', do_not_clear=False)],
    [sg.Button('Enviar'), sg.Button('Sair')],
    [sg.Text("Chatbot Respostas:", size=(40, 1))],
    [sg.Output(size=(50, 20), key='-OUTPUT-')]
]

# criando a janela
janela = sg.Window('Chatbot OpenAI', layout)

lista_mensagens = []

while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED or evento == 'Sair':
        break

    if evento == 'Enviar':
        mensagem_usuario = valores['-INPUT-']
        if mensagem_usuario:
            print(f"Você: {mensagem_usuario}")
            resposta = enviar_mensagem(mensagem_usuario, lista_mensagens)
            lista_mensagens.append(resposta)
            print(f"Chatbot: {resposta['content']}")

# fechamento
janela.close()

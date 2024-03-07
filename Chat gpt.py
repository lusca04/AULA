import openai
chave_api = "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"
openai.api_key = chave_api


def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=lista_mensagens,
    )
    return resposta["choices"][0]["message"]


lista_mensagens = []
while True:
    texto = input("escreva sua mensagem aqui:")

    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        lista_mensagens.append(resposta)
        print(resposta['content'])

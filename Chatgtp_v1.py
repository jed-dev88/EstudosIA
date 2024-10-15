import openai

from dotenv import load_dotenv,find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

def geracao_texto(mensagens):

    resposta = client.chat.completions.create(
    messages=mensagens,
    model = 'gpt-4o-mini',
    temperature=0,
    max_tokens=1000,
    stream = True,
    )

    print('Assistant: ', end='')
    texto_completo = ''

    for respota_stream in resposta:
        texto = respota_stream.choices[0].delta.content
        if texto:
            print(texto, end='')
            texto_completo += texto
    print()

    mensagens.append({'role':'assistant','content': texto_completo}),
    return mensagens

if __name__ == '__main__':

    print('Bem-vindo ao JedChat, pergunte qualquer coisa? ')
    mensagens = []
    
    while True:
        input_usuario = input('Jed: ')
        mensagens.append({'role':'user','content': input_usuario})
        mensagens = geracao_texto(mensagens)
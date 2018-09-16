import requests

url = "https://api.telegram.org/bot620155979:AAHMyrpOIi7z22PcDUu9uKIxA9vuepGR4hc/"

#Função para pegar atualizações no chat bot
def get_updates_json(request):
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()

#Função para pegar as ultimas atualizações
def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

#Função para indentificar o chat id do update
def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id
#Função para enviar a mensagem para o user
def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

chat_id = get_chat_id(last_update(get_updates_json(url)))

send_mess(chat_id, 'Olá, meu amiguinho ! ')

#Essa função vai fazer o chat responder sem ter que executar o script cada vez que o usuario mandar mensagem
def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
           update_id += 1
    sleep(1)

if __name__ == '__main__':
    main()

from datetime import datetime
from application.configs.broker_configs import mqtt_broker_configs

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com sucesso: {client}')
        client.subscribe(mqtt_broker_configs["TOPIC"])
    else:
        print(f'Erro ao conectar! Código={rc}')

def on_subscribe(client, userdata, mid, granted_qos):
    print(f'Inscrito no tópico: {mqtt_broker_configs["TOPIC"]}')
    print(f'QoS: {granted_qos}')

def on_message(client, userdata, message):
    data_atual = datetime.now()
    data = data_atual.strftime("%d/%m/%Y %H:%M")
    print('Mensagem recebida!')
    print(message.payload.decode())
    print(data)
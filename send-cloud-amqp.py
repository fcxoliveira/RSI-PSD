#!/usr/bin/env python
import pika
import time

arq = open('Coleta de 15 minutos.txt', 'r')
arq1 = open('formatado.txt', 'w')

lista = arq.readlines()
temp = []
credentials = pika.PlainCredentials('dsonamxr', 'pdOx_g75U4-81DMwpU-WxOE_fiCbakrn')
connection = pika.BlockingConnection(pika.ConnectionParameters('crocodile.rmq.cloudamqp.com', 5672, 'dsonamxr', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='amq.topic', durable=True,
                         exchange_type='topic')

print("Enviando.....")
for x in range(2, len(lista), 2):
	temp.append(lista[x])
	arq1.write(lista[x] )
	lista[x].replace('\r','')
	lista[x].replace('\n','')
	lista[x].replace('\r','')
	lista[x].replace('\n','')
	msg = lista[x]
	msg.replace('\r','')
	print(msg)
	time.sleep(0.5)
	channel.basic_publish(exchange='amq.topic',
                      routing_key='coleta',
                      body=msg)
connection.close()

arq.close()
arq1.close()

#!/usr/bin/env python
import pika
import time

arq = open('Coleta de 15 minutos.txt', 'r')
arq1 = open('formatado.txt', 'w')

lista = arq.readlines()
temp = []

credentials = pika.PlainCredentials('psd', 'psd')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, 'psd', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='amq.topic', durable=True,
                         exchange_type='topic')

for x in range(2, len(lista), 2):
	temp.append(lista[x])
	arq1.write(lista[x] )
	lista[x].replace('\r','')
	lista[x].replace('\n','')
	msg = lista[x]
	print(msg)
	time.sleep(0.5)
	channel.basic_publish(exchange='amq.topic',
                      routing_key='coleta',
                      body=msg)

connection.close()

arq.close()
arq1.close()

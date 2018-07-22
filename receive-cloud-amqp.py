#/usr/bin/env python
import pika

credentials = pika.PlainCredentials('dsonamxr','pdOx_g75U4-81DMwpU-WxOE_fiCbakrn')
connection = pika.BlockingConnection(pika.ConnectionParameters('crocodile.rmq.cloudamqp.com', 5672, 'dsonamxr', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='amq.topic', durable=True,
                         exchange_type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='amq.topic',
                       queue=queue_name,
                       routing_key='coleta')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

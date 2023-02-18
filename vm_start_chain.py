import paho.mqtt.client as mqtt
import time
import socket

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    client.subscribe("imagalla/pong")

    client.message_callback_add("imagalla/pong", on_message_from_pong)

def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "  msg: " + str(msg.payload, "utf-8"))

def on_message_from_pong(client, userdata, message):
    print("Custom callback - Number (pong): " + message.payload.decode())
    num = int(message.payload.decode())+1
    time.sleep(0.5)
    client.publish("imagalla/ping", num)
    print("Publishing number payload (ping)")


if __name__ == '__main__':
    client = mqtt.Client()

    client.on_connect = on_connect

    client.connect( host = "172.20.10.4",
                    port = 1883,
                    keepalive = 60
    )

    client.loop_start()
    time.sleep(1)

while True:
    num_payload = input("")
    client.publish("imagalla/ping", f"{num_payload}")
    print("Publishing number payload (ping)")
    client.on_message = on_message_from_pong
    time.sleep(1)
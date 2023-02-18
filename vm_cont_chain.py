import paho.mqtt.client as mqtt
import time
import socket

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code " + str(rc))

    client.subscribe("imagalla/ping")

    client.message_callback_add("imagalla/ping", on_message_from_ping)

def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "  msg: " + str(msg.payload, "utf-8"))

def on_message_from_ping(client, userdata, message):
    print("Custom callback - Number (ping): " + message.payload.decode())
    num = int(message.payload.decode())+1
    time.sleep(0.5)
    client.publish("imagalla/pong", num)
    print("Publishing number payload (pong)")

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
    client.on_message = on_message_from_ping
    time.sleep(1)
import time as t
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

ENDPOINT = "a2kyzm0tjc22w-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "hyukpk"
PATH_TO_CERTIFICATE = "/home/hyukpk/certs/raspberry_pi_4.cert.pem"
PATH_TO_PRIVATE_KEY = "/home/hyukpk/certs/raspberry_pi_4.private.key"
PATH_TO_AMAZON_ROOT_CA_1 = "/home/hyukpk/certs/root-CA.crt"
MESSAGE = "HELLO WORLD!"

# Initialize MQTT message callback
myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_AMAZON_ROOT_CA_1, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE)

def customCallback(client, userdata, message):
    print("Received a new message: ")
    message_payload = json.loads(message.payload)
    print(message_payload)
    print("from topic: ")
    print(message.topic)
    print("---------\n\n")

    # Here, we'll just print a simple message instead of checking for a specific command
    # and responding based on that command
    if message_payload.get("command") == "action_required":
        response_topic = "response/topic"
        response_message = "Received your message, here's a simple response:" + MESSAGE
        print("Sending a simple response message.")
        myAWSIoTMQTTClient.publish(response_topic, json.dumps({"response": response_message}), 0)


# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()
myAWSIoTMQTTClient.subscribe("command/topic", 1, customCallback)

# Keep the script running
while True:
    t.sleep(1)

import time as t 
import json 
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
#import cv 
#import base64

#def capture_image():
#    cam = cv2.VideoCapture(0)
#    ret, frame = cam.read()
#    if ret:
#        ret, jpeg = cv2.imencode('.jpg', frame)
#if ret:
#            return jpeg.tobytes()
#    cam.release()
#    return None
#
#def encode_image(image_bytes):
#    return based64.b64envode(image_bytes).decode('utf-8')


ENDPOINT = "a2kyzm0tjc22w-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "hyukpk"
PATH_TO_CERTIFICATE = "/home/hyukpk/certs/raspberry_pi_4.cert.pem"
PATH_TO_PRIVATE_KEY = "/home/hyukpk/certs/raspberry_pi_4.private.key"
PATH_TO_AMAZON_ROOT_CA_1 = "/home/hyukpk/certs/root-CA.crt"
MESSAGE = "HELLO WORLD!"

#initialize MQTT message call back
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
    print(message_payload.get("command"))

   # if message_payload.get("command") == "action_required":

    #    response = {
     #       "response" : "action completed",
      #      "details": MESSAGE
       # }

        #response_topic = "response/topic"
       # myAWSIoTMQTTClient.publish(response_topic, json.dumps(response), 1)


#connect and subcribe to AWS IoT
myAWSIoTMQTTClient.connect()
myAWSIoTMQTTClient.subscribe("command/topic", 1, customCallback)

#keep the script running 
while True:

    t.sleep(1)

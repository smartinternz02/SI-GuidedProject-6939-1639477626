import wiotp.sdk.device
import time
import os
import datetime
from ibm_watson import TextToSpeechV1
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator , BasicAuthenticator
import playsound
'''

authenticator = BasicAuthenticator('apikey-v2-34uhhlix6hcy13v2gisbh6vsiegrpl5wkwasyqmqnfl6', '7f517d7221399711c579625ed6d3e874')
service = CloudantV1(authenticator=authenticator)
service.set_service_url('https://apikey-v2-34uhhlix6hcy13v2gisbh6vsiegrpl5wkwasyqmqnfl6:7f517d7221399711c579625ed6d3e874@ff20a5d8-f28e-4fa4-b046-473245d0e43f-bluemix.cloudantnosqldb.appdomain.cloud')'''

authenticator = IAMAuthenticator('kZsyz69sNctJRNFm7QxalUZ-setaah0drfP3s2tcXTr_')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/a445e70c-f7f6-4625-8ced-2434293c320c')

myConfig = { 
    "identity": {
        "orgId": "y9045l",
        "typeId": "mobile",
        "deviceId":"09876"
    },
    "auth": {
        "token": "12345678"
    }
}
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

def myCommandCallback(cmd):
    print("Message received fromIBM IoT Platform %s" % cmd.data['command'])
    m=cmd.data['command']
    with open('medicine.mp3', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                'You have to take'+m+'medicine now',
                voice='en-US_AllisonV3Voice',
                accept='audio/mp3'
                ).get_result().content)
        os.remove('medicine.mp3')
        while True:
                client.commandCallback = myCommandCallback
                client.disconnect()
        

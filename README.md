# Whatsapp Chatbot

## Steps

1. Create an Account with [Twilio](https://www.twilio.com/), it's free for create a bot for whatsapp.
2. Open the [Sandbox Whatsapp](https://www.twilio.com/console/sms/whatsapp/sandbox) to Start the whatsapp BOT.
3. Install venv package, using the Script `install_venv.sh` on the **Virtual-Ambient** Directory.
4. Start the `virtualAmbient.py` using python3 to start the Listening for Whatsapp Requests
5. Install [ngrok](https://ngrok.com/) on your computer, where he will create a HTTP URL temporary to test your Bot

## Start

* Start ngrok on terminal inside **Virtual-Ambient/** Directory: 

```shell
> ./ngrok http 5000
```

* Copy the _Forwarding_ URL and insert /bot in the end: Example: ` http://d4a37d74b89d.ngrok.io/bot`

* Insert this URL on the configuration of POST Link on twilio: [https://www.twilio.com/console/sms/whatsapp/sandbox](https://www.twilio.com/console/sms/whatsapp/sandbox)
 
* On the other Terminal, start the `python3 virtualAmbient.py`

* Write something on your whatsapp and wait the response

* After the messages, it will save the informations on the file **info.txt**

* Open other Terminal on the directory **Server** and Start the program `insertdata.py`, it saves the tags with the informations on the file **index.html**

* Start the Server using the program `infoserver.py` where it reads the **index.html** and showing the infos on the Link: http://loclahost:8080
 
## Example Running

Youtube video running the project: [Chatbot de Whatsapp usando python](https://youtu.be/WhzQBnKjbzY)

## Observation

Always watching how much you can spend on Twilio, you pay for all messages sended, but, in Trial you can use the Trial Balance.

Check on this [LINK](https://www.twilio.com/console/billing) your currency test.
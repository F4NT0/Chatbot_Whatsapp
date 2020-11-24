#!/bin/bash

#
# Venv Whatsapp bot for python
#
sudo apt-get install python3-venv
python3 -m whatsapp-bot-venv
source whatsapp-bot-venv/bin/activate
pip3 install twilio flask requests
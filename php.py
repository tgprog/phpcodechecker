#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
from telebot import types
from telebot import util
import re
import time
from time import sleep
import sys
import json
import os
import logging
import subprocess
#by @hacker_sudo
#our channel = @freebaaazaar
import requests
import random
from random import randint
#by @hacker_sudo
#our channel = @freebaaazaar
import base64
import urllib
from urllib import urlretrieve as dw
import urllib2
import redis
#by @hacker_sudo
#our channel = @freebaaazaar
import requests as req
reload(sys)
sys.setdefaultencoding("utf-8")
admin =103358505
rediss = redis.StrictRedis(host='localhost', port=6379, db=0)


API_TOKEN = '238030738:AAFlRmw8v-urHu0WTKszgH-6mSMmInDCZzY'
#by @hacker_sudo
#our channel = @freebaaazaar
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(regexp='^(/feedback) (.*)')
def feeder(m):
	text=m.text.split()[1]
	cid=m.chat.id
	bot.send_message(admin,'text:>{}\nname:>{}\nusername:>@{}'.format(text,m.from_user.first_name,m.from_user.username))
	bot.send_message(cid,'{}*message sent to * [yasin](t.me/hacker_sudo) _wait for check your message_'.format(m.from_user.first_name),parse_mode='Markdown')
	#by @hacker_sudo
#our channel = @freebaaazaar
@bot.message_handler(commands=['ch'])
def time(m):
    yasin = m.text.replace("/send ","")
    bot.send_message(-1001052290909, "{}".format(yasin), parse_mode="Markdown")
@bot.message_handler(commands=['start'])
def start(m):
	cid=m.chat.id
	name=m.from_user.first_name
	last=m.from_user.last_name
	id=m.from_user.id
	bot.send_chat_action(cid,'TYPING')
	rediss.sadd('memberspy',id)
	markup=types.InlineKeyboardMarkup()
	feedback=types.InlineKeyboardButton("📞FeedBack📞",callback_data='fb')
	channel=types.InlineKeyboardButton('📣Ourchannel:)📣',url='t.me/freebaaazaar')
	bot_=types.InlineKeyboardButton('🤖phpcodecheckerbot:)🤖',url='t.me/PhpCodeCheckerrobot')
	dev=types.InlineKeyboardButton('dev',url='telegram.me/hacker_sudo')
	markup.add(channel,bot_,dev)
	markup.add(feedback)
	bot.send_message(cid,"""
	hi _{}{}_
	welcome to [PhpCodeCheckerrobot](t.me/PhpCodeCheckerrobot)
	send your code for check that :)
	BOT CONNECT TO *http://phpcodechecker.com*""".format(name,last),parse_mode='Markdown',reply_markup=markup)
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
#by @hacker_sudo
#our channel = @freebaaazaar
@bot.message_handler(commands=['stats'])
def send_stats(m):
        usrs = str(rediss.scard('memberspy'))
        text = 'Users : {}'.format(usrs)
        bot.send_message(m.chat.id,text)
#by @hacker_sudo
#our channel = @freebaaazaar
@bot.message_handler(func=lambda message : True)
def pcc(m):
    try:
        
        cid=m.chat.id
        text=m.text
        # Get the dataset
        url = 'http://phpcodechecker.com/api/?code={}'.format(text)
        response = urllib.urlopen(url)
        # Convert bytes to string type and string type to dict
        string = response.read().decode('utf-8')
        lis=json.loads(string)
        markup=types.InlineKeyboardMarkup()
        news=types.InlineKeyboardButton('🤖Channel🤖',url='t.me/freebaaazaar')
        markup.add(news)
        bot.forward_message(cid,admin,m.message_id)
        bot.send_chat_action(cid,'TYPING')
        bot.send_message(cid,"ERRORS:\n<b>{}</b>".format(lis['syntax']['message']),parse_mode='HTML',reply_markup=markup)
    except (ValueError,KeyError) as r:
        print(r)

 #by @hacker_sudo
#our channel = @freebaaazaar   
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  if call.message:
    if call.data == "fb":
      bot.send_message(call.message.chat.id,"{}{} for *send message to admin write*:\n/feedback <text>\nexample:\n_/feedback hello:)_".format(call.from_user.first_name,call.from_user.last_name),parse_mode='Markdown')
#by @hacker_sudo
#our channel = @freebaaazaar
bot.polling(True)
#by @hacker_sudo
#our channel = @freebaaazaar

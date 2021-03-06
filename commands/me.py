#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import logging

from utils import my_bot, user_action_log


# Команда /me
# TODO: из-за parse_mode="Markdown" не проходят запросы типа
#       "/me вызывает @rm_bk."
# TODO: отрефакторить говнокод
def me_message(message):
    # В ЛС бот не может удалять сообщения пользователя
    try:
        my_bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception:
        logging.exception("message")
    # Если у пользователя есть юзернэйм, то берём его как your_name
    if message.from_user.username is not None:
        your_name = '[@{}](tg://user?id={})'.format(message.from_user.username, message.from_user.id)
    # Иначе, берём имя пользователя, которое есть всегда
    else:
        your_name = '[{}](tg://user?id={})'.format(message.from_user.first_name, message.from_user.id)
    # Если /me непусто, берём всё, что после '/me '
    if len(message.text.split()) < 2:
        return
    your_message = message.text.split(maxsplit=1)[1]
    your_me = "{} {}".format(your_name, your_message)
    try:
        # Если /me было ответом на какое-то сообщение, то посылаем запрос как ответ
        # TODO: расширить эту фичу на все команды
        if getattr(message, 'reply_to_message') is not None:
            my_bot.send_message(message.chat.id, your_me, parse_mode="Markdown", disable_notification=True,
                                reply_to_message_id=message.reply_to_message.message_id)
        else:
            my_bot.send_message(message.chat.id, your_me, parse_mode="Markdown", disable_notification=True)
    except Exception:
        logging.exception("message")
    user_action_log(message, "called the me:\n{}".format(your_me))

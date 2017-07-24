# mm-randbot
Рандомный бот написанный рандомом для рандомного чата Мехмата в Telegram (плавно переходящий в algebrach_bot). Написан на Python 2.7, для работы нужны следующие дополнительные модули:
- PyOWM - https://github.com/csparpa/pyowm
- TeleBot - https://github.com/eternnoir/pyTelegramBotAPI 
- Wikipedia - https://pypi.python.org/pypi/wikipedia/
   
На данный момент mm-randbot (algebrach_bot) выполняет следующие команды:

-  /maths — скидывает пользователю случайную картинку из соответствующей папки (определение или теорема случайного предмета);
-  /challenge — скидывает пользователю случайную картинку из соответствующей папки (случайная математическая задача);
-  /wiki — скидывает пользователю факт из рандомной статьи либо из английской, либо из русской Википедии;
-  /wiki 'запрос на русском' — скидывает пользователю обобщение статьи по запросу и ссылку на статью по запросу;
-  /wolfram 'запрос' — скидывает пользователю картинку с результатом вычислений WolframAlpha по запросу (если найдёт);
-  /links — скидывает содержимое указанного текстового файла (список полезных мехматовских ссылок);
-  /weather — скидывает текущее состояние погоды в Москве, а также прогноз на три ближайших дня (пока только на английском);
-  /wifi — скидывает содержимое указанного текстового файла (список доступных мехматовских Wi-Fi сетей);
-  /roll — скидывает случайное целое число от 0 до 100, иногда посылает картинку;
-  /truth — скидывает рандомную строчку из файла (только правду);
-  /d6 — кидает UTF-8 кости
-  /number 'int' — игра с угадыванием рандомного числа от 0 до abs('int') за фиксированное число попыток. Если abs('int')>99, то в случае победы присылает "приз" в виде картинки или гифки из фиксированной папки;
-  /kek — присылает случайную строчку из текстового файла;
-  /meme — присылает либо картинку, либо гифку из указанной папки.

В фоне он обращается к API Вконтакте с проверкой наличия новых постов в паблике. В случае их появления, извлекает текст/картинки/ссылки/текст репоста (если доступны) и переправляет всё найденное в чат Telegram.


Это мой самый первой бот, написан в первую очередь, чтобы попробовать с нуля освоить Telegram API.

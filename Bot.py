import telebot,random,os,requests
from telebot import types
bot = telebot.TeleBot('#Your Telegram Bot Token!')

# Github: https://github.com/PluginX
# Telegram: https://t.me/Plugin

Max_Files_For_User = 4                                                                   #how many user can host bots
Black_Listed_Librarys = ['os','base64','input','bot.py','base32','marshal','selenium']   #Black listed lib or words!

@bot.message_handler(commands=['start'])
def send_welcome(message):

    try:
        bot.send_message(message.chat.id, text="*التحقق مما اذا كنت في قاعدة البيانات * 🕔\ارجو الانتظر",parse_mode='markdown')
        first = message.chat.first_name

        data = requests.get('https://apis.red/.......').text

        if str(message.chat.id) in data:
            data2 = requests.get(f'https://apis.red/isVerified/check/?id={message.chat.id}').text
            if 'لديك بالفعل حساب على عنوان IP هذا!' in data2:
                bot.send_message(message.chat.id,text=f"*مرحبا* {first}.\nمرحبا\n  نحو الافضل *Python* المضيف بوت\n\n* أنت لست على قاعدة البيانات من فضلك افتح عنوان url هذا حتى أتمكن من إضافة معرفك على قاعدة بيانات الروبوت التأكد من أنك لست روبوتًا*!\n\nhttps://apis.red/isVerified/check/?id={str(message.chat.id)}\n\n عندما تنتهي اكتب */start !*",parse_mode='markdown')
            else:
                key = types.InlineKeyboardMarkup()
                b1 = types.InlineKeyboardButton(text='قناتي🧚', url='https://t.me/aoo1_1')
                b2 = types.InlineKeyboardButton(text='souece </>', url='https://t.me/rosnw1')

                key.add(b1)
                key.add(b2)

                bot.send_video(message.chat.id, 'https://t.me/aoo1_1/179',
                               caption=f'*مرحبا* {first}.\nمرحبا\n  نحو الافضل *Python* المصيف بوت\n\n** الإصدار الحالي: V0.2**\nصنع بواسطة : @rwwwr\n\n/help\n  * للحصول على صفحة المساعدة*\n\n/pip + اسم المكتبة\n  * لتثبيت مكتبة*\n\n/run + معرف الملف الخاص بك\n  * لتشغيل الروبوت الخاص بك!*',
                               parse_mode='markdown', reply_markup=key)
        else:
            try:
                bot.send_message(message.chat.id,text=f"*مرحبا* {first}.\nمرحبا\n  نحو الافضل *Python* المضيف بوت\n\n* أنت لست على قاعدة البيانات من فضلك افتح عنوان url هذا حتى أتمكن من إضافة معرفك على قاعدة بيانات الروبوت التأكد من أنك لست روبوتًا*!\n\nhttps://apis.red/isVerified/check/?id={str(message.chat.id)}\n\n عندما تنتهي اكتب */start !*",parse_mode='markdown')
            except:
                bot.send_message(message.chat.id, text="* الايبي معطل* 🚫\nالرجال اخبار مطور البوت: @rwwwr",parse_mode='markdown')
    except:
        bot.send_message(message.chat.id, text="* الايبي معطل* 🚫\nالرجال اخبار مطور البوت: @rwwwr",
                         parse_mode='markdown')


@bot.message_handler(func=lambda m: True)
def Get(message):

    msg = message.text
    first = message.chat.first_name

    try:
        data = requests.get('https://apis.red/.......').text

        if str(message.chat.id) in data:
            if msg.startswith('/pip'):
                try:

                    data = str(msg).split(' ')
                    the_pip = data[1]

                    if 'telebot' in the_pip:
                        bot.send_message(message.chat.id, text="تم تثبيته من قبل مطور البوت ✅")

                    elif 'pyTelegramBotAPI' in the_pip:
                        bot.send_message(message.chat.id, text="Installed by the developer ✅")

                    elif 'requests' in the_pip:
                        bot.send_message(message.chat.id, text="تم تثبيته من قبل مطور البوت ✅")

                    else:
                        os.system(f"pip install {the_pip}")
                        bot.send_message(message.chat.id, text="ثبت المكتبة بنجاح ✅")

                except:
                    bot.send_message(message.chat.id,
                                     text=f"Sorry you leave something empty!\nOr you are missing some requires\nPlease try again /start ")

            elif msg.startswith('/run'):
                try:

                    data = str(msg).split(' ')
                    the_file_name = data[1]

                    os.startfile(f"bots\{message.chat.id}\{the_file_name}.py")
                    bot.send_message(message.chat.id, text="بوتك اشتغل بنجاح ✅")

                except:
                    bot.send_message(message.chat.id,
                                     text=f"Sorry you leave something empty!\nOr you are missing some requires\nPlease try again /start ")

            elif msg.startswith('/help'):
                try:

                    key = types.InlineKeyboardMarkup()
                    b1 = types.InlineKeyboardButton(text='مطور البوت', url='https://t.me/rwwwr')
                    b2 = types.InlineKeyboardButton(text='programming🐍</>', url='https://t.me/vvcvz')
                    key.add(b1)
                    key.add(b2)

                    bot.send_photo (message.chat.id، photo = 'https: //t.me/aoo1_1/179'،caption= "* صفحة التعليمات * 📑 \ n1- اسحب ملف python إلى الروبوت \ n2- ثم الروبوت  سيمنحك * معرّف الملف * \ n \ n3- ثم ثبّت مكتباتك \ n 🔍 باستخدام / pip + * اسم المكتبة * \ n \ n4- قم بتشغيل الروبوت الخاص بك \ n 🔍 باستخدام / run + * File iD * \ n \ n  * جهة الاتصال *: @rwwwr "، parse_mode = 'markdown'، reply_markup = key)

                except:
                    bot.send_message(message.chat.id,
                                     text=f"آسف لأنك تركت شيئا فارغا!\n أو أنك تفتقد بعض المتطلبات\n حاول مرة اخرى /start ")

            else:
                bot.send_message(message.chat.id, text=f"Sorry!\nI cant understand what the hell you want!")

        else:
            try:
                bot.send_message(message.chat.id,
                                 text=f"* مرحبًا * {first}. \ n مرحبًا \ n إلى الأفضل * Python * host bot \ n \ n * أنت لست في قاعدة البيانات ، يرجى فتح عنوان url هذا حتى يمكنني إضافة معرفك إلى قاعدة بيانات الروبوت والتأكد من أنك لست كذلك  روبوت *! \ n \ nhttps: //apis.red/isVerified/check/؟ id = {str (message.chat.id)} \ n \ n عند الانتهاء اكتب * / ابدأ من جديد!*",
                                 parse_mode='markdown')
            except:
                bot.send_message(message.chat.id, text="*الايبي معطل* 🚫\nالرجال اخبار مطور البوت: @rwwwr",
                                 parse_mode='markdown')
    except:
        bot.send_message(message.chat.id, text="*API is down* 🚫\nPlease contact the coder: @rwwwr",
                         parse_mode='markdown')

@bot.message_handler(content_types=['document'])
def save(message):

    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'

    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    ran = 'a'+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)

    try:
        os.makedirs('bots/'+str(message.chat.id)+'/')
    except:
        pass
    with open('bots/'+ str(message.chat.id) + '/' + ran+'.py', 'wb') as new_file:
        new_file.write(downloaded_file)

    getLen = len(os.listdir('bots/'+ str(message.chat.id) + '/'))

    if int(getLen) >= int(Max_Files_For_User+1):
        bot.send_message(message.chat.id, text=f'*You have upload {getLen} files\n You cant upload more* 🚫',
                         parse_mode='markdown')
        os.remove('bots/' + str(message.chat.id) + '/' + ran + '.py')
    else:
        try:
            BlackListedLib = ''
            emptystr = False
            for i in Black_Listed_Librarys:
                search = str(downloaded_file).find(i)
                if search > 0:
                    emptystr = True
                    BlackListedLib += i
                    break

            if BlackListedLib == 'os':
                search = str(downloaded_file).find('post')
                if search > 0:
                    emptystr = False
                

            if emptystr == True:
                bot.reply_to(message, text=f'You cant use *{BlackListedLib}* 🚫\nFile Removed! ', parse_mode='markdown')
                os.remove('bots/' + str(message.chat.id) + '/' + ran + '.py')
            else:
                bot.send_message(message.chat.id, text=f'*بوتك اشتغل بنجاح✅* ✅\n*معرف الملف الخاص بك*:',parse_mode='markdown')
                bot.send_message(message.chat.id, text=f'```{ran}```',parse_mode='markdown')
        except:
            bot.send_message(message.chat.id, text=f'*Error in file upload contact the coder* 🚫\nPlease try again later',parse_mode='markdown')


bot.polling(True)

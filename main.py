import hashlib
import logging
import os
import time

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle

from config import API_TOKEN, formats
from services import docx_replace, replace_kiril

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def get_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text="Перейти в канал", url='t.me/pafekuto_seikatsu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def check_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text="Подписаться", url='t.me/pafekuto_seikatsu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def start_markup():
    buttons = [
        [types.InlineKeyboardButton(text="Начать использовать в чатах", switch_inline_query='')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    pars = message.text.split('/start')
    # if len(pars) != 2 and pars[0] != '':

    print(message.text)
    if pars[1] == ' ad':
        """await message.reply("Размещение рекламы вариантов в открывающемся режиме инлайн - 2000тг/неделя\n"
                            "Отправка ссылки на ваш канал в боте (при обработке длинных текстов) - 5000тг/неделя\n\n"
                            "Обращаться к @katawabaka")"""
        await message.reply("Сәлем, мен кириллицадан латынға аударып жатырмын.\n"
                            "Боту можно отправлять документы (docx, pptx, xlsx, odt, ods, odp) и текст, а также "
                            "использовать напрямую в других чатах, "
                            "написав @QazLatinBot\n\n"

                            "Sälem, men kirillisadan latynğa audaryp jatyrmyn.\n"
                            "Sız botqa qūjattar (docx, pptx, xlsx, odt, ods, odp) men mätındı jıbere alasyz, "
                            "sondai-aq ony basqa chattarda tıkelei paidalana alasyz.\n "
                            "@QazLatinBot jazu arqyly\n\n @katawabaka"
                            , reply_markup=start_markup())
    else:
        await message.reply("Сәлем, мен кириллицадан латынға аударып жатырмын.\n"
                            "Боту можно отправлять документы (docx, pptx, xlsx, odt, ods, odp) и текст, а также "
                            "использовать "
                            "напрямую в других чатах, "
                            "написав @QazLatinBot\n\n"

                            "Sälem, men kirillisadan latynğa audaryp jatyrmyn.\n"
                            "Sız botqa qūjattar (docx, pptx, xlsx, odt, ods, odp) men mätındı jıbere alasyz, "
                            "sondai-aq ony basqa "
                            "chattarda tıkelei paidalana alasyz.\n"
                            "@QazLatinBot jazu arqyly\n\n@katawabaka"
                            , reply_markup=start_markup())


@dp.message_handler()
async def echo(message: types.Message):
    dlina = len(message.text)
    check_member = await bot.get_chat_member('@pafekuto_seikatsu', message.from_user.id)
    if check_member.status not in ["member", "creator"] and dlina > 200:
        return await message.reply("Ваш текст слишком длинный. Чтобы обработать его подпишитесь на канал и отправьте "
                                   "его еще раз", reply_markup=check_keyboard())
    else:
        text = message.parse_entities(as_html=True)
        print(text)
        text = replace_kiril(text)
        await message.answer(text, parse_mode='html')


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def scan_message(message: types.Message):
    check_member = await bot.get_chat_member('@pafekuto_seikatsu', message.from_user.id)
    if check_member.status not in ["member", "creator"]:
        return await message.reply("Чтобы обработать документ подпишитесь на канал и отправьте "
                                   "файл еще раз", reply_markup=check_keyboard())
    else:
        if message.document.file_name[-4:] in formats:
            doc_id: str = hashlib.md5((message.document.file_name + str(time.time())).encode()).hexdigest()
            doc_id = doc_id + message.document.file_name[-4:]
            path = f'files_temp/{doc_id}'
            new_path = f'files_temp/{message.document.file_name}'
            await message.document.download(path)
            docx_replace(path, new_path)
            await message.answer_document(open(new_path, 'rb'))
            os.remove(path)
            os.remove(new_path)
        else:
            await message.answer('неверный формат', parse_mode='html')


@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    text = inline_query.query or '.'
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    ad_id: str = 'advertisement'
    descript: str = 'нажмите сюда, чтобы отправить'
    text = replace_kiril(text)
    if len(text) < 200:
        input_content = InputTextMessageContent(text)
    else:
        descript: str = 'напишите в лс боту чтобы перевести целиком'
        input_content = InputTextMessageContent(text[:200]+'...')
    ad_content = InputTextMessageContent(message_text='Перейти в канал "арматура"')
    item = InlineQueryResultArticle(
        id=result_id,
        thumb_url='https://akorda.kz/assets/media/flag_mediumThumb.jpg',
        title=f'Латынға {inline_query.query[:20]!r}...',
        description=descript,
        input_message_content=input_content,
    )
    ad = InlineQueryResultArticle(
        id=ad_id,
        thumb_url='https://pbs.twimg.com/media/E-RM4RxWYAEm0B8.jpg',
        title=f'здесь могла быть Ваша реклама',
        description=f'а пока что здесь мой личный канал @pafekuto_seikatsu',
        input_message_content=ad_content,
        reply_markup=get_keyboard()
    )
    # don't forget to set cache_time=1 for testing (default is 300s or 5m)
    await bot.answer_inline_query(inline_query.id, results=[ad, item], cache_time=50,
                                  switch_pm_text='Перейти в бота @QazLatinBot',
                                  switch_pm_parameter='ad')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

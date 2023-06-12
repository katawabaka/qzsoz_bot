import json

API_TOKEN = '5803238240:AAGFHa6H-8kTYujF4OASTHkbh6dq88j6Zec'
letters_ru_low = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                  'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'э', 'ю', 'я', 'ә', 'і', 'ң', 'ғ', 'ү', 'ұ', 'қ', 'ө', 'һ',
                  'ь', 'ъ']
letters_latin_low = ['a', 'b', 'v', 'g', 'd', 'e', 'e', 'j', 'z', 'i', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't',
                     'u', 'f', 'h', 's', 'ch', 'ş', 'ş', 'y', 'e', 'iu', 'ia', 'ä', 'ı', 'ñ', 'ğ', 'ü', 'ū', 'q', 'ö',
                     'h', "", ""]
letters_ru_high = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
                   'У', 'Ф', 'Х', 'Ц', 'Ш', 'Щ', 'Ы', 'Э', 'Ә', 'І', 'Ң', 'Ғ', 'Ү', 'Ұ', 'Қ', 'Ө', 'Һ',
                   'Ь', 'Ъ']
"""letters_latin_high = ['A', 'B', 'V', 'G', 'D', 'E', 'Ö', 'J', 'Z', 'İ', 'İ', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S',
                      'T', 'U', 'F', 'H', 'S', 'Ch', 'Ş', 'Ş', 'Y', 'E', 'İu', 'Ia', 'Ä', 'I', 'Ñ', 'Ğ', 'Ü', 'Ū', 'Q',
                      'Ö', 'H', "", ""]"""

letters_latin_high = ['A', 'B', 'V', 'G', 'D', 'E', 'Ö', 'J', 'Z', 'İ', 'İ', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S',
                      'T', 'U', 'F', 'H', 'S', 'Ş', 'Ş', 'Y', 'E', 'Ä', 'I', 'Ñ', 'Ğ', 'Ü', 'Ū', 'Q',
                      'Ö', 'H', "", ""]

letters = {}

huevye_letters = {'Ю': ['İu', 'İU'], 'Я': ['İa', 'İA'], 'Ч': ['Ch', 'CH']}

for i in range(len(letters_ru_low)):
    letters[letters_ru_low[i]] = letters_latin_low[i]

for i in range(len(letters_ru_high)):
    letters[letters_ru_high[i]] = letters_latin_high[i]

formats = ['docx', 'pptx', 'xlsx', '.doc', '.xls', '.ppt', '.odt', '.odp', '.ods']
huevye_letters = {'Ю': ['İu', 'İU'], 'Я': ['İa', 'İA'], 'Ч': ['Ch', 'CH']}

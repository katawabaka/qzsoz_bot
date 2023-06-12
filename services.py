from config import letters, huevye_letters
import zipfile


def docx_replace(source, latin):
    zin = zipfile.ZipFile(source, 'r')
    zout = zipfile.ZipFile(latin, 'w')

    for item in zin.infolist():
        buffer = zin.read(item.filename)
        print(item.filename)
        if item.filename.endswith('xml'):
            res = buffer.decode("utf-8")
            res = replace_kiril(res)
            buffer = res.encode("utf-8")

        zout.writestr(item, buffer)

    zout.close()
    zin.close()


def replace_kiril(source):
    for letter in list(letters.keys()):
        source = source.replace(letter, letters[letter])
    for letter in list(huevye_letters.keys()):
        x = source.find(letter)
        while x != -1:
            x = source.find(letter)
            if x != -1:
                try:
                    source[source.find(letter) + 1].isupper()
                    if source[source.find(letter) + 1].isupper() or source[source.find(letter) - 1].isupper():
                        print('?')
                        source = source[:x] + huevye_letters[letter][1] + source[x + 1:]
                        print(huevye_letters[letter][1])
                    else:
                        source = source[:x] + huevye_letters[letter][0] + source[x + 1:]
                except IndexError:
                    if source[source.find(letter) - 1].isupper():
                        source = source[:x] + huevye_letters[letter][1] + source[x + 1:]
                    else:
                        source = source[:x] + huevye_letters[letter][0] + source[x + 1:]

    return source

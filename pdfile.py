import fitz
from config import letters

"""new_data = {key.encode('utf-8'): val.encode('utf-8') for key, val in letters.items()}
doc = fitz.Document('ГОСТ 34321-06.pdf')
count = doc.page_count
print(count)
for i in range(count):
    ru = doc[i].get_text()
    print(ru)
    for i in letters:
        ru.replace(i, letters[i])
    print(ru)
doc.save('cock.pdf')"""
import fitz

doc = fitz.open("ГОСТ 34321-06.pdf")
count = doc.page_count
for i in range(count):
    page = doc[i]
    print(page.get_text())
    for rect in page.search_for('а'):
        page.

page.apply_redactions()
doc.save('cock.pdf')
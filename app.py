from convert import Convert
import json

js = json.loads(open('layout.json','r',encoding='utf-8').read())
data1 = Convert().openPDF('copel.pdf').convert().normalizeText().getLayout(js)
data2 = Convert().openPDF('copel2.pdf').convert().normalizeText().getLayout(js)
print(data1)
print(data2)
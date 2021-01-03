from convert import Convert


#LAYOUT:
#   UN. CONS.: 6,1
#   DT REF.: 6,0
#   VALOR: 8,2
#   RESPONS.: 10
#   END.: 11
#   LOCAL.: 12,0-4
#   CEP: 12,7
#   CPF: 13,1

data = Convert().openPDF('copel.pdf').convert().normalizeText().getList()
uncons = data[6][1]
dtref = data[6][0]
valor = data[8][2]
resp = " ".join(data[10])
end = " ".join(data[11])
local = " ".join(data[12][0:5])
cep = data[12][7]
cpf = data[13][1]
print('un consumidora: %s' %uncons)
print('data: %s' %dtref)
print('valor: %s' %valor)
print('responsável: %s' %resp)
print('endereço: %s' %end)
print('local: %s' %local)
print('cep: %s' %cep)
print('cpf: %s' %cpf)
# phrase = Convert().openPDF('copel2.pdf').convert().normalizeText().getList()
# print(phrase[4][4])
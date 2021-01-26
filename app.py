from convert import Convert
import json

#abre o layout utilizado
jpdfcopel = json.loads(open('layoutpdfcopel.json','r',encoding='utf-8').read())
jpdftelecom = json.loads(open('layouttelecom.json','r',encoding='utf-8').read())
#Abre a conta, converte em texto, normaliza (remove linhas em branco e espaços excedentes)
conta = Convert().openFile('Fatura Copel Energia - 06-2020 - UC 85584010.pdf').convert().normalizeText()
# conta = Convert().openFile('Fatura Copel Telecom - 06-2020 - NI 1332822-4.pdf').convert().normalizeText()
#lista com os campos da conta, dividos palavra por palavra
info_conta = conta.getList()
# print(info_conta)
#aplicação de formatação da conta pelo layout
if conta.detect("TELECOMUNICACOES"):
    conta_formatada = conta.getLayout(jpdftelecom)
else:
    conta_formatada = conta.getLayout(jpdfcopel)
    
print(conta_formatada)
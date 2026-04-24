import json

try:
    with open("arquivos.json","r")as myjson:
        arquivos = json.load(myjson)
except FileNotFoundError:
    arquivos = []

class Anotar():
    def __init__(self,nome, gasto,):
        self.total= 0
        self.nome = nome
        self.gasto= gasto
        arquivos.append({
            "Nome":nome,
            "Gasto":gasto
        })
        with open("arquivos.json","w") as myjson:
            json.dump(arquivos, myjson, indent=3)
        for i in arquivos:
            self.total += i["Gasto"]

    def Diminuir(self, quantia):
        self.quantia= quantia
        if self.total == 0:
            print("Não a nenhum gasto feito nesse mês! ")
        else:
            self.total -= self.quantia
    
    def Listar(self):
        for x in arquivos:
            print(x)
    
    def Somar(self,):
        print(F"Somando todos os gastos deu R$ {self.total} Reais")
    
g1= None
while True:
    janela= int(input(" \n 1- Anotar gasto \n 2- Diminuir gasto \n 3- Listar gasto \n 4- Somar gastos \n 0- Sair \n Digite o numero desejado: "))
    if janela == 1:
        name= input("Digite o nome objeto em que gastou: ")
        value= float(input("Digite o valor: "))
        g1= Anotar(nome= name, gasto= value)
    elif janela == 2:
        if g1:
           quantia = float(input("Digite a quantia: "))
           g1.Diminuir(quantia)
        else:
             print("Crie um gasto primeiro!")
    elif janela == 3:
        g1.Listar()
    elif janela == 4:
        g1.Somar()
    else:
        break
#FUNÇÕES
def criarTxt(arqName):
    try:
        arq = open(arqName+'.txt', 'r')

    except:
        arq = open(arqName+'.txt', 'w')
        arq.close()

    return arqName+'.txt'

def macNaLinha(mac, texto):
    if mac in texto:
        return True
    else:
        return False
#VÁRIAVEIS
mac = "38:9a:f6:97:3e:97"
arq = open("C:/Users/filip/Downloads/rsipsd/rsipsd/Coleta de 15 minutos.txt", "r")
nomeArq = criarTxt("dados")
texto = arq.readlines()
qtLinhas = len(texto)
status = "n"

for nLinha in range(qtLinhas):
    linha = texto[nLinha]
    resposta = macNaLinha(mac, linha)
    respostaCount = macNaLinha("Count:", linha)
    arq1 = open(nomeArq,"a")
    print(status)
    if respostaCount == True:
        if status == "y":
            print (linha)
            status = "n"
            arq1.write(linha)
        else:
            print(linha)
    else:
        if resposta == True and nLinha != qtLinhas:
            status = "y"
            arq1.write(linha)
        else:
            continue
arq.close()
arq1.close()

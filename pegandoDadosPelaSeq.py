#!/usr/bin/env python
# -*- coding: utf-8 -*-
#FUNÇÕES
def criarTxt(arqName):
    try:
        arq = open(arqName+'.txt', 'r')

    except:
        arq = open(arqName+'.txt', 'w')
        arq.close()

    return arqName+'.txt'

def macNaLinha(mac, linha):
    if mac in linha:
        return True
    else:
        return False

def localizarArea(tempomac):
    areadomac = ""
    tempoadd = 10800
    if 1531598820 <= tempomac < 1531599120:
        areadomac = "area-infantil"
        return areadomac
    elif 1531598700 <= tempomac < 1531598820:
        areadomac = 'area-entrada-vitrine'
        return areadomac
    elif 1531598400 <= tempomac <= 1531598640 or 1531600680 <= tempomac < 1531600740:
        areadomac = "area-caixa"
        return areadomac
    elif 1531599540 <= tempomac < 1531599720:
        areadomac = "area-leitura2"
        return areadomac
    elif 1531599780 <= tempomac < 1531600200:
        areadomac = "area-geek"
        return areadomac
    elif 1531599120 <= tempomac < 1531599540:
        areadomac = "area-leitura1"
        return areadomac
    elif 1531600260 <= tempomac < 1531600320:
        areadomac = "area-literatura1"
        return areadomac
    elif 1531600380 <= tempomac < 1531600500:
        areadomac = 'area-banca'
        return  areadomac
    elif 1531600980 <= tempomac < 1531601100:
        areadomac = 'area-artes'
        return  areadomac
    elif 1531601460 <= tempomac < 1531601580:
        areadomac = 'area-fora'
        return  areadomac
    elif 1531600920 <= tempomac < 1531600980:
        areadomac = 'area-cd'
        return areadomac
    return areadomac


def procuraPotencia(linha):
    args = linha.split(" ")
    potencia = int(args[1])
    return potencia

def procuraTempo(linha):
    tam = len(linha)
    args = linha.split(": ")
    tempo = float(args[7])
    return tempo

def macsAreas(listamacs, listatxts, tempos, arquivo):
    macs = {}
    for num_txt in range(len(listatxts)):
        txt = listatxts[num_txt]
        qtLinhas = len(txt)
        for num_mac in range(len(listamacs)):
            mac = listamacs[num_mac]
            info = []
            count = 0
            for nLinha in range(qtLinhas):
                linha = txt[nLinha]
                tempo_inic = tempos[num_txt]
                nome = str(num_txt)
                resposta = macNaLinha(mac, linha)
                if (resposta):
                    potencia = procuraPotencia(linha)
                    tempo_seg = procuraTempo(linha)
                    tempo_total = tempo_inic + tempo_seg
                    area = localizarArea(tempo_total)
                    print(area)
                    if(area != ""):
                        count += 1
                        potencia_dic = {"potencia": potencia}
                        tempo_dic = {"tempo na area": tempo_total}
                        txt_dic = {"txt": nome}
                        area_dic = {"area": area}
                        temp = [tempo_dic, txt_dic, area_dic, potencia_dic]
                        linha_wrt = mac + ";" + area + ";" + nome + ";" + str(tempo_total) + ";" + str(potencia)
                        escreveInfo(linha_wrt, arquivo[num_mac])
                        info.append(temp)
                        macs[mac] = {count: info}
    return macs


def escreveInfo(info, arquivo):
    arq = open(arquivo, "a")
    info = info + "\n"
    arq.write(info)

#VÁRIAVEIS
mac1 = "88:79:7e:94:86:e4"
mac2 = "50:92:b9:a4:21:0a"
nomearq1 = "Livraria Cultura1531598412.7513387.txt"
nomearq2 = "Livraria Cultura1531598437.6770883.txt"
nomearq3 = "Livraria Cultura1531598435.563922.txt"

arq1 = open(nomearq1, "r")
arq2 = open(nomearq2, "r")
arq3 = open(nomearq3, "r")
arquivo1 = criarTxt("macmotog")
arquivo2 = criarTxt("macsamsung")
texto1 = arq1.read().split("\n")
texto2 = arq2.read().split("\n")
texto3 = arq3.read().split("\n")

tempo3 = 1531598436.652075
tempo2 = 1531598438.6926088
tempo1 = 1531598413.7586567

nomes = ["3"]
txtlist = [texto1, texto2, texto3]
maclist = [mac1, mac2]
tempos = [tempo1, tempo2, tempo3]
arquivo = [arquivo1, arquivo2]
dic_info = macsAreas(maclist, txtlist, tempos, arquivo)
print(dic_info)



arq1.close()
arq2.close()
arq3.close()

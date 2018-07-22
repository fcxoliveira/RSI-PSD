def ler_areas(txt):
    arq = open(txt,"r")
    tempoinicial_1700 = 1531587600
    texto = arq.read().split("\n")
    areas = {}
    for area in range(len(texto)):
        try:
            info = texto[area].split(';')
            entrada = info[1]
            temposiniciais = entrada.split(":")
            #print(temposiniciais)
            horasaddentrada  = (int(temposiniciais[0]) - 17)*3600
            minutosaddentrada = (int(temposiniciais[1]) - 0)*60
            tempoaddentrada = tempoinicial_1700 + horasaddentrada + minutosaddentrada
            #print(tempoaddentrada)


            saida = info[2]
            temposfinais = saida.split(":")
            #print(temposfinais)
            horasaddsaida  = (int(temposfinais[0]) - 17)*3600
            minutosaddsaida = (int(temposfinais[1]) - 0)*60
            tempoaddsaida = tempoinicial_1700 + horasaddsaida + minutosaddsaida
            #print(tempoaddsaida)

            nome = info[0]
            string = str(tempoaddentrada) + ":" + str(tempoaddsaida)
            areas[string] = nome
        except:
            continue
    arq.close()
    return areas

area = ler_areas("tempo_dos_locais.txt")
print(area)

from sklearn import tree
from randomList import randomList
def criarDataList(lista):
    valores = []
    classes = []
    for i in range(len(lista)):
        nlista = lista[i].split(";")
        temp = [float(nlista[0]), float(nlista[1]), float(nlista[2])]
        temp2 = [nlista[3]]
        valores.append(temp)
        classes.append(temp2)
    return valores, classes
arq_med = open("base-media-cultura.csv","r")
arq_mdn = open("base-mediana-cultura.csv","r")

instancias_med = arq_med.read().split("\n")
instancias_med = instancias_med[1:]
instancias_mdn = arq_mdn.read().split("\n")
instancias_mdn = instancias_mdn[1:]

tt_med, to_med = randomList(instancias_med)
tt_mdn, to_mdn = randomList(instancias_mdn)

treino_med, y_to  = criarDataList(to_med)
teste_med, y_tt = criarDataList(tt_med)
treino_mdn, z_to = criarDataList(to_mdn)
teste_mdn, z_tt = criarDataList(tt_mdn)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(treino_med, y_to)

clf1 = tree.DecisionTreeClassifier()
clf1 = clf1.fit(treino_mdn, z_to)
print("Teste com Média")
for k in range(len(teste_med)):
    print("Classe Predita:")
    print(clf.predict([teste_med[k]]))
    print("Classe Resposta:")
    print(y_tt[k][0])
    print("--------")
    
print("Teste com Mediana")
for p in range(len(teste_mdn)):
    print("Classe Predita:")
    print(clf.predict([teste_mdn[p]]))
    print("Classe Resposta:")
    print(z_tt[p][0])
    print("--------")


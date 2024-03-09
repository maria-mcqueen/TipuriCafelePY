#domeniu--------------------------------
def creeazaCafea(cod,nume,tara,pret):
    return{
        "cod": cod,
        "nume": nume,
        "tara": tara,
        "pret": pret
    }

def getCod(cafea):
    return cafea["cod"]

def getNume(cafea):
    return cafea["nume"]

def getTara(cafea):
    return cafea["tara"]

def getPret(cafea):
    return cafea["pret"]

def setCod(cafea,cod):
    cafea[cod] = "cod"

def setNume(cafea,nume):
    cafea["nume"] = nume

def setTara(cafea,tara):
    cafea["tara"] = tara

def setPret(cafea,pret):
    cafea["pret"] = pret


def toString(cafea):
    return " cod " + str(getCod(cafea)) + " nume " + getNume(cafea) + " tara " + getTara(cafea) + " pret " + str(getPret(cafea))



#operatii------------------------

def adaugaCafea(cod,nume,tara,pret,listaCafele):
    '''
    adauga cafea
    :param cod: int
    :param nume: str
    :param tara: str
    :param pret: fl
    :param listaCafele:lista
    :return:
    '''

    cafea = creeazaCafea(cod,nume,tara,pret)
    listaCafele.append(cafea)

def modificaCafea(cod,numeNou,taraNou,pretNou,listaCafele):
    '''
    modifica cafea
    :param cod: int
    :param numeNou:str
    :param taraNou: str
    :param pretNou: int
    :param listaCafele:lista
    :return:
    '''
    for cafea in listaCafele:
        if getCod(cafea) == cod:
            setNume(cafea,numeNou)
            setTara(cafea,taraNou)
            setPret(cafea,pretNou)

def stergeCafea(cod,listaCafele):
    '''
    sterge cafea
    :param cod: int
    :param listaCafele: lista
    :return:
    '''

    for cafea in listaCafele:
        if getCod(cafea) == cod:
            listaCafele.remove(cafea)

def cautare(cheie, listaCafele):
    rezultat = []
    for cafea in listaCafele:
        if cheie in str(getCod(cafea)) or cheie in getTara(cafea) or cheie in str(getPret(cafea)) or cheie in getNume(cafea):
            rezultat.append(cafea)
    return rezultat

def stergeCafeaDupaTara(tara, listaCafele):
    '''
    sterge dupa tara
    :param tara: str
    :param listaCafele:lista
    :return:
    '''
    i=0
    while i < len(listaCafele):
        if getTara(listaCafele[i]) == tara:
            listaCafele.pop(i)
            i-=1
        i+=1

def cafeleDinInterval(pretMin, pretMax,listaCafele):
    '''
    cafele din interval
    :param pretMin: int
    :param pretMax: int
    :param listaCafele:lista
    :return:
    '''

    rezultat = []
    for cafea in listaCafele:
        if pretMin < getPret(cafea) <pretMax:
            rezultat.append(cafea)

    return rezultat


def sumaPretPerTara(listaCafele):
    '''
    suma per tara
    :param listaCafele:lista
    :return:
    '''
    rezultat = {}
    for cafea in listaCafele:
        tara = getTara(cafea)
        pret = getPret(cafea)
        if tara in rezultat:
            rezultat[tara] +=pret
        else:
            rezultat[tara] =pret
    return rezultat

#ui-----------------------------------

def printMenu():
    print("1.Adauga cafea")
    print("2.Modifica cafea")
    print("3.Sterge cafea")
    print("4.Sterge cafele dupa tara")
    print("5.Afiseaza cafele din interval")
    print("6.Suma preturi per tara")
    #print("7.")
    #print("8.")
    print("c.Cauta cafea dupa cheie")
    print("a.Afiseaza cafele")
    print("x.Iesire")

def uiAdaugaCafea(listaCafele):
    try:
        cod = int(input("dati codul: "))
        nume = input("dati numele: ")
        tara = input("dati tara: ")
        pret= float(input("dati pretul: "))
        adaugaCafea(cod,nume,tara,pret,listaCafele)
    except ValueError as e:
        print(e)

def uiModificaCafea(listaCafele):
    try:
        cod = int(input("dati codul pt modificare: "))
        numeNou =input("numele nou: ")
        taraNou=input("dati tara 9: ")
        pretNou= float(input("dati pretul nou: "))
        modificaCafea(cod,numeNou,taraNou,pretNou,listaCafele)
    except ValueError as e:
        print(e)

def uiStergeCafea(listaCafele):
    try:
        cod= int(input("dati codul de sters: "))
        stergeCafea(cod,listaCafele)
    except ValueError as e:
        print(e)

def uiStergeDupaTara(listaCafele):
    try:
        tara = input("dati tara: ")
        stergeCafeaDupaTara(tara,listaCafele)
    except ValueError as e:
        print(e)

def printCafele(listaCafele):
    for cafea in listaCafele:
        print(toString(cafea))

def uiCautare(listaCafele):
    try:
        cheie = input("dati cheia: ")
        return cautare(cheie,listaCafele)
    except IndexError as e:
        print(e)

def uiCafeleDinInterval(listaCafele):
    try:
        pretMin = int(input("dati pretul minim: "))
        pretMax = int(input("dati pretul maxim: "))
        return cafeleDinInterval(pretMin,pretMax,listaCafele)
    except ValueError as e:
        print(e)

#teste------------------------------

def testAdauga():
    listaCafele=[]
    adaugaCafea(1,"tas","esp",1,listaCafele)
    adaugaCafea(2,"nes","eng",2,listaCafele)

    assert len(listaCafele) == 2


def testModifica():
    listaCafele = []
    adaugaCafea(1, "tas", "esp", 1, listaCafele)
    adaugaCafea(2, "nes", "eng", 2, listaCafele)

    modificaCafea(1,"sat","esp",1,listaCafele)

    assert getNume(listaCafele[0]) == "sat"

def testSterge():
    listaCafele = []
    adaugaCafea(1, "tas", "esp", 1, listaCafele)
    adaugaCafea(2, "nes", "eng", 2, listaCafele)

    stergeCafea(1,listaCafele)

    assert len(listaCafele) == 1

def testCauta():
    listaCafele = []
    adaugaCafea(1, "tas", "esp", 1, listaCafele)
    adaugaCafea(2, "nes", "eng", 2, listaCafele)

    rezultat = cautare("tas",listaCafele)
    assert len(rezultat) == 1

def testStergeDupaTara():
    listaCafele = []
    adaugaCafea(1, "tas", "esp", 1, listaCafele)
    adaugaCafea(2, "nes", "eng", 2, listaCafele)

    assert len(listaCafele) == 2

    stergeCafeaDupaTara("esp",listaCafele)

    assert len(listaCafele) == 1

def testCafeleDinInterval():
    listaCafele = []
    adaugaCafea(1, "tas", "esp", 1, listaCafele)
    adaugaCafea(2, "nes", "eng", 5, listaCafele)
    adaugaCafea(3,"don","rou",7,listaCafele)

    assert len(listaCafele) == 3
    rezultat = cafeleDinInterval(4,9,listaCafele)
    assert len(rezultat) == 2

def testSumaPerTara():
    listaCafele = []
    adaugaCafea(1, "tas", "esp", 1, listaCafele)
    adaugaCafea(2, "nes", "esp", 5, listaCafele)
    adaugaCafea(3, "don", "rou", 7, listaCafele)

    rezultat = sumaPretPerTara(listaCafele)

    assert rezultat["esp"] == 6

def testAll():
    testAdauga()
    testModifica()
    testSterge()
    testCauta()
    testStergeDupaTara()
    testCafeleDinInterval()
    testSumaPerTara()

#main--------------------------------

def main():
    testAll()
    listaCafele=[]
    while True:
        printMenu()
        optiune =input("dati optiunea: ")
        if optiune == "1":
            uiAdaugaCafea(listaCafele)
        elif optiune =="2":
            uiModificaCafea(listaCafele)
        elif optiune == "3":
            uiStergeCafea(listaCafele)
        elif optiune =="4":
            uiStergeDupaTara(listaCafele)
        elif optiune =="5":
            printCafele(uiCafeleDinInterval(listaCafele))
        elif optiune =="6":
            print(sumaPretPerTara(listaCafele))
        elif optiune =="a":
            printCafele(listaCafele)
        elif optiune == "c":
            printCafele(uiCautare(listaCafele))
        elif optiune =="x":
            break
        else:
            print("optiune gresita")


main()
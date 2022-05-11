# lista=["Warszawa",'Gdansk','Sosnowiec','Grudziadz']
# print(list(map(lambda x: x[:3], lista)))

# lista=[]
# with open('australian.dat', 'r') as file:
#     for line in file:
#         lista.append(list(map(lambda x: float(x),line.split())))
# for x in range(6):
#     print(lista[x])


# lista=[5,5]
# lista1=[1,1]
# print(lista.index(0))
import math
import math as m
import random
import numpy as np

listaData = []

with open('australian.dat', 'r') as file:
    for line in file:
        listaData.append(list(map(lambda var: float(var), line.split())))


def odleglosc(index1, index2, lista):
    wynik = 0
    for i in range(len(lista[index1]) - 1):
        wynik += m.pow(lista[index1][i] - lista[index2][i], 2)

    print(m.sqrt(wynik))
    return m.sqrt(wynik)


def pracaDomowa(lista):
    my_dict = {"0": [], "1": []}
    for i in range(len(lista) - 1):
        for j in range(i, len(lista) - 1):
            if lista[i][len(lista[0]) - 1] == 1:
                my_dict['1'].append(odleglosc(i, j, lista))
            else:
                my_dict['0'].append(odleglosc(i, j, lista))

    return my_dict


def mierzymy(x, lista):
    slownik = dict()
    listatupek = []
    suma = 0
    for element in lista:
        for i in range(max(len(x), len(element)) - 1):
            suma += (x[i] - element[i]) ** 2
        zmienna = m.sqrt(suma)
        suma = 0
        listatupek.append((element[14], zmienna))
        if element[14] in slownik.keys():
            slownik[element[14]].append(zmienna)
        else:
            slownik[element[14]] = [zmienna]
    return listatupek


def grupujemy(lista):
    grupy = dict()
    for element in lista:
        decyzyjna = element[0]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(element[1])
        else:
            grupy[decyzyjna] = [element[1]]
    # for klucz in grupy.keys():
    #     grupy[klucz].sort()
    # for klucz in grupy.keys():
    #     suma = 0
    #     for ele in grupy[klucz][:k]:
    #         suma += ele
    #     grupy[klucz] = suma
    return grupy


def decyzja(slownik):
    klucze = list(slownik.keys())
    ilosc = 1
    klasa = klucze[0]
    minimum = slownik[klucze[0]]
    for key in klucze[1:]:
        if minimum > slownik[key]:
            minimum = slownik[key]
            klasa = key
            ilosc = 1
        elif minimum == slownik[key]:
            ilosc += 1
    if ilosc > 1:
        return
    return klasa


def metryka_euklidesowa(l1, l2):
    suma = 0
    for i in range(max(len(l1),
                       len(l2)) - 1):  # max bo l1 może być len 14 labo 15, a l2 też 15 lub 14 (14 bo bez decyzji kredytowej)
        suma += (l1[i] - l2[i]) ** 2
    return m.sqrt(suma)


def metrykaEuklidesowa2(x, y):
    v1 = np.array(x)
    v2 = np.array(y)
    a = v2 - v1
    return m.sqrt(np.dot(a, a))


def praca_domowa(array):
    lista_nowych_wartosci = []
    for x in array:
        lista_nowych_wartosci.append(x[:14] + [float(random.randint(0, 1))])

    slownik_minimalnych_odleglosci = dict()
    slownik_odleglosci = dict()

    zmiany = 0
    aktualna_odleglosc = 0
    iter = 0

    while True:
        iter += 1
        for decyzja in range(2):
            for i in range(len(lista_nowych_wartosci)):
                if lista_nowych_wartosci[i][-1] == decyzja:
                    odleglosc = 0
                    for j in range(len(lista_nowych_wartosci)):
                        if lista_nowych_wartosci[j][-1] == decyzja:
                            odleglosc += metrykaEuklidesowa2(lista_nowych_wartosci[i], lista_nowych_wartosci[j])
                    slownik_odleglosci[i] = odleglosc
            min_odleglosc = list(dict(sorted(slownik_odleglosci.items(), key=lambda value: value[1])).keys())[0]
            slownik_minimalnych_odleglosci[decyzja] = min_odleglosc
            slownik_odleglosci = {}

        print(f'środek ciężkości: {slownik_minimalnych_odleglosci}')
        if lista_nowych_wartosci[slownik_minimalnych_odleglosci.get(0)][-1] != 0:
            print(
                f'błąd dla zero!!!')
        if lista_nowych_wartosci[slownik_minimalnych_odleglosci.get(0)][-1] != 0:
            print(
                f'błąd dla jeden!!!')

        for decyzja in range(2):
            for i in range(len(lista_nowych_wartosci)):

                if i in slownik_minimalnych_odleglosci.values():
                    continue

                if lista_nowych_wartosci[i][-1] == decyzja:
                    aktualna_odleglosc = metrykaEuklidesowa2(
                        lista_nowych_wartosci[slownik_minimalnych_odleglosci.get(decyzja)],
                        lista_nowych_wartosci[i])
                    odleglosc_zero = metrykaEuklidesowa2(lista_nowych_wartosci[slownik_minimalnych_odleglosci.get(0)],
                                                         lista_nowych_wartosci[i])
                    odleglosc_jeden = metrykaEuklidesowa2(lista_nowych_wartosci[slownik_minimalnych_odleglosci.get(1)],
                                                          lista_nowych_wartosci[i])
                    if aktualna_odleglosc > odleglosc_jeden:
                        lista_nowych_wartosci[i][-1] = float(1)
                        zmiany += 1
                    if aktualna_odleglosc > odleglosc_zero:
                        lista_nowych_wartosci[i][-1] = float(0)
                        zmiany += 1

        elementow_jeden = 0
        elementow_zero = 0

        for x in lista_nowych_wartosci:
            if x[14] == 1.0:
                elementow_jeden += 1
            if x[14] == 0.0:
                elementow_zero += 1

        if str(iter):
            iter_string = str(iter)

        print(
            f'zmiany w {iter_string} iteracji {zmiany}\nelementów 0: {elementow_zero} ||| elementow 1:{elementow_jeden}')
        if zmiany == 0:
            break
        zmiany = 0

    return lista_nowych_wartosci


def func1(x):
    return x ** 2


def monte_carlo(func, poziom, pion, ilosc_pkt):
    iloscPodWykresem = 0
    punkty_x = np.random.uniform(0, poziom, ilosc_pkt)
    punkty_y = np.random.uniform(0, pion, ilosc_pkt)
    punkty_y_wyliczone = [func(x) for x in punkty_x]

    for i in range(len(punkty_y)):
        if punkty_y[i] <= punkty_y_wyliczone[i]:
            iloscPodWykresem += 1

    pole = iloscPodWykresem / ilosc_pkt * poziom * pion

    return round(pole, 2)


def metodaProstokatowIlosc(iloscPodzialow, funkcja, poziom):
    suma = 0
    for i in range(iloscPodzialow):
        x_0 = poziom / iloscPodzialow * i - 1
        x_1 = poziom / iloscPodzialow * i
        y_0 = funkcja(x_0)
        y_1 = funkcja(x_1)
        srednia = (y_0 + y_1) / 2
        suma += srednia
    return round(suma / iloscPodzialow)


def metodaProstokatowEpsilon(epsilon, funkcja, poziom):
    suma1 = 0
    iloscPodzialow = 0
    wynik = math.inf
    while wynik >= epsilon:
        suma = 0
        iloscPodzialow += 10
        for i in range(iloscPodzialow):
            x_0 = poziom / iloscPodzialow * i - 1
            x_1 = poziom / iloscPodzialow * i
            y_0 = funkcja(x_0)
            y_1 = funkcja(x_1)
            srednia = (y_0 + y_1) / 2
            suma += srednia
        if suma1 == 0:
            suma1 = suma
        else:
            wynik = (suma - suma1) / iloscPodzialow
            suma1 = suma

    return suma / iloscPodzialow


# def sredniaArytmetyczna(lista):
#     listaDanych=[]
#
#     for x in lista:
#         listaDanych.append(x[:4])
#
#     print(listaDanych)
#     print(listaSrednich)
def wnioskowanieStatystyczne(lista):
    listaDanych = []
    listaSrednich = []
    listaOdchylen = []
    listaWariancji = []
    for x in lista:
        listaDanych.append(x[:14])
    # for i in listaDanych:
    for i in listaDanych:
        count = 0
        for y in i:
            count += y
        mu = count / len(i)  # znana wartość oczekiwana
        listaSrednich.append(count / len(i))
        # wariancja
        sumaWariancja = 0
        for x in i:
            sumaWariancja += ((x - mu) ** 2) / len(i)
        listaWariancji.append(sumaWariancja)
        # odchylenie standardowe jako pierwiastek z wariancji
        s = np.sqrt(sumaWariancja)
        listaOdchylen.append(s)
    print(listaWariancji)
    print(listaOdchylen)


# sredniaArytmetyczna(listaData)
wnioskowanieStatystyczne(listaData)
# print(f"Epsilon: {metodaProstokatowEpsilon(0.02, func1, 10)}")
# print(f"Prostokaty: {metodaProstokatowIlosc(100, func1, 10)}")
# print(f"Monte Carlo: {monte_carlo(func1, 10, 10, 100)}")

# praca_domowa(listaData)
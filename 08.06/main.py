from random import random

import numpy as np
import math


def metryka_euklidesowa(l1, l2):
    suma = 0
    for i in range(max(len(l1),
                       len(l2)) - 1):  # max bo l1 może być len 14 labo 15, a l2 też 15 lub 14 (14 bo bez decyzji kredytowej)
        suma += (l1[i] - l2[i]) ** 2
    return math.sqrt(suma)


def mierzymy(x, lista):
    slownik = dict()
    listatupek = []
    suma = 0
    for element in lista:
        for i in range(max(len(x), len(element)) - 1):
            suma += (x[i] - element[i]) ** 2
        zmienna = math.sqrt(suma)
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

def metrykaEuklidesowa2Skalar(x,y):
    v1 = np.array(x)
    v2 = np.array(y)
    a = v2 - v1
    return math.sqrt(np.dot(a, a))


def praca_domowa_kolorowanie(array):
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
                            odleglosc += metrykaEuklidesowa2Skalar(lista_nowych_wartosci[i], lista_nowych_wartosci[j])
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
                    aktualna_odleglosc = metrykaEuklidesowa2Skalar(
                        lista_nowych_wartosci[slownik_minimalnych_odleglosci.get(decyzja)],
                        lista_nowych_wartosci[i])
                    odleglosc_zero = metrykaEuklidesowa2Skalar(lista_nowych_wartosci[slownik_minimalnych_odleglosci.get(0)],
                                                         lista_nowych_wartosci[i])
                    odleglosc_jeden = metrykaEuklidesowa2Skalar(lista_nowych_wartosci[slownik_minimalnych_odleglosci.get(1)],
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


def monte_carlo(func, poziomo, pionowo, ilosc_punktow):
    liczba_pod_wykresem = 0
    punkty_x = np.random.uniform(0, poziomo, ilosc_punktow)
    punkty_y = np.random.uniform(0, pionowo, ilosc_punktow)
    punkty_y_wyliczone = [func(x) for x in punkty_x]

    for i in range(len(punkty_y)):
        if punkty_y[i] <= punkty_y_wyliczone[i]:
            liczba_pod_wykresem += 1

    pole = liczba_pod_wykresem / ilosc_punktow * poziomo * pionowo

    return round(pole, 2)


def metodaProstokatowIlosc(ile_dzielone, funkcja, poziomo):
    suma = 0
    for i in range(ile_dzielone):
        x_0 = poziomo / ile_dzielone * i - 1
        x_1 = poziomo / ile_dzielone * i
        y_0 = funkcja(x_0)
        y_1 = funkcja(x_1)
        srednia = (y_0 + y_1) / 2
        suma += srednia
    return round(suma / ile_dzielone)


def metodaProstokatowEpsilon(epsilon, funkcja, poziomo):
    suma1 = 0
    iloscPodzialow = 0
    wynik = math.inf
    while wynik >= epsilon:
        suma = 0
        iloscPodzialow += 10
        for i in range(iloscPodzialow):
            x_0 = poziomo / iloscPodzialow * i - 1
            x_1 = poziomo / iloscPodzialow * i
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


def sredniaWektor():
    lst = [1, 2, 3, 4, 5]
    lstOne = [1, 1, 1, 1, 1]
    arr = np.array(lst)
    arrOne = np.array(lstOne)
    arrScalar = np.dot(arr, arrOne) / len(arr)
    return arrScalar


def wariancjaWektor():
    lst = [1, 2, 3, 4, 5]
    lstOne = [1, 1, 1, 1, 1]
    arr = np.array(lst)
    arrOne = np.array(lstOne)
    srednia = sredniaWektor()
    wariancja = np.sum(((arr - arrOne * srednia) ** 2) / len(arr))
    return wariancja


def odchylenieStandardowe():
    wariancja = wariancjaWektor()
    odchylenie = math.sqrt(wariancja)
    return odchylenie


def regresja():
    x = np.array([[1, 2], [1, 5], [1, 7], [1, 8]])
    y = np.array([1, 2, 3, 3])
    beta = np.dot((np.linalg.inv(np.dot(x.T, x))), np.dot(x.T, y))
    print(beta)


def projekcja(u, a):
    dzielenie_gora = np.dot(u.T, a)
    dzielenie_dol = np.dot(u.T, u)
    if dzielenie_dol == 0:
        return u
    return np.multiply(u, dzielenie_gora / dzielenie_dol)


def dlugosc_wektora(a):
    dlugosc = math.sqrt(np.dot(a.T, a))
    if dlugosc != 0:
        return dlugosc
    else:
        return 1


def rozklad_qr(a):
    numer_kroku = len(a[0])
    wektory = []
    dlugosc_wektora = len(a)

    for x in range(numer_kroku):
        vector_n = []
        for i in range(dlugosc_wektora):
            # wypisanie wektorów
            vector_n.append(a[i][x])
        wektory.append(vector_n)

    u_wektory = []
    e_wektory = []
    print(wektory)

    for krok in range(numer_kroku):
        if krok == 0:
            # obiczanie u1/u2 itd
            u_wektory.append(np.array(wektory[krok]))
            e_n = np.multiply(1 / dlugosc_wektora(u_wektory[krok]), u_wektory[krok])
            e_wektory.append(e_n)
            continue

        projekcja_lista = []
        for n in range(krok):
            # obiczanie projekcji
            projekcja_n = projekcja(u_wektory[n], wektory[krok])
            projekcja_lista.append(projekcja_n)

        u_n = wektory[krok]
        for n_projekcja in projekcja_lista:
            u_n = np.subtract(u_n, n_projekcja)

        u_wektory.append(u_n)
        e_n = np.multiply(1 / dlugosc_wektora(u_wektory[krok]), u_wektory[krok])
        e_wektory.append(e_n)

    q = np.array([vector for vector in e_wektory]).T
    r = np.dot(q.T, a)
    print(e_wektory)
    print(projekcja_lista)
    print(f'r\n.{r}')
    print(f'q\n.{q}')
    return np.around(np.dot(q, r), decimals=2)

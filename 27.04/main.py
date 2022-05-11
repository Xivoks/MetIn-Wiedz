import numpy as np
import math


def projekcja(u, a):
    dzielenie_gora = np.dot(u.T, a)
    dzielenie_dol = np.dot(u.T, u)
    if dzielenie_dol == 0:
        return u
    return np.multiply(u, dzielenie_gora / dzielenie_dol)


def dlugosc_macierzy(a):
    dlugosc = math.sqrt(np.dot(a.T, a))
    if dlugosc!=0:
        return dlugosc
    else:
        return 1


def dekompresja_qr(a):
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
    # print(wektory)

    for krok in range(numer_kroku):
        if krok == 0:
            # obiczanie u1/u2 itd
            u_wektory.append(np.array(wektory[krok]))
            e_n = np.multiply(1 / dlugosc_macierzy(u_wektory[krok]), u_wektory[krok])
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
        e_n = np.multiply(1 / dlugosc_macierzy(u_wektory[krok]), u_wektory[krok])
        e_wektory.append(e_n)

    q = np.array([vector for vector in e_wektory]).T

    r = np.dot(q.T, a)
    # print(e_wektory)
    # print(projekcja_lista)
    print(f'r\n.{r}')
    print(f'q\n.{q}')
    return q
    # return np.around(np.dot(q, r), decimals=2)

def nowa_macierz(a):
    q = dekompresja_qr(a)
    return np.dot(np.dot(q.T,a),q)

def wartosc_wlasna_macierzy(a):
    licznik = 0
    nowa_macierz_a = a
    while (np.diag(nowa_macierz_a)-np.dot(nowa_macierz_a,np.ones((5,1))).T).all()>0.01 :
        nowa_macierz_a = nowa_macierz(nowa_macierz_a)
        licznik=licznik+1
        print("Macierz_A_"+str(licznik)+":",nowa_macierz_a,sep="\n")
    return np.diag(nowa_macierz_a)

# matrix = [
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 1],
#     [0, 1, 0, 0, 1],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0]
# ]
# matrix = [
#     [1, 0],
#     [1, 1],
#     [0, 1]
# ]
matrix = np.array([[1.,2.,3.,4.,5.],[2.,2.,3.,4.,5.],[3.,3.,3.,4.,5.],[4.,4.,4.,4.,5.],[5.,5.,5.,5.,5.]])

qr = dekompresja_qr(matrix)
# print(f'qr\n{qr}')
# print(f'matrix_plus\n{nowa_macierz(matrix)}')

wynik = wartosc_wlasna_macierzy(matrix)
print("Wynik", np.round(wynik,decimals=4), sep = "\n")
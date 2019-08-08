import os
import sys
import math
import time
import matplotlib.pyplot as plt
import random

'''
Программа поиска в динамической строке совпадений.
06.08.2019
'''


def PoiskStandart(A, B):
    '''
    Функция принимает две строки и ищет совпадение строки B в A.
    Для сравнения используется стандартный инструмент "А in B".
    :param A: Строка с функцией динамического массива (имитации).
    :param B: Искомая строка.
    :return: True or False
    '''
    
    longA = len(A) + len(B) - 1 #Требуемая длинна для имитации динамической строки
    Coef = int(math.ceil(longA / len(A))) #Коэфициент умножения
    localA = A * Coef

    if B in localA: return True
    else: return False

def PoiskSrez(A, B):
    '''
    Функция принимает две строки и ищет совпадение строки B в A.
    Для сравнения используется поочерёдный срез из строки А и сравнение с В.
    :param A: Строка с функцией динамического массива (имитации).
    :param B: Искомая строка.
    :return: True or False
    '''

    longA = len(A) + len(B) - 1  # Требуемая длинна для имитации динамической строки.
    Coef = int(math.ceil(longA / len(A)))  # Коэфициент умножения.
    localA = A * Coef

    for i in range(0, (len(A))): # Используется ограничение подбора оригинальной строкой А.
        if localA[i:(i+len(B))] == B:
            return True
    else: return False

def PoiskPostepSravnen(A, B):
    '''
    Функция принимает две строки и ищет совпадение строки B в A.
    Для сравнения используется побуквенное сравнение строки В с А.
    :param A: Строка с функцией динамического массива (имитации).
    :param B: Искомая строка.
    :return: True or False
    '''

    for i in range(0, len(A)):
        if A[i] == B[0]: # Сравнение первого символа.
            for dyn in range(0, len(B)): # Сравнение последующих символов.
                if (i + dyn) >= len(A): # Проверка входа за пределы строки.
                    K = math.floor((i + dyn) / len(A))
                    locI = i + dyn - len(A) * K # Перенос координаты вначалодинамической строки.
                else: locI = i + dyn
                if A[locI] == B[dyn]:
                    if (dyn + 1) == len(B):return True
                    else: continue
                else: break
            else: return True
    else: return False

def Generator(Long, numSym, numStr):
    '''
    Создаёт список строк заданной длинны и количеством уникальных символов.
    Количество уникальных символов не должно превышать 26.
    :param LA: Длинна строки
    :param numSym: Количество уникальнх символов (1-26).
    :param numStr: Количство строк равное для А и В.
    :return: Список строк.
    '''

    DataSym = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k',
               'l','z','x','c','v','b','n','m']
    list = []
    for String in range(0, numStr):
        localList = []
        for sym in range(0, Long):
            localList.append(random.choice(DataSym[0:numSym])) # Добавление случайного уникального символа.
        localString= "".join(localList) # Объединение списка в строку.
        list.append(localString)
    return list


def Test(function, lenA = 0, lenB = 0, numSym = 0, numStr = 0 ):
    '''
    Функция тестирования других функций, засекает время, сравнивает результаты.
    :param function: Список тестируемых функций.
    :param lenA: Длинна строки А (динамическая строка).
    :param lenB: Длинна строки В (искомое).
    :param numSym: Количество уникальных символов.
    :param numStr: Количество строк.
    :return: Список вида [имя функции, время выполнения, длинна А, длинна В, коичесво уникальнх символов]
    '''
    
    print('Начало тестирования')
    if lenA == 0:
        lenA = int(input('Введите длинну динамической строки: '))
    if lenB == 0:
        lenB = int(input('Ввеите длинну искомой строки: '))
    if numSym == 0:
        numSym = int(input('Введите количество уникальных символов: '))
    if numStr == 0:
        numStr = int(input('Введите количество строк: '))
        
    listA = Generator(lenA, numSym, numStr)
    listB = Generator(lenB, numSym, numStr)
    locResult = []
    
    for fun in function:
        Start = time.time()
        functionResult = [fun]
        for A in listA:
            for B in listB:
                '''print('A = ', A, 'B = ', B)'''
                functionResult.append(fun(A, B)) # Выполнение функций.
        Final = time.time()
        functionResult.append(Final - Start) # Расчёт времени выполнения.
        locResult.append(functionResult)
    
    for i in range(1, len(locResult[0]) - 1): # Проверка совпадения результата.
        if locResult[0][i] == locResult[1][i] == locResult[2][i]: #Упрощение для случая из 3-х функций.
            continue
        else: 
            print(' Результаты расходятся')
            sys.exit()
    else: print('Результаты сходятся')

    ResultList = []
    for locList in locResult: # Чистка от "Да" и "Нет", добавление параметров вычисления.
        ResultList.append(locList[0])
        ResultList.append(locList[-1])
        ResultList.append(lenA)
        ResultList.append(lenB)
        ResultList.append(numSym)

    return ResultList



def Main(lenA, lenB, numSym, numStr):
    '''
    Инициирующая функция.
    :param lenA: Список длин динамической строки А.
    :param lenB: Список длин искомых строк В.
    :param numSym: Список колиества уникальных символов.
    :param numStr: Число случаев для каждого параметра.
    :return: Ничего не возвращает
    '''
    allData = []
    for LA in range(0, len(lenA)):
        for LB in range(0, len(lenB)):
            for NS in range(0, len(numSym)):
                allData.append(Test(function,lenA[LA], lenB[LB], numSym[NS], numStr)) # Вычисление всех вариантов.

    showGraph(allData)
    print(allData)


def save(name='', form='png'):
    '''
    Функция сохранения.
    :param name: Имя файла.
    :param form: Формат файла.
    :return:
    '''
    direct = os.getcwd()
    print(direct)
    plt.savefig('{}.{}'.format(name, form), form='png') #Сохранение изображение в текущей директории.

def plotGrap(*args, **kwargs):
    '''
    Функция печати графиков.
    :param args: Все списки координат Х и У.
    :param kwargs: Специальные параметры печати.
    :return:
    '''
    print('START GRAPH')
    xlist = []
    ylist = []

    for i, arg in enumerate(args):
        if (i % 2) == 0:
            xlist.append(arg)
        else:
            ylist.append(arg)
    print('Xlist = ', xlist)
    print('Ylist = ', ylist)

    colors = kwargs.pop('colors', 'k')
    linewidth = kwargs.pop('linewidth', 1)
    label = ['Standart', 'Srez', 'PoBukvenSravnenye']



    fig = plt.figure() # Создание холста
    ax = fig.add_subplot(111) # Создание области рисования
    print('AX =', type(ax))
    i = 0
    for x, y, color in zip(xlist, ylist, colors):
        lab = label[i]
        i += 1
        print(x,y,color,linewidth, lab)
        ax.plot(x, y, color = color, linewidth = linewidth, label = lab) # Создание графика

    ax.grid(True)
    ax.legend()
    plt.show()


def filtr(St1, n1, St2, n2, n3,  funct, DB):
    '''
    Функция фильтрации из общего массива данных случаев с стандартными параметрами.
    Прим. Для построения графиков используется случай, когда одна переменная изменяется, а остальные статичны.
    Фильтр находит случаи когда все статичные параметры сходятся и возвращает параметр на координате n3.
    Координаты принимаются в относительной системе где началом является название функции.
    Вид стандартной ячейки: [ Имя функции[k], время выполнения[k+1], длинна А[k+2], длинна В[k+3],
    количество уник.символов[k+4], Имя функции[k].....
    :param St1: Статичный параметр 1.
    :param n1: Координата статичного параметра 1 в относительной системе координат.
    :param St2: Статичный праметр 2.
    :param n2: Координата статичного параметра 2.
    :param n3: Координата искомого параметра (изменяемого).
    :param funct: Имя функции.
    :param DB: Список данных.
    :return: Список изеняемых параметров.
    '''
    Result = []
    for i in range(0, len(DB)):
        for k in range(0, len(DB[i])):
            if DB[i][k] == funct and DB[i][k + n1] == St1 and DB[i][k + n2] == St2: # Проверка стат.парам.
                Result.append(DB[i][k + n3])
    return Result





def showGraph(dataList):
    '''
    Фильтрация данных для построения графиков.
    P.S. Лютый костыль.
    :param dataList: Список данных.
    :return:
    '''
    T1A = filtr(lenB[0], 3, numSym[0], 4, 1, PoiskStandart, dataList)
    L1A = filtr(lenB[0], 3, numSym[0], 4, 2, PoiskStandart, dataList)
    T2A = filtr(lenB[0], 3, numSym[0], 4, 1, PoiskSrez, dataList)
    L2A = filtr(lenB[0], 3, numSym[0], 4, 2, PoiskSrez, dataList)
    T3A = filtr(lenB[0], 3, numSym[0], 4, 1, PoiskPostepSravnen, dataList)
    L3A = filtr(lenB[0], 3, numSym[0], 4, 2, PoiskPostepSravnen, dataList)

    T1B = filtr(lenA[0], 2, numSym[0], 4, 1, PoiskStandart, dataList)
    L1B = filtr(lenA[0], 2, numSym[0], 4, 3, PoiskStandart, dataList)
    T2B = filtr(lenA[0], 2, numSym[0], 4, 1, PoiskSrez, dataList)
    L2B = filtr(lenA[0], 2, numSym[0], 4, 3, PoiskSrez, dataList)
    T3B = filtr(lenA[0], 2, numSym[0], 4, 1, PoiskPostepSravnen, dataList)
    L3B = filtr(lenA[0], 2, numSym[0], 4, 3, PoiskPostepSravnen, dataList)

    T1NS = filtr(lenA[0], 2, lenB[0], 3, 1, PoiskStandart, dataList)
    NS1 = filtr(lenA[0], 2, lenB[0], 3, 4, PoiskStandart, dataList)
    T2NS = filtr(lenA[0], 2, lenB[0], 3, 1, PoiskSrez, dataList)
    NS2 = filtr(lenA[0], 2, lenB[0], 3, 4, PoiskSrez, dataList)
    T3NS = filtr(lenA[0], 2, lenB[0], 3, 1, PoiskPostepSravnen, dataList)
    NS3 = filtr(lenA[0], 2, lenB[0], 3, 4, PoiskPostepSravnen, dataList)




    colors = ['red', 'green', 'blue']

    plotGrap(L1A, T1A, L2A, T2A, L3A, T3A, colors=colors, linewidth=2)
    '''save('Long_A+')''' # Сохраняет пустые листы.
    plotGrap(L1B, T1B, L2B, T2B, L3B, T3B, colors=colors, linewidth=2)
    '''save('Long_B+')'''
    plotGrap(NS1, T1NS, NS2, T2NS, NS3, T3NS, colors=colors, linewidth=2)
    '''save('Number_symvol+)'''


function = [PoiskStandart, PoiskSrez, PoiskPostepSravnen]
# Исходные данные пока задавать здесь.
lenA = [10,20,50,100, 150, 200] # Список длин динамической строки.
lenB = [10, 20, 50, 100] # Список длин искомой строки.
numSym = [5, 10, 15, 20, 26] # Список количесва симполов. Не больше 26!
numStr = 100 # Количество генераций для каждого варианта.
Main(lenA, lenB, numSym, numStr)

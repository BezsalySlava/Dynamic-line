import os
import sys
import math
import time
import matplotlib.pyplot as plt
import random

'''
Программа поиска в динамической строке совпадений.
Search program of coincidence dynamic string.
06.08.2019
'''


def SearchStandart(A, B):
    '''
    Function takes two string and search coincidence string B in dynamic string A.
    Used standard tool 'A in B'

    Функция принимает две строки и ищет совпадение строки B в A.
    Для сравнения используется стандартный инструмент "А in B".

    :param A: Dynamic strind A. Строка с функцией динамического массива (имитации).
    :param B: Search string. Искомая строка.
    :return: True or False
    '''
    
    longA = len(A) + len(B) - 1 # Requied length to simulate a dynamic string.
    # Требуемая длинна для имитации динамической строки 
    Coef = int(math.ceil(longA / len(A))) # Coefficient multiplications. Коэфициент умножения
    localA = A * Coef

    if B in localA: return True
    else: return False

def SearchShear(A, B):
    '''
    Function takes two string and search coincidence string B in dynamic string A.
    Used consistent shear string A and comparison with B.

    Функция принимает две строки и ищет совпадение строки B в A.
    Для сравнения используется поочерёдный срез из строки А и сравнение с В.

    :param A:  Dynamic strind A. Строка с функцией динамического массива (имитации).
    :param B: Search string. Искомая строка.
    :return: True or False
    '''

    longA = len(A) + len(B) - 1  # Requied length to simulate a dynamic string.
    # Требуемая длинна для имитации динамической строки.
    Coef = int(math.ceil(longA / len(A)))  # Coefficient multiplications. Коэфициент умножения.
    localA = A * Coef

    for i in range(0, (len(A))): # Limitation shear original string A.
        # Используется ограничение подбора оригинальной строкой А.
        if localA[i:(i+len(B))] == B:
            return True
    else: return False

def SearchByLetter(A, B):
    '''
    Function takes two string and search coincidence string B in dynamic string A.
    Used letter by letter comparison string B with dynamic string A

    Функция принимает две строки и ищет совпадение строки B в A.
    Для сравнения используется побуквенное сравнение строки В с А.

    :param A: Dynamic strind A. Строка с функцией динамического массива (имитации).
    :param B: Search string. Искомая строка.
    :return: True or False
    '''

    for i in range(0, len(A)):
        if A[i] == B[0]: # First symbol comarison. Сравнение первого символа.
            for dyn in range(0, len(B)): # Following symbol comparison. Сравнение последующих символов.
                if (i + dyn) >= len(A): # Border check. Проверка входа за пределы строки.
                    K = math.floor((i + dyn) / len(A))
                    locI = i + dyn - len(A) * K # Carry to the begining string A.
                    #  Перенос координаты в начало динамической строки.
                else: locI = i + dyn
                if A[locI] == B[dyn]:
                    if (dyn + 1) == len(B):return True
                    else: continue
                else: break
            else: return True
    else: return False

def Generator(Long, numSym, numStr):
    '''
    Creates a list of strings of a given lenght and the number of unique symbols.
    The number of unique symbols must not exceed 26.

    Создаёт список строк заданной длинны и количеством уникальных символов.
    Количество уникальных символов не должно превышать 26.

    :param LA: String lenght. Длинна строки.
    :param numSym: The number of unique symbol (1-26). Количество уникальнх символов (1-26).
    :param numStr: The number of strings for A and B.
    Количство строк равное для А и В.
    :return: List of strings. Список строк.
    '''

    DataSym = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k',
               'l','z','x','c','v','b','n','m']
    list = []
    for String in range(0, numStr):
        localList = []
        for sym in range(0, Long):
            localList.append(random.choice(DataSym[0:numSym])) # Add random unique symbol,
            # Добавление случайного уникального символа.
        localString= "".join(localList) # Union a list into a string. Объединение списка в строку.
        list.append(localString)
    return list


def Test(function, lenA = 0, lenB = 0, numSym = 0, numStr = 0 ):
    '''
    Function testing other functions. Poinpoints time, compares the results.
    Функция тестирования других функций. Засекает время, сравнивает результаты.

    :param function: List of tested functions. Список тестируемых функций.
    :param lenA: Sring A lenght(dynamisc string). Длинна строки А (динамическая строка).
    :param lenB: String lenght B. Длинна строки В (искомое).
    :param numSym: Number of unique symbols. Количество уникальных символов.
    :param numStr: Number of strings. Количество строк.
    :return: View list [function name, lead time, lenght A, lenght B, number of unique symbols]
    Список вида [имя функции, время выполнения, длинна А, длинна В, коичесво уникальнх символов]
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
                functionResult.append(fun(A, B)) # Function run. Выполнение функций.
        Final = time.time()
        functionResult.append(Final - Start) # Lead time. Расчёт времени выполнения.
        locResult.append(functionResult)
    
    for i in range(1, len(locResult[0]) - 1): # Chtcking result coincidence. Проверка совпадения результата.
        if locResult[0][i] == locResult[1][i] == locResult[2][i]: #Happening for 3 functions.
            # Упрощение для случая из 3-х функций.
            continue
        else: 
            print(' Результаты расходятся')
            sys.exit()
    else: print('Результаты сходятся')

    ResultList = []
    for locList in locResult: # Cleaning for 'True' and 'False'. Adding calculation parameters.
        #  Чистка от "Да" и "Нет", добавление параметров вычисления.
        ResultList.append(locList[0])
        ResultList.append(locList[-1])
        ResultList.append(lenA)
        ResultList.append(lenB)
        ResultList.append(numSym)

    return ResultList



def Main(lenA, lenB, numSym, numStr):
    '''
    Trigger function.
    Инициирующая функция.
    :param lenA: List of lenght dynamic strings A. Список длин динамической строки А.
    :param lenB: List of lenght strings B. Список длин искомых строк В.
    :param numSym: List of number unique symbols. Список колиества уникальных символов.
    :param numStr: Number of happening for each parameter. Число случаев для каждого параметра.
    :return: None
    '''
    allData = []
    for LA in range(0, len(lenA)):
        for LB in range(0, len(lenB)):
            for NS in range(0, len(numSym)):
                allData.append(Test(function,lenA[LA], lenB[LB], numSym[NS], numStr))

    showGraph(allData)
    print(allData)


def save(name='', form='png'):
    '''
    Save function.
    Функция сохранения.
    :param name: File name. Имя файла.
    :param form: File format. Формат файла.
    :return: None
    '''
    direct = os.getcwd()
    print(direct)
    plt.savefig('{}.{}'.format(name, form), form='png') #Сохранение изображение в текущей директории.

def plotGrap(*args, **kwargs):
    '''
    Chart printing function.
    Функция печати графиков.
    :param args: All lists coordinates X and Y. Все списки координат Х и У.
    :param kwargs: Special printing options. Специальные параметры печати.
    :return:None
    '''
    print('START GRAPH')
    print(kwargs)
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
    axisName = kwargs.pop('axisName', 1)
    label = ['Standart', 'Srez', 'PoBukvenSravnenye']



    fig = plt.figure() #  Figure creation. Создание фигуры
    ax = fig.add_subplot(111) # Axis creation. Создание области рисования

    print('AX =', type(ax))
    i = 0
    for x, y, color in zip(xlist, ylist, colors):
        lab = label[i]
        i += 1
        print(x,y,color,linewidth, lab)
        ax.plot(x, y, color = color, linewidth = linewidth, label = lab) # Chart creation. Создание графика
    ax.set_xlabel(axisName[0])
    ax.set_ylabel(axisName[1])

    ax.grid(True)
    ax.legend()
    plt.show()


def filtr(Con1, n1, Con2, n2, n3,  funct, DB):
    '''
    Filtering function from a common case data array with standard parameters.
    Note. To plot, the case is used when one variable changes, while the rest are static.
    The filter finds cases when all static parameters converge and returns a parameter at coordinate n3.
    Coordinates are taken in a relative system where the start is the name of the function.
    Type of a standard cell: [Function name [k], runtime [k + 1], long A [k + 2], long B [k + 3],
    number of unique characters [k + 4], Function name [k] .....

    Функция фильтрации из общего массива данных случаев с стандартными параметрами.
    Прим. Для построения графиков используется случай, когда одна переменная изменяется, а остальные статичны.
    Фильтр находит случаи когда все статичные параметры сходятся и возвращает параметр на координате n3.
    Координаты принимаются в относительной системе где началом является название функции.
    Вид стандартной ячейки: [ Имя функции[k], время выполнения[k+1], длинна А[k+2], длинна В[k+3],
    количество уник.символов[k+4], Имя функции[k].....

    :param Con1: Static parameter 1. Статичный параметр 1.
    :param n1: The coordinate of the static parameter 1 in the relative coordinate system.
    Координата статичного параметра 1 в относительной системе координат.
    :param Con2:  Static parameter 2. Статичный праметр 2.
    :param n2: The coordinate of the static parameter 2. Координата статичного параметра 2.
    :param n3: The coordinate of the desired parameter (modifiable). Координата искомого параметра (изменяемого).
    :param funct: Function name. Имя функции.
    :param DB: Data list. Список данных.
    :return: List of parameters to be changed. Список изеняемых параметров.
    '''
    Result = []
    for i in range(0, len(DB)):
        for k in range(0, len(DB[i])):
            if DB[i][k] == funct and DB[i][k + n1] == Con1 and DB[i][k + n2] == Con2: # Checking static parameters.
                # Проверка статичных параметров.
                Result.append(DB[i][k + n3])
    return Result






def showGraph(dataList):
    '''
    Data filtering for graphing.
    Фильтрация данных для построения графиков.
    P.S. Лютый костыль.
    :param dataList: Data list. Список данных.
    :return: None
    '''
    T1A = filtr(lenB[0], 3, numSym[0], 4, 1, SearchStandart, dataList)
    L1A = filtr(lenB[0], 3, numSym[0], 4, 2, SearchStandart, dataList)
    T2A = filtr(lenB[0], 3, numSym[0], 4, 1, SearchShear, dataList)
    L2A = filtr(lenB[0], 3, numSym[0], 4, 2, SearchShear, dataList)
    T3A = filtr(lenB[0], 3, numSym[0], 4, 1, SearchByLetter, dataList)
    L3A = filtr(lenB[0], 3, numSym[0], 4, 2, SearchByLetter, dataList)

    T1B = filtr(lenA[0], 2, numSym[0], 4, 1, SearchStandart, dataList)
    L1B = filtr(lenA[0], 2, numSym[0], 4, 3, SearchStandart, dataList)
    T2B = filtr(lenA[0], 2, numSym[0], 4, 1, SearchShear, dataList)
    L2B = filtr(lenA[0], 2, numSym[0], 4, 3, SearchShear, dataList)
    T3B = filtr(lenA[0], 2, numSym[0], 4, 1, SearchByLetter, dataList)
    L3B = filtr(lenA[0], 2, numSym[0], 4, 3, SearchByLetter, dataList)

    T1NS = filtr(lenA[0], 2, lenB[0], 3, 1, SearchStandart, dataList)
    NS1 = filtr(lenA[0], 2, lenB[0], 3, 4, SearchStandart, dataList)
    T2NS = filtr(lenA[0], 2, lenB[0], 3, 1, SearchShear, dataList)
    NS2 = filtr(lenA[0], 2, lenB[0], 3, 4, SearchShear, dataList)
    T3NS = filtr(lenA[0], 2, lenB[0], 3, 1, SearchByLetter, dataList)
    NS3 = filtr(lenA[0], 2, lenB[0], 3, 4, SearchByLetter, dataList)




    colors = ['red', 'green', 'blue']

    plotGrap(L1A, T1A, L2A, T2A, L3A, T3A, colors=colors, linewidth=2, axisName=['Long A (sym)', 'Time (s)'])
    '''save('Long_A+')''' # Save blank sheets. Сохраняет пустые листы.
    plotGrap(L1B, T1B, L2B, T2B, L3B, T3B, colors=colors, linewidth=2, axisName=['Long B (sym)', 'Time (s)'])
    '''save('Long_B+')'''
    plotGrap(NS1, T1NS, NS2, T2NS, NS3, T3NS, colors=colors, linewidth=2, axisName=['Number of symbols', 'Time (s)'])
    '''save('Number_symvol+)'''


function = [SearchStandart, SearchShear, SearchByLetter]
# Initial data is set here.
# Исходные данные пока задавать здесь.
lenA = [10,20,50,100, 150, 200] # A list of lengths of a dynamic string. Список длин динамической строки.
lenB = [10, 20, 50, 100] # List of search string lengths. Список длин искомой строки.
numSym = [5, 10, 15, 20, 26] # List of the number of simpols. Not more than 26! Список количесва симполов. Не больше 26!
numStr = 100 # The number of generations for each option. Количество генераций для каждого варианта.
Main(lenA, lenB, numSym, numStr)

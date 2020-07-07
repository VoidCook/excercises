import decimal

def zadanie1(first, last):
    first = list(map(int, first.split('-', 1)))
    last = list(map(int, last.split('-', 1)))
    tab = list()
    while first[0] < last[0] or (first[0] == last[0] and first[1] < last[1] - 1):
        first[1] += 1
        if first[1] == 1000:
            first[0] += 1
            first[1] = 1
        tab.append(f'{first[0]:02}' + '-' + f'{first[1]:03}')
    return tab

def zadanie2(tab, n):
    return [i for i in range(1, n+1) if i not in set(tab)]

def zadanie3():
    return [decimal.Decimal(i/10.0) for i in range(20, 56, 5)]

def main():
    first = "79-900"
    last = "80-155"
    print(zadanie1(first, last))
    print(zadanie2([2,3,7,4,9], 10))
    print(zadanie3())
    for i in zadanie3():
        print(i)

if __name__ == '__main__':
    main()
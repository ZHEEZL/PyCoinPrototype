# its prototype.
# PyCoin Project
version = '1.0.1'
transaction_count = 0
n = 10000
my_balance = 0
balance1 = 0
balance2 = 0
e = 0
while True:
    word = input('Введите команду! Для помощи напишите "help".')
    if word == 'transfer' or word == 'перевод':
        transfer_from = input('Откуда перевести?')
        if transfer_from == 'n':
            while e != 1:
                try:
                    sum = float(input('Сколько перевести?'))
                    e += 1
                except ValueError:
                    print('Это не число!')
            e = 0
            if sum < 0 or sum > n:
                print('Число ниже нуля, или выше баланса!')
            else:
                transfer_to = input('Куда перевести?')
                if transfer_to == 'my_balance':
                    n -= sum
                    my_balance += sum
                    transaction_count += 1
                    print('Переведено', sum, 'на my_balance')
                elif transfer_to == 'balance1':
                    n -= sum
                    balance1 += sum
                    transaction_count += 1
                    print('Переведено', sum, 'на balance1')
                elif transfer_to == 'balance2':
                    n -= sum
                    balance2 += sum
                    transaction_count += 1
                    print('Переведено', sum, 'на balance2')
        elif transfer_from == 'my_balance':
            while e != 1:
                try:
                    sum = float(input('Сколько перевести?'))
                    e += 1
                except ValueError:
                    print('Это не число!')
            e = 0
            if sum < 0 or sum > my_balance:
                print('Число ниже нуля, или выше баланса!')
            else:
                transfer_to = input('Куда перевести?')
                if transfer_to == 'n':
                    my_balance -= sum
                    n += sum
                    transaction_count += 1
                    print('Переведено', sum, 'на n')
                elif transfer_to == 'balance1':
                    my_balance -= sum
                    balance1 += sum
                    transaction_count += 1
                    print('Переведено', sum, 'на balance1')
                elif transfer_to == 'balance2':
                    my_balance -= sum
                    balance2 += sum
                    transaction_count += 1
                    print('Переведено', sum, 'на balance2')
        elif transfer_from == 'balance1':
            while e != 1:
                try:
                    sum = float(input('Сколько перевести?'))
                    e += 1
                except ValueError:
                    print('Это не число!')
            e = 0
            if sum < 0 or sum > balance1:
                print('Число ниже нуля, или выше баланса!')
            else:
                transfer_to = input('Куда перевести?')
                if transfer_to == 'n':
                    balance1 -= sum
                    n += sum
                    transaction_count += 1
                    print('Переведено', sum, 'на n')
                elif transfer_to == 'my_balance':
                    balance1 -= sum
                    my_balance += sum
                    transaction_count += 1
                    print('Переведено', sum, 'на my_balance')
                elif transfer_to == 'balance2':
                    balance1 -= sum
                    balance2 += sum
                    transaction_count += 1
                    print('Переведено', sum, 'на balance2')
        elif transfer_from == 'balance2':
            while e != 1:
                try:
                    sum = float(input('Сколько перевести?'))
                    e += 1
                except ValueError:
                    print('Это не число!')
            e = 0
            if sum < 0 or sum > balance2:
                print('Число ниже нуля, или выше баланса!')
            else:
                transfer_to = input('Куда перевести?')
                if transfer_to == 'n':
                    balance2 -= sum
                    n += sum
                    transaction_count += 1
                    print('Переведено', sum, 'на n')
                elif transfer_to == 'my_balance':
                    balance2 -= sum
                    my_balance += sum
                    transaction_count += 1
                    print('Переведено', sum, 'на my_balance')
                elif transfer_to == 'balance1':
                    balance2 -= sum
                    balance1 += sum
                    transaction_count += 1
                    print('Переведено', sum, 'на balance1')
    elif word == 'test' or word == 'тест':
        print(n, my_balance, balance1, balance2)
    elif word == 'check' or word == 'проверка':
        checkword = input('Какой кошелёк хотите проверить?')
        if checkword == 'n':
            print('Баланс на n:', n)
        elif checkword == 'my_balance':
            print('Баланс на my_balance:', my_balance)
        elif checkword == 'balance1':
            print('Баланс на balance1:', balance1)
        elif checkword == 'balance2':
            print('Баланс на balance2:', balance2)
    elif word == 'count' or word == 'количество':
        print('Всего валюты:', n + my_balance + balance1 + balance2)
    elif word == 'help' or word == 'помощь':
        print('help - список и для чего команды')
        print('count - количество валюты')
        print('test - проверка всех балансов')
        print('stop - остановка программы')
        print('check - проверка определённого баланса')
        print('transfer - перевод с одного кошелька на другой, с запросом суммы')
        print('burn - сжечь с кошелька n')
        print('mint - напечатать на кошелёк n')
        print('transaction_count - количество переводов')
        print('autors - Автор')
    elif word == "mint" or word == 'печать':
        mint = int(input('Сколько напечатать'))
        if mint < 0:
            print('ERROR')
        else:
            n += mint
            print(mint, 'было напечатано и переведено на n')
    elif word == 'burn' or word == 'сжечь':
        burn = int(input('Сколько сжечь'))
        if burn < 0:
            print('ERROR')
        else:
            if n < burn:
                print('В n  - нет денег')
            else:
                n -= burn
                print('Сожжено', burn)
    elif word == 'transaction_count':
        print('количество переводов:', transaction_count)
    elif word == 'autors':
        print('2022 Bomjang Studios')
    elif word == 'version':
        print('PyCoin version', version)
    elif word == 'stop' or word == 'стоп':
        print('Остановка')
        break
    else:
        print('Неправильно введена команда!')
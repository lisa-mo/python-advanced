def getNumber01():  # Первый вариант
    while type:
        getNumber = input('Введите число: ')                 # Ввод числа
        try:                                    # Проверка что getTempNumber преобразуется в число без ошибки
            getTempNumber = int(getNumber)
        except ValueError:                      # Проверка на ошибку неверного формата (введены буквы)
            print('"' + getNumber + '"' + ' - не является числом')
        else:                                   # Если getTempNumber преобразован в число без ошибки, выход из цикла while
            break
    return abs(getNumber)                   # возвращает модуль getTempNumber (для искл. отрицат. чисел)

print(getNumber01())
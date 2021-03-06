#Проверка числа на простоту
def simple(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for div in range(3,x):
            if x % div == 0:
                return False
        return True
# print(simple(2))

# Вывод всех делителей числа
def all_dividors(x):
    all_dividors_list = [i for i in range(1, x+1) if x%i == 0]
    return all_dividors_list
# print (all_dividors(25))
#
# # #Выводит самый большой простой делитель числа

def max_simple_div(x):
    simple_div_list = [i for i in range(x, 1, -1) if x % i == 0 and simple(i) is True]
    return max(simple_div_list)
# print(max_simple_div(77))

# def max_simple_div(x):
# simple_div_list = []
#      for i in range(x, 1, -1):
#          if x % i == 0 and simple(i) is True:
#              simple_div_list.append(i)
#              break
#          else:
#              continue
#     return max(simple_div_list)
# # print(max_simple_div(77))

# Каноническое разложение числа на простые множители
# (https://zaochnik.com/spravochnik/matematika/delimost/razlozhenie-chisel-na-prostye-mnozhiteli/)
def canon_simple_dividors(x):
    all_simple_dividors_list = []
    for n in range(2, int(x)):
        if x % n == 0:
            all_simple_dividors_list.append(n)
            x = x/n
        else:
            n +=1
    list = [f'{div}^{all_simple_dividors_list.count(div)}' for div in set(all_simple_dividors_list)]
    return list
# print(canon_simple_dividors(130))


# Самый большой делитель (не обязательно простой) числа.
def max_dividor(x):
    if (x == 1) or (simple(x) is True):
        return x
    else:
        all_dividors_list = [i for i in range(1, x) if x%i == 0]
        return max(all_dividors_list)
# print (max_dividor(2))
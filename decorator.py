# Напишите декоратор, оптимизирующий работу декорируемой функции. 
# Декоратор должен сохранять результат работы функции на ближайшие три запуска 
# и вместо выполнения функции возвращать сохранённый результат. 
# После трёх запусков функция должна вызываться вновь, 
# а результат работы функции — вновь кешироваться.


def cache3(func):
    cache_func = func()
    dictionary = {
                'count_call' : 0,
                'func' : cache_func
    }
    MAX_CALL = 3
    
    def wrapper():
        dictionary['count_call'] += 1
        if dictionary['count_call'] <= MAX_CALL:
            return dictionary['func']
        else:
            dictionary['count_call'] = 1
            cache_func = func()
            return cache_func
    return wrapper


@cache3
def heavy():
    print('Сложные вычисления')
    return 1


print(heavy())
# Сложные вычисления
# 1
print(heavy())
# 1
print(heavy())
# 1

# Опять кеш устарел, надо вычислять заново
print(heavy())
# Сложные вычисления
# 1

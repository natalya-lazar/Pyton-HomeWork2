# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

n = int(input('Введите сколько километров машина проезжает за день (n) - '))
m = int(input('Введите длину маршрута (m) - '))
print(m // n + (n % m != 0))

# print(-(-m//n))

# a = (m + (n - 1)) // n
# print(a)
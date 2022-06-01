"""
Неизвестный водитель совершил ДТП и скрылся с места происшествия.
Полиция опрашивает свидетелей. Каждый из них говорит, что запомнил какие-то буквы и цифры номера.
Но при этом свидетели не помнят порядок этих цифр и букв.
Полиция хочет проверить несколько подозреваемых автомобилей. Будем говорить,
что номер согласуется с показанием свидетеля, если все символы, которые назвал свидетель,
присутствуют в этом номере (не важно, сколько раз).

Формат ввода
Сначала задано число - количество свидетелей. Далее идет M строк,
каждая из которых описывает показания очередного свидетеля. Эти строки непустые и
состоят из не более чем 20 символов. Каждый символ в строке - либо цифра,
либо заглавная латинская буква, причём символы могут повторяться.
Затем идёт число - количество номеров. Следующие строки представляют из себя
номера подозреваемых машин и имеют такой же формат, как и показания свидетелей.

Формат вывода
Выпишите номера автомобилей, согласующиеся с максимальным количеством свидетелей.
Если таких номеров несколько, то выведите их в том же порядке, в котором они были заданы на входе.
"""
# после разбора

m = int(input())
wits = []  # показания свидетелей

for _ in range(m):
    wits.append(set(input().strip()))

n = int(input())
nums = []  # список возможных номеров
max_wit_count = 0

for _ in range(n):
    num = input().strip()
    num_set = set(num)  # для поиска вхождений
    wit_count = 0  # количество совпадающих показаний
    for wit in wits:
        if wit <= num_set:  # если подмножество входит в множество
            wit_count += 1
    nums.append((num, wit_count))
    max_wit_count = max(max_wit_count, wit_count)  # обновляем максимум

ans = []
for num in nums:
    if num[1] == max_wit_count: 
        ans.append(num[0])

print('\n'.join(ans))
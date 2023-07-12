# Задача 1
# Три друга взяли вещи в поход....

dict_man_and_items = dict(Pol=('Кружка', 'Ложка', "Бумага", "Мячик"), Bob=('Кружка', "Спички", "Спинер", "Щетка"),
                          Joy=('Ложка', "Бумага", "Щетка"))

result_union = set()
for i in set(dict_man_and_items.values()):
    result_union = result_union.union(i)
print(result_union)   # вещи взяли все друзья


one_friend_s_unique_items = set()
for i in dict_man_and_items.keys():
    gg = dict_man_and_items.copy()
    gg.pop(i)
    r_union = set()
    for j in set(gg.values()):
        r_union = r_union.union(j)

    a = set(dict_man_and_items[i]).difference(r_union)
    one_friend_s_unique_items = one_friend_s_unique_items.union(a)

print(one_friend_s_unique_items) # уникальные вещи у каждого
#--------------------------------------------------------------------------------


all_but_one = dict()
for i in dict_man_and_items.keys():
    gg = dict_man_and_items.copy()
    gg.pop(i)
    intersect = set()
    for l in gg.values():
        intersect = set(l)
        break

    for j in gg.values():
        intersect = intersect.intersection(set(j))

    f = intersect.difference(dict_man_and_items[i])

    all_but_one[i] = f

print(all_but_one)  # выводит имя и список вещей которых у него нет но есть у других



# Задача 2
list_elements = [1, 4, 1, 5, 6, 1, 2, 0, 9, 9, 9, 1, 4, 0]
list_of_duplicate_elements = []
for i in set(list_elements):
    if list_elements.count(i) > 1:
        list_of_duplicate_elements.append(i)

print(list_of_duplicate_elements)  # список дубликатов
list_elements = list(set(list_elements))
print(list_elements) # список без дубликатов

# Задача 3
string = 'a f g l a l r o f d n b s S B q p m g H D K s l A a b d a D F F f a A J l Q o q o'
count_elements = []
for i in set(string.lower().split()):
    count_elements.append((i, string.lower().count(i)))
count_elements.sort(key=lambda x: x[1], reverse=True)
print(count_elements[:10])

# Задача 4
items = {'спички': 00.1, 'гантеля': 7, 'фен': 1.5, 'кружка': 0.2, 'ложка': 0.05, 'тарелка': 0.3}
backpack = 7.2   # float(input('грузовметимость: \n'))
ves = 0
result = {}
for i in items.items():
    ves = ves + i[1]
    if ves > backpack:
        ves = ves - i[1]
        continue
    result[i[0]] = i[1]

print(result)  # вывод одного из возможных вариантов
# -----------------------------------------------------------------
import itertools

list_items = list(items.items()) # делаем из словаря список для удобства

perm_set = list(itertools.permutations(range(len(list_items))))  # список всех возможных комбинаций расположения по индексам

result = set()
for i in perm_set:
    res = []
    ves = 0
    for j in i:
        ves = ves + list_items[j][1]
        if ves > backpack:
            ves = ves - list_items[j][1]
            continue
        res.append((list_items[j][0], list_items[j][1]))
    result.add(frozenset(res))

for i in result:
    i = dict(i)
    print(i)       # вывод всех возможных вариантов

"""{'кружка': 0.2, 'фен': 1.5, 'тарелка': 0.3, 'ложка': 0.05, 'спички': 0.1}
   {'гантеля': 7, 'ложка': 0.05, 'спички': 0.1}
   {'кружка': 0.2, 'гантеля': 7}"""
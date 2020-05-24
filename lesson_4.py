"""Упражнение продолжает практическую работу из последнего видеоурока.
Для усовершенствования приложения разберитесь, как можно реализовать получение common words с соседних страниц — тех,
на которые есть ссылки.

Возможен следующий алгоритм решения задачи:
1. Получить ссылки на соседние страницы. Для этого можно воспользоваться библиотекой BeautifulSoup.
Не забудьте отобрать только правильные ссылки, которые указывают на другие страницы Википедии.
(Вы можете распознать их по тексту \wiki).
2. Спарсить отдельно соседние страницы. Для этого вам необходимо перебрать в цикле все полученные ссылки.
3. Сложить все в один список."""

from bs4 import BeautifulSoup as Bs
import re
import requests

enter = 'Дерево'
# enter = input('Введите запрос:\n').capitalize()

gen_link = 'https://ru.wikipedia.org/wiki/'+enter+''
result = requests.get(gen_link).text
with open('wiki.txt', 'w', encoding='utf8') as f:
    write = f.write(result)

with open('wiki.txt', 'r') as f:
    read = f.read()

# need = re.findall('<span class="toctext">([а-яА-я]+)</span>', read)
need = re.findall('<a href="#Кипарисовые"><span class="tocnumber">2.1.2</span> <span class="toctext">Кипарисовые</span></a>', read)
print(need)





import module # Подключаем Модули/Библиотеки, которые нужны для проекта

from module import * # Імпортируем всё или только то, с чем будем работать

APIsite = 'Site'
needPosition = 7
subsection = ['SEND TO TRANSFER LIST', 'KEEP ITEM', 'QUICK SELL NOW']

def label_determiner(result): # Определение характерных меток для идентификация
    result = APIsite
    if result == CUSTOMIZE:
        send_result = customize_label
        response = requests.get(send_result)
        return response.json()
    elif result == 'NEW_ITEM':
        send_result = new_item_label
        response = requests.get(send_result)
        return response.json()
    else:
        return print('Not subject to analysis!!!')

def customize_label(needPosition): # Робота с меткой CUSTOMIZE
    position = APIsite
    if position == 2:
        move = needPosition - position
        # Можно по-разному, например ввести счетчик, и закрепить за каждым числом комбинацию действий
        if move <= 4:
            return print('Right, Right, Down')
    else:
        pass

def new_item_label(subsection): # Робота с меткой NEW_ITEM
    position = APIsite
    if subsection == 'KEEP ITEM':
        if 'KEEP ITEM' == notAction:
        return print('Vertical carousel action Up & Down')
    else:
        subsection = (CountOfElement + NumberOfActivityCard + NameOfCard + TypeOfActiveCard)
        print(subsection)
# Logic-Ident-of-Picture-TestTask-Scripter
Just only Logic

![GitHub](https://img.shields.io/github/license/IRONKAGE/Logic-Ident-of-Picture-TestTask-Scripter?style=plastic) ![GitHub Code Size](https://img.shields.io/github/languages/code-size/IRONKAGE/Logic-Ident-of-Picture-TestTask-Scripter?style=plastic) ![Languges](https://img.shields.io/github/languages/count/IRONKAGE/Logic-Ident-of-Picture-TestTask-Scripter?style=plastic)

## Need to connect in Tensorflow or PyTorch ar Analog for Recognized Pictures

## Need to connect in Tesseract or Analog for Recognized Text

## I didnt do the Above 😉

### Задача:

1. Определить характерные метки для идентификация типа картинки:
    - "не подлежит анализу"
    - "CUSTOMIZE"
    - "NEW ITEM"
2. Для "CUSTOMIZE":
    - определить позицию активного подраздела (от 1 до 8 слева направо сверху вниз);
    - минимально необходимый набор последовательности действий для перехода к произвольному заданному номеру позиции (например, активная позиция 2, заданная позиция перехода 7 – набор действий «право» - «право» - «вниз»
3. Для "NEW ITEM":
    - активный подраздел (SEND TO TRANSFER LIST | KEEP ITEM | QUICK SELL NOW)
    - если не активен "KEEP ITEM" - определить последовательность действий для перехода (вертикальная карусель, действия «вверх» / «вниз»)
    - если "KEEP ITEM" активен:
        1. определить количество элементов (карточек) в разделе
        2. номер активной карточки в подразделе
        3. имена/названия карточек
        4. определить активная карточка игрок или другой тип карточки
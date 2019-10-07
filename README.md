# Обрезка ссылок с помощью Битли

Утилита генерирует короткие ссылки с использованием Bit.ly API, а также позволяет посчитать количество переходов по короткой ссылке.

### Как установить

Для корректной работы необходимо зарегистрироваться на сайте https://bitly.com/ и получить Generic Access Token.

Полученный токен необходимо сохранить в файле .env в виде строки заданного формата
```
TOKEN=полученный Generic Access Token
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Примеры использования

#### Генерация короткой ссылки

```
python3 main.py https://www.comon.ru/user/a1408/strategy/detail/?id=11285
bit.ly/2Mldi8v
```

#### Подсчет переходов
```
python3 main.py bit.ly/2Mldi8v
1
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
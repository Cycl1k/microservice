# Микросервисы
Разработаны два сервиса
-------

Python сервис с тремя endpoint'ами:
/greet/{name} - Что возращает приветствие с именем
/greet/history - Возвращаяет всю историю приветствий из БД
/status - Возращает статус сервера


--------

GO сервис, то же имеет два endpoint'а:
/greer - Возвращает приветствие
/greet/history - Возвращаяет историю приветсвий

Так же сервис каждый 30 секунд отправляет запросы на /status Python сервиса и записывает эти даннные в БД

# Сборка

Клонировать репозиторий 

`gh repo clone Cycl1k/microservice`

Создайте файл .env с переменными окружения:

`PYTHON_PORT = 8060
GO_PORT = 8070
POST_DB = greetdb
POST_DB_USER = userdb
POST_DB_PSWD = master
POST_PORT = 5432`

Запустить Docker compose

`docker compose up -d` 

Тестовое задание: 
Необходимо реализовать микросервис используя язык программирования python. 

Функциональные части сервиса: 
a) Реализация api: 
- Регистрация пользователей
- Аутентификация пользователей
- Список пользователей

б) Функционал взаимодействия через шину данных. 
Доменный объект - Задача. 
Задача содержит следующие информацию: 
- номер задачи
- статус

Необходимо: 
- Создать 2 канала для получения задачи и ответа на задачу. должна поддерживаться приоритезация
- При получении задачи, данные валидируются. 
- Данные должны храниться в БД 
- Обработка задачи представляет собой поэтапная смена статусов (создана, в обработке, ответ). Должна быть реализована фоновая обработка задачи с отдельными методами для каждого значения статуса 
- Ответ на задачу должен содержать статус задачи, идентификатор, время выполнения задачи 
- Периодическая задача по удалению старых сообщений 

Требования: 
- Код репозитория на GitHub или архивом
- Python 3, Django или FastApi 
- Docker, docker-compose 
- RMQ или Kafka 
- Postgresql 
- автотесты
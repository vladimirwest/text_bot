# Voice2txt Bot
Бот для ВКонтакте, одна из основных функций которого - распознавание голосовых сообщений.
Помимо этого, присутствуют дополнительные функции бота это: подбрасывание монетки (решка или орел), рандом в заданном диапазоне, погода, новости, пробки и пересылка emotes с twitch.tv.
## Использование
Вам необходимо иметь аккаунт в соц.сети ВКонтакте и состоять в [группе бота](https://vk.com/voice2txt)
Далее напишите ему сообщение "помощь" для получения описания команд и на этом все!
## Команды

| Команда | Аргументы | Описание |
| ------------- | ------------- | ---------------- |				
| помощь | \- | Показывает список команд и их описания | 
| монетка | \- | С вероятностью 50 на 50 выводит "решка" или "орел" |
| рандом | [Начало диапазона] - [Конец диапазона] | Выведет рандомное целое число в указанном диапазоне, включая границы |
| погода | \- , сегодня, завтра, прогноз | " -, сегодня " - Покажет прогноз погоды на сегодня, " завтра " - Покажет прогноз погоды на завтра, " прогноз " - Покажет прогноз погоды на 5 дней вперед, считая сегодняшний. В прогноз погоды входит: температура, направление и скорость ветра, влажность ночью, утром, днем и вечером. |
| emote | Код эмоции, Размер эмоции | Выведет эмоцию с [twitch](https://www.twitch.tv), если найдет ее по введенному коду. (Возможен поиск эмоций доступных только подписчикам). Размер указывает на размер возвращаемого изображения: параметр принимает значения 1-3. (1-маленький, 3-самый большой). По умолчанию используется 2. |
| новости | \- | Покажет новости с сервиса Яндекс.Новости (пока доступен только Нижний Новгород) |
| пробки | \- , Район | " - " - Кинет карту города с пробками с сервиса Яндекс.Карты, "Название района" - Кинет приближенную карту пробок района в запросе. |

Для доступа к функции распознавания голосовых сообщений достаточно просто записать или переслать подобные сообщения боту.

## Использованные инструменты
Для работы с ВКонтакте использовался механизм [Callback API](https://vk.com/dev/bots_docs?f=2.1.%20Callback%20API) вкупе с [Flask](http://flask.pocoo.org), выбранным за его простоту и гибкость. Callback API представляет собой механизм веб-запросов (при наступлении новых событий в сообществе) на сервер, что позволяет практически моментально и очень удобно их обрабатывать. С помощью Flask мы анализируем поступающие сообщения и решаем, что с ними делать дальше. Для распознавания голосовых сообщений использовался сервис [wit.ai](https://wit.ai) с его Python SDK [pywit](https://github.com/wit-ai/pywit) . Отличие этого сервиса от, к примеру, Google Speech и Yandex SpeechKit в том, что он бесплатный, что являлось очень весомым фактором для нас во время написания проекта. Среди текстовых команд для погоды мы использовали [PyOWM](https://github.com/csparpa/pyowm) , для новостей и пробок сервисы Яндекс.Новости и Яндекс.Карты соответственно. Для команды emote мы использовали [API](https://twitchemotes.com/apidocs) сайта [twitchemotes](https://twitchemotes.com), на котором находятся наполненные всей необходимой информацией для работы с эмоциями JSON файлы. Бот был размещен на бесплатном web-хостинге [PythonAnywhere](https://www.pythonanywhere.com). Выбор пал на этот хостинг из-за его бесплатности и удобства размещения web-приложения.

## Лицензия
[MIT Licence](https://github.com/vladimirwest/text_bot/blob/master/LICENSE).

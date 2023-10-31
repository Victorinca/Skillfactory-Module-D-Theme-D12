# Skillfactory Module D. Theme D12

Completed homework for Skillfactory Course: 'Python Web Developer'. Module D - 'Backend-development in Python and Django'. Theme D12 - 'Advanced Django Capabilities'.

## Репозиторий учебного проекта NewsPaper для курсов "Веб-разработчик на Python" и "Fullstack-разработчик на Python"
### [Модуль D. Тема D12 "Продвинутые возможности работы с Django. Логирование"](https://victorinca.github.io/Skillfactory-Module-D-Theme-D12/)

Приложение новостного портала NewsPaper, созданное с помощью Python и Django, чтобы можно было: 1) смотреть новости 2) читать статьи 3) оставлять комментарии.

Итоговое задание по теме D12 "Продвинутые возможности работы с Django. Логирование" заключается в создании автоматической системы логирования для записи логов в файлы и отправки логов на почту админу.

База данных: sqlite.

Состоит из приложений news и accounts.

#### Приложение news включает в себя модели:
1) Author - авторы статей, новостей (далее - постов).
2) Category - категории постов - темы, которые они отражают (бизнес и экономика, наука и технологии, образование и вакансии, стиль жизни и здоровье и т.д.).
3) Post - посты (статьи и новости), которые создают пользователи. Каждый объект может иметь одну или несколько категорий.
4) PostCategory - промежуточная модель (явная) для связи "многие ко многим".
5) Comment - хранение комментариев к постам, оставляемых под каждой новостью/статьёй.
6) Subscription - подписки на категории.

Все модели собраны в единый скрипт (код) в приложении news в файл models.py.

#### В качестве результата задания нужно усовершенствовать новостной портал NewsPaper - создать механизм логирования.

По итогу работы настройки логирования должны выполнять следующее:

1) В консоль должны выводиться все сообщения уровня DEBUG и выше, включающие время, уровень сообщения, сообщения. Для сообщений WARNING и выше дополнительно должен выводиться путь к источнику события (используется аргумент pathname в форматировании). А для сообщений ERROR и CRITICAL еще должен выводить стэк ошибки (аргумент exc_info). Сюда должны попадать все сообщения с основного логгера django.

2) В файл general.log должны выводиться сообщения уровня INFO и выше только с указанием времени, уровня логирования, модуля, в котором возникло сообщение (аргумент module) и само сообщение. Сюда также попадают сообщения с регистратора django

3) В файл errors.log должны выводиться сообщения только уровня ERROR и CRITICAL. В сообщении указывается время, уровень логирования, само сообщение, путь к источнику сообщения и стэк ошибки. В этот файл должны попадать сообщения только из логгеров django.request, django.server, django.template, django.db_backends.

4) В файл security.log должны попадать только сообщения, связанные с безопасностью, а значит только из логгера django.security. Формат вывода предполагает время, уровень логирования, модуль и сообщение.

5) На почту должны отправляться сообщения уровней ERROR и выше из django.request и django.server, по формату как в errors.log, но без стэка ошибок.

6) Более того, при помощи фильтров указать, что в консоль сообщения отправляются только при DEBUG = True, а на почту и в файл general.log только при DEBUG = False.

#### Упорядоченный текст задания - задание ещё раз, но в более понятной форме:

1) В консоль - все сообщения с основного логгера django: 
- уровень DEBUG и выше, 
формат: время, уровень сообщения, сообщение

- уровень WARNING и выше 
формат: время, уровень сообщения, сообщение, путь к источнику события (аргумент pathname)

- уровень ERROR и CRITICAL 
формат: время, уровень сообщения, сообщение, путь к источнику события (аргумент pathname), стэк ошибки (аргумент exc_info)

3) В файл general.log + сообщения с регистратора django
уровень INFO и выше
формат: время, уровень логирования; модуль, в котором возникло сообщение (аргумент module); сообщение

4) В файл errors.log - сообщения только из логгеров django.request, django.server, django.template, django.db_backends
уровень ERROR и CRITICAL
формат: время, уровень логирования, сообщение, путь к источнику сообщения, стэк ошибки (аргумент exc_info)

5) В файл security.log - сообщения только связанные с безопасностью из логгера django.security 
формат: время, уровень логирования, модуль, сообщение

6) На почту - из django.request и django.server
уровень ERROR и выше
формат: время, уровень логирования, сообщение, путь к источнику сообщения

7) При помощи фильтров указать, что 
в консоль сообщения отправляются только при DEBUG = True
на почту и в файл general.log только при DEBUG = False

#### Запуск проекта

1) Создать виртуальное окружение (далее - ВО) - изолированну версию Python, которая находится у вас в папке venv:

python -m venv venv

2) Активировать ВО:

2.1) В Windows _PowerShell_ или _cmd_:

venv\sripts\activate

2.2) В Windows _GitBash_

source venv/sripts/activate

2.3) Linux, MacOS

source venv/bin/activate

3) Установить через pip

3.1) Django с активированной средой (в виртуальную среду):

python -m pip install Django

3.2) Дополнительные пакеты:

pip install django-filter

pip install django-dbbackup

pip install django-allauth

pip install django-apscheduler

4) Перейти в папку проекта, где находится файл manage.py с помощью команды: cd название_папки (в эту папку должны быть скопированы все файлы из репозитория), например, 

cd NewsPaper

5) Проверить, что находимся в нужной папке с помощью команды ls. Если после выполнения команды в терминале виден файл manage.py - можно запускать проект. Иначе - см. п.4. 

6) Запускаем проект командой 

python manage.py runserver

или

./manage.py runserver

Сообщение говорит нам о том, что приложение начало работу по адресу 127.0.0.1:8000.

Открываем любой браузер и переходим по адресу http://127.0.0.1:8000/.

Полезные команды:

- посмотреть список доступных команд для Django:

python manage.py help

#### Доступы в приложении - учётные записи

Панель администратора:
http://127.0.0.1:8000/admin/ 

Администратор:
- логин: admin
- пароль: admin-admin

Пользователи:
- логин: user1@mail.com
- пароль: user1-user1

- логин: user2@mail.com
- пароль: user2-user2

- логин: test1@mail.com
- пароль: test1-test1

и т.п.

- логин: test5@mail.com
- пароль: test5-test5

## Поддержать, отблагодарить автора
Если представленная работа Вам понравилась, принесла пользу, сэкономила время, то Вы можете поддержать автора, воспользовавшись различными платежными системами.
- [Поддержать автора через ЮMoney](https://yoomoney.ru/to/4100117804016773)
- [Выразить признательность через Qiwi](https://qiwi.com/n/VICTORINCA)
- [Поблагодарить автора через WebMoney](https://donate.webmoney.com/w/vMlRR539aSfBwnNYzTBTgl)
#### Благодарю Вас за щедрость!
#### Ваша поддержка и признательность очень приятны и важны!

## Ссылки

- [Ссылка на страницу проекта](https://victorinca.github.io/Skillfactory-Module-D-Theme-D12/)
- [Ссылка на GitHub](https://github.com/Victorinca/Skillfactory-Module-D-Theme-D12)
  
По всем вопросам, которые касаются выполненного задания, можно писать на почту victoriavladimirskaya@gmail.com.
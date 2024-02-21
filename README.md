# DogHome - Ваш путеводитель в мире приютов и собак

DogHome - это веб-приложение, разработанное с использованием Django и Bootstrap, которое помогает приютам для животных эффективно управлять информацией о собаках и предоставляет пользователям удобный доступ к этой информации. Проект создан для улучшения прозрачности и доступности информации о собаках, их приютах, и помогает в поиске новых домов для пушистых друзей.

## Особенности

- **Список Собак**: В приложении представлен список собак, которых можно забрать домой. Каждая собака представлена с фотографией и кратким описанием.

- **Информация о Приютах**: Пользователи могут просматривать информацию о приютах для животных, включая их название, адрес и контактные данные.

- **Детали собаки**: При клике на собаку пользователь переходит на страницу с подробной информацией о выбранной собаке, включая ее имя, фотографии и полное описание.

- **Страницы приютов**: Каждый приют имеет свою собственную страницу с подробной информацией. Пользователи могут узнать больше о приюте, его миссии и как им помочь.

- **Интуитивный интерфейс**: Мы использовали Bootstrap для улучшения дизайна и обеспечения удобства использования приложения.

## Установка и Запуск

1. **Клонирование репозитория**:
   ```bash
   git clone https://github.com/SemenovaMar1a/DogHome.git cd DogHome
3. **Создание и активация виртуальной среды**:
   ```bash
   pip install virtualenv
   virtualenv venv
   venv\Scripts\activate
5. **Установка зависимостей**:
   ```bash
   pip install -r requirements.txt
7. **Применение миграций**:
   ```bash
   python manage.py migrate
9. **Запуск сервера разработки Django**:
    ```bash
    python manage.py runserver
11. **Доступ к веб-приложению**: Теперь вы можете открыть веб-браузер и перейти по адресу, указанному в выводе команды runserver. Ваше веб-приложение должно быть доступно по этому адресу, и вы можете начать работу с ним.

## Использование
- **Главная страница**: По умолчанию, вы попадаете на главную страницу, где отображается краткая информация о сайте и список приютов.

- **Приюты**: Перейдите на страницу "Приютов", чтобы узнать больше о различных приютах для животных.

- **Подробности о собаке**: При клике на собаку, вы переходите на страницу с подробной информацией о выбранной собаке.
- **Меню**: В меню сверху вы найдете все доступные вкладки для удобной навигации.

## Требования

- Python 3.x
- Django 4.x
- Bootstrap 5.x
- База данных: SQLite (по умолчанию)

## Внесение вклада
Если вы хотите внести вклад в развитие проекта "DogHome", пожалуйста, ознакомьтесь с нашим [CONTRIBUTING](https://github.com/SemenovaMar1a/DogHome/blob/master/CONTRIBUTING.md) и присоединяйтесь к команде разработчиков.  

## Лицензия
Проект распространяется под лицензией MIT. Подробности смотрите в файле [LICENSE](https://github.com/SemenovaMar1a/DogHome/blob/master/LICENSE.md). 

## Свяжитесь с нами
Если у вас есть вопросы или предложения, не стесняйтесь связаться с нами.

Email: Semenova.semyono@yandex.ru<br>
Следите за мной на [GitHub](https://github.com/SemenovaMar1a).
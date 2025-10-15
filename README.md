# nFac - Backend Development Project

## Overview

This project is a backend development of an inventory management system built with **Django** and **PostgreSQL**. The main goal was to build a server-side application that can manage inventory data and provide API endpoints for future use.

## Features

- **Backend Framework**: Django
- **Database**: PostgreSQL
- **APIs**: Implemented REST APIs for managing inventory and user data
- **Authentication**: User authentication via JWT (JSON Web Tokens)
- **API Testing**: All APIs tested using Postman

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/dikend1/PlayPod.git
2. Navigate to the project directory:
    ```bash
   cd PlayPod
3. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
5. Set up environment variables:
   Make sure you set up the necessary environment variables in .env (like SECRET_KEY, DATABASE_URL).
   Use django-environ to manage them.
6. Run the Django development server:
    ```bash
   python manage.py runserver
## Deployment
AWS: The application was deployed to AWS. However, due to issues with Docker and some other configurations, the deployment process took longer than expected.

Railway: The server was also deployed on Railway. However, the frontend was missing, and only the backend was visible on the platform.

## Challenges Faced
Docker build issues that delayed the deployment process.

GitHub issues took about 1.5 hours to resolve.

Limited time due to academic exams (linear algebra and calculus) and participation in the WE HACK hackathon, where I helped the team to win 2nd place.

Lack of frontend development skills led to using GPT for generating a simple frontend (using HTML and CSS).


```markdown
## Сообщение на русском

Всем привет!

Вот что я сделал:

1. **Серверная часть**:
   - Реализовал backend системы управления инвентарем с использованием **Django** и **PostgreSQL**.
   - Разработал API для работы с данными инвентаря и пользователей.
   - Реализовал аутентификацию с использованием **JWT**.
   - Все API были протестированы через **Postman**.

2. **Проблемы**:
   - На этапе деплоя возникли проблемы с Docker, что заняло много времени.
   - Были проблемы с GitHub, которые я решал 1,5 часа.
   - На выходных у меня был рубеж по **линейной алгебре** и **калькулюсу 2**, я весь вечер готовился.
   - После этого участвовал в хакатоне **WE HACK**, где моя команда заняла **2-е место**. Я работал над серверной частью.
   - После хакатона я уснул, а сегодня весь день занимался проектом и тестировал серверную часть через Postman.
   - После AWS планировал деплой на **Railway**, но так как у меня была только серверная часть, фронтенд не был виден, но деплой работает просто не видно. Фронтенд был сделан с использованием **GPT** (я знаю немного HTML и CSS), но из-за нехватки времени использовал **Lovable** для создания простого интерфейса.

Прошу прощения за то, что не успел сделать все идеально, но все работает локально, и я снял видео, чтобы продемонстрировать процесс. Пожалуйста, посмотрите видео, я очень хочу попасть в инкубатор. Спасибо!

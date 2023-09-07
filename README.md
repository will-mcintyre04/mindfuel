<div align="center">
        <img src="https://github.com/will-mcintyre04/flask-practice/assets/78566536/2aa7439b-19c7-49b9-aedf-89497e9acf96" width="400px">
</div>

<h1 align="center">Welcome to Mindfuel 🌟</h1>
    
[![License](https://img.shields.io/github/license/will-mcintyre04/mindfuel)](https://github.com/will-mcintyre04/mindfuel)
![GitHub pull requests](https://img.shields.io/github/issues-pr/will-mcintyre04/mindfuel)
![GitHub issues](https://img.shields.io/github/issues/will-mcintyre04/mindfuel)
![Issues Closed](https://img.shields.io/github/issues-closed/will-mcintyre04/mindfuel.svg)

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-306998?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FF4500?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-663300?style=for-the-badge&logo=jinja&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![PythonAnywhere](https://img.shields.io/badge/PythonAnywhere-3776AB?style=for-the-badge&logo=pythonanywhere&logoColor=white)

## 🚀 About the Mindfuel App
Mindfuel is a Flask-based web application that delivers daily motivational quotes to users. It's designed to uplift and inspire users with a clean and user-friendly interface. Quotes are fetched daily from the <a href="https://zenquotes.io/">ZenQuotes</a> API and emailed at 8am EST.

## 💡 Key Features
- Subscribing and unsubscribing to daily quotes.
- Simple and intuitive user interface.

## 🌈 How It Works
Mindfuel operates by providing an interface for users to subscribe or unsubscribe from receiving motivational quotes daily. It connects a Python-Anywhere hosted MySQL back-end database using flask-sqlalchemy to an interactive front-end webpage.

> To learn more about the code behind sending the emails, click <a href="https://github.com/will-mcintyre04/quote-emailer">here</a>

## 💌 Subscribe to Mindfuel
Visit the website <a href="https://willymac.pythonanywhere.com">here</a> to start getting emails in your inbox!

## 🏃‍♂️ Getting Started
Follow these steps to set up and run the Mindfuel app on your local machine.
### 1. Clone the repository
```sh
git clone https://github.com/will-mcintyre04/mindfuel.git

cd mindfuel
```
### 2. Install dependancies
To install all required dependencies, run the following command on your <a href="https://docs.python.org/3/library/venv.html">virtual environment</a>:
```sh
pip install -r requirements.txt
```

### 3. Create local, configured SQLite datbase
```sh
flask shell
>>> from app.extensions import db
>>> from app.models import Email
>>> db.create_all()
>>> exit()
```
This will create an app.db database with an `emails` tab;e within the `instance` directory.

### 4. Run the app
```sh
flask --app app run
```



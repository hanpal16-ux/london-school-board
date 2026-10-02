London School Board – Student Management System
Project Description

London School Board is a web application built with Django and MySQL that helps a school manage its student information. Authenticated users can register new students, view the list of students, and browse a product catalog with images. Administrators can manage students, teachers, and products through the Django admin panel.

This project was developed as part of the Full Stack Software Development program at Canadian Business College (CBC).

Technologies
Python 3.12
Django 5.1
MySQL 8.0
HTML
CSS
JavaScript
Pillow (image uploads)
How to Run
Clone the repository:
bash
   git clone https://github.com/hanpal16-ux/london-school-board.git
   cd london-school-board
Create and activate a virtual environment (Python 3.12 recommended):
bash
   python -m venv venv
   venv\Scripts\activate
Install the dependencies:
bash
   pip install "django<5.2" mysqlclient pillow

Note: Django 5.1 is used because it supports MySQL 8.0. Django 5.2 and newer require MySQL 8.4 or higher. 4. Create a MySQL database named student_management. 5. Open myproject/settings.py and update the DATABASES section with your MySQL username and password. 6. Apply the migrations:

bash
   python manage.py migrate
(Optional) Create an admin user:
bash
   python manage.py createsuperuser
Start the development server:
bash
   python manage.py runserver
Open http://127.0.0.1:8000/ in your web browser.
Features
User registration, login, and logout
Protected pages that require the user to be logged in
Add new students through a form
View a list of all registered students
Product catalog with images, descriptions, prices, and categories
Admin panel to manage students, teachers, and products
Author

Hanner Palacios

# Django_MySQL_Blog_project


This Django blog project is a simple blogging platform where users can view posts on the homepage and manage the blog posts through the Django admin panel. The project is built using Django and MySQL.

## Features

- Public-facing homepage displaying all blog posts.
- Admin panel for managing blog posts (create, update, delete).

## Technologies

- Python 3.12
- Django 5.0.6
- MySQL

## Setup

Follow these instructions to get this project running on your local machine.

### Prerequisites

- Python 3.12
- Django 5.0.6
- MySQL Server
- `mysqlclient` Python library

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/django-blog.git
 


2. Create a Virtual environment:

   python -m venv venv

    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. install dependencies:
     pip install -r requirements.txt

5. Configure your database settings in blog/settings.py under the DATABASES section.

6. Run migrations:
    python manage.py makemigrations
    python manage.py migrate

7. Create a superuser:
  python manage.py createsuperuser

8. Start the server:
  python manage.py runserver

9. Visit http://127.0.0.1:8000/admin to access the admin panel and http://127.0.0.1:8000/ to view the blog.


### Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.
























   


>>>>>>> 209a80e (Create README.md)

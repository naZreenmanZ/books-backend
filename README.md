📚 Book Management System - Django Backend
A Django REST API for managing books and book lists, allowing users to create book lists, add books to lists, and retrieve them.


🚀 Features
✅ View all books 📖
✅ Create & delete book lists 📚
✅ Add & remove books from a list 📝
✅ RESTful API with Django REST Framework 🌐
✅ CORS enabled for frontend integration 🔄


/books_backend
│── books_backend/      # Django Project
│── books/              # App for managing books
│── books/models.py     # Database models
│── books/serializers.py # DRF Serializers
│── books/views.py      # API views
│── books/urls.py       # App-specific URLs
│── manage.py           # Django entry point
│── requirements.txt    # Dependencies
│── README.md           # Documentation


🔧 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-repo/book-management.git
cd book-management


2️⃣ Create a Virtual Environment
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate  # Windows


3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py migrate


5️⃣ Create a Superuser
python manage.py createsuperuser


6️⃣ Run the Server
python manage.py runserver

Server will be available at http://127.0.0.1:8000/.



Here's a well-structured README.md file for your Django app, including setup, API endpoints, and best practices.

📚 Book Management System - Django Backend
A Django REST API for managing books and book lists, allowing users to create book lists, add books to lists, and retrieve them.

🚀 Features
✅ View all books 📖
✅ Create & delete book lists 📚
✅ Add & remove books from a list 📝
✅ RESTful API with Django REST Framework 🌐
✅ CORS enabled for frontend integration 🔄

📂 Project Structure
bash
Copy
Edit
/books_backend
│── books_backend/      # Django Project
│── books/              # App for managing books
│── books/models.py     # Database models
│── books/serializers.py # DRF Serializers
│── books/views.py      # API views
│── books/urls.py       # App-specific URLs
│── manage.py           # Django entry point
│── requirements.txt    # Dependencies
│── README.md           # Documentation
🔧 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-repo/book-management.git
cd book-management
2️⃣ Create a Virtual Environment
bash
Copy
Edit
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate  # Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Apply Migrations
bash
Copy
Edit
python manage.py migrate
5️⃣ Create a Superuser
bash
Copy
Edit
python manage.py createsuperuser
6️⃣ Run the Server
bash
Copy
Edit
python manage.py runserver
Server will be available at http://127.0.0.1:8000/.



🛠 API Endpoints
Books API
Method	Endpoint	Description
GET	/api/books/	Get all books
POST	/api/books/	Create a new book
Book Lists API
Method	Endpoint	Description
GET	/api/book-lists/	Get all book lists
POST	/api/book-lists/	Create a new book list
POST	/api/book-lists/{id}/add_books/	Add books to a list
DELETE	/api/book-lists/{id}/remove_book/	Remove a book from a list


Here's a well-structured README.md file for your Django app, including setup, API endpoints, and best practices.

📚 Book Management System - Django Backend
A Django REST API for managing books and book lists, allowing users to create book lists, add books to lists, and retrieve them.

🚀 Features
✅ View all books 📖
✅ Create & delete book lists 📚
✅ Add & remove books from a list 📝
✅ RESTful API with Django REST Framework 🌐
✅ CORS enabled for frontend integration 🔄

📂 Project Structure
bash
Copy
Edit
/books_backend
│── books_backend/      # Django Project
│── books/              # App for managing books
│── books/models.py     # Database models
│── books/serializers.py # DRF Serializers
│── books/views.py      # API views
│── books/urls.py       # App-specific URLs
│── manage.py           # Django entry point
│── requirements.txt    # Dependencies
│── README.md           # Documentation


🔧 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-repo/book-management.git
cd book-management


2️⃣ Create a Virtual Environment
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate  # Windows


3️⃣ Install Dependencies
pip install -r requirements.txt


4️⃣ Apply Migrations
python manage.py migrate


5️⃣ Create a Superuser
python manage.py createsuperuser


6️⃣ Run the Server
python manage.py runserver


Server will be available at http://127.0.0.1:8000/.

🛠 API Endpoints
Books API
Method	Endpoint	Description
GET	/api/books/	Get all books
POST	/api/books/	Create a new book
Book Lists API
Method	Endpoint	Description
GET	/api/book-lists/	Get all book lists
POST	/api/book-lists/	Create a new book list
POST	/api/book-lists/{id}/add_books/	Add books to a list
DELETE	/api/book-lists/{id}/remove_book/	Remove a book from a list




🔍 Troubleshooting
ModuleNotFoundError: Run pip install -r requirements.txt.
Database issues: Run python manage.py migrate --run-syncdb.
CORS issues: Ensure django-cors-headers is installed and configured in settings.py:
INSTALLED_APPS = [
    'corsheaders',
    ...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True  # Allow frontend requests


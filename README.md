🚀 Django REST API – Demo Assignment

Backend / Full Stack Developer Task

A clean, scalable Django REST Framework application developed as part of a technical assignment.
This project demonstrates RESTful CRUD operations, third-party API integration, and database-driven reporting, following real-world backend development best practices.


---

📌 Key Features

✅ RESTful CRUD APIs using Django REST Framework

✅ PostgreSQL-ready backend (SQLite used for local development)

✅ Third-party API integration (Live Weather API)

✅ Data reporting & aggregation endpoint

✅ Django Admin Panel for data management

✅ Clean, maintainable project structure

✅ Secure environment variable handling



---

🛠️ Tech Stack

Language: Python

Framework: Django 5.x

API: Django REST Framework

Database: SQLite (PostgreSQL-ready)

External API: Open-Meteo Weather API

Version Control: Git



---

🧠 Architecture & Design Decisions

Implemented separation of concerns:

Models → Serializers → Views → URLs


Used ModelViewSet to efficiently handle CRUD operations

APIs are stateless and REST-compliant

External API calls handled using requests with basic error handling

Reporting logic implemented using Django ORM aggregation

Designed with scalability and maintainability in mind



---

📂 Project Structure

backend/
├── api/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   └── views.py
│
├── backend/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .env.example


---

🔗 API Endpoints

🔹 Products CRUD

GET    /api/products/
POST   /api/products/
PUT    /api/products/{id}/
DELETE /api/products/{id}/


---

🔹 Weather API (Third-Party Integration)

GET /api/weather/

Fetches live weather data from an external API.


---

🔹 Reporting API

GET /api/report/

Example response:

{
  "total_products": 0,
  "average_price": null
}


---


⚙️ Setup Instructions (Local Development)

Follow the steps below to run the project locally.

1️⃣ Clone the repository

git clone https://github.com/poojakalukhe2003/django-rest-api-demo.git
cd django-rest-api-demo


--

2️⃣ Create a virtual environment

python -m venv venv

---

3️⃣ Activate the virtual environment

Windows

venv\Scripts\activate

Mac / Linux

source venv/bin/activate


---

4️⃣ Install dependencies

pip install -r requirements.txt


---

5️⃣ Configure environment variables

Create a .env file in the project root using .env.example as reference:

DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

> Note: The .env file is intentionally not committed to GitHub for security reasons.


---

6️⃣ Apply database migrations

python manage.py migrate


---

7️⃣ Create superuser (optional)

python manage.py createsuperuser


---

8️⃣ Run the development server

python manage.py runserver


---

🧪 Access the Application

Admin Panel:
http://127.0.0.1:8000/admin/

API Endpoints:

/api/products/

/api/weather/

/api/report/



---

📈 Possible Enhancements

Authentication & role-based access

Pagination and filtering

API documentation (Swagger / OpenAPI)

Dockerized deployment

Production PostgreSQL configuration



---

👩‍💻 Author

Pooja
Backend / Full Stack Developer


---

🏁 Final Notes

This project focuses on clarity, clean code, and real-world backend practices rather than over-engineering.
The goal was to deliver a maintainable and production-ready foundation within the given timeframe.

Thank you for reviewing this submission.


---

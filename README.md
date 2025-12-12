# Trackify -- Smart Parcel Tracking & Delivery Management System

Trackify is a modern, role-based delivery management platform built with
**Python (Flask)**.\
It provides a seamless experience for customers, delivery companies, and
administrators --- all in one clean system.

Trackify allows users to create shipments, companies to process and
update them, and admins to manage the entire ecosystem.

------------------------------------------------------------------------

## 🚀 Features

### 👤 Public (no account needed)

-   Homepage\
-   About page\
-   Pricing page\
-   FAQ\
-   Contact\
-   Public tracking page (track by Tracking ID)

### 🧑‍💻 User (Client)

-   Create shipment requests\
-   View all shipments\
-   View shipment details\
-   Real-time shipment timeline\
-   Automatic price calculation\
-   Track shipments via tracking ID

### 🏢 Company

-   View pending shipment requests\
-   Accept / Reject shipments\
-   Update shipment status\
-   Edit company profile & pricing

### 🛠️ Admin

-   Manage all users\
-   Manage all companies\
-   Manage all shipments\
-   System statistics dashboard

------------------------------------------------------------------------

## 🧱 Tech Stack

-   **Backend:** Flask, SQLAlchemy, Flask-Migrate\
-   **Frontend:** HTML, CSS (Bootstrap), Jinja2\
-   **Database:** SQLite / PostgreSQL\
-   **Other:** WTForms, Bcrypt

------------------------------------------------------------------------

## 🗂️ Project Structure

    project/
    │
    ├── app.py
    ├── config.py
    ├── requirements.txt
    ├── README.md
    │
    ├── /instance
    │     └── database.sqlite
    │
    ├── /app
    │   ├── __init__.py
    │   ├── extensions.py
    │   ├── decorators.py
    │   │
    │   ├── /models
    │   ├── /forms
    │   ├── /routes
    │   │     ├── public.py
    │   │     ├── auth.py
    │   │     ├── user.py
    │   │     ├── company.py
    │   │     ├── admin.py
    │   │
    │   ├── /services
    │   ├── /templates
    │   ├── /static
    │
    └── /migrations

------------------------------------------------------------------------

## 🛠️ Installation

``` bash
git clone https://github.com/yourusername/trackify.git
cd trackify
```

Create a virtual environment:

``` bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate    # Windows
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Set up the database:

``` bash
flask db init
flask db migrate
flask db upgrade
```

Run the server:

``` bash
flask run
```

------------------------------------------------------------------------

## 🔧 Environment Variables

Create a `.env` file:

    SECRET_KEY=your-secret-key
    DATABASE_URL=sqlite:///instance/database.sqlite

------------------------------------------------------------------------

## 🧩 Future Improvements

-   Real-time tracking\
-   Email notifications\
-   Multi-company support\
-   User--company chat\
-   Full API version

------------------------------------------------------------------------

Project Will Be Done Soon... :)
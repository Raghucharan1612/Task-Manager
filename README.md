# 📝 Task Manager Web App

A simple and efficient **Task Manager Web Application** built using **Django, MySQL, HTML, and CSS**.
This project allows users to manage daily tasks with full **CRUD (Create, Read, Update, Delete)** functionality.

---

## 🚀 Features

* ➕ Add new tasks
* 📋 View all tasks
* ✅ Mark tasks as completed
* ❌ Delete tasks
* 🎨 Clean and responsive UI

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Database:** MySQL
* **Frontend:** HTML, CSS
* **Tools:** MySQL Workbench, VS Code

---

## 📂 Project Structure

```
taskproject/
│
├── manage.py
├── taskproject/
│   ├── settings.py
│   ├── urls.py
│
├── taskapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── home.html
│   │   └── add.html
│   ├── static/
│   │   └── css/
│   │       └── style.css
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

### 2. Install dependencies

```
pip install django mysqlclient
```

### 3. Configure MySQL Database

Update `settings.py`:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'task_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the server

```
python manage.py runserver
```

### 6. Open in browser

```
http://127.0.0.1:8000/
```

---

## 🔄 How It Works

1. User adds a task via form
2. Django processes request and stores data in MySQL
3. Tasks are displayed on the homepage
4. Users can mark tasks as completed or delete them

---

## 📸 Screenshots (Optional)

*Add screenshots of your UI here*

---

## 📌 Future Improvements

* User authentication (login/signup)
* Task deadlines & priorities
* Search and filter functionality
* REST API integration

---

## 👨‍💻 Author

**Raghu Charan R A**

---

## ⭐ Acknowledgment

This project was built as a beginner-friendly full-stack application to understand Django and database integration.

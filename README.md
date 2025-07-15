# Member API

A secure and lightweight RESTful API for managing member records, built with Flask and SQLite. This API allows authenticated users to perform full CRUD (Create, Read, Update, Delete) operations on a member database.

📍 **Live Demo**: [https://maazk.pythonanywhere.com/](https://maazk.pythonanywhere.com/)

---

## 🔧 Features

* 🛡️ Basic Authentication (username/password protected)
* 📄 Full CRUD operations:

  * Get all members
  * Get a specific member
  * Add a new member
  * Edit existing member
  * Delete a member
* 💾 SQLite-backed storage
* 🧱 Clean RESTful design with JSON responses

---

## 🔐 Authentication

All endpoints are protected via **Basic Auth**.

* **Username**: `admin`
* **Password**: `pass`

Include credentials in each request using the `Authorization` header.

Example:

```
Authorization: Basic YWRtaW46cGFzcw==
```

---

## 🚀 API Endpoints

| Method | Endpoint       | Description             |
| ------ | -------------- | ----------------------- |
| GET    | `/member`      | Get all members         |
| GET    | `/member/<id>` | Get a member by ID      |
| POST   | `/member`      | Add a new member        |
| PUT    | `/member/<id>` | Update entire member    |
| PATCH  | `/member/<id>` | Partially update member |
| DELETE | `/member/<id>` | Delete a member         |

### Example JSON Request (POST/PUT/PATCH)

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "level": "Gold"
}
```

---

## 🗃️ Database Schema

```sql
CREATE TABLE members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    level TEXT NOT NULL
);
```

---

## 🛠️ Setup Instructions

### 🔨 Prerequisites

* Python 3.7+
* `virtualenv` (optional but recommended)

### 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/member_api.git
   cd member_api
   ```

2. Create virtual environment and activate:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:

   ```bash
   sqlite3 members.db < schema.sql
   ```

5. Run the server:

   ```bash
   python app.py
   ```

Server will start at `http://127.0.0.1:5000`

---

## 📂 Project Structure

```
.
├── app.py           # Main Flask application
├── database.py      # DB connection helper
├── requirements.txt # Python dependencies
├── schema.sql       # DB schema for members table
└── members.db       # SQLite DB (generated at runtime)
```

---

## 🧪 Testing the API

Use tools like:

* [Postman](https://www.postman.com/)
* [curl](https://curl.se/)
* [httpie](https://httpie.io/)

Example `curl` request:

```bash
curl -u admin:pass http://127.0.0.1:5000/member
```

---

## 📌 Note

* This project is intended for learning and demo purposes. Do **not** use hardcoded credentials in production.

---

## 🙋‍♂️ Author

**Maaz Khan**
Deployed at: [https://maazk.pythonanywhere.com/](https://maazk.pythonanywhere.com/)

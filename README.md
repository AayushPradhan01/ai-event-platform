# 🎯 AI Event Recommendation Platform

## 🚀 Overview

This project is a **scalable, microservices-based backend system** built using **Python and FastAPI**. It is designed to simulate a real-world event platform (like BookMyShow or Meetup) enhanced with **AI-powered recommendations**.

The system follows **industry-level system design principles**, focusing on scalability, performance, and clean architecture.

---

## 🧠 Key Features

### 🔐 Authentication & Security

* User Registration & Login
* JWT-based Authentication
* OAuth2 integration with FastAPI
* Secure password hashing using bcrypt

---

### 🧩 Microservices Architecture

* User Service (implemented)
* Event Service (planned)
* Booking Service (planned)
* Recommendation Service (AI-based)

---

### ⚡ System Design Concepts Used

* Client-Server Architecture
* REST APIs
* OAuth2 Authentication
* Dependency Injection
* Scalable Microservices Structure
* Rate Limiting (planned)
* Caching (planned)
* Load Balancing (planned)
* Message Queues (planned)
* Idempotency (planned)

---

### 🗄️ Data Engineering & Storage

* SQL-based database (upcoming)
* NoSQL support (planned)
* Data pipelines for ML (planned)
* Feature engineering for recommendations

---

### 🤖 AI & Machine Learning (Upcoming)

* User behavior analysis
* Event recommendation system
* Model training using:

  * NumPy
  * Pandas
  * Scikit-learn
* Hyperparameter tuning
* Data visualization using Matplotlib

---

## 🏗️ Tech Stack

| Layer        | Technology                  |
| ------------ | --------------------------- |
| Backend      | FastAPI (Python)            |
| Auth         | JWT + OAuth2                |
| Database     | SQL Server (planned)        |
| ML           | NumPy, Pandas, Scikit-learn |
| Architecture | Microservices               |
| DevOps       | Git, GitHub (CI/CD planned) |

---

## 📂 Project Structure

```
ai-event-platform/
│
├── services/
│   └── user-service/
│       ├── app/
│       │   ├── routes/
│       │   ├── services/
│       │   ├── schemas/
│       │   └── models/
│       └── main.py
│
├── data-engineering/
├── infrastructure/
├── shared/
├── tests/
```

---

## 🧪 How to Run

```bash
# Activate virtual environment
venv\Scripts\activate

# Run FastAPI server
uvicorn main:app --reload
```

---

## 🌐 API Documentation

Once server is running:

```
http://127.0.0.1:8000/docs
```

---

## 🎯 Current Progress

✅ User Registration API
✅ Login with JWT Authentication
✅ OAuth2 Integration
✅ Protected Routes

---

## 🔜 Upcoming Features

* Database Integration (SQL Server)
* Event Management Service
* Booking System
* AI Recommendation Engine
* Caching & Performance Optimization
* Distributed System Enhancements

---

## 💡 Goal of This Project

To reach the skill level of a **3–4 years experienced Software Engineer** by implementing:

* Real-world backend architecture
* Advanced system design concepts
* AI integration into applications
* Production-level coding practices

---

## 👨‍💻 Author

Aayush Shankar
Application Engineer | Aspiring AI + System Design Expert

---

## ⭐ Note

This project is built for **learning, experimentation, and mastering real-world software engineering concepts**.

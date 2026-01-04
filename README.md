# 🚀 AI SaaS – Natural Language to SQL Platform

## 📌 Project Description

The **AI SaaS – Natural Language to SQL Platform** is a **production-style AI SaaS application** that allows users to query databases using **plain English**, which is automatically converted into **SQL queries** using a **locally hosted Large Language Model (LLM)**.

This project simulates how real-world SaaS analytics tools enable **non-technical users, analysts, and product teams** to access data insights without writing SQL, while still maintaining backend control and validation.

The primary goal of this project is to **demonstrate real-world backend + AI + system design skills**, making it highly relevant for **Software Engineer / Backend Engineer / AI Engineer roles**.

### Key Highlights

* End-to-end system (UI → API → LLM → Database)
* Converts **natural language into SQL queries**
* Uses **local LLM (Ollama + LLaMA 3)** — zero API cost
* Fully offline, privacy-first design
* Clean, scalable, interview-ready SaaS architecture

---

## 🧠 System Architecture

```
User (React UI)
     |
FastAPI API Gateway
     |
Prompt Builder / Validator
     |
Ollama (LLaMA3 LLM)
     |
Generated SQL Query
     |
Relational Database (MySQL)
     |
Query Results
     |
Response back to UI
```

---

## 🛠️ Tech Stack & Why Chosen

### Backend

* **Python 3.10+** – Industry-standard language with strong backend & AI ecosystem
* **FastAPI** – High-performance, async-ready, production-grade API framework
* **Pydantic** – Robust request/response validation and schema enforcement

### AI / LLM

* **Ollama (LLaMA 3)**

  * Fully **offline LLM inference**
  * No paid APIs or rate limits
  * Demonstrates real text-to-SQL LLM integration

### Frontend

* **React.js** – Industry-leading frontend framework
* **Axios** – Clean and maintainable API communication

### Database

* **MySQL** – Widely used relational database in enterprise applications

### DevOps / Tooling

* **Docker** – Reproducible, scalable local deployment
* **Git & GitHub** – Version control and project showcasing

✅ This stack closely mirrors **real SaaS analytics architectures used by startups and MNCs in Bangalore**.

---

## ⚙️ Step-by-Step Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/divithraju/AI-SaaS-Natural-Language-to-SQL.git
cd AI-SaaS-Natural-Language-to-SQL
```

---

### 2️⃣ Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
# .venv\\Scripts\\activate  # Windows

pip install -r requirements.txt
```

---

### 3️⃣ Install & Run Ollama (Local LLM)

```bash
# Install Ollama (Linux / Mac)
curl -fsSL https://ollama.com/install.sh | sh

# Pull LLaMA 3 model
ollama pull llama3

# Start Ollama server
ollama serve
```

---

### 4️⃣ Configure Database

* Create a **MySQL database**
* Update database credentials in backend configuration (`.env` or config file)

Example:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=sample_db
```

---

### 5️⃣ Start FastAPI Server

```bash
uvicorn main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Swagger API Docs:

```
http://127.0.0.1:8000/docs
```

---

### 6️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

## 🧪 How It Works

1. User enters a **natural language query** (e.g., "Show total sales by month")
2. Frontend sends the query to the **FastAPI backend**
3. Backend builds a structured prompt and sends it to the **local LLM**
4. LLM generates the corresponding **SQL query**
5. Backend validates and executes SQL against **MySQL**
6. Query results are returned and rendered in the UI

---

## 👨‍💻 My Individual Contributions

* Designed **end-to-end SaaS architecture** from scratch
* Built **FastAPI backend** with clean routing and validation
* Implemented **prompt engineering for text-to-SQL generation**
* Integrated **Ollama + LLaMA 3** for local AI inference
* Connected backend to **MySQL for query execution**
* Developed **React-based UI** for real-time querying
* Containerized services using **Docker**
* Wrote **production-quality README and setup documentation**

---

## 🎯 Why This Project Stands Out

✅ Uses **real LLM-based text-to-SQL conversion**
✅ Fully **offline & cost-free** AI SaaS
✅ Mirrors real **data analytics SaaS architecture**
✅ Clear separation of concerns
✅ Strong demonstration of backend + AI integration

---

## 📌 Future Enhancements

* SQL safety & query validation layer
* Role-based access control (RBAC)
* Support for PostgreSQL & SQLite
* Query history & saved reports
* Cloud deployment (AWS / GCP)

---

## 📞 Contact

**Divith Raju**
🎓 B.Tech – Artificial Intelligence & Data Science (2026)
📍 Bangalore, India

🔗 GitHub: [https://github.com/divithraju](https://github.com/divithraju  

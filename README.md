# AI SaaS – Natural Language to SQL (Ollama + FastAPI + React)
This project is a full-stack AI SaaS application that converts natural language (English) into SQL queries using a local Ollama LLM (llama3) and executes them on a MySQL database.

It supports SELECT, INSERT, UPDATE, and DELETE operations.
# Features
🧠 Natural language → SQL using Ollama (local LLM)

🗄️ MySQL database execution

🔁 Supports SELECT / INSERT / UPDATE / DELETE

⚡ FastAPI backend

🖥️ React + Vite frontend

🔐 CORS enabled for frontend-backend communication

🧪 Easy to test with Postman or UI
# How It Works

User enters a natural language request in the UI

Request is sent to FastAPI backend

Backend sends a prompt to Ollama (llama3)

LLM generates SQL query

SQL is executed on MySQL

Result is returned and displayed in UI
# Future Enhancements

SQL safety validation (block DROP/TRUNCATE)

Auto-detect operation (no dropdown)

Authentication & credits system

Data table UI with live refresh

Cloud deployment (AWS / Azure)
# Author

Built by Divith Raju as an AI SaaS learning & portfolio project 🚀

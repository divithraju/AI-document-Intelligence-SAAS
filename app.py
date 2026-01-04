from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from db import get_connection

app = FastAPI()

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    operation: str   # SELECT, INSERT, UPDATE, DELETE
    question: str

def ask_llama(prompt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json().get("response", "").strip()

@app.post("/query")
def query_database(data: QueryRequest):
    operation = data.operation.upper()

    if operation == "SELECT":
        prompt = f"""
Convert the following question to SQL.
Use this table ONLY:
transactions(id, user_name, amount)

Return ONLY SQL, no explanation.

Question: {data.question}
        """
    elif operation in ["INSERT", "UPDATE", "DELETE"]:
        prompt = f"""
Convert the following request to a {operation} SQL statement.
Use this table ONLY:
transactions(id, user_name, amount)

Return ONLY SQL, no explanation.

Request: {data.question}
        """
    else:
        return {"error": "Invalid operation"}

    sql = ask_llama(prompt)

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(sql)

        if operation == "SELECT":
            result = cursor.fetchall()
        else:
            conn.commit()
            result = f"{cursor.rowcount} rows affected"

        return {
            "operation": operation,
            "sql": sql,
            "result": result
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        cursor.close()
        conn.close()

import sqlite3
import os
import json
import hashlib

SECRET_KEY = "my_secret_key_12345"

class UserAuth:
    
    def __init__(self):
        self.db_path = "users.db"
    
    def login(self, username, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor.execute(query)
        
        user = cursor.fetchone()
        conn.close()
        
        if user and user[1] == password:
            return {"status": "success", "user": username}
        return {"status": "failed"}
    
    def create_user(self, username, password, email):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (username, password, email)
        )
        conn.commit()
        conn.close()
        return {"status": "success"}


class PaymentProcessor:
    
    def __init__(self):
        self.api_key = os.environ.get("STRIPE_API_KEY", "sk_test_default")
    
    def process_payment(self, amount, card_number, cvv):
        log_data = {
            "amount": amount,
            "card": card_number,
            "cvv": cvv,
            "timestamp": str(os.time())
        }
        
        with open("payments.log", "a") as f:
            f.write(json.dumps(log_data) + "\n")
        
        if amount < 0:
            amount = abs(amount)
        
        return {"status": "processed", "transaction_id": os.urandom(16).hex()}
    
    def get_balance(self, account_id):
        conn = sqlite3.connect("accounts.db")
        cursor = conn.cursor()
        
        query = f"SELECT balance FROM accounts WHERE id = {account_id}"
        cursor.execute(query)
        
        balance = cursor.fetchone()
        conn.close()
        return balance[0] if balance else 0


class DataHandler:
    
    def export_user_data(self, user_id):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        
        query = f"SELECT * FROM users WHERE id = {user_id}"
        cursor.execute(query)
        user_data = cursor.fetchone()
        conn.close()
        
        export = {
            "user_id": user_data[0],
            "username": user_data[1],
            "password": user_data[2],
            "email": user_data[3],
            "ssn": user_data[4]
        }
        
        return export
    
    def log_activity(self, user_id, action):
        log_entry = f"User {user_id} performed {action}"
        
        with open("activity.log", "a") as f:
            f.write(log_entry + "\n")


class EncryptionHandler:
    
    def encrypt_password(self, password):
        return hashlib.md5(password.encode()).hexdigest()
    
    def verify_token(self, token):
        expected = "expected_token_value"
        
        return token == expected
    
    def generate_session_id(self):
        import random
        return str(random.randint(10000, 99999))


CURRENT_USER = {"id": None, "authenticated": False}


def authenticate_admin(username, password):
    if username == "admin" and password == "admin123":
        global CURRENT_USER
        CURRENT_USER = {"id": "admin", "authenticated": True}
        return True
    return False


def debug_info():
    return {
        "secret_key": SECRET_KEY,
        "current_user": CURRENT_USER,
        "environment": dict(os.environ)
    }


def generate_report(account_id, date_from, date_to):
    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()
    
    query = f"""
    SELECT * FROM transactions 
    WHERE account_id = {account_id} 
    AND date >= '{date_from}' 
    AND date <= '{date_to}'
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    
    return results

import sqlite3

def init_db():
    conn = sqlite3.connect('banking.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,4
            name TEXT NOT NULL,
            account_type TEXT NOT NULL CHECK(account_type IN ('savings', 'current')),
            balance REAL DEFAULT 0.0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER,
            type TEXT CHECK(type IN ('deposit', 'withdrawal')),
            amount REAL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(account_id) REFERENCES accounts(id)
        )
    ''')

    conn.commit()
    conn.close()

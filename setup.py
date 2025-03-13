import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("schedule.db")
cursor = conn.cursor()

# Create Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    userid TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    preferred_tech TEXT NOT NULL
)
""")

# Create Schedule Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS schedule (
    preferred_tech TEXT NOT NULL,
    date TEXT NOT NULL,
    task TEXT NOT NULL
)
""")

# Insert Sample Users
cursor.executemany("INSERT INTO users (userid, password, preferred_tech) VALUES (?, ?, ?)", [
    ('john123', '970151', 'Python'),
    ('alice99', '970151', 'Java'),
    ('mark45', '970151', '.NET')
])

# Insert Sample Schedule
cursor.executemany("INSERT INTO schedule (preferred_tech, date, task) VALUES (?, ?, ?)", [
    ('Python', '2025-03-05', 'Complete Flask API development'),
    ('Java', '2025-03-05', 'Work on Spring Boot authentication'),
    ('.NET', '2025-03-05', 'Implement JWT authentication in .NET Core')
])

conn.commit()
conn.close()

print("SQLite Database Created Successfully!")

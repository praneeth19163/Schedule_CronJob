import sqlite3
from datetime import datetime, timedelta

DATABASE = "/home/praneeth/flask_project/schedule.db"  

def refresh_schedule():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()


    cursor.execute("DELETE FROM schedule WHERE date < date('now')")

  
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

    cursor.execute("SELECT COUNT(*) FROM schedule WHERE date = ?", (tomorrow,))
    task_count = cursor.fetchone()[0]

    if task_count == 0:
        print("There are no tasks for tomorrow.")
    else:
        print(f"Tasks for {tomorrow} already exist.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    refresh_schedule()


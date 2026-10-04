import sqlite3
from datetime import datetime



DATABASE_NAME = "students.db"



def connect():

    return sqlite3.connect(
        DATABASE_NAME
    )



def create_tables():

    conn = connect()

    cursor = conn.cursor()



    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            telegram_id INTEGER UNIQUE,

            name TEXT,

            username TEXT,

            joined_date TEXT

        )
        """
    )



    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS results (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            telegram_id INTEGER,

            exam_name TEXT,

            score INTEGER,

            total INTEGER,

            percentage INTEGER,

            date TEXT

        )
        """
    )



    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS registrations (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            telegram_id INTEGER,

            full_name TEXT,

            phone_number TEXT,

            username TEXT,

            payment_proof_file_id TEXT,

            status TEXT DEFAULT 'pending',

            date TEXT

        )
        """
    )



    # Migration: older installs may have a registrations table
    # without phone_number - add it if it's missing.

    cursor.execute(
        "PRAGMA table_info(registrations)"
    )

    existing_columns = [row[1] for row in cursor.fetchall()]

    if "phone_number" not in existing_columns:

        cursor.execute(
            "ALTER TABLE registrations ADD COLUMN phone_number TEXT"
        )



    conn.commit()

    conn.close()





def save_student(user):

    conn = connect()

    cursor = conn.cursor()



    cursor.execute(
        """
        INSERT OR IGNORE INTO students
        (
            telegram_id,
            name,
            username,
            joined_date
        )

        VALUES (?, ?, ?, ?)
        """,

        (
            user.id,
            user.full_name,
            user.username,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            )
        )
    )


    conn.commit()

    conn.close()





def save_result(
        telegram_id,
        exam_name,
        score,
        total,
        percentage
):

    conn = connect()

    cursor = conn.cursor()



    cursor.execute(
        """
        INSERT INTO results
        (
            telegram_id,
            exam_name,
            score,
            total,
            percentage,
            date
        )

        VALUES (?, ?, ?, ?, ?, ?)

        """,

        (
            telegram_id,
            exam_name,
            score,
            total,
            percentage,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            )
        )
    )



    conn.commit()

    conn.close()





def save_registration(
        telegram_id,
        full_name,
        phone_number,
        username,
        payment_proof_file_id
):

    conn = connect()

    cursor = conn.cursor()



    cursor.execute(
        """
        INSERT INTO registrations
        (
            telegram_id,
            full_name,
            phone_number,
            username,
            payment_proof_file_id,
            status,
            date
        )

        VALUES (?, ?, ?, ?, ?, 'pending', ?)
        """,

        (
            telegram_id,
            full_name,
            phone_number,
            username,
            payment_proof_file_id,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            )
        )
    )



    conn.commit()

    registration_id = cursor.lastrowid

    conn.close()


    return registration_id





def get_registration(registration_id):

    conn = connect()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
        id,
        telegram_id,
        full_name,
        phone_number,
        username,
        status

        FROM registrations

        WHERE id = ?
        """,

        (registration_id,)
    )


    row = cursor.fetchone()

    conn.close()


    return row





def update_registration_status(registration_id, status):

    conn = connect()

    cursor = conn.cursor()


    cursor.execute(
        """
        UPDATE registrations
        SET status = ?
        WHERE id = ?
        """,

        (status, registration_id)
    )


    conn.commit()

    conn.close()





def get_pending_registrations():

    conn = connect()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
        id,
        telegram_id,
        full_name,
        phone_number,
        username,
        date

        FROM registrations

        WHERE status = 'pending'

        ORDER BY date ASC
        """
    )


    rows = cursor.fetchall()

    conn.close()


    return rows





def get_total_students():

    conn = connect()

    cursor = conn.cursor()


    cursor.execute(
        "SELECT COUNT(*) FROM students"
    )


    count = cursor.fetchone()[0]


    conn.close()


    return count




def get_all_telegram_ids():

    conn = connect()

    cursor = conn.cursor()


    cursor.execute(
        "SELECT telegram_id FROM students"
    )


    ids = [row[0] for row in cursor.fetchall()]


    conn.close()


    return ids





def get_results_count():

    conn = connect()

    cursor = conn.cursor()


    cursor.execute(
        "SELECT COUNT(*) FROM results"
    )


    count = cursor.fetchone()[0]


    conn.close()


    return count





def get_top_scores(limit=10):

    conn = connect()

    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT 
        telegram_id,
        score,
        total,
        percentage

        FROM results

        ORDER BY percentage DESC

        LIMIT ?

        """,

        (limit,)
    )


    results = cursor.fetchall()


    conn.close()


    return results
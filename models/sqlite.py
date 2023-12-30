import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data


    def create_table_words(self):
        sql = """
        CREATE TABLE Words (
            id INTEGER PRIMARY KEY,
            en varchar(255) NOT NULL UNIQUE,
            uz varchar(255) NOT NULL UNIQUE ,
            medium varchar(255) NULL,
            date DATETIME DEFAULT CURRENT_TIMESTAMP
            );
"""
        self.execute(sql, commit=True)
    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id INTEGER PRIMARY KEY,
            name varchar(255) NULL ,
            telegram_id varchar(255) NOT NULL UNIQUE
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_words(self,  en: str, uz: str, medium: str = None):
        sql = """
          INSERT OR IGNORE INTO Words (en, uz, medium)
    VALUES (?,?, ?);
        """
        self.execute(sql, parameters=(en, uz, medium ), commit=True)
    def add_users(self, name: str, telegram_id: str):
        sql = """
          INSERT OR IGNORE INTO Users (name, telegram_id)
    VALUES (?,?);
        """
        self.execute(sql, parameters=(name, telegram_id, ), commit=True)

    def select_all_words(self):
        sql = """
        SELECT * FROM Words
        """
        return self.execute(sql, fetchall=True)

    def select_words(self, **kwargs):
        sql = "SELECT * FROM Words WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)
    def select_random_word(self):
        sql = """
        SELECT en, uz FROM Words ORDER BY RANDOM() LIMIT 4;
        """
        return self.execute(sql, fetchall=True)


    def count_words(self):
        return self.execute("SELECT COUNT(*) FROM Words;", fetchone=True)
    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
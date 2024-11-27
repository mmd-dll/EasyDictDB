import sqlite3
import json

DB_NAME = "data_store.db"

def save(data_dict:dict, table_name="data_table"):
    """To save data in SQL easliy

    Args:
        data_dict (dict): the dict data to save
        table_name (str, optional): name for data help you to load it. Defaults to "data_table".

    Raises:
        ValueError: what?
    """    
    if not isinstance(data_dict, dict):
        raise ValueError("Input data must be a dictionary.")
    
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL
            )
        """)
        
        json_data = json.dumps(data_dict)
        cursor.execute(f"INSERT INTO {table_name} (data) VALUES (?)", (json_data,))
        conn.commit()

def load(table_name="data_table"):
    """to load data from sql data

    Args:
        table_name (str, optional): name of data you save. Defaults to "data_table".

    Returns:
        dict: the data you save with this name
    """    
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT data FROM {table_name}")
        rows = cursor.fetchall()
        
        return [json.loads(row[0]) for row in rows][0]
    

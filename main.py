import sqlite3
import json

def initialize_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dictionaries (
            id TEXT PRIMARY KEY,
            data TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save(dictionary,dict_id):
    """
    Save a dictionary to the database.

    Args:
        dictionary (dict): The dictionary to save.
        dict_id (str): The unique identifier for the dictionary.

    This function serializes the dictionary into JSON format and stores it
    in the SQLite database under the provided unique identifier. If an entry
    with the same identifier already exists, it will be replaced.
    """
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    data_json = json.dumps(dictionary)
    cursor.execute('''
        INSERT OR REPLACE INTO dictionaries (id, data)
        VALUES (?, ?)
    ''', (dict_id, data_json))
    conn.commit()
    conn.close()

def load(dict_id):
    """
    Loads and returns a dictionary from the database based on the given ID.

    Args:
        dict_id (str): The ID of the dictionary to retrieve.

    Returns:
        dict or None: The dictionary data as a Python dictionary if found, 
        otherwise None.

    Raises:
        sqlite3.Error: If a database error occurs.
        json.JSONDecodeError: If the retrieved data cannot be decoded as JSON.
    """
    ""
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT data FROM dictionaries WHERE id = ?
    ''', (dict_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return json.loads(result[0])
    else:
        return None

initialize_db()

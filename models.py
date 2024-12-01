import sqlite3

# Returns all players data
def all_players():
    connection = sqlite3.connect("NBA_Player_Statistics.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM NBA_Player_Statistics')
    players = cursor.fetchall()
    connection.commit()
    connection.close()
    return players


# finds the player based on inputed name and searches
def search_players(name):
    connection = sqlite3.connect("NBA_Player_Statistics.db")
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM NBA_Player_Statistics WHERE NAME LIKE "%{name}%"')
    players = cursor.fetchall()
    connection.commit()
    connection.close()
    return players

def add_players(NAME:str, TEAM:str, POS:str, GP:int, MPG:float, FT:float, TWO_P:float, THREE_P:float, eFG:float, PPG:float, RPG:float, APG:float, SPG:float, BPG:float, TPG:float):
    connection = sqlite3.connect("NBA_Player_Statistics.db")
    cursor = connection.cursor()
    
    #Grabs next available ID
    cursor.execute('SELECT MAX(ID) FROM NBA_Player_Statistics')
    max_id = cursor.fetchone()[0]
    next_id = (max_id + 1)

    cursor.execute(f'INSERT INTO NBA_Player_Statistics (ID,NAME,TEAM,POS,GP,MPG,FT,TWO_P,THREE_P,eFG,PPG,RPG,APG,SPG,BPG,TPG) VALUES ("{next_id}", "{NAME}", "{TEAM}", "{POS}", "{GP}", "{MPG}", "{FT}", "{TWO_P}", "{THREE_P}", "{eFG}", "{PPG}", "{RPG}", "{APG}", "{SPG}", "{BPG}", "{TPG}")')
    cursor.execute(f'SELECT * FROM NBA_Player_Statistics')
    players = cursor.fetchall()
    connection.commit()
    connection.close()
    return players

# finds the player based on inputed name and deletes
def delete_players(id):
    connection = sqlite3.connect("NBA_Player_Statistics.db")
    cursor = connection.cursor()
    cursor.execute(f'DELETE from NBA_Player_Statistics WHERE ID = "{id}"')
    cursor.execute(f'SELECT * FROM NBA_Player_Statistics')
    players = cursor.fetchall()
    connection.commit()
    connection.close()
    return players

def sort_players(stat, order):
    connection = sqlite3.connect("NBA_Player_Statistics.db")
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM NBA_Player_Statistics ORDER BY "{stat}" {order}')
    players = cursor.fetchall()
    connection.commit()
    connection.close()
    return players

def update_players(stat, value, id):
    connection = sqlite3.connect("NBA_Player_Statistics.db")
    cursor = connection.cursor()
    cursor.execute(f'UPDATE NBA_Player_Statistics SET {stat} = "{value}" WHERE ID = "{id}"')
    cursor.execute(f'SELECT * FROM NBA_Player_Statistics')
    players = cursor.fetchall()
    connection.commit()
    connection.close()
    return players
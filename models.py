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
    cursor.execute(f'INSERT INTO NBA_Player_Statistics (NAME,TEAM,POS,GP,MPG,FT,TWO_P,THREE_P,eFG,PPG,RPG,APG,SPG,BPG,TPG) VALUES ("{NAME}", "{TEAM}", "{POS}", "{GP}", "{MPG}", "{FT}", "{TWO_P}", "{THREE_P}", "{eFG}", "{PPG}", "{RPG}", "{APG}", "{SPG}", "{BPG}", "{TPG}")')
    cursor.execute(f'SELECT * FROM NBA_Player_Statistics')
    players = cursor.fetchall()
    connection.commit()
    connection.close()
    return players


# finds the player based on inputed name and deletes
def delete_players(name):
    connection = sqlite3.connect("NBA_Player_Statistics.db")
    cursor = connection.cursor()
    cursor.execute(f'DELETE from NBA_Player_Statistics WHERE NAME = "{name.capitalize()}"')
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

def update_players(stat, value, name, team):
    connection = sqlite3.connect("NBA_Player_Statistics.db")
    cursor = connection.cursor()
    print(f"stat={stat}")
    print(f"value={value}")
    print(f"name={name}")
    print(f"team={team}")
    cursor.execute(f'UPDATE NBA_Player_Statistics SET "{stat}" = "{value}" WHERE NAME = "{name.capitalize()}" AND TEAM = "{team.capitalize()}"')
    cursor.execute(f'SELECT * FROM NBA_Player_Statistics')
    players = cursor.fetchall()
    connection.commit()
    connection.close()
    return players
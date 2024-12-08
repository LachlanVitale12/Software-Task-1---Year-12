# imports sqlite3 to be used
import sqlite3

# Returns all players data
# begins by connecting to the database
# then it executes SQL selecting all players from the database
# then returns it as the variable players
def all_players():
    connection = sqlite3.connect("NBA_Player_Statistics.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM NBA_Player_Statistics')
    players = cursor.fetchall()
    connection.commit()
    connection.close()
    return players

# finds the player based on inputed name
# begins by connecting to the database
# then it selects all players from the database whose name includes the
# inputed name
# then returns it as the variable players
def search_players(name):
    connection = sqlite3.connect("NBA_Player_Statistics.db")
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM NBA_Player_Statistics WHERE NAME LIKE "%{name}%"')
    players = cursor.fetchall()
    connection.commit()
    connection.close()
    return players

# Searched the database by a team and returns all players from team
# begins by connecting to the database
# then it selects all players from the database whose team is equal
# to the inputed team
# then returns it as the variable players
def search_team(team):
    connection = sqlite3.connect("NBA_Player_Statistics.db")
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM NBA_Player_Statistics WHERE TEAM = "{team}"')
    players = cursor.fetchall()
    connection.commit()
    connection.close()
    return players

# Adds a player with all parameters the user puts in
# begins by connecting to the database
# then it find the highest id in the database and adds 1 to set the next id
# for the player. Then it inserts the players new found id as well as every other
# variable the user inputted into the database. then it selects all players from
# the database and returns all players in the database with the new player
# then returns it as the variable players
def add_players(NAME:str, TEAM:str, POS:str, GP:int, MPG:float, FT:float, TWO_P:float, THREE_P:float, eFG:float, PPG:float, RPG:float, APG:float, SPG:float, BPG:float, TPG:float):
    connection = sqlite3.connect("NBA_Player_Statistics.db")
    cursor = connection.cursor()
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
# begins by connecting to the database
# then depending on the id the user inputed, that player is deleted from the
# database. then every player from the new database is returned
# then returns it as the variable players
def delete_players(id):
    connection = sqlite3.connect("NBA_Player_Statistics.db")
    cursor = connection.cursor()
    cursor.execute(f'DELETE from NBA_Player_Statistics WHERE ID = "{id}"')
    cursor.execute(f'SELECT * FROM NBA_Player_Statistics')
    players = cursor.fetchall()
    connection.commit()
    connection.close()
    return players

# Sorts all players in a database by a certain stat either in ASC or DEC order
# begins by connecting to the database
# then it selects all players from the database in the order of the selected stat
# by the user in either asc or dec order as selected by the user
# then returns it as the variable players
def sort_players(stat, order):
    connection = sqlite3.connect("NBA_Player_Statistics.db")
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM NBA_Player_Statistics ORDER BY "{stat}" {order}')
    players = cursor.fetchall()
    connection.commit()
    connection.close()
    return players

# Updates a players stat based on what the User inputs
# begins by connecting to the database
# then it updates the player that the user selects via the id. then it updates
# the selected stat to the new selected value as inputed by the user. then it
# selects all players in the database.
# then returns it as the variable players
def update_players(stat, value, id):
    connection = sqlite3.connect("NBA_Player_Statistics.db")
    cursor = connection.cursor()
    cursor.execute(f'UPDATE NBA_Player_Statistics SET {stat} = "{value}" WHERE ID = "{id}"')
    cursor.execute(f'SELECT * FROM NBA_Player_Statistics')
    players = cursor.fetchall()
    connection.commit()
    connection.close()
    return players
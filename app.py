# Modules get imported
from flask import Flask, render_template, request, send_file
from models import all_players, search_players, add_players, delete_players, sort_players, update_players, search_team
# Initialises the flask application
app = Flask(__name__)
# MANIFEST LOADER
@app.route('/manifest.json')
def serve_manifest():
    # Returns manifest
    return send_file('manifest.json', mimetype='application/manifest+json')
# SERVICE WORKER LOADER
@app.route('/sw.js')
def serve_sw():
    # Returns the service worker
    return send_file('sw.js', mimetype='application/javascript')
# HOMEPAGE
@app.route('/')
def home():
    # using all players function it grabs everything from database
    players = all_players()
    # returns players and the home html page
    return render_template('home.html', players=players)
# SEARCH PLAYER PAGE
@app.route('/search', methods = ["POST","GET"])
def search():
    # if a get request was used to access this page all players are shown
    # If a post request was used then depending on if they searched for a
    # player or team, it returns their search query
    if request.method == "GET":
        players = all_players()
    elif request.method == "POST":
        if "searched_user" in request.form:
            # grabs the input from the 'searched player' id form
            # using that players name, it is put into the search players function
            # the function will return all players whose names are like the inputed name
            player_name = request.form.get("searched_player")
            players = search_players(player_name)
        elif "searched_team" in request.form:
            # grabs the input from the 'searched team' id form
            # using that teams name, it is put into the search team function
            # the function will return all players who are apart of the inputed team
            team_name = request.form.get("searched_team")
            players = search_team(team_name)
    # the result returns the number of players found through either of the requests
    result = f"{len(players)} player(s) found"
    # returns the search html page, the result strign and the players
    return render_template('search.html', players=players, result=result)
# SORT BY PLAYER STAT PAGE
@app.route('/sort', methods = ["POST","GET"])
def sort():
    # if a get request was used to access this page all players are shown
    # If a post request was used then depending on what stat and order
    # they selected, the function sort players will return the players
    # in that order
    if request.method == "GET":
        players = all_players()
    elif request.method == "POST":
        stat = request.form.get("stat")
        order = request.form.get("order")
        players = sort_players(stat, order)
    # returns the sort html page and players
    return render_template('sort.html', players=players)
# ADD PLAYER PAGE
@app.route('/add', methods = ["POST","GET"])
def add():
    result = "Enter Player Data Below:"
    # if a get request was used to access this page all players are shown
    # If a post request was used then all the user inputs in the form are 
    # set to their proper data type and passed into the add player function
    # which adds the new player to the database. this would go through the
    # error checker described below before it is added
    if request.method == "GET":
        players = all_players()
    elif request.method == "POST":
        # ERROR CHECKING SYSTEM
        # Sees if an error occurs when any of the variables are set to their proper data type
        # Adds the user through the function at the bottom and returns the result of it being successful
        # If there is any error, the except statement would begin and return the result of an error
        try:
            name = request.form.get("NAME")
            team = request.form.get("TEAM")
            pos = request.form.get("POS")
            gp = int(request.form.get("GP"))
            mpg = float(request.form.get("MPG"))
            ft = float(request.form.get("FT"))
            two_p = float(request.form.get("TWO_P"))
            three_p = float(request.form.get("THREE_P"))
            efg = float(request.form.get("eFG"))
            ppg = float(request.form.get("PPG"))
            rpg = float(request.form.get("RPG"))
            apg = float(request.form.get("APG"))
            spg = float(request.form.get("SPG"))
            bpg = float(request.form.get("BPG"))
            tpg = float(request.form.get("TPG"))
            players = add_players(name, team, pos, gp, mpg, ft, two_p, three_p, efg, ppg, rpg, apg, spg, bpg, tpg)
            # displays a sucessful result
            result = "Data added Successfully"
        except:
            players = all_players()
            # displays an error
            result = "Error: incorrect data types"
    # returns the add html page, players and result
    return render_template('add.html', players=players, result=result)
# DELETE PLAYER PAGE
@app.route('/delete', methods = ["POST","GET"])
def delete():
    result=""
    # if a get request was used to access this page all players are shown
    # If a post request was used then using the delete players function
    # the players id that was inputted into the form would get deleted
    # from the database
    if request.method == "GET":
        players = all_players()
    elif request.method == "POST":
        output = request.form.get("deleted_user")
        players = delete_players(output)
        # displays a sucessful result
        result = "Player Deleted"
    # returns the delete html page, players and result
    return render_template('delete.html', players=players, result=result)
# UPDATE PLAYER PAGE
@app.route('/update', methods = ["POST","GET"])
def update():
    result = "Enter Player Data Below:"
    # if a get request was used to access this page all players are shown
    # If a post request was used then the user inputs into the form the
    # players id, what stat they want to change and the new value
    # it then goes through an error checking system described below
    # it is then passed into the update player function where the new
    # value for the player is added into the database
    if request.method == "GET":
        players = all_players()
    elif request.method == "POST":
        # ERROR CHECKING SYSTEM
        # Sees if an error occurs when any of the variables are set to their proper data type
        # Adds the user through the function at the bottom and returns the result of it being successful
        # If there is any error, the except statement would begin and return the result of an error
        try:
            id = request.form.get("id")
            stat = request.form.get("stat")
            value = request.form.get("value")
            if stat == "GP":
                value = int(value)
            elif stat in ["MPG","FT","TWO_P","THREE_P","eFG","PPG","RPG","APG","SPG","BPG","TPG"]:
                value = float(value)
            else:
                value = str(value)
            players = update_players(stat, value, id)
            # displays a sucessful result
            result = "Data added Successfully"
        except:
            players = all_players()
            # displays an error
            result = "Error: incorrect data type"
        # returns the update html page, players and the result
    return render_template('update.html', players=players, result=result)
# INDEX PAGE
@app.route('/index')
def index():
    # Returns the index html page
    return render_template('index.html')
# starts the flask server
# port 8000 allows it to be accessed by others on the same network
if __name__ == ('__main__'):
    app.run(debug=True, port=8000)
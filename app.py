from flask import Flask, render_template, request, send_file
from models import all_players, search_players, add_players, delete_players, sort_players, update_players


app = Flask(__name__)

# MANIFEST LOADER
@app.route('/manifest.json')
def serve_manifest():
    return send_file('manifest.json', mimetype='application/manifest+json')

# SERVICE WORKER LOADER
@app.route('/sw.js')
def serve_sw():
    return send_file('sw.js', mimetype='application/javascript')


# HOMEPAGE
@app.route('/')
def home():
    players = all_players()
    return render_template('home.html', players=players)


# SEARCH PLAYER PAGE
@app.route('/search', methods = ["POST","GET"])
def search():
    if request.method == "GET":
        players = all_players()
    elif request.method == "POST":
        output = request.form.get("searched_user")
        players = search_players(output)
    result = f"{len(players)} player(s) found"
    return render_template('search.html', players=players, result=result)


# SORT BY PLAYER STAT PAGE
@app.route('/sort', methods = ["POST","GET"])
def sort():
    if request.method == "GET":
        players = all_players()
    elif request.method == "POST":
        stat = request.form.get("stat")
        order = request.form.get("order")
        players = sort_players(stat, order)
    return render_template('sort.html', players=players)


# ADD PLAYER PAGE
@app.route('/add', methods = ["POST","GET"])
def add():
    result = "Enter Player Data Below:"
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
            result = "Data added Successfully"
        except:
            players = all_players()
            result = "Error: incorrect data types"
    return render_template('add.html', players=players, result=result)


# DELETE PLAYER PAGE
@app.route('/delete', methods = ["POST","GET"])
def delete():
    result=""
    if request.method == "GET":
        players = all_players()
    elif request.method == "POST":
        output = request.form.get("deleted_user")
        players = delete_players(output)
        result = "Player Deleted"
    return render_template('delete.html', players=players, result=result)


# UPDATE PLAYER PAGE
@app.route('/update', methods = ["POST","GET"])
def update():
    result = "Enter Player Data Below:"
    if request.method == "GET":
        players = all_players()
    elif request.method == "POST":

        # ERROR CHECKING SYSTEM
        # Sees if an error occurs when any of the variables are set to their proper data type
        # Adds the user through the function at the bottom and returns the result of it being successful
        # If there is any error, the except statement would begin and return the result of an error
        try:
            name = request.form.get("name")
            team = request.form.get("team")
            stat = request.form.get("stat")
            value = request.form.get("value")
            if stat == "GP":
                value = int(value)
            elif stat in ["MPG","FT","TWO_P","THREE_P","eFG","PPG","RPG","APG","SPG","BPG","TPG"]:
                value = float(value)
            else:
                value = str(value)
            players = update_players(stat, value, name, team)
            result = "Data added Successfully"
        except:
            players = all_players()
            result = "Error: incorrect data type"
    return render_template('update.html', players=players, result=result)


# INDEX PAGE
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == ('__main__'):
    app.run(debug=True)
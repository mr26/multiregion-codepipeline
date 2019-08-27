#!/usr/bin/python3

from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

app.config["DEBUG"] = True

teams = [
    {'id': 0,
     'team': 'Washington Wizards',
     'coach': "Scott Brooks",
     'pg': 'John Wall',
     'sg': 'Bradley Beal',
     'sf': 'Trevor Ariza',
     'pf': 'Jabari Parker',
     'c': 'Thomas Bryant'},
    {'id': 1,
     'team': 'Houston Rockets',
     'coach': 'Mike Dantoni',
     'pg': 'Chris Paul',
     'sg': 'Eric Gordon',
     'sf': 'James Harden',
     'pf': 'PJ Tucker',
     'c': 'Clint Capela'},
    {'id': 2,
     'team': 'Golden State Warriors',
     'coach': 'Steve Kerr',
     'pg': 'Steph Curry',
     'sg': 'Klay Thompson',
     'sf': 'Kevin Durant',
     'pf': 'Draymond Green',
     'c': 'Demarcus Cousins',}
    ]
     


@app.route('/', methods=['GET'])
def home():
    return "This is a Flask-based API Application written in Python TEST16"

@app.route('/testpage')
def tpage():
    return "testpage output"


@app.route('/api/v1/resources/teams/all')
def api_all():
    return jsonify(teams)


@app.route('/api/v1/resources/teams')
def api_id():
    results = []

    if 'team' in request.args:
        team = request.args['team']
        for i in teams:
            if i['team'] == team:
                results.append(i)
                return jsonify(results)
    if 'id' in request.args:
        id = int(request.args['id'])
        for team in teams:
            if team['id'] == id:
                results.append(team)
                return jsonify(results)

#    if 'id' in request.args:
#        id = int(request.args['id'])
#        for team in teams:
#            if team['id'] == id:
#                results.append(team)
#                return jsonify(results)
#    elif 'team' in request.args:
#        team = request.args['team']
#        for team in teams:
#            if team['team'] == team:
#                results.append(team)
#                return jsonify(results)
#    else:
#        return "Error: No id field provided.  Please specify an id."

#    results = []
    
#    for team in teams:
#        if team['id'] == id:
#            results.append(team)
#        elif team['team'] == team:
#            results.append(team)
   
#    return jsonify(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

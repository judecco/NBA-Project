from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import AddPlayer, UpdatePlayer

application =Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flask_nba'
application.config['SECRET_KEY'] = "GREENBAYRAPTORS"


import mysql.connector
mydb = mysql.connector.connect( 
    host= "localhost",
    user= "root",
    passwd = "root",
    database= "flask_nba"
    )

cursor = mydb.cursor(buffered=True)

@application.route('/')
def index():
    stuff= "A list for <strong>Every</strong> active NBA player"
    return render_template("index.html", stuff=stuff )

@application.route('/players', methods=["GET", "POST"])
def players():
    cursor.execute("Select * from nba_player_library")
    allrecords=cursor.fetchall()
    print()
    return render_template("players.html",records=allrecords)

@application.route('/conference/')
def conference():
    cursor.execute("Select * from nba_team_library")
    allrecords=cursor.fetchall()
    print()
    return render_template("conference.html", records=allrecords)

@application.route('/W_conference',methods=["GET", "POST"])
def W_conference():
    if request.method=="POST":
        division=request.form["Division"]
        cursor.execute("Select * from nba_team_library where division_id='{0}'".format(division))
        allrecords=cursor.fetchall()
    else:
        cursor.execute("Select * from nba_team_library where division_id in('D4', 'D5', 'D6')")
        allrecords=cursor.fetchall()
    return render_template("w_conference.html",records=allrecords)

@application.route('/E_conference',methods=["GET", "POST"])
def E_conference():
    if request.method=="POST":
        division=request.form["Division"]
        cursor.execute("Select * from nba_team_library where division_id='{0}'".format(division))
        allrecords=cursor.fetchall()
    else:
        cursor.execute("Select * from nba_team_library where division_id in('D1', 'D2', 'D3')")
        allrecords=cursor.fetchall()
    return render_template("E_conference.html",records=allrecords)

       

@application.route("/AddPlayer", methods=[ "GET", "POST"])
def new_player():
    form1= AddPlayer()
    if form1.validate_on_submit():
        cursor.execute(f"INSERT into nba_player_library(first_name, last_name, hometown, college, height, position, team ) values('{form.first_name.data}', '{form.last_name.data}', '{form.hometown.data}', '{form.college.data}', '{form.height.data}', '{form.position.data}', '{form.team.data}' ")
        mydb.commit()
    cursor.execute("select * from nba_team_library")
    teams_list=cursor.fetchall()
    cursor.execute("select * from nba_division_wiki")
    return render_template("AddPlayer.html",form=form1, teams=teams_list)

@application.route("/saveeditplayer", methods=[ "GET", "POST"])
def saveeditplayer():
    form= UpdatePlayer()
    if form.validate_on_submit():
        print("hello")
        updateQuery="UPDATE nba_player_library set first_name ='{0}', last_name ='{1}', hometown='{2}', college='{3}', height='{4}', position='{5}', team='{6}' where player_id={7} ".format(form.first_name.data, form.last_name.data, form.hometown.data,form.college.data, form.height.data, form.position.data, form.team.data,form.player_id.data)
        print(updateQuery)
        cursor.execute(updateQuery)
        mydb.commit()
    return redirect("/players")

@application.route("/editplayer/<int:playerid>", methods=[ "GET", "POST"])
def editplayer(playerid):
    form= UpdatePlayer()
    cursor.execute("select * from nba_player_library where player_id={0}".format(playerid))
    player_data=cursor.fetchone()
    
    form.first_name.data= player_data[0]
    form.last_name.data =  player_data[1]
    form.hometown.data = player_data[2]
    form.college.data = player_data[3]
    form.height.data = player_data[4]
    form.position.data = player_data[5]
    form.team.data = player_data[6]
    form.player_id.data = player_data[7]
    cursor.execute("select * from nba_team_library")
    teams_list=cursor.fetchall()
    if form.validate_on_submit():
        print("hello")
        cursor.execute("UPDATE nba_player_library first_name='{0}', last_name='{1}', hometown='{2}', college='{3}', height='{4}', position='{5}', team='{6}' where player_id={7} )".format(form.first_name.data, form.last_name.data, form.hometown.data,form.college.data, form.height.data, form.position.data, form.team.data,playerid))
        mydb.commit()
        return redirect("/")
    return render_template("EditPlayer.html",form=form, teams=teams_list)


@application.route("/saveNewPlayer",methods=["post"])
def add_new_player():
    record=request.form
    sqlInsertQuery=" insert into nba_player_library values('{0}','{1}','{2}','{3}',{4},'{5}','{6}',{7})".format(request.form["first_name"],request.form["last_name"], request.form["hometown"], request.form["college"], request.form["height"], request.form["position"], request.form["team"],'null')
    print(sqlInsertQuery)
    cursor.execute(sqlInsertQuery)
    mydb.commit()
    return redirect("players")

@application.route("/deletePlayer/<player_id>")
def deletePlayer(player_id):
    cursor.execute("DELETE FROM nba_player_library WHERE Player_ID = {0}".format(player_id))
    mydb.commit()
    return redirect("/players")     

application.run(debug=True, host = "0.0.0.0")
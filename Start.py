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
    return render_template("players.html")

@application.route('/conference/')
def conference():
    cursor.execute("Select * from nba_team_library")
    allrecords=cursor.fetchall()
    print()
    return render_template("conference.html", records=allrecords)

@application.route('/W_conference',methods=["post"])
def W_conference():
    division=request.form["Division"]
    cursor.execute("Select * from nba_team_library where division_id='{0}'".format(division))
    allrecords=cursor.fetchall()
    print("---",division)
    if division=="D4" or division=="D5" or division=="D6":
        return render_template("W_conference.html",records=allrecords)
    else:
        return render_template("E_conference.html",records=allrecords)
        


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
       

@application.route('/home')
def home():
    things=" Please choose an option"
    return render_template("home.html")

@application.route("/AddPlayer", methods=[ "GET", "POST"])
def new_player():
    form= AddPlayer()
    choices=(team_id, team_name for teams in nba_team_library)
    if form.validate_on_submit():
        cursor.execute(f"INSERT into nba_player_library(first_name, last_name, hometown, college, height, position, team ) values('{form.first_name.data}', '{form.last_name.data}', '{form.hometown.data}', '{form.college.data}', '{form.height.data}', '{form.position.data}', '{form.team.data}' ")
    return render_template("AddPlayer.html", form=form)

#@application.route("/filter",methods=["POST"])
#def filterdiv():
   # if request.form["division"]=="all":
        #return redirect("/")
    #else:
        #data = filterdiv.query.filter_by(division=request.form["Atlantic"]).all()
        #return render_template("conference.html",records=data)
#display a list
#@application.route('/filter/<division_id>/<division_name>', methods=['POST', 'GET'])
#def division(division_id, division_name):
 #   form = ListForm()
  #  cursor.execute("SELECT item_name, date_created, iditems FROM items WHERE list_owner = '{0}';".format(list_id))
   # items_in_list = cursor.fetchall()
#
 #   if form.is_submitted():
  #      cursor.execute("INSERT INTO items (iditems, item_name, list_owner, date_created) VALUES(NULL, '{0}', '{1}', now());".format(form.list_item.data, list_id))
   #     db.commit()
    #    flash(f'New List Created!!', 'success')
     #   return redirect(url_for('list', list_id=list_id, list_name=list_name))

    #return render_template("list.html", form=form, list_items = items_in_list, list_name=list_name, list_id=list_id)

application.run(debug=True, host = "0.0.0.0")
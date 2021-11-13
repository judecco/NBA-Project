from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired



class AddPlayer(FlaskForm):
    first_name = StringField("First Name",validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    hometown = StringField("Hometown", validators=[DataRequired()])
    college= StringField("College/University", validators=[DataRequired()])
    height = IntegerField("Height", validators=[DataRequired()])
    position = SelectField('Position', choices=[('PG', 'Point Guard'), ('SG', 'Shooting Guard'), ('SF', 'Small Forward'), ('PF', 'Power Forward'), ('C', 'Center')], validators=[DataRequired()])
    team = SelectField('Team', choices=[('123', 'Atlanta Hawks'),('125', 'Brooklyn Nets' ),('127',' Chicago Bulls'),('129','Dallas Mavericks' ),('131','Detroit Pistons' ), ('133','Houston Rockets' ), ('135','Los Angeles Clippers') ], validators=[DataRequired()])
    submit = SubmitField('Add')

class UpdatePlayer(FlaskForm):
    player_id=IntegerField("Player ID", validators=[DataRequired()])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    hometown = StringField("Hometown", validators=[DataRequired()])
    college= StringField("College/University", validators=[DataRequired()])
    height = IntegerField("Height", validators=[DataRequired()])
    position = SelectField('Position', choices=[('PG', 'Point Guard'), ('SG', 'Shooting Guard'), ('SF', 'Small Forward'), ('PF', 'Power Forward'), ('C', 'Center')], validators=[DataRequired()])
    team = SelectField('Team', choices=[('Atlanta Hawks', 'Atlanta Hawks'), ('Boston Celtics', 'Boston Celtics'), ('Brooklyn Nets', 'Brooklyn Nets'), ('Charlotte Hornets', 'Charlotte Hornets'), ('Chicago Bulls', 'Chicago Bulls'), ('Cleveland Cavaliers', 'Cleveland Cavaliers'), ('Dallas Mavericks', 'Dallas Mavericks'), ('Denver Nuggets', 'Denver Nuggets'), ('Detroit Pistons', 'Detroit Pistons'), ('Golden State Warriors', 'Golden State Warriors'), ('Houston Rockets', 'Houston Rockets'), ('Indiana Pacers', 'Indiana Pacers'), ('Los Angeles Clippers', 'Los Angeles Clippers'), ('Los Angeles Lakers', 'Los Angeles Lakers'), ('Mepmphis Grizzlies', 'Memphis Grizzlies'), ('Miami Heat', 'Miami Heat'), ('Milwaukee Bucks', 'Milwaukee Bucks'), 
    ('Minnesota Timberwolves', 'Minnesota Timberwolves'), ('New Orleans Pelicans', 'New Orleans Pelicans'), ('New York Knicks'), ('Oklahoma City Thunder', 'Oklahoma City Thunder'), ('Orlando Magic', 'Orlando Magic'), ('Philadelphia 76ers', 'Philidelphia 76ers'),('Pheonix Suns', 'Pheonix Suns'), ('Portland Trail Blazers', 'Portland Trail Blazers'), ('Sacramento Kings', 'Sacramento Kings'), ('San Sntonio Spurs', 'San Antonio Spurs'), ('Toronto Raptors', 'Toronto Raptors'), ('Utah Jazz', 'Utah Jazz'), ('Washington Wizards', 'Washington Wizards')], validators=[DataRequired()])
    submit = SubmitField('Add Player')
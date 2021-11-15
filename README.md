# NBA-Project

QA-DevOps-Fundamental-Project- NBA Database App:  
This repository contains my deliverable for the QA devops fundamental project.

## Contents:
Project Brief   
App Design
CI Pipeline 
Risk Assessment
The App
Updates
Known Issues
Future Work

Project Brief:
For this project we were given the task to create and design a web app of our choosing. Within this app there needed to be a CRUD (create, read, update and delete) functionality, the app needed to use the micro-framework of Flask, as well as having a minimum of two tables sharing a one-to-many relationship where the information within the tables is stored in a MYSQL database.

App Design:
I have decided to create a NBA players database app which would allow users to add players to their respective teams (create functionality), allow the consumer to also view some information about the team (read functionality). The app also allows the consumer to edit a player’s information if there were to be a change in their situation, i.e., if a player gets transferred to a new team (edit functionality) as well as giving the consumer the ability to remove a player from the database if they made a mistake or the player is no longer active in the league (delete functionality). The database for this project comprises of a Players table and a Teams table, with each team associated with many players (one-to-many relationship).

There was also an additional filter function that was added to this project. This gave the consumer the ability to filter through divisions to make it easier to view teams based on their division rather than the whole conference. This meant a divisions table was also added to the database in order for the function to be facilitated.

The aim for any future work would be to create team profiles and allow the consumer to be able to view all the players from each team through the team profile rather than through the list of every single player that is uploaded.

Risk Assessment:
After developing the idea for the project, it was seen as a viable next step to commence a risk assessment to identify but also develop measures and ideas that can be used to control the risks. The measures established could then be applied to the app.
![RA](https://raw.githubusercontent.com/judecco/NBA-Project/master/images/Picture6.png)

The probability and impact level (both respectively rated out of 5) of each individual risk found were estimated prior to and post implementation of control measures, to quantify the effect of implementing the measures.

The App:
When first navigating the app, the user is met with the main homepage:
Homepage:
The homepage is a simple page with a small introduction of what the app entails. The nav bar provides links which allows the user to either view the player database (the list of players currently added to the database) or the option to view the teams based on which conference they want to look at. 
![Home](https://raw.githubusercontent.com/judecco/NBA-Project/master/images/Picture1.png)

Players:
Within this page, the user can see exactly what players have been added to the database, with the players information also available for view (first name, last name, hometown, college, height, position, team). The consumer would have the ability to create a new player which would allow them to put in the information necessary to add players to the database. The user can also edit the players within the database, giving them the ability to change the information on each player if there are any changes to be made. They are also able to delete a player from the database if there were to be a player no longer active. 
![Players Home](https://raw.githubusercontent.com/judecco/NBA-Project/master/images/Picture4.png)
![Players Form](https://raw.githubusercontent.com/judecco/NBA-Project/master/images/Picture5.png)

Conference:
Finally, users can navigate through the different conferences, filtering through each conference by the division to see what teams are in the division and the name of the arena that they play in. 
![Eastern Conference](https://raw.githubusercontent.com/judecco/NBA-Project/master/images/Picture2.png)
![Western Conference](https://raw.githubusercontent.com/judecco/NBA-Project/master/images/Picture3.png)

Known Issues:
There were significant difficulties when attempting to connect the vm to the sql server. 
Continuously met with error messages that I had not been given any advice on how to deal with so it would take much longer than expected to progress.
Testing was not completed due to time constraints and the inability to connect the app to the online server.
MySQL connector was not being recognised in my code in the terminal.
When adding players to the database there is no assurance that a player can not have a duplicate profile.

Future Work
Add Team Profiles to the app, giving a bit more of a background to the team and extra information.
Add Players list to the Team profiles which would allow the individual to view every player profile that has been added to the team.
Give the user the ability to view the information about the player by clicking on their profile
I would also like to add a page that has all the results from the current NBA season, giving the user a more rounded experience when using the app.




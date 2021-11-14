from flask import url_for
from flask_testing import TestCase
from Start import application, mydb, AddPlayer

class TestBase(TestCase):
    def create_app(self):
        application.config.update(SQLALCHEMY_DATABASE_URI="sqlite://test.db",
        SECRET_KEY= "GREENBAYRAPTORS",
        DEBUG = True,
        WTF_CSRF_ENABLED=False
        )
        return application

    def setUp(self):
        mydb.create_all()
        sample = AddPlayer(first_name='Jake', last_name='Steve', hometown= 'Georgia', college='UCL', Height= 188, Position='SF', Team = 'Los Angeles Lakers' )
        mydb.session.add(sample)
        mydb.session.commit()

    def tearDown(self):
        mydb.session.remove()
        mydb.drop_all()


    
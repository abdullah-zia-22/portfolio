from flask import Flask, render_template
from db import MySqlDatabase

# create flask app
app = Flask(__name__)


def get_projects():
    cursor,db=MySqlDatabase.connection()
    cursor.execute("SELECT * from projects order by id desc;")
    cards_list=cursor.fetchall()
    MySqlDatabase.close_connection(cursor,db)
    return cards_list


@app.errorhandler(Exception)
def handle_exception(message):
    return render_template('error.html', message="Bad Request"), 400


@app.errorhandler(404)
def err_404(message):
    return render_template('error.html', message='404 Page Not Found'), 404


@app.route('/')
def main_page():
    return render_template('index.html', title='Muhammad Abdullah - Homepage')


@app.route('/home')
def home():
    return render_template('base.html', title='Base')

@app.route('/about')
def about_page():
    return render_template('about.html', title="About")

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    return render_template('contact.html', title='Contact Page')


@app.route('/projects')
def projects_page():
    return render_template('projects.html', title="Projects", cards=get_projects())

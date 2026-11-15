from flask import Flask, render_template,send_file
import json
import os

# create flask app
app = Flask(__name__)


def get_projects():
    file_path = os.path.join('api','static', 'assets', 'projects.json')
    with open(file_path, 'r') as file:
            projects = json.load(file)
    return projects['projects']


def get_featured_projects():
    featured_names = [
        'CLARA — AI-Powered Recruitment and Candidate Assessment Platform',
        'Sentimantle — Hotel Review Intelligence Platform',
        'Gift Marketplace',
    ]
    projects_by_name = {project['name']: project for project in get_projects()}
    featured_projects = []
    for name in featured_names:
        project = projects_by_name[name]
        paragraphs = project['description'].split('\n\n')
        featured_projects.append({**project, 'summary': paragraphs[1]})
    return featured_projects


@app.errorhandler(Exception)
def handle_exception(message):
    return render_template('error.html', message="Bad Request"), 400


@app.errorhandler(404)
def err_404(message):
    return render_template('error.html', message='404 Page Not Found'), 404


@app.route('/')
def main_page():
    return render_template(
        'index.html',
        title='Muhammad Abdullah - Homepage',
        featured_projects=get_featured_projects(),
    )


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

@app.route('/resume')
def resume():
    return send_file("static/assets/Muhammad Abdullah Web.pdf", as_attachment=True)
from functions import *
from flask import Flask


app = Flask(__name__)


@app.route('/')
def page_main():
    '''Основная страница'''

    candidates = get_all()
    result = format_candidates(candidates)
    return result


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    '''Поиск по номеру кандидата'''

    candidate = get_by_pk(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result


@app.route('/skills/<skill>')
def page_skills(skill):
    '''Поиск по навыку кандитатов'''

    candidates = get_by_skill(skill.lower())
    result = format_candidates(candidates)
    return result


app.run()

from functions import *
from flask import Flask


app = Flask(__name__)


@app.route('/')
def page_main():
    '''Основная страница'''

    candidates: list[dict[str, int | str]] = get_all()
    result: str = format_candidates(candidates)
    return result


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    '''Поиск по номеру кандидата'''

    candidate: dict[str, int | str] | str = get_by_pk(uid)
    if type(candidate) == str:
        return candidate
    else:
        result: str = f'<img src="{candidate["picture"]}">'
        result += format_candidates([candidate])
        return result


@app.route('/skills/<skill>')
def page_skills(skill):
    '''Поиск по навыку кандитатов'''

    candidates: list[dict[str, int | str]] = get_by_skill(skill.lower())
    result: str = format_candidates(candidates)
    return result


app.run()

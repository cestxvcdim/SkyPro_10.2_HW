import requests


def format_candidates(candidates: list[dict[str, int | str]]) -> str:
    '''Упрощённый вид'''

    result: str = '<pre>'
    for candidate in candidates:
        result += f'{candidate["name"]}\n' \
                  f'{candidate["position"]}\n' \
                  f'{candidate["skills"]}\n' \
                  f'<pre>'
    return result


def get_all() -> list[dict[str, int | str]]:
    '''Возвращает всех кандидатов'''

    return requests.get('https://www.jsonkeeper.com/b/G9LL').json()


def get_by_pk(pk_name: int) -> dict[str, int | str] | str:
    '''Возвращает кандидата по pk, если такого кандитата не было найдено, выведет неправильный pk'''

    candidates: list[dict[str, int | str]] = get_all()
    for candidate in candidates:
        if candidate["pk"] == pk_name:
            return candidate
    return 'Wrong pk'


def get_by_skill(skill_name: str) -> list[dict[str, int | str]]:
    '''Возвращает список кандидатов по навыкам'''

    candidates: list[dict[str, int | str]] = get_all()
    result: list = []
    for candidate in candidates:
        if skill_name in candidate["skills"].lower().split(', '):
            result.append(candidate)
    return result

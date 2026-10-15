#!/usr/bin/env python3
"""Поиск в интернете через Perplexity Sonar — основной инструмент сбора досье.

Зачем свой поиск, а не встроенный инструмент агента. Встроенный поиск у
разных установок разный (внутренний поисковик, ddgs, OpenAI), и качество
досье от него гуляет. Sonar сам читает источники, отвечает связным текстом со
ссылками и замечает противоречия — на нём методика и отлажена.

    search.py --wave1 "<Имя Фамилия>" [--org "<организация>"] [--latin "<Name Surname>"]
                                                  волна 1: личность и якоря (8 вопросов)
    search.py --wave2 "<Имя Фамилия>" [--org …] [--latin …]
                                                  волна 2: поиск по прошлому (8 вопросов)
    search.py --wave3 "<Имя Фамилия>" [--org …] [--latin …]
                                                  волна 3: связи — соратники, компании, сделки (8)
    search.py --wave4 "<Имя Фамилия>" [--org …] [--latin …]
                                                  волна 4: свежая повестка и спорное (8 вопросов)
    search.py "вопрос 1" ["вопрос 2" ... до 8]   свои вопросы — что волны не закрыли
    search.py --log                               сколько запросов уже сделано

Зачем готовые волны. В системе, где методика отлажена, встроенный поиск
агента и был Sonar: модель отправляла восемь вопросов за ход и не думала,
каким инструментом искать. Здесь встроенный поиск — другой движок, и в живых
прогонах агент уходил в него, а в Sonar отправлял пару запросов для галочки.
Готовая волна делает правильный путь самым коротким: одна команда — восемь
вопросов первого слоя методики через Sonar.

Каждый запрос пишется в журнал search_log.jsonl в рабочем каталоге навыка:
по нему видно, сколько поиска было на самом деле.

Настройки: PERPLEXITY_API_KEY (обязателен), DOSSIER_SONAR_MODEL (по умолчанию
«sonar»), DOSSIER_SEARCH_TIMEOUT_SEC (по умолчанию 60).
"""
from __future__ import annotations

import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

sys.dont_write_bytecode = True

SONAR_URL = "https://api.perplexity.ai/chat/completions"
MAX_QUERIES = 8          # волна — до восьми запросов, как в методике
MAX_ANSWER_CHARS = 3500  # ответ на один запрос; дисциплина вывода
LOG_NAME = "search_log.jsonl"


def work_dir() -> pathlib.Path:
    for env in ("OUROBOROS_SKILL_STATE_DIR", "OUROBOROS_TASK_DRIVE"):
        v = os.environ.get(env)
        if v:
            return pathlib.Path(v)
    return pathlib.Path.cwd()


def env_first(*names: str, default: str = "") -> str:
    for n in names:
        v = (os.environ.get(n) or "").strip()
        if v:
            return v
    return default


# Вопросы волн 1 и 2 — слои 0–1 поискового справочника и «поиск по прошлому».
# Формулировки — вопросами: Sonar понимает вопрос целиком и отвечает связно.
# Две формулировки латиницей: для иностранцев англоязычные источники полнее.
WAVES = {
    "wave1": [
        "{name}{org} — кто это? Последняя известная должность и организация, с какого года — по официальным источникам",
        "{name}{org}: биография — полное имя, год и место рождения, гражданство",
        "{name}{org}: образование — вуз, факультет, годы, учёные степени",
        "{name}{org}: хронология карьеры — все работодатели и должности по годам",
        "{latin}{org_en}: LinkedIn profile, current role and career history",
        "{name}{org}: интервью, выступления, авторские колонки от первого лица",
        "{name}{org}: награды, звания, членство в советах директоров и ассоциациях",
        "Есть ли другие публичные люди с именем {name} (тёзки, однофамильцы) и чем они отличаются от {name}{org}?",
    ],
    "wave2": [
        "{name}{org}: что было до текущей должности — предыдущие компании, роли, годы, промежутки в карьере",
        "{name}{org}: ключевые проекты, сделки, запуски, публикации или патенты — с датами",
        "{name}{org}: публично заявленные позиции по отрасли, финансам, технологиям и искусственному интеллекту",
        "{name}{org}: стиль управления и принятия решений — свидетельства коллег и собственные слова",
        "{name}{org}: публичные конфликты, судебные споры, санкции, критика — со ссылками на документы",
        "{name}{org}: главные новости за последние 12 месяцев",
        "{latin}{org_en}: interviews and public statements 2025–2026",
        "{latin}{org_en}: early career, education and previous employers",
    ],
    # Волна 3 — обход графа связей: каждый именной объект — свой вопрос.
    # Готовая волна задаёт общий каркас; найденные имена — своими вопросами.
    "wave3": [
        "{name}{org}: сооснователи, партнёры, ключевые соратники и наставники — кто и в какие годы",
        "{name}{org}: компании, в которые инвестировал или где входит в совет директоров — с годами",
        "{name}{org}: крупнейшие сделки, слияния и поглощения с его участием — контрагенты, суммы, даты",
        "{name}{org}: книги, статьи, патенты, соавторы — с годами",
        "{name}{org}: выступления на конференциях и форумах за последние два года — где, о чём",
        "{name}{org}: кто публично критикует или оппонирует — суть и источники",
        "{latin}{org_en}: business partners, co-founders, board seats and major deals",
        "{latin}{org_en}: investments and portfolio companies with dates",
    ],
    # Волна 4 — свежая повестка (для «Тем на обсуждение») и перепроверка спорного.
    "wave4": [
        "{name}{org}: что публично заявлял за последние три месяца — темы, цитаты, даты",
        "{name}{org}: текущие приоритеты и стратегия организации на ближайшие годы",
        "{name}{org}: ближайшие события — сделки, отчётность, выступления, запуски",
        "{name}{org}: в чём источники расходятся — дата и место рождения, образование, даты назначений",
        "{name}{org}: какие цифры о нём и его компании чаще всего цитируют и насколько они точны",
        "{name}{org}: личные профессиональные интересы и темы, которые сам поднимает в интервью",
        "{latin}{org_en}: latest news and statements, last 3 months",
        "{latin}{org_en}: strategy, priorities and outlook 2026",
    ],
}
WAVE_FLAGS = tuple("--" + k for k in WAVES)


def wave_queries(kind: str, name: str, org: str = "", latin: str = "") -> list:
    org_ru = f" ({org})" if org else ""
    org_en = f", {org}" if org else ""
    latin = latin or name
    return [q.format(name=name, org=org_ru, org_en=org_en, latin=latin) for q in WAVES[kind]]


def parse_wave_args(args: list):
    """--wave1 "Имя" [--org "…"] [--latin "…"] → (вид, вопросы) или (None, ошибка)."""
    kind = args[0].lstrip("-")
    rest = args[1:]
    opts = {"org": "", "latin": ""}
    name_parts = []
    i = 0
    while i < len(rest):
        a = rest[i]
        if a in ("--org", "--latin"):
            if i + 1 < len(rest):
                opts[a[2:]] = rest[i + 1].strip()
            i += 2
            continue
        if a.startswith(("--org=", "--latin=")):
            k, _, v = a[2:].partition("=")
            opts[k] = v.strip()
            i += 1
            continue
        if a.startswith("--"):
            # Придуманный флаг ушёл бы в Sonar частью имени — восемь платных
            # запросов вида «Иван Петров --lang en (Пример) — кто это?».
            return None, (f"Флага {a} нет. Волна принимает только --org и --latin: "
                          f"search.py --{kind} \"Имя Фамилия\" --org \"…\" --latin \"…\"")
        name_parts.append(a)
        i += 1
    name = " ".join(x.strip() for x in name_parts if x.strip())
    if not name:
        return None, f"После --{kind} нужно имя человека: search.py --{kind} \"Имя Фамилия\" [--org \"…\"] [--latin \"…\"]"
    PERSON[0] = " / ".join(x for x in (name, opts["latin"]) if x)
    return kind, wave_queries(kind, name, opts["org"], opts["latin"])


PERSON = [""]  # имя из волны — в журнал: сборка узнаёт по нему, про кого поиск


def log_query(record: dict) -> None:
    try:
        d = work_dir()
        d.mkdir(parents=True, exist_ok=True)
        with (d / LOG_NAME).open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError as exc:
        print(f"  (журнал поиска не записан: {exc})")


def ask(query: str, key: str, model: str, timeout: float) -> dict:
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Ты помогаешь собрать деловое досье. Отвечай по-русски, "
                                          "только фактами из источников, с датами. Если источники "
                                          "расходятся — укажи обе версии."},
            {"role": "user", "content": query},
        ],
        "temperature": 0,
    }
    last = ""
    for attempt in range(3):
        req = urllib.request.Request(
            SONAR_URL, data=json.dumps(body).encode(),
            headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                payload = json.load(resp)
            answer = str((payload.get("choices") or [{}])[0].get("message", {}).get("content") or "")
            urls = []
            for r in payload.get("search_results") or []:
                if isinstance(r, dict) and r.get("url"):
                    # Дата публикации — для «свежести данных» и даты источника в досье.
                    date = str(r.get("date") or r.get("last_updated") or "")[:10]
                    urls.append((str(r.get("title") or "")[:90], str(r["url"]), date))
            for u in payload.get("citations") or []:
                if isinstance(u, str) and all(u != x[1] for x in urls):
                    urls.append(("", u, ""))
            return {"ok": True, "answer": answer, "sources": urls}
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "ignore")[:160]
            if exc.code in (401, 403):
                return {"ok": False, "fatal": True, "error": f"Sonar отказал по ключу (HTTP {exc.code}): {detail}"}
            last = f"HTTP {exc.code}: {detail}"
        except Exception as exc:  # noqa: BLE001
            last = f"{type(exc).__name__}: {str(exc)[:120]}"
        if attempt < 2:
            time.sleep(2)
    return {"ok": False, "error": last}


def show_log() -> int:
    path = work_dir() / LOG_NAME
    try:
        lines = [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
    except (OSError, json.JSONDecodeError):
        lines = []
    ok = sum(1 for x in lines if x.get("ok"))
    print(f"Запросов к Sonar в журнале: {len(lines)} (успешных {ok}). Журнал: {path}")
    return 0


def main() -> int:
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 64
    if args[0] == "--log":
        return show_log()
    wave = ""
    if args[0] in WAVE_FLAGS:
        wave, queries = parse_wave_args(args)
        if wave is None:
            print(f"[!] {queries}")
            return 64
    elif args[0].startswith("--"):
        # Незнакомый флаг не уходит в Sonar вопросом: в прогоне «--wave3»,
        # «--org» и имя отправились бы как восемь бессмысленных запросов.
        print(f"[!] Флага {args[0]} нет. Готовые волны: {', '.join(WAVE_FLAGS)}; "
              f"свои вопросы — без флагов: search.py \"вопрос 1\" \"вопрос 2\" … (до 8).")
        return 64
    else:
        queries = [a.strip() for a in args if a.strip()][:MAX_QUERIES]
        if len(args) > MAX_QUERIES:
            print(f"[!] За один вызов — не больше {MAX_QUERIES} запросов; лишние отброшены.")

    key = (os.environ.get("PERPLEXITY_API_KEY") or "").strip()
    if not key:
        print("[!] PERPLEXITY_API_KEY не передан скрипту. Проверьте ключ в настройках и доступ "
              "к нему в карточке навыка.", file=sys.stderr)
        return 1
    model = env_first("DOSSIER_SONAR_MODEL", "OUROBOROS_SONAR_MODEL", default="sonar")
    try:
        timeout = float(env_first("DOSSIER_SEARCH_TIMEOUT_SEC", default="60"))
    except ValueError:
        timeout = 60.0

    from concurrent.futures import ThreadPoolExecutor
    started = time.time()
    with ThreadPoolExecutor(max_workers=len(queries)) as pool:
        results = list(pool.map(lambda q: ask(q, key, model, timeout), queries))

    failed = 0
    for i, (q, res) in enumerate(zip(queries, results), 1):
        log_query({"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "query": q, "ok": bool(res.get("ok")),
                   "sources": len(res.get("sources") or []), "model": model, "wave": wave or "custom", "person": PERSON[0],
                   # Адреса источников Sonar — сборка сверяет с ними источники досье.
                   "urls": [src[1] for src in (res.get("sources") or [])][:15]})
        print(f"\n=== {i}. {q}")
        if not res.get("ok"):
            failed += 1
            print(f"[!] ошибка: {res.get('error')}")
            if res.get("fatal"):
                print("Проверьте PERPLEXITY_API_KEY — без него поиск и триангуляция невозможны.")
            continue
        answer = res["answer"]
        if len(answer) > MAX_ANSWER_CHARS:
            answer = answer[:MAX_ANSWER_CHARS] + " …[обрезано]"
        print(answer)
        if res["sources"]:
            print("Источники:")
            for n, src in enumerate(res["sources"][:10], 1):
                title, url = src[0], src[1]
                date = src[2] if len(src) > 2 else ""
                print(f"  [{n}] {title} {url}".rstrip() + (f" · {date}" if date else ""))
    print(f"\nВолна: {len(queries)} запросов, ошибок {failed}, {time.time() - started:.0f} с.")
    show_log()
    nxt = {
        "wave1": "волна 2 — поиск по прошлому: тот же вызов с --wave2",
        "wave2": "волна 3 — связи: тот же вызов с --wave3, затем по каждому новому "
                 "работодателю, вузу, сделке — свой вопрос (search.py \"вопрос 1\" … до 8)",
        "wave3": "волна 4 — свежая повестка и спорное: тот же вызов с --wave4",
        "wave4": "незакрытые якоря — своими вопросами (до 8 за вызов), затем render_dossier.py --schema",
    }.get(wave, "следующая волна — незакрытые якоря и спорное, своими вопросами (до 8 за вызов)")
    print(f"Дальше: {nxt}. Ищите только через search.py — встроенный поиск агента здесь не Sonar;")
    print("источники досье берите из ответов search.py: сборка проверит, что не меньше половины "
          "из них нашёл Sonar.")
    if failed:
        print("Если запрос упал (сеть, сбой платформы) — повторите ТОТ ЖЕ вызов; "
              "встроенный поиск — не замена.")
    return 1 if failed == len(queries) else 0


if __name__ == "__main__":
    sys.exit(main())

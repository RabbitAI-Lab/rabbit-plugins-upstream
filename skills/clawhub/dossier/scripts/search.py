#!/usr/bin/env python3
"""Поиск в интернете через Perplexity Sonar — основной инструмент сбора досье.

Зачем свой поиск, а не встроенный инструмент агента. Встроенный поиск у
разных установок разный (внутренний поисковик, ddgs, OpenAI), и качество
досье от него гуляет. Sonar сам читает источники, отвечает связным текстом со
ссылками и замечает противоречия — на нём методика и отлажена.

    search.py "вопрос 1" ["вопрос 2" ... до 8]   волна запросов параллельно
    search.py --log                               сколько запросов уже сделано

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
                    urls.append((str(r.get("title") or "")[:90], str(r["url"])))
            for u in payload.get("citations") or []:
                if isinstance(u, str) and all(u != x[1] for x in urls):
                    urls.append(("", u))
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
                   "sources": len(res.get("sources") or []), "model": model})
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
            for n, (title, url) in enumerate(res["sources"][:10], 1):
                print(f"  [{n}] {title} {url}".rstrip())
    print(f"\nВолна: {len(queries)} запросов, ошибок {failed}, {time.time() - started:.0f} с.")
    show_log()
    return 1 if failed == len(queries) else 0


if __name__ == "__main__":
    sys.exit(main())

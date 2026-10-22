# -*- coding: utf-8 -*-
"""context.py — реестр контекста для вопросов правлению: что уже известно о Сбере, его компаниях,
конкурентах и о России.

Зачем: модель не знает текущего положения компании и страны и задаёт вопросы, ответ на которые уже есть
или которые не имеют смысла (кредитовать бывшую «дочку» Сбера, вкладываться в прямого конкурента).
Поэтому перед каждым вопросом собирается контекст из двух источников:
  kb  — база знаний о Сбере (data/sber_knowledge_base.json, скрипт sber_kb.py): что Сбер делает, какие
        компании входят в группу, какие были проданы; записи появляются здесь автоматически;
  web — поиск в интернете: какие компании работают в отрасли в России и как они связаны со Сбером, уточнения
        по стране и по банку. Не больше 2 запросов на вопрос.

Скрипт в сеть не ходит: поиск делает агент своим инструментом веб-поиска (в ГигаАгенте — встроенный
поиск платформы), а сюда сдаёт запрос и результаты. Контекст — не источник фактов резюме: чисел из него в тексте нет.

Команды:
  add  <job> --json '{"slot": "q1", "scope": "company"|"country", "query": "…", "provider": "…",
                      "results": [{"title", "url", "date", "snippet"}], "error": ""}'      — запись поиска (web)
  list <job> [--slot q1]

slot  — черновой номер вопроса (q1…q6): все записи одного вопроса — с одним slot.
scope — company: вопрос о нашей компании; country: вопрос о стране.
В веб-запросе — «Сбер»/«Сбербанк» или «Россия»/«РФ»/«российский»: поиск идёт о нашей стороне.
"""
from __future__ import annotations

import argparse
import datetime
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _core as core  # noqa: E402

MAX_WEB_PER_SLOT = 2
MAX_KB_PER_SLOT = 4
MAX_SLOTS = 6                       # 3 вопроса + запас на замену
SCOPES = {"company": "о нашей компании (Сбер)", "country": "о стране (Россия)"}
SIDE_RX = r"сбер|sber|росси|\bрф\b|russia|российск"
SNIPPET_MAX = 700


def _path(jdir: Path) -> Path:
    return jdir / "context.json"


def _clip(text, n: int) -> str:
    text = re.sub(r"\s+", " ", core.as_text(text))
    return text if len(text) <= n else text[:n] + "…"


def load_store(jdir: Path) -> dict:
    st = core.read_json(_path(jdir), {"seq": 0, "entries": []})
    for e in st["entries"]:
        e.setdefault("kind", "web")
    return st


def check_slot(store: dict, slot: str, scope: str, kind: str) -> str:
    """Пустая строка — можно записать; иначе причина отказа."""
    if not re.fullmatch(r"q[1-9]", slot):
        return "slot — черновой номер вопроса: q1, q2, …"
    if scope not in SCOPES:
        return "scope — company (вопрос о нашей компании) или country (вопрос о стране)"
    same = [e for e in store["entries"] if e["slot"] == slot]
    if same and same[0]["scope"] != scope:
        return "у вопроса %s scope уже %s: у одного вопроса — одна сторона" % (slot, same[0]["scope"])
    limit = MAX_WEB_PER_SLOT if kind == "web" else MAX_KB_PER_SLOT
    done = [e for e in same if e["kind"] == kind]
    if len(done) >= limit:
        return ("лимит: не больше %d %s на один вопрос — для %s уже: %s" % (
            limit, "запросов в интернет" if kind == "web" else "обращений к базе знаний", slot,
            "; ".join("%s «%s»" % (e["id"], e["query"]) for e in done)))
    if len({e["slot"] for e in store["entries"]} | {slot}) > MAX_SLOTS:
        return "больше %d вопросов с контекстом: используйте уже открытые slot" % MAX_SLOTS
    return ""


def record(jdir: Path, entry: dict) -> dict:
    """Записать запись контекста (web или kb). entry: slot, scope, kind, query, provider, results, error."""
    store = load_store(jdir)
    store["seq"] += 1
    e = {"id": "c%03d" % store["seq"], "slot": entry["slot"], "scope": entry["scope"], "kind": entry["kind"],
         "query": entry["query"], "provider": _clip(entry.get("provider"), 40), "results": entry.get("results", []),
         "error": _clip(entry.get("error"), 500), "at": datetime.datetime.now().isoformat(timespec="seconds")}
    store["entries"].append(e)
    core.write_json(_path(jdir), store)
    return e


def cmd_add(args) -> None:
    jdir = core.job_dir(args.job)
    d = core.load_payload(args, "запись контекста")
    if not isinstance(d, dict):
        core.fail("Нужен JSON-объект: {slot, scope, query, provider, results, error}.")
    slot = core.as_text(d.get("slot")).lower()
    scope = core.as_text(d.get("scope")).lower()
    query = core.as_text(d.get("query"))
    if len(query) < 6:
        core.fail("Пустой или слишком короткий запрос.")
    if not re.search(SIDE_RX, query, re.I):
        core.fail("Запрос не о нашей стороне: в нём должно быть «Сбер»/«Сбербанк» или «Россия»/«РФ»/«российский».",
                  "Примеры: «беспилотные грузовики Россия компании», «Сбербанк Navio кредит», «Россия регулирование беспилотников 2026».")
    store = load_store(jdir)
    why = check_slot(store, slot, scope, "web")
    if why:
        if why.startswith("лимит"):
            core.out({"ok": True, "accepted": False, "slot": slot, "error": why,
                      "next": "Пишите вопрос по уже найденному (context.py list --slot %s)." % slot})
        core.fail(why)
    results = []
    for r in (d.get("results") or [])[:8]:
        if isinstance(r, dict) and (r.get("url") or r.get("snippet")):
            results.append({"title": _clip(r.get("title"), 200), "url": _clip(r.get("url"), 400),
                            "date": _clip(r.get("date"), 40), "snippet": _clip(r.get("snippet"), SNIPPET_MAX)})
    e = record(jdir, {"slot": slot, "scope": scope, "kind": "web", "query": query, "provider": d.get("provider"),
                      "results": results, "error": d.get("error")})
    left = MAX_WEB_PER_SLOT - len([x for x in store["entries"] if x["slot"] == slot and x["kind"] == "web"]) - 1
    if e["error"] or not results:
        nxt = ("Поиск не дал результатов (%s). %s" % (e["error"] or "пусто",
               "Можно переформулировать запрос (остался %d)." % left if left else
               "Запросы в интернет для этого вопроса исчерпаны: опирайтесь на базу знаний и скажите пользователю, что поиск не помог."))
    else:
        nxt = ("Прочитайте результаты: какие компании в России работают по теме вопроса, как каждая связана со Сбером "
               "(наша, связанная с группой, конкурент, независимая — сверяйте с sber_kb.py), что уже сделано или решено. %s "
               "Затем пишите вопрос: у вопроса — scope, context_ids, known и players. Числа из поиска в текст резюме не переносите."
               % ("Ещё один запрос — если чего-то не хватает (остался %d)." % left if left else "Запросов для этого вопроса больше нет."))
    core.out({"ok": True, "accepted": True, "id": e["id"], "slot": slot, "scope": scope, "kind": "web",
              "web_queries_left": left, "results": results, "error": e["error"], "next": nxt})


def cmd_list(args) -> None:
    jdir = core.job_dir(args.job)
    store = load_store(jdir)
    entries = [e for e in store["entries"] if not args.slot or e["slot"] == args.slot.lower()]
    core.out({"ok": True, "entries": entries,
              "by_slot": {s: ["%s (%s)" % (e["id"], e["kind"]) for e in store["entries"] if e["slot"] == s]
                          for s in sorted({e["slot"] for e in store["entries"]})}})


def load(jdir: Path) -> dict:
    """Для summary.py: {id: запись}."""
    return {e["id"]: e for e in load_store(jdir)["entries"]}


def main() -> None:
    core.setup_stdio()
    ap = core.JsonArgumentParser(prog="context.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("add"); p.add_argument("job"); p.add_argument("--json"); p.add_argument("--file"); p.set_defaults(fn=cmd_add)
    p = sub.add_parser("list"); p.add_argument("job"); p.add_argument("--slot"); p.set_defaults(fn=cmd_list)
    args = ap.parse_args()
    if not getattr(args, "fn", None):
        core.fail("Не указана команда.", "Доступно: add, list.")
    args.fn(args)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:
        core.fail("Внутренняя ошибка context.py: %s: %s" % (type(e).__name__, e))

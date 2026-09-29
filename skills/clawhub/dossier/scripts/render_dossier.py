#!/usr/bin/env python3
"""Собирает досье в Word строго по заданной структуре.

Почему скрипт, а не указания модели. Оформление, которое модель делает
каждый раз заново, каждый раз получается разным: то шрифт применён к
абзацам, но не к таблицам, то интервал сбился, то документ вырос на пять
страниц. Здесь оформление задано один раз и не зависит от прогона —
модель отвечает только за содержание.

Вход — JSON. Не свободный текст: свободный текст пришлось бы разбирать
обратно, а разбор — это ещё одно место, где всё ломается молча.

    python3 render_dossier.py dossier.json "Досье — Иванов Иван — 2026-08-27.docx"
    python3 render_dossier.py --check dossier.json     только проверить бюджет
    python3 render_dossier.py --schema                 показать формат входа
    python3 render_dossier.py --fit    <файл>          срезать под бюджет по правилу

Скрипт пишет ТОЛЬКО внутрь одного рабочего каталога — по порядку
`OUROBOROS_SKILL_STATE_DIR`, иначе `OUROBOROS_TASK_DRIVE`, иначе текущий
каталог: путь приходит аргументом, то есть в конечном счёте от модели, и без
ограничения досье можно было бы записать поверх настроек или другого навыка.
Читать JSON можно откуда угодно (только чтение). Сеть не трогается,
подпроцессы не запускаются.

Оформление фиксировано: Arial 12, интервал 1,5, поля 2 см, максимум две
страницы. Превышение бюджета — ошибка, а не предупреждение: документ на
три страницы никто не читает перед встречей.
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import sys

sys.dont_write_bytecode = True  # каталог навыка может быть только для чтения

# --- Бюджет ------------------------------------------------------------------
# Arial 12 с интервалом 1,5 при полях 2 см даёт ~2700 знаков на странице A4.
# Две страницы — 5400. Держим небольшой запас на заголовки и таблицу.
CHARS_PER_PAGE = 2700
MAX_PAGES = 2
BUDGET = CHARS_PER_PAGE * MAX_PAGES

# Контекст встречи меняет назначение документа: «Темы на обсуждение»
# превращаются из списка зацепок в проработанную повестку. Под неё нужна
# отдельная страница, иначе разделу негде развернуться.
TOPICS_LIMIT_WITH_CONTEXT = 2800
BUDGET_WITH_CONTEXT = CHARS_PER_PAGE * 3

# --- Структура ---------------------------------------------------------------
# Порядок разделов фиксирован и одинаков в чате и в документе: читатель не
# должен переучиваться, переходя из одного в другое.
# Заголовки, зависящие от рода. Два варианта: (мужской, женский).
# «Кто он» над досье женщины бросается в глаза сильнее, чем кажется:
# документ сразу выглядит собранным без внимания.
SECTIONS = [
    ("completeness", ("Полнота данных", "Полнота данных"),     True,  250),
    ("summary",      ("Одним абзацем", "Одним абзацем"),       True,  500),
    ("who",          ("Кто он", "Кто она"),                    True,  600),
    ("known_for",    ("Чем известен", "Чем известна"),         True,  900),
    ("culture",      ("Культурный контекст", "Культурный контекст"), False, 400),
    ("avoid",        ("Чего не касаться", "Чего не касаться"), True,  300),
    # «О чём говорить» и «что обсуждать» — один раздел: читатель перед встречей
    # читает их подряд и не различает, а деление одного списка надвое даёт повторы.
    ("topics",       ("Темы на обсуждение", "Темы на обсуждение"), True, 1500),
    ("unconfirmed",  ("Не подтверждено", "Не подтверждено"),   True,  400),
    ("analysis",     ("Анализ", "Анализ"),                     False, 400),
]

# Полнота данных считается внутри — она нужна агенту, чтобы решить, хватает
# ли материала. Руководителю в документе служебная арифметика («8/10 якорей
# закрыты») не нужна и мешает: он открывает досье, чтобы узнать человека, а
# не оценивать работу над ним.
HIDDEN_IN_DOCX = {"completeness"}


def heading(spec, gender: str) -> str:
    """Заголовок раздела с учётом рода: gender = 'f' — женский, иначе мужской."""
    if isinstance(spec, (list, tuple)):
        return spec[1] if str(gender or "").lower().startswith("f") else spec[0]
    return str(spec)


# Месяцы на любом языке, встреченные в датах, приводим к русским. Досье
# читает русскоязычный руководитель: «по состоянию на agosto 2026» выглядит
# недоделкой, даже когда факт верен.
MONTHS = {
    "january": "январь", "february": "февраль", "march": "март", "april": "апрель",
    "may": "май", "june": "июнь", "july": "июль", "august": "август",
    "september": "сентябрь", "october": "октябрь", "november": "ноябрь",
    "december": "декабрь",
    "enero": "январь", "febrero": "февраль", "marzo": "март", "abril": "апрель",
    "mayo": "май", "junio": "июнь", "julio": "июль", "agosto": "август",
    "septiembre": "сентябрь", "octubre": "октябрь", "noviembre": "ноябрь",
    "diciembre": "декабрь",
    "janeiro": "январь", "fevereiro": "февраль", "março": "март", "abril": "апрель",
    "maio": "май", "junho": "июнь", "julho": "июль", "setembro": "сентябрь",
    "outubro": "октябрь", "novembro": "ноябрь", "dezembro": "декабрь",
}


def ru_dates(text: str) -> str:
    """Заменяет иноязычные месяцы на русские, не трогая остального текста."""

    def repl(m):
        word = m.group(0)
        ru = MONTHS.get(word.lower())
        return ru if ru else word

    return re.sub(r"[A-Za-zÀ-ÿ]{3,12}", repl, text)

SCHEMA = {
    "name": "Полное имя, как в источниках",
    "gender": "'m' или 'f' — от этого зависят заголовки «Кто он» / «Кто она»",
    "meeting_context": "Необязательно. Контекст встречи, если владелец его дал. "
                       "При заполнении «Темы на обсуждение» расширяются до 2800 знаков, "
                       "а документ — до трёх страниц",
    "prepared": "Дата подготовки досье, ГГГГ-ММ-ДД — идёт в колонтитул",
    "last_known_role": "Последнее известное место работы и должность",
    "as_of": "Дата, на которую это известно (ГГГГ-ММ-ДД или «март 2025»)",
    "completeness": "Оценка полноты для чата. В документ НЕ выводится",
    "summary": "Один абзац: кто это и почему важен для разговора",
    "who": "Должность, организация, срок, образование. Только подтверждённое",
    "known_for": ["Факт с номером источника [1]", "Ещё факт [2]"],
    "culture": "Необязательно. Только если разговор на стыке деловых культур",
    "avoid": "Конкретика или «специфических тем под запретом не выявлено». Семья, "
             "здоровье, утраты — только обобщённо («личная жизнь и семья»), без имён и дат",
    "topics": ["О чём говорить и что обсуждать — одним списком: тема, "
               "почему она уместна, зацепка из биографии [3]. При заданном "
               "meeting_context раздел становится проработанной повесткой"],
    "unconfirmed": ["Что не подтвердилось и чего не хватило"],
    "analysis": ["Необязательно. Вывод, а не факт — помечается отдельно"],
    "sources": [
        {"n": 1, "title": "Название", "date": "2025-03-15",
         "strength": "сильный", "url": "https://example.com"}
    ],
    "figures": [
        {"value": "1 млн+", "source": 1,
         "quote": "ДОСЛОВНАЯ цитата из источника 1, содержащая это число"},
        {"value": "около 47 лет", "source": 3,
         "derived_from": "Вывод, а не цитата: из года окончания вуза (2001) [3]. "
                         "В тексте досье такое число обязано идти с «около» или «примерно»"},
    ],
}


# Запас, с которым просим сокращать. Ровно до лимита сокращать бесполезно:
# разделы считаются вместе, и сумма пересчитывается заново на каждом круге —
# срезав ровно превышение, автор промахивается снова. На GLM-5.2 это давало
# асимптоту 4760 -> 1246 -> 489 -> 327 -> 215 знаков превышения: пять кругов
# подряд, сходится, но раунды кончаются раньше. Цель с запасом превращает
# асимптоту в один-два шага.
TRIM_HEADROOM = 0.90


def target_for(limit: int) -> int:
    """До скольки просить сократить раздел с лимитом `limit`."""
    return int(limit * TRIM_HEADROOM)


def schema_with_limits() -> dict:
    """SCHEMA с проставленными лимитами разделов.

    Лимиты берутся из SECTIONS, а не переписываются руками: два списка
    разъедутся при первой же правке, и модель будет писать под вчерашнюю рамку.

    Без этого модель узнавала о бюджете только нарушив его: схема описывала,
    ЧТО писать, и молчала о том, СКОЛЬКО. Первое попадание в бюджет выходило
    случайным — у кого хватало запаса раундов, тот и доходил до файла.
    """
    out = dict(SCHEMA)
    for key, _spec, _req, limit in SECTIONS:
        if not limit or key not in out:
            continue
        note = f"ЛИМИТ {limit} знаков"
        if key == "topics":
            note += f" ({TOPICS_LIMIT_WITH_CONTEXT} при заданном meeting_context)"
        value = out[key]
        if isinstance(value, list):
            out[key] = list(value) + [f"<<{note} на весь раздел>>"]
        else:
            out[key] = f"{value}. {note}"
    out["_бюджет"] = (
        f"Весь документ — не более {BUDGET} знаков ({MAX_PAGES} страницы); "
        f"с заданным meeting_context — {BUDGET_WITH_CONTEXT} ({BUDGET_WITH_CONTEXT // CHARS_PER_PAGE} страницы). "
        f"Лимит каждого раздела — отказ, а не пожелание: превышение любого из них "
        f"не даст собрать документ. Пишите сразу под рамку."
    )
    return out


def as_text(value) -> str:
    """Разделы приходят строкой или списком — приводим к тексту одинаково."""
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return "\n".join(str(v).strip() for v in value if str(v).strip())
    return str(value).strip()


def budget_for(data: dict) -> int:
    """Общий бюджет знаков.

    Когда владелец дал контекст встречи, «Темы на обсуждение» становятся
    главным разделом документа: там сводится опыт человека с повесткой
    мероприятия. Ужимать его до 800 знаков — терять ровно то, ради чего
    досье и заказывали. Поэтому при заданном контексте бюджет раздела
    растёт до 2000, а весь документ — до трёх страниц.
    """
    return BUDGET_WITH_CONTEXT if as_text(data.get("meeting_context")) else BUDGET


def limits_for(data: dict) -> dict:
    """Лимиты разделов; при заданном контексте «Темы» расширяются."""
    limits = {key: limit for key, _t, _r, limit in SECTIONS}
    if as_text(data.get("meeting_context")):
        limits["topics"] = TOPICS_LIMIT_WITH_CONTEXT
    return limits


def measure(data: dict) -> tuple[int, list[tuple[str, int, int]]]:
    """Считает знаки по разделам. Возвращает (всего, [(раздел, факт, бюджет)])."""
    rows = []
    gender = data.get("gender") or "m"
    limits = limits_for(data)
    total = len(as_text(data.get("name"))) + len(as_text(data.get("last_known_role"))) + 60
    for key, spec, _required, _limit in SECTIONS:
        title = heading(spec, gender)
        limit = limits[key]
        n = len(as_text(data.get(key)))
        if n:
            n += len(title) + 2
        # Полнота данных в документ не идёт — и место не занимает.
        if key in HIDDEN_IN_DOCX:
            n = 0
        total += n
        rows.append((title, n, limit))
    # Таблица источников: строка занимает примерно 90 знаков полезной ширины.
    total += 90 * len(data.get("sources") or [])
    return total, rows


# --- Проверка цифр -----------------------------------------------------------
# Одно из досье утверждало «аналитика для 1 млн+
# частных инвесторов [1]». Источник [1] — собственная анкета человека в отраслевом реестре —
# говорит про частных инвесторов и оба канала, но НИКАКОГО числа не содержит.
# Сплошной поиск по 194 333 знакам всей доказательной базы прогона дал ноль
# совпадений «число + инвестор». Модель взяла верное утверждение и дописала к
# нему порядок величины, оставив ссылку на источник, в котором его нет.
#
# Опаснее всего то, что число правдоподобное: проверить его на глаз нельзя.
# Поэтому проверка машинная, а не инструкцией. Правило простое: каждое
# числовое утверждение в тексте обязано иметь запись в `figures` — либо с
# ДОСЛОВНОЙ цитатой источника, где это число стоит, либо с пометкой, что оно
# выведено. Процитировать то, чего в источнике нет, невозможно.

_CITE_RE = re.compile(r"\[\d+\]")
_SCALE = r"млн|млрд|тыс(?:яч[аи]?|\.)?|миллион\w*|миллиард\w*|%|руб\w*|₽|долл\w*|\$|€"
_FIGURE_PATTERNS = [
    # Число со шкалой: «1 млн+», «250 млн», «15 %», «$3 млрд».
    re.compile(r"[$€₽]?\s*\d[\d\s.,]*\+?\s*(?:%s)" % _SCALE, re.I),
    # Голое целое от двух знаков: «47 лет», «15 отраслей», «950 советов» — но НЕ
    # год. Порог именно двузначный: возраст и счётные утверждения («14+
    # инвестбанков») — самые частые места, где к верному факту дописывают
    # неверную величину. Однозначные числа пропускаем: шума от них больше, чем
    # риска.
    re.compile(r"(?<![\d.,])\d{2,}(?![\d.,])"),
]
_YEAR_RE = re.compile(r"^(?:1[89]|20)\d{2}$")
_HEDGES = ("около", "примерно", "порядка", "ориентировочно", "оценк", "приблизительно", "~")


def _norm_figure(text: str) -> str:
    """Сводим написание к сравнимому виду: регистр, пробелы, плюс, неразрывные."""
    s = str(text or "").lower().replace(" ", " ").replace("+", " ")
    s = re.sub(r"[\s,]+", " ", s)
    return s.strip(" .")


def _vf():
    """verify_facts как модуль: общие функции без дублирования кода."""
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import verify_facts  # noqa: E402
    return verify_facts


def _figure_in_text(value: str, text: str) -> bool:
    """«$10 млрд» в досье и «$10 billion» в цитате — одно число."""
    try:
        return _vf().figure_in_text(value, text)
    except Exception:  # noqa: BLE001 — сравнение строк выше остаётся в силе
        return False


def _numeric_claims(data: dict) -> list[tuple[str, str]]:
    """Находит числовые утверждения в теле досье. Возвращает [(раздел, фрагмент)]."""
    found: list[tuple[str, str]] = []
    fields = [k for k, _s, _r, _l in SECTIONS if k != "completeness"]
    fields.append("last_known_role")
    for key in fields:
        text = _CITE_RE.sub(" ", as_text(data.get(key)))
        for pat in _FIGURE_PATTERNS:
            for m in pat.finditer(text):
                frag = m.group(0).strip()
                # Год — не величина: «с 2022 года» проверять нечего.
                if _YEAR_RE.match(frag.replace(" ", "")):
                    continue
                found.append((key, frag))
    return found


def check_figures(data: dict) -> list[str]:
    """Каждое число в тексте должно быть подтверждено записью в `figures`."""
    problems: list[str] = []
    raw = data.get("figures")
    figures = [f for f in (raw or []) if isinstance(f, dict)]
    known_sources = {str(s.get("n")) for s in (data.get("sources") or []) if isinstance(s, dict)}

    for fig in figures:
        value = str(fig.get("value") or "").strip()
        if not value:
            problems.append("в figures есть запись без поля «value»")
            continue
        src = str(fig.get("source") or "").strip()
        if src and src not in known_sources:
            problems.append(f"figures «{value}»: источник [{src}] отсутствует в списке источников")
        quote = str(fig.get("quote") or "").strip()
        derived = str(fig.get("derived_from") or "").strip()
        if not quote and not derived:
            problems.append(
                f"figures «{value}»: нужна либо дословная цитата источника (quote), "
                f"либо пояснение вывода (derived_from)")
            continue
        if quote and _norm_figure(value) not in _norm_figure(quote) and not _figure_in_text(value, quote):
            problems.append(
                f"figures «{value}»: этого числа в quote нет — процитируйте источник "
                f"ДОСЛОВНО (язык цитаты любой: «$10 млрд» = «$10 billion») или пометьте "
                f"число как выведенное (derived_from)")
        if quote and not src:
            problems.append(f"figures «{value}»: цитата есть, а номер источника не указан")

    covered = [_norm_figure(f.get("value")) for f in figures if f.get("value")]
    hedged = {
        _norm_figure(f.get("value"))
        for f in figures
        if f.get("derived_from") and not f.get("quote")
    }
    for key, frag in _numeric_claims(data):
        norm = _norm_figure(frag)
        match = next((c for c in covered if c and (c in norm or norm in c)), None)
        if match is None:
            problems.append(
                f"раздел «{key}»: число «{frag}» ничем не подтверждено — "
                f"добавьте запись в figures с дословной цитатой источника "
                f"или уберите число из текста")
            continue
        if match in hedged:
            context = _CITE_RE.sub(" ", as_text(data.get(key))).lower()
            if not any(h in context for h in _HEDGES):
                problems.append(
                    f"раздел «{key}»: «{frag}» выведено, а не взято из источника — "
                    f"такое число подаётся с «около» или «примерно»")
    return problems


# --- Числа словами ------------------------------------------------------------
# Проверку цифр можно обойти, записав величину словами: «около восьмидесяти
# шести подчинённых», «свыше четырёх триллионов». Так и случилось в живом
# прогоне — скрипт искал цифры и не видел слов. Поэтому числительные от
# одиннадцати и выше, а также шкалы («тысяч», «миллионов», «триллионов») без
# цифры перед ними считаются обходом: величина пишется цифрами и идёт в figures.
_NUMWORD_RE = re.compile(
    r"(?<![\w-])(одиннадцат|двенадцат|тринадцат|четырнадцат|пятнадцат|шестнадцат|"
    r"семнадцат|восемнадцат|девятнадцат|двадцат|тридцат|сорок[аеу]?(?![\w-])|пятьдесят|"
    r"пятидесят|шестьдесят|шестидесят|семьдесят|семидесят|восемьдесят|восьмидесят|"
    r"девяност|двухсот|двести|тр[её]хсот|триста|четыр[её]хсот|четыреста|пятьсот|"
    r"пятисот|шестьсот|шестисот|семьсот|семисот|восемьсот|восьмисот|девятьсот|девятисот)\w*",
    re.I)
_SCALEWORD_RE = re.compile(
    r"(?<![\w-])(тысяч\w*|миллион\w*|миллиард\w*|триллион\w*|thousand|million|billion|trillion)",
    re.I)


def check_number_words(data: dict) -> list[str]:
    problems = []
    fields = [k for k, _s, _r, _l in SECTIONS if k != "completeness"] + ["last_known_role"]
    for key in fields:
        text = _CITE_RE.sub(" ", as_text(data.get(key)))
        for m in _NUMWORD_RE.finditer(text):
            problems.append(
                f"раздел «{key}»: число записано словами («{m.group(0)}») — так оно обходит "
                f"проверку. Запишите цифрами и добавьте в figures с цитатой, либо уберите")
        for m in _SCALEWORD_RE.finditer(text):
            before = text[:m.start()].rstrip()
            if before and (before[-1].isdigit() or before[-1] in "+$€₽"):
                continue  # «4 триллиона», «$3 млрд» — обычная величина, её ловит проверка цифр
            problems.append(
                f"раздел «{key}»: величина без цифры («…{text[max(0, m.start() - 25):m.end()]}») — "
                f"запишите число цифрами с записью в figures или уберите величину")
    return problems


# --- Запретные сведения ---------------------------------------------------------
# Инструкция: не собираем данные членов семьи, здоровье, частную жизнь. В живом
# прогоне в «Кто он» попали жена, дети и двоюродная сестра. Проверка грубая
# намеренно: лучше убрать лишнее, чем унести на встречу семейную справку.
_PRIVATE_RE = re.compile(
    r"(?<![\w-])(жена|жены|жене|женой|женат\w*|замуж\w*|супруг\w*|муж|мужа|мужем|"
    r"дет(и|ей|ям|ьми)|ребён\w*|ребен\w*|сын|сына|сыном|сыновья\w*|доч(ь|ери|ерью|ерей)|"
    r"двоюродн\w*|кузен\w*|кузин\w*|племянни\w*|внук\w*|внучк\w*|"
    r"болезн\w*|диагноз\w*|госпитализ\w*|ориентаци\w*|домашн\w* адрес\w*|"
    r"скончал\w*|умер(?:ла|ли|ший|шая|шего|шей|шему)?|смерт\w*|гибел\w*|погиб\w*|"
    r"инвалид\w*|паралич\w*|церебральн\w*|онколог\w*|похорон\w*)(?![\w-])",
    re.I)


def check_private(data: dict) -> list[str]:
    """Семья, здоровье, частная жизнь — ни в одном разделе.

    «Чего не касаться» раньше не проверялся, и в живом прогоне туда попала
    история о болезни и смерти сына героя досье — с именем и годом. Раздел
    называет тему, а не пересказывает её: «личная жизнь и семья» — достаточно.
    """
    problems = []
    fields = [k for k, _s, _r, _l in SECTIONS if k != "completeness"] + ["last_known_role"]
    for key in fields:
        text = as_text(data.get(key))
        for m in _PRIVATE_RE.finditer(text):
            hint = (" В «Чего не касаться» назовите тему обобщённо («личная жизнь и семья»), "
                    "без имён, дат и подробностей" if key == "avoid" else " Уберите")
            problems.append(
                f"раздел «{key}»: запретные сведения («{m.group(0)}») — семья, здоровье и "
                f"частная жизнь в досье и в ответе не упоминаются.{hint}")
    return problems


# --- Ссылки на источники --------------------------------------------------------
_SENT_RE = re.compile(r"(?<=[.!?])\s+|\n+")
_REFERENCE_DOMAINS = ("wikipedia.org", "wikiwand.com", "ruwiki.ru", "britannica.com")


def check_citations(data: dict) -> list[str]:
    """Каждая фраза в «Кто он» и «Чем известен» несёт номер источника."""
    problems = []
    for key in ("who", "known_for"):
        for sent in _SENT_RE.split(as_text(data.get(key))):
            sent = sent.strip(" -•\t")
            if len(sent) >= 25 and not _CITE_RE.search(sent) and "[Анализ]" not in sent:
                problems.append(f"раздел «{key}»: фраза без номера источника — «{sent[:70]}…»")
    for src in data.get("sources") or []:
        if not isinstance(src, dict):
            continue
        url = str(src.get("url") or "").lower()
        if any(d in url for d in _REFERENCE_DOMAINS) and "сильн" in str(src.get("strength") or "").lower():
            problems.append(
                f"источник [{src.get('n')}]: справочник/энциклопедия — это средний или слабый "
                f"источник, не «сильный»")
    return problems


# --- Триангуляция: сборка без неё невозможна -------------------------------------
def triangulation_gaps(data: dict) -> list[str]:
    """Утверждения, которые verify_facts.py НЕ подтвердил (по его кэшу)."""
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import verify_facts as vf  # noqa: E402

    srcmap = vf.sources_by_number(data)
    cache = vf.load_cache()
    good = ("ПОДТВЕРЖДЕНО", "ПЕРВОИСТОЧНИК", "ПОДТВЕРЖДЕНО (источник не открылся)")
    gaps = []
    for claim in vf.collect_claims(data):
        if vf.primary_only(claim, srcmap):
            continue
        hit = cache.get(vf.claim_key(claim, srcmap))
        if not (isinstance(hit, dict) and hit.get("status") in good):
            gaps.append(claim["text"][:90])
    return gaps


def unverified_allowed():
    """Причина сбоя триангуляции, если verify_facts.py недавно упал из-за ключа
    или сети; иначе None — тогда --unverified не принимается."""
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import time as _time
    import verify_facts as vf  # noqa: E402
    try:
        st = json.loads((vf.work_dir() / vf.STATUS_NAME).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if st.get("status") not in ("no_key", "auth", "network"):
        return None
    if _time.time() - float(st.get("ts") or 0) > 6 * 3600:
        return None
    return str(st.get("detail") or st.get("status"))


# --- Поиск шёл через Sonar -------------------------------------------------------
# В живом прогоне агент прочитал «ищите через search.py», сам написал «вижу
# новый шаг — search.py» и всё равно собрал материал встроенным поиском:
# восемь запросов, ни одного через Sonar. Инструкция этого не удерживает,
# поэтому сборка сверяется с журналом search.py: был ли хотя бы один
# успешный запрос про этого человека за последние часы.
SEARCH_WINDOW_HOURS = 12
_TRANSLIT = dict(zip(
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
    ["a", "b", "v", "g", "d", "e", "e", "zh", "z", "i", "y", "k", "l", "m", "n", "o",
     "p", "r", "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya"]))


def _latin(text: str) -> str:
    s = "".join(_TRANSLIT.get(ch, ch) for ch in str(text or "").lower())
    s = s.replace("dzh", "j").replace("kh", "h").replace("ё", "e")
    return re.sub(r"[^a-z0-9 ]+", " ", s)


def _name_keys(data: dict) -> list[str]:
    names = " ".join(as_text(data.get(k)) for k in ("name", "name_en", "name_latin"))
    keys = []
    for tok in _latin(names).split():
        if len(tok) >= 5:
            keys.append(tok[:5])
        elif len(tok) >= 3:
            keys.append(tok)
    return sorted(set(keys))


def search_evidence(data: dict) -> tuple[int, int]:
    """(успешных запросов Sonar про этого человека, всего успешных) за окно."""
    import time as _time
    path = _vf().work_dir() / "search_log.jsonl"
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return 0, 0
    keys = _name_keys(data)
    now = _time.time()
    about, total = 0, 0
    for line in lines:
        try:
            rec = json.loads(line)
            ts = _time.mktime(_time.strptime(str(rec.get("ts")), "%Y-%m-%dT%H:%M:%S"))
        except (ValueError, TypeError, json.JSONDecodeError, OverflowError):
            continue
        if not rec.get("ok") or now - ts > SEARCH_WINDOW_HOURS * 3600:
            continue
        total += 1
        q = " " + _latin(rec.get("query")) + " "
        if any((" " + k) in q for k in keys):
            about += 1
    return about, total


def chat_text(data: dict, ver: str, why_unverified: str = "") -> str:
    """Готовый текст ответа в чат — тот же, что в документе, в том же порядке.

    Агент раз за разом начинал ответ с «Готово. Файл отправлен.» вместо оценки
    полноты и пересказывал досье своими словами, добавляя то, что проверка
    отсекла. Поэтому текст собирает скрипт — из того же JSON, что и документ.
    """
    gender = data.get("gender") or "m"
    out = []
    if why_unverified:
        out.append(f"⚠️ Триангуляция НЕ отработала: {why_unverified}. "
                   f"Досье через внешние источники НЕ проверено.")
    out.append(f"**Полнота данных:** {as_text(data.get('completeness'))}")
    out.append("")
    out.append(f"## Досье — {as_text(data.get('name'))}")
    role = as_text(data.get("last_known_role"))
    as_of = ru_dates(as_text(data.get("as_of")))
    if role:
        out.append(role + (f" (по состоянию на {as_of})" if as_of else ""))
    for key, spec, _req, _lim in SECTIONS:
        if key == "completeness":
            continue
        value = data.get(key)
        if not as_text(value):
            continue
        out.append("")
        out.append(f"**{heading(spec, gender)}**")
        if isinstance(value, (list, tuple)):
            out.extend(f"- {str(v).strip()}" for v in value if str(v).strip())
        else:
            out.append(as_text(value))
    srcs = [s for s in (data.get("sources") or []) if isinstance(s, dict)]
    if srcs:
        out.append("")
        out.append("**Источники**")
        for s in srcs:
            out.append(f"[{s.get('n')}] {s.get('title') or ''} — {s.get('url') or ''}".strip())
    out.append("")
    check = "БЕЗ ТРИАНГУЛЯЦИИ" if why_unverified else "проверка verify_facts"
    out.append(f"Собрано: dossier v{ver} · {check} · вёрстка render_dossier · модель <МОДЕЛЬ>")
    return "\n".join(out)


def skill_version() -> str:
    try:
        head = (pathlib.Path(__file__).resolve().parent.parent / "SKILL.md").read_text(encoding="utf-8")[:3000]
        m = re.search(r"^version:\s*([\w.]+)", head, re.M)
        return m.group(1) if m else "?"
    except OSError:
        return "?"


def validate(data: dict) -> list[str]:
    problems = []
    for key in ("name", "last_known_role", "summary", "sources"):
        if not as_text(data.get(key)) and not data.get(key):
            problems.append(f"нет обязательного поля «{key}»")
    gender = data.get("gender") or "m"
    for key, spec, required, _limit in SECTIONS:
        if required and not as_text(data.get(key)):
            if key in HIDDEN_IN_DOCX:
                # В документ не выводится, но нужна для первой строки ответа в чате.
                problems.append(f"поле «{key}» обязательно: оценка полноты идёт первой строкой "
                                f"в чат (в документ не выводится)")
                continue
            problems.append(f"раздел «{heading(spec, gender)}» обязателен — напишите "
                            f"«сведений нет», если наполнить нечем")
    srcs = data.get("sources") or []
    if not srcs:
        problems.append("список источников пуст — досье без источников не сдаётся")
    for s in srcs:
        if not str(s.get("url") or "").startswith("http"):
            problems.append(f"источник {s.get('n')}: нет адреса")
    total, rows = measure(data)
    budget = budget_for(data)
    pages = budget // CHARS_PER_PAGE
    if total > budget:
        target = target_for(budget)
        problems.append(
            f"превышен бюджет: {total} знаков против {budget} "
            f"(≈{total / CHARS_PER_PAGE:.1f} страницы вместо {pages}) — "
            f"СОКРАТИТЕ ДО {target} (убрать {total - target}). "
            f"Либо запустите «--fit <файл>»: скрипт срежет сам, по правилу и вслух")
    # Лимит раздела — тоже отказ, а не пометка. Раньше он только печатался:
    # «Кто она 1026 / 600 превышен», и тут же «ГОДНО». Раздел раздувался вдвое,
    # съедал место у остальных, и ловил это лишь общий бюджет — то есть уже
    # тогда, когда документ поехал за два листа.
    for title, actual, limit in rows:
        if limit and actual > limit:
            target = target_for(limit)
            problems.append(
                f"раздел «{title}»: {actual} знаков из {limit} — "
                f"СОКРАТИТЕ ДО {target} (убрать {actual - target}). "
                f"Цель ниже лимита намеренно: разделы считаются вместе, и "
                f"срезав ровно превышение, вы промахнётесь снова")
    if data.get("gender") not in ("m", "f", None, ""):
        problems.append("поле gender принимает только 'm' или 'f'")
    # Отдельного раздела «О чём говорить» нет — всё про разговор идёт в topics.
    # Молча игнорировать лишнее поле нельзя: автор решил бы, что раздел на месте.
    if data.get("talk_about"):
        problems.append(
            "поле «talk_about» не поддерживается: «о чём говорить» и «что обсуждать» — "
            "один раздел «topics». Перенесите содержимое туда")
    problems.extend(check_figures(data))
    problems.extend(check_number_words(data))
    problems.extend(check_private(data))
    problems.extend(check_citations(data))
    return problems


def require_docx():
    """python-docx — сторонняя библиотека, и без неё скрипт бесполезен.

    Проверяем ДО сбора данных и до записи файла: сообщение «нет python-docx»
    полезнее, чем ImportError из середины сборки.
    """
    try:
        import docx  # noqa: F401
    except ImportError:
        raise SystemExit(
            "[!] Не установлена библиотека python-docx — собрать документ нечем.\n"
            "    Навык объявляет её зависимостью (python-docx>=1.1): проверьте, что\n"
            "    окружение навыка собрано после установки/ревью. Вручную: pip install python-docx")


def default_base() -> pathlib.Path:
    """Каталог, куда разрешено писать.

    По умолчанию — собственный каталог состояния навыка: скрипт не должен
    иметь возможности писать за пределы своей песочницы. Рабочий каталог
    задачи используется, только если он задан явно через OUROBOROS_TASK_DRIVE.
    Готовый файл агент отдаёт владельцу через send_file — тому всё равно,
    из какого каталога читать.
    """
    state = os.environ.get("OUROBOROS_SKILL_STATE_DIR")
    if state:
        return pathlib.Path(state)
    drive = os.environ.get("OUROBOROS_TASK_DRIVE")
    if drive:
        return pathlib.Path(drive)
    return pathlib.Path.cwd()


def safe_out_path(raw: str, base: pathlib.Path) -> pathlib.Path:
    """Не даём записать файл куда угодно.

    Путь приходит аргументом командной строки, а значит в конечном счёте от
    модели. Без ограничения досье можно было бы записать поверх настроек или
    другого навыка. Разрешаем только внутрь base — см. default_base().
    """
    candidate = pathlib.Path(raw).expanduser()
    if not candidate.is_absolute():
        candidate = base / candidate
    candidate = candidate.resolve()
    base = base.resolve()
    # Строго ВНУТРЬ base. Оговорки «или сам base» здесь быть не должно: base —
    # это каталог, писать в него как в файл незачем, а лазейку закрывала только
    # проверка расширения ниже.
    if base not in candidate.parents:
        raise SystemExit(
            f"[!] Путь вне рабочего каталога: {candidate}\n"
            f"    Разрешено писать только внутрь {base}\n"
            f"    Уберите ../ и абсолютные пути из имени файла.")
    if candidate.suffix.lower() != ".docx":
        raise SystemExit(f"[!] Ожидается имя файла .docx, получено: {candidate.name}")
    return candidate


def allowed_roots() -> list[pathlib.Path]:
    """Каталоги, внутри которых скрипту разрешено что-либо ПЕРЕЗАПИСЫВАТЬ."""
    roots = []
    for env in ("OUROBOROS_SKILL_STATE_DIR", "OUROBOROS_TASK_DRIVE"):
        v = os.environ.get(env)
        if v:
            roots.append(pathlib.Path(v).resolve())
    if not roots:
        roots.append(pathlib.Path.cwd().resolve())
    return roots


def resolve_input(raw: str) -> tuple[pathlib.Path | None, list[str]]:
    """Найти JSON досье. Возвращает (путь или None, где искали).

    Агент часто передаёт голое имя «dossier.json», а текущий каталог скрипта —
    не каталог задачи. Вместо отказа ищем по тем же местам, куда агент мог
    сохранить файл, и при неудаче честно перечисляем, где искали: угадывание
    пути в прошлых прогонах стоило по пятнадцать минут.
    """
    p = pathlib.Path(raw).expanduser()
    tried = []
    candidates = [p]
    if not p.is_absolute():
        for env in ("OUROBOROS_TASK_DRIVE", "OUROBOROS_SKILL_STATE_DIR"):
            v = os.environ.get(env)
            if v:
                candidates.append(pathlib.Path(v) / p)
    for c in candidates:
        tried.append(str(c))
        if c.is_file():
            return c, tried
    return None, tried


def build(data: dict, out_path: pathlib.Path) -> None:
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt, RGBColor

    doc = Document()

    # Оформление задаётся СТИЛЮ, а не абзацам: иначе таблицы и списки
    # останутся на шрифте по умолчанию, и документ поедет.
    normal = doc.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(12)
    # Для кириллицы одного font.name мало — Word берёт шрифт из отдельного
    # поля, и без этой строки текст выйдет другим шрифтом.
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
    normal.element.rPr.rFonts.set(qn("w:cs"), "Arial")
    pf = normal.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    pf.space_after = Pt(6)
    pf.space_before = Pt(0)

    for section in doc.sections:
        section.top_margin = section.bottom_margin = Cm(2)
        section.left_margin = section.right_margin = Cm(2)

    def style_heading(par, size, color=(0x1F, 0x3B, 0x4D)):
        for run in par.runs:
            run.font.name = "Arial"
            run.font.size = Pt(size)
            run.font.bold = True
            run.font.color.rgb = RGBColor(*color)
            run._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
        par.paragraph_format.space_before = Pt(8)
        par.paragraph_format.space_after = Pt(2)

    # --- Пометка о непроверенном досье ----------------------------------------
    # Непроверенное досье внешне неотличимо от проверенного, поэтому отличать
    # его должна первая строка самого документа, а не примечание в чате.
    if data.get("_unverified"):
        warn = doc.add_paragraph()
        r = warn.add_run("⚠️ Внешняя проверка фактов (триангуляция) НЕ проводилась. "
                         "Сведения не подтверждены независимыми источниками.")
        r.bold = True
        r.font.color.rgb = RGBColor(0xB0, 0x00, 0x20)

    # --- Шапка ---------------------------------------------------------------
    title = doc.add_paragraph(as_text(data.get("name")), style="Heading 1")
    style_heading(title, 16)

    role = doc.add_paragraph()
    run = role.add_run(as_text(data.get("last_known_role")))
    run.font.size = Pt(12)
    run.font.bold = True
    as_of = as_text(data.get("as_of"))
    if as_of:
        tail = role.add_run(f"  ·  по состоянию на {ru_dates(as_of)}")
        tail.font.size = Pt(11)
        tail.font.color.rgb = RGBColor(0x55, 0x5F, 0x6B)
    role.paragraph_format.space_after = Pt(8)

    # Блок полноты данных в документ НЕ идёт: агент считает якоря для себя,
    # чтобы решить, хватает ли материала, но руководителю служебная
    # арифметика не нужна — он открывает досье, чтобы узнать человека.

    # --- Разделы -------------------------------------------------------------
    gender = data.get("gender") or "m"
    for key, spec, _required, _limit in SECTIONS:
        if key in HIDDEN_IN_DOCX:
            continue
        section_title = heading(spec, gender)
        body = data.get(key)
        text = as_text(body)
        if not text:
            continue
        head = doc.add_paragraph(section_title, style="Heading 2")
        style_heading(head, 12)
        if isinstance(body, (list, tuple)):
            for item in body:
                item = str(item).strip()
                if not item:
                    continue
                par = doc.add_paragraph(style="List Bullet")
                add_rich_text(par, item)
                par.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
                par.paragraph_format.space_after = Pt(2)
                for run in par.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(12)
                    run._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), "Arial")
        else:
            for chunk in text.split("\n"):
                if chunk.strip():
                    add_rich_text(doc.add_paragraph(), chunk.strip())

    # --- Источники таблицей --------------------------------------------------
    srcs = data.get("sources") or []
    if srcs:
        head = doc.add_paragraph("Источники", style="Heading 2")
        style_heading(head, 12)
        tbl = doc.add_table(rows=1, cols=4)
        tbl.style = "Table Grid"
        for i, name in enumerate(("№", "Источник", "Дата", "Сила")):
            cell = tbl.rows[0].cells[i]
            cell.text = ""
            run = cell.paragraphs[0].add_run(name)
            run.font.name = "Arial"
            run.font.size = Pt(10)
            run.font.bold = True
            run._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
        for s in srcs:
            cells = tbl.add_row().cells
            values = (str(s.get("n") or ""), str(s.get("title") or ""),
                      str(s.get("date") or ""), str(s.get("strength") or ""))
            for i, value in enumerate(values):
                cells[i].text = ""
                par = cells[i].paragraphs[0]
                par.paragraph_format.space_after = Pt(0)
                if i == 1 and str(s.get("url") or "").startswith("http"):
                    add_hyperlink(par, value or s["url"], s["url"])
                else:
                    run = par.add_run(value)
                    run.font.name = "Arial"
                    run.font.size = Pt(10)
                    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")

    # --- Колонтитул ----------------------------------------------------------
    footer = doc.sections[0].footer.paragraphs[0]
    footer.text = (f"Досье: {as_text(data.get('name'))}  ·  подготовлено {as_text(data.get('prepared'))}"
                   + ("  ·  БЕЗ ТРИАНГУЛЯЦИИ" if data.get("_unverified") else ""))
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in footer.runs:
        run.font.name = "Arial"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0x77, 0x7F, 0x88)
        run._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")

    try:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        doc.save(str(out_path))
    except OSError as exc:
        raise SystemExit(
            f"[!] Не удалось записать файл {out_path}: {type(exc).__name__}: {exc}\n"
            f"    Проверьте, что рабочий каталог навыка доступен на запись и есть место на диске.")


_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")


def add_rich_text(paragraph, text: str) -> None:
    """Текст с разметкой **жирного**: пометка **[Анализ]** в Word должна быть
    жирной, а не звёздочками — звёздочки в документе выглядят как недоделка."""
    pos = 0
    for m in _BOLD_RE.finditer(text):
        if m.start() > pos:
            paragraph.add_run(text[pos:m.start()])
        paragraph.add_run(m.group(1)).bold = True
        pos = m.end()
    if pos < len(text):
        paragraph.add_run(text[pos:])


def add_hyperlink(paragraph, text, url):
    """Кликаемая ссылка. python-docx этого не умеет — собираем через XML."""
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn

    part = paragraph.part
    r_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    for tag, attrs in (("w:rFonts", {qn("w:ascii"): "Arial", qn("w:hAnsi"): "Arial",
                                     qn("w:eastAsia"): "Arial"}),
                       ("w:sz", {qn("w:val"): "20"}),
                       ("w:color", {qn("w:val"): "1155CC"}),
                       ("w:u", {qn("w:val"): "single"})):
        el = OxmlElement(tag)
        for k, v in attrs.items():
            el.set(k, v)
        rPr.append(el)
    run.append(rPr)
    t = OxmlElement("w:t")
    t.text = text
    run.append(t)
    link.append(run)
    paragraph._p.append(link)


# Порядок сокращения не выдуман здесь — он опубликован в SKILL.md как правило:
# «Анализ» -> «Культурный контекст» -> примеры в «Чем известен». Раз это
# правило, его можно исполнять детерминированно, а не просить модель следовать
# ему прозой. Одинаковый вход даёт одинаковый выход на любой модели.
#
# Три раздела не трогаются никогда: полнота данных, «Не подтверждено» и
# «Источники». Это то, ради чего досье вообще читают, и именно там живёт
# граница между проверенным и непроверенным.
TRIM_ORDER = [
    ("analysis", 0),      # вывод, а не факт — уходит первым, можно до нуля
    ("culture", 0),       # необязательный раздел
    ("known_for", 3),     # примеры; меньше трёх не оставляем
    ("topics", 3),
]
TRIM_PROTECTED = ("completeness", "unconfirmed", "sources")


def _section_limit(key: str, data: dict) -> int:
    """Лимит раздела с учётом расширения «Тем» при заданном контексте встречи."""
    return limits_for(data).get(key, 0)


def _measure_section(key: str, data: dict) -> int:
    return len(as_text(data.get(key)))


def fit_to_budget(data: dict) -> tuple[bool, list[str]]:
    """Срезать документ под бюджет по правилу. Возвращает (влезло, что убрано).

    Режем только целыми элементами списков и только необязательные разделы:
    обрывать биографию на полуслове хуже, чем отказать. Прозаические разделы
    сверх лимита остаются на совести автора — им скрипт называет цель.

    Два условия остановки, и оба нужны: общий бюджет и собственный лимит
    раздела. Без второго --fit укладывался в сумму, оставляя «Чем известен»
    вдвое сверх нормы, и следующий же --check отказывал по нему — то есть
    круг сокращения не заканчивался, а только менял повод.
    """
    removed: list[str] = []
    budget = budget_for(data)
    target = target_for(budget)

    def total() -> int:
        return measure(data)[0]

    def over(key: str) -> bool:
        limit = _section_limit(key, data)
        return bool(limit) and _measure_section(key, data) > target_for(limit)

    for key, floor in TRIM_ORDER:
        while total() > target or over(key):
            value = data.get(key)
            if isinstance(value, list):
                if len(value) <= floor:
                    break
                dropped = value.pop()
                removed.append(f"{key}\u0000убран пункт — {str(dropped)[:70]}…")
            elif isinstance(value, str) and value.strip():
                if floor:
                    break
                removed.append(f"{key}\u0000раздел убран целиком ({len(value)} знаков)")
                data[key] = ""
            else:
                break
    return total() <= budget, removed


def run_fit(src: pathlib.Path, data: dict) -> int:
    """Режим --fit: сократить под бюджет, переписать файл, отчитаться вслух."""
    before = measure(data)[0]
    budget = budget_for(data)
    # Сокращать нужно не только при превышении общего бюджета, но и когда
    # сокращаемый раздел вышел за свой лимит: иначе --check отказывает по
    # разделу, а --fit отвечает «сокращать нечего», и круг не размыкается.
    over_sections = [key for key, _floor in TRIM_ORDER
                     if _section_limit(key, data)
                     and _measure_section(key, data) > _section_limit(key, data)]
    if before <= budget and not over_sections:
        print(f"Сокращать нечего: {before} знаков из {budget}, лимиты разделов соблюдены.")
        return 0

    ok, removed = fit_to_budget(data)
    after = measure(data)[0]

    print(f"Было {before} знаков, стало {after} (бюджет {budget}).")
    if removed:
        print("\nУбрано — по правилу «Анализ» -> «Культурный контекст» -> примеры:")
        for line in removed:
            key, _, what = line.partition("\u0000")
            print(f"  − «{key}»: {what}")
    else:
        print("\nУбирать оказалось нечего: необязательные разделы уже пусты.")

    # Молчаливое усечение здесь недопустимо. Владелец должен увидеть, что из
    # досье что-то вынули, — иначе документ выглядит полным, каким не является.
    touched: list[str] = []
    for line in removed:
        key = line.partition("\u0000")[0]
        if key not in touched:
            touched.append(key)
    note = ("Часть необязательных разделов сокращена, чтобы уложиться в объём: "
            + ", ".join(touched) + ".")
    if removed:
        unconf = data.get("unconfirmed")
        if isinstance(unconf, list):
            unconf.append(note)
        elif isinstance(unconf, str):
            data["unconfirmed"] = (unconf + " " + note).strip()

    # Переписываем исходный файл, только если он лежит в разрешённом каталоге
    # (каталог навыка или задачи). Иначе — пишем копию в рабочий каталог:
    # путь пришёл от модели, и перезаписывать произвольный файл нельзя.
    resolved = src.resolve()
    if any(root == resolved.parent or root in resolved.parents for root in allowed_roots()):
        dest = resolved
    else:
        dest = default_base().resolve() / resolved.name
        dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")
    if dest == resolved:
        print(f"\nФайл переписан: {dest}")
    else:
        print(f"\nИсходный файл вне рабочего каталога — сокращённая версия записана сюда:\n  {dest}")
        print("  Дальше работайте с этим путём (--check, verify_facts, сборка).")

    still_over = [key for key, _floor in TRIM_ORDER
                  if _section_limit(key, data)
                  and _measure_section(key, data) > _section_limit(key, data)]
    if still_over:
        print("\nВнимание: разделы всё ещё сверх лимита (дальше резать нельзя — "
              "дошли до минимума пунктов): " + ", ".join(still_over)
              + ". Сократите формулировки сами; цель назовёт --check.")
        ok = False
    if not ok:
        print("\nНЕ ГОДИТСЯ: под бюджет не уложились даже после сокращения.")
        print("Дальше резать нельзя — остались только защищённые разделы")
        print("(полнота данных, «Не подтверждено», «Источники»).")
        print("Сократите прозу обязательных разделов: скрипт назовёт цель в --check.")
        return 1
    # После сокращения — полная проверка того, что получилось: объём сошёлся,
    # но числа, обязательные поля и лимиты прозы проверяются заново, чтобы
    # «ГОДНО по объёму» не выдавалось за готовность к сборке.
    rest = validate(data)
    if rest:
        print("\nОбъём сошёлся, но досье ещё НЕ ГОДИТСЯ:")
        for p in rest:
            print(f"  [!] {p}")
        return 1
    print("\nГОДНО: объём сошёлся, остальные проверки пройдены. Можно рендерить.")
    return 0


def main() -> int:
    args = [a for a in sys.argv[1:]]
    if "--schema" in args:
        print(json.dumps(schema_with_limits(), ensure_ascii=False, indent=2))
        return 0

    # Зависимость проверяется ДО всего остального: сообщение «нет python-docx»
    # полезнее, чем ImportError из середины сборки, когда данные уже собраны.
    if "--check" not in args and "--fit" not in args:
        require_docx()

    check_only = "--check" in args
    fit_only = "--fit" in args
    unverified = "--unverified" in args
    args = [a for a in args if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 64

    src, tried = resolve_input(args[0])
    if src is None:
        print(f"[!] нет файла {args[0]}. Искал:")
        for t in tried:
            print(f"    {t}")
        print("    Передайте АБСОЛЮТНЫЙ путь к dossier.json в каталоге задачи.")
        return 1
    try:
        data = json.loads(src.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"[!] JSON не разбирается: {exc}")
        return 1

    if fit_only:
        return run_fit(src, data)

    total, rows = measure(data)
    problems = validate(data)

    budget = budget_for(data)
    pages = budget // CHARS_PER_PAGE
    ctx = " (задан контекст встречи — «Темы» расширены)" if as_text(data.get("meeting_context")) else ""
    print(f"Объём: {total} знаков из {budget} "
          f"(≈{total / CHARS_PER_PAGE:.1f} страницы из {pages}){ctx}")
    for title, n, limit in rows:
        if n:
            mark = "  превышен" if n > limit else ""
            print(f"  {title:<24} {n:>5} / {limit}{mark}")

    if problems:
        print()
        print("НЕ ГОДИТСЯ:")
        for p in problems:
            print(f"  [!] {p}")
        print()
        print("Сокращать в порядке: «Анализ» → «Культурный контекст» → примеры")
        print("в «Чем известен». НЕ сокращать: полноту данных, «Не подтверждено»,")
        print("«Источники».")
        return 1

    if check_only:
        print("\nГОДНО: можно рендерить.")
        about, _total = search_evidence(data)
        if not about:
            print("[i] В журнале search.py нет запросов про этого человека — сборка откажет.")
            print("    Сначала соберите материал через search.py (Sonar).")
        return 0

    base = default_base()
    raw_out = args[1] if len(args) > 1 else str(src.with_suffix(".docx").name)
    out = safe_out_path(raw_out, base)
    # Предварительная проверка: каталог доступен на запись — до того, как
    # собирать документ, а не после.
    try:
        base.mkdir(parents=True, exist_ok=True)
        probe = base / ".write_probe"
        probe.write_text("ok", encoding="utf-8")
        probe.unlink()
    except OSError as exc:
        print(f"[!] Рабочий каталог {base} недоступен на запись: {type(exc).__name__}: {exc}")
        return 1
    # Сборка без триангуляции невозможна: скрипт сам сверяется с тем, что
    # подтвердил verify_facts.py. В живом прогоне ключа не было, проверка шла
    # только в --dry-run, а досье ушло владельцу как обычное — с пометкой в
    # самом конце ответа. Теперь такой путь только явный и с пометкой в файле.
    gaps = triangulation_gaps(data)
    if gaps and not unverified:
        print("\nНЕ ГОДИТСЯ: триангуляция не пройдена — verify_facts.py не подтвердил:")
        for g in gaps[:15]:
            print(f"  [!] {g}")
        if len(gaps) > 15:
            print(f"  … и ещё {len(gaps) - 15}")
        print("\nЗапустите verify_facts.py БЕЗ --dry-run и добейтесь «ГОДНО».")
        print("Если триангуляция невозможна (нет ключа, сбой сети) — собирайте с флагом")
        print("--unverified: документ получит пометку, а ответ в чат ОБЯЗАН начинаться строкой")
        print("«⚠️ Триангуляция НЕ отработала: <причина>. Досье через внешние источники НЕ проверено.»")
        return 1
    if gaps and unverified:
        # --unverified — только после НАСТОЯЩЕГО сбоя триангуляции. В прогоне
        # агент сам решил «ключа нет», не запустив verify_facts.py ни разу, хотя
        # ключ был и Sonar работал. Теперь флаг требует свежую запись о сбое.
        why = unverified_allowed()
        if why is None:
            print("\nНЕ ГОДИТСЯ: --unverified разрешён только после реального сбоя триангуляции.")
            print("Сначала запустите verify_facts.py БЕЗ --dry-run. Если он подтвердит факты —")
            print("соберите без флага. Если откажет из-за неподтверждённых утверждений —")
            print("исправьте досье. Флаг допустим, только если скрипт упал из-за ключа или сети.")
            return 1
        print(f"\nТриангуляция невозможна: {why}. Собираю с пометкой «БЕЗ ТРИАНГУЛЯЦИИ».")
        data["_unverified"] = True
        data["_unverified_why"] = why

    # Поиск через Sonar — обязателен, если Sonar вообще доступен.
    about, total = search_evidence(data)
    if not about:
        if data.get("_unverified"):
            print("[i] Запросов search.py про этого человека нет — Sonar недоступен по той же причине.")
        else:
            print("\nНЕ ГОДИТСЯ: материал собран не через search.py (Perplexity Sonar).")
            print(f"  В журнале поиска за {SEARCH_WINDOW_HOURS} ч нет ни одного успешного запроса "
                  f"про «{as_text(data.get('name'))}» (всего успешных запросов: {total}).")
            print("  Встроенный поиск агента — только добор. Сделайте волну запросов:")
            print('  skill_exec(skill="dossier", script="search.py", args=["<Имя Фамилия> биография", ...])')
            print("  и дополните досье найденным. В запросах пишите имя человека — по нему")
            print("  сборка узнаёт, что поиск был про него (кириллица и латиница равноценны).")
            return 1
    else:
        print(f"Поиск через Sonar: {about} запрос(ов) про этого человека в журнале.")

    build(data, out)
    size = out.stat().st_size
    print(f"\nГотово: {out}  ({size:,} байт)")
    ver = skill_version()
    print("\nДальше, обязательно, одним ходом:")
    print("  1. send_file этого файла.")
    print("  2. В чат — ТЕКСТ НИЖЕ КАК ЕСТЬ, от первой до последней строки. Замените только")
    print("     <МОДЕЛЬ> на модель, которая отвечала. Ничего не добавляйте и не пересказывайте:")
    print("     в чате не должно быть сведений, которых нет в документе.")
    print("\n===== ТЕКСТ ДЛЯ ЧАТА =====")
    print(chat_text(data, ver, str(data.get("_unverified_why") or "") if data.get("_unverified") else ""))
    print("===== КОНЕЦ ТЕКСТА =====")
    return 0


if __name__ == "__main__":
    sys.exit(main())

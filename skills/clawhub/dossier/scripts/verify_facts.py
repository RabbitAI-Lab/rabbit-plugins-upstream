#!/usr/bin/env python3
"""Триангуляция фактов досье через Sonar — ДО сборки документа.

Зачем отдельный шаг, а не проверка при вёрстке. Проверка чисел в
`render_dossier.py` стоит на выходе: она ловит число без доказательства, но
доказательством считает то, что модель сама же и записала. И главное —
текст в чат владелец получает из того же JSON, а не из документа. Значит,
непроверенное утверждение доходит до человека раньше, чем что-либо
успевает отказать.

Здесь проверка идёт наружу, к настоящим источникам, и до того, как
владелец что-либо увидит. Семь раз отмерь: волны поиска → кросс-проверка
подагентами по инструкции → ЭТОТ скрипт → и только потом вёрстка.

Что делает:

  1. Собирает утверждения — ВСЕ числа из `figures` и ВСЕ фактические фразы
     со ссылкой на источник из «Кто он», «Чем известен», должности.
     Предела нет: проверяется каждое. Обращения идут в восемь потоков,
     поэтому семнадцать утверждений занимают шестнадцать секунд, а не две
     минуты, и ограничивать их число не приходится.
  2. По каждому идёт в Sonar с САМИМ утверждением, а не с именем человека.
  3. Считает домены, которые НА САМОМ ДЕЛЕ подтверждают: в сниппете есть
     само число (для величин) или минимум два значимых слова утверждения
     (для фактов). Подтверждение — совпадение в двух РАЗНЫХ доменах.
     Просто присутствие домена в выдаче не считается: на утверждение про
     диплом приходило 15 доменов, включая книжный магазин и Газпром.
  3a. Для чисел вдобавок открывается САМА цитируемая страница и число
     ищется на ней. Поиск по интернету атрибуцию не устанавливает.
  4. Утверждения, опирающиеся только на первоисточник, который по природе
     уникален — LinkedIn, GitHub, arXiv, Google Scholar, ORCID, — кросс-
     проверку не проходят: требовать второй источник для того, что
     существует в одном месте, значит запретить верный факт.

  verify_facts.py dossier.json                проверить ВСЕ утверждения
  verify_facts.py dossier.json --dry-run      показать план без обращений к сети
  verify_facts.py dossier.json --fresh        проверить заново, не используя кэш
  verify_facts.py --explain                   как устроена проверка

Время. У скрипта жёсткий предел платформы (300 с). Проверка идёт с общим
дедлайном: всё, что не успело, помечается «НЕ ПРОВЕРЕНО (время)» — это
отказ, а не пропуск. Уже подтверждённое кэшируется в рабочем каталоге
навыка, поэтому повторный вызов с тем же файлом проверяет только остаток.

Настройки: PERPLEXITY_API_KEY (обязателен), DOSSIER_SONAR_MODEL (по
умолчанию «sonar»), DOSSIER_VERIFY_TIMEOUT_SEC (таймаут одного запроса,
по умолчанию 45), DOSSIER_VERIFY_DEADLINE_SEC (общий дедлайн, по
умолчанию 240).

Код возврата 1 — есть неподтверждённые утверждения. Это отказ, а не
предупреждение: досье уносят на встречу, и там цена ошибки выше цены
задержки.
"""
from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.dont_write_bytecode = True  # каталог навыка может быть только для чтения

# Источники, уникальные по своей природе: карьерный трек человека, его
# репозитории, его препринты, его публикации. Второго независимого
# подтверждения у них не бывает и быть не может — требовать его значит
# выбрасывать верные факты. Профиль первого лица здесь и есть первоисточник.
PRIMARY_ONLY_DOMAINS = {
    "linkedin.com", "github.com", "arxiv.org", "scholar.google.com",
    "orcid.org", "researchgate.net", "gitlab.com", "huggingface.co",
    "elibrary.ru", "istina.msu.ru",
}

# Разделы, из которых берутся фактические утверждения. «Анализ» не берём
# намеренно: это помеченный вывод, а не факт, и проверять его как факт —
# смешивать то, что инструкция велит разделять.
CLAIM_SECTIONS = ("last_known_role", "who", "known_for")

CITE_RE = re.compile(r"\[(\d+)\]")
SENT_SPLIT = re.compile(r"(?<=[.!?;])\s+|\n+")
SONAR_URL = "https://api.perplexity.ai/chat/completions"

# Предела нет и быть не должно: проверяется КАЖДОЕ утверждение. Сначала
# стоял срез на 15 — он молча отсекал хвост, и агент отчитывался «все 15
# подтверждены» при 17 в досье. Потом отказ выше тридцати — но отказ вместо
# проверки это та же непроверенная выдача, только с другой стороны.
#
# Единственная настоящая причина, по которой хотелось ограничить, — время:
# обращения к Sonar шли по очереди, и 17 утверждений съедали две минуты из
# трёх отпущенных скрипту. Правильный ответ на нехватку времени — считать
# параллельно, а не отказываться считать. Восьми потоков хватает на сотню
# утверждений внутри лимита.
VERIFY_WORKERS = 8

# Общий дедлайн проверки. Платформа убивает скрипт на 300 секундах, и убитый
# скрипт не печатает ничего — агент видит обрыв и не знает, что проверено.
# Поэтому свой дедлайн раньше платформенного: не успели — честно говорим,
# что именно не проверено, и кэшируем подтверждённое для повторного вызова.
DEFAULT_DEADLINE_SEC = 240.0
DEFAULT_REQUEST_TIMEOUT_SEC = 45.0
_DEADLINE_AT = [time.time() + DEFAULT_DEADLINE_SEC]


def time_left() -> float:
    return _DEADLINE_AT[0] - time.time()


def env_first(*names: str, default: str = "") -> str:
    for n in names:
        v = (os.environ.get(n) or "").strip()
        if v:
            return v
    return default


def work_dir() -> pathlib.Path:
    """Куда разрешено писать кэш: каталог навыка, иначе задачи, иначе текущий."""
    for env in ("OUROBOROS_SKILL_STATE_DIR", "OUROBOROS_TASK_DRIVE"):
        v = os.environ.get(env)
        if v:
            return pathlib.Path(v)
    return pathlib.Path.cwd()


def resolve_input(raw: str) -> tuple:
    """Найти JSON досье: как передан, затем в каталоге задачи и навыка."""
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


CACHE_NAME = "verify_cache.json"


def claim_key(claim: dict, srcmap: dict) -> str:
    """Ключ кэша: текст утверждения + адреса его источников.

    Поменялся текст или ссылка — это другое утверждение, и оно проверяется
    заново. Кэшируется только подтверждённое: отказ всегда перепроверяется.
    """
    urls = [str((srcmap.get(str(n)) or {}).get("url") or "") for n in claim.get("sources") or []]
    raw = json.dumps([claim.get("kind"), claim.get("text"), claim.get("value"), urls],
                     ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:32]


def load_cache() -> dict:
    try:
        data = json.loads((work_dir() / CACHE_NAME).read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:  # noqa: BLE001
        return {}


STATUS_NAME = "verify_status.json"


def write_status(status: str, detail: str, src=None) -> None:
    """Итог последнего запуска — для render_dossier.py.

    Флаг --unverified разрешён только после настоящего сбоя триангуляции
    (нет ключа, отказ по ключу, сеть). Иначе агент мог решить «ключа нет»,
    не запуская проверку, и собрать досье без неё — так и было в прогоне.
    """
    try:
        d = work_dir()
        d.mkdir(parents=True, exist_ok=True)
        (d / STATUS_NAME).write_text(json.dumps({
            "status": status, "detail": detail, "ts": time.time(),
            "file": str(src) if src else "",
        }, ensure_ascii=False), encoding="utf-8")
    except OSError:
        pass


def save_cache(cache: dict) -> None:
    try:
        d = work_dir()
        d.mkdir(parents=True, exist_ok=True)
        tmp = d / (CACHE_NAME + ".tmp")
        tmp.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
        os.replace(tmp, d / CACHE_NAME)
    except Exception as exc:  # noqa: BLE001
        print(f"  (кэш не записан: {type(exc).__name__}: {str(exc)[:80]})")

# Слово короче этого в сравнении не участвует: «года», «был», «для» есть
# в любом тексте и подтверждают что угодно.
MIN_TOKEN_LEN = 5
STOPWORDS = {
    "который", "которая", "которые", "также", "более", "менее", "после",
    "перед", "между", "около", "самым", "своей", "своих", "этого", "этой",
}


def as_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return "\n".join(str(v).strip() for v in value if str(v).strip())
    return str(value).strip()


def registrable_domain(url: str) -> str:
    """Домен без www и поддоменов: два последних ярлыка.

    Грубо, но для счёта независимости достаточно: example.ru и press.example.ru —
    один источник, а не два. Тонкости вроде co.uk здесь не важны: они дают
    ошибку в сторону строгости, а не наоборот.
    """
    try:
        host = urllib.parse.urlparse(url).netloc.lower().split(":")[0]
    except Exception:  # noqa: BLE001
        return ""
    host = host[4:] if host.startswith("www.") else host
    parts = [p for p in host.split(".") if p]
    if len(parts) >= 3 and parts[-2] in {"co", "com", "gov", "org", "ac", "edu"}:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:]) if len(parts) >= 2 else host


def sources_by_number(data: dict) -> dict[str, dict]:
    out = {}
    for s in data.get("sources") or []:
        if isinstance(s, dict) and s.get("n") is not None:
            out[str(s["n"])] = s
    return out


def collect_claims(data: dict) -> list[dict]:
    """Числа из figures и фактические фразы со ссылкой — в один список."""
    claims: list[dict] = []
    seen: set[str] = set()
    person = as_text(data.get("name"))

    for fig in data.get("figures") or []:
        if not isinstance(fig, dict):
            continue
        value = str(fig.get("value") or "").strip()
        if not value:
            continue
        quote = str(fig.get("quote") or "").strip()
        derived = str(fig.get("derived_from") or "").strip()
        if derived and not quote:
            # Выведенное число проверять внешним поиском нечего: оно и не
            # утверждается как прочитанное. Его страхует пометка «около».
            continue
        text = f"{person}: {quote or value}" if person else (quote or value)
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)
        claims.append({
            "kind": "число",
            "text": text,
            "value": value,
            "sources": [str(fig.get("source"))] if fig.get("source") else [],
        })

    for section in CLAIM_SECTIONS:
        for sentence in SENT_SPLIT.split(as_text(data.get(section))):
            sentence = sentence.strip(" -•\t")
            refs = CITE_RE.findall(sentence)
            if not refs or len(sentence) < 25:
                continue
            bare = CITE_RE.sub("", sentence).strip()
            key = bare.lower()
            if key in seen:
                continue
            seen.add(key)
            claims.append({
                "kind": "факт",
                "text": f"{person}: {bare}" if person else bare,
                "value": "",
                "sources": refs,
            })
    return claims


def primary_only(claim: dict, srcmap: dict[str, dict]) -> str:
    """Если утверждение опирается ТОЛЬКО на уникальный первоисточник — его имя."""
    doms = []
    for n in claim.get("sources") or []:
        url = str((srcmap.get(str(n)) or {}).get("url") or "")
        dom = registrable_domain(url)
        if not dom:
            return ""
        doms.append(dom)
    if not doms:
        return ""
    if all(d in PRIMARY_ONLY_DOMAINS for d in doms):
        return ", ".join(sorted(set(doms)))
    return ""


def numeric_core(value: str) -> str:
    """Числовое ядро величины: «1 млн+» → «1 млн», «около 47 лет» → «47»."""
    v = str(value or "").lower().replace(" ", " ")
    # Десятичная запятая — не разделитель: «79,1 млн» → «79.1 млн», иначе
    # ниже она превратилась бы в пробел и число «79 1» не нашлось бы нигде.
    v = re.sub(r"(\d),(\d{1,2})(?!\d)", r"\1.\2", v)
    m = re.search(r"\d[\d\s.,]*\s*(?:трлн|млн|млрд|тыс\w*|%|миллион\w*|миллиард\w*|триллион\w*)?", v)
    if not m:
        return ""
    core = re.sub(r"[\s,]+", " ", m.group(0)).strip(" .")
    return core


# --- Одно число в разных языках --------------------------------------------------
# Досье пишется по-русски, а источники чаще английские: «$10 млрд» в тексте и
# «$10 billion» на странице — одна величина. Прежняя проверка сравнивала
# строки, и в живом прогоне агент потратил два десятка ходов, подгоняя
# цитаты. Теперь числа сравниваются как числа: значение × шкала, проценты
# отдельно. Совпадение точное — «$3 трлн» не подтверждается «$3.1 trillion».
_SCALE_WORDS = [
    (r"трлн|триллион\w*|trillion\w*|tn(?![a-z])", 10**12),
    (r"млрд|миллиард\w*|billion\w*|bn(?![a-z])", 10**9),
    (r"млн|миллион\w*|million\w*|mln(?![a-z])|mn(?![a-z])", 10**6),
    (r"тыс\.?|тысяч\w*|thousand\w*", 10**3),
]
_SCALE_LETTER = {"t": 10**12, "b": 10**9, "m": 10**6, "k": 10**3}
_AMOUNT_RE = re.compile(
    r"(?<![\d.,])(\d{1,3}(?:[   ']\d{3})+(?:[.,]\d+)?|\d+(?:[.,]\d+)*)"
    r"(?:\s*(%|percent\b|per cent\b|процент\w*|" + "|".join(p for p, _ in _SCALE_WORDS) + r")"
    r"|([tbmkTBMK])(?![A-Za-zА-Яа-я]))?",
    re.I)


def _parse_number(raw: str):
    s = re.sub(r"[   ']", "", raw)
    if "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s:
        s = s.replace(",", "") if re.fullmatch(r"\d{1,3}(,\d{3})+", s) else s.replace(",", ".")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return None


def amounts(text: str) -> list:
    """Все величины в тексте как (число с учётом шкалы, это_процент)."""
    out = []
    for m in _AMOUNT_RE.finditer(str(text or "")):
        num = _parse_number(m.group(1))
        if num is None:
            continue
        word = (m.group(2) or "").lower()
        letter = (m.group(3) or "").lower()
        pct = word.startswith(("%", "percent", "per cent", "процент"))
        mult = _SCALE_LETTER.get(letter, 1)
        for pat, factor in _SCALE_WORDS:
            if word and re.fullmatch(pat, word):
                mult = factor
                break
        out.append((num * mult, pct))
    return out


def figure_in_text(value: str, text: str) -> bool:
    """Есть ли величина из value в тексте — независимо от языка и записи."""
    wanted = amounts(value)
    if not wanted:
        return False
    have = amounts(text)
    for num, pct in wanted:
        if not any(p == pct and abs(n - num) <= max(abs(num), 1) * 1e-9 for n, p in have):
            return False
    return True


def literal_present(core: str, haystack: str) -> bool:
    """Стоит ли число в тексте доказательства ДОСЛОВНО.

    Проверка нарочно тупая и не зависит от суждения модели. Именно она даёт
    гарантию: Sonar может назвать фразу подтверждённой, проглотив цифру, —
    здесь цифра либо есть в источниках, либо её нет.
    """
    if not core:
        return False
    hay = re.sub(r"[\s, ]+", " ", str(haystack or "").lower())
    if core in hay:
        return True
    if figure_in_text(core, haystack):
        return True
    # «1 млн» и «1 000 000» — одно и то же число, записанное по-разному.
    m = re.match(r"^(\d+(?:\.\d+)?)\s*(млн|млрд|тыс\w*|миллион\w*|миллиард\w*)?$", core)
    if not m:
        return False
    num, scale = m.group(1), (m.group(2) or "")
    mult = {"млн": 10**6, "миллион": 10**6, "млрд": 10**9, "миллиард": 10**9, "тыс": 10**3}
    factor = next((v for k, v in mult.items() if scale.startswith(k)), 1)
    try:
        full = int(float(num) * factor)
    except (TypeError, ValueError):
        return False
    if factor == 1:
        return False
    plain = str(full)
    grouped = f"{full:,}".replace(",", " ")
    return plain in hay.replace(" ", "") or grouped in hay


_TAG_RE = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.I | re.S)
_ANY_TAG = re.compile(r"<[^>]+>")


def fetch_source_text(url: str, timeout: float = 20.0) -> tuple[str, str]:
    """Текст страницы источника. Возвращает (текст, причина отказа)."""
    timeout = min(timeout, time_left())
    if timeout < 3:
        return "", "не хватило времени до дедлайна"
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36",
            "Accept-Language": "ru,en;q=0.8",
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read(1_500_000)
        html = raw.decode("utf-8", "replace")
    except Exception as exc:  # noqa: BLE001
        return "", f"{type(exc).__name__}: {str(exc)[:90]}"
    text = _ANY_TAG.sub(" ", _TAG_RE.sub(" ", html))
    return re.sub(r"\s+", " ", text), ""


def check_cited_source(claim: dict, srcmap: dict[str, dict]) -> tuple[str, str]:
    """Стоит ли число в САМОМ источнике, на который ссылается досье.

    Самый сильный слой проверки и единственный, который устанавливает
    атрибуцию. Поиск по интернету её не устанавливает: «1 млн» встречается в
    статьях про популярные инвестиционные сервисы, и триангуляция по этому совпадению дважды из
    пяти признавала выдумку подтверждённой. Вопрос не «есть ли такое число
    где-нибудь», а «есть ли оно ТАМ, куда поставлена ссылка».

    Возвращает (вердикт, пояснение): ЕСТЬ / НЕТ / НЕ ПРОВЕРИТЬ.
    """
    core = numeric_core(claim.get("value") or "")
    if not core:
        return "НЕ ПРОВЕРИТЬ", "величину не разобрать"
    urls = [str((srcmap.get(str(n)) or {}).get("url") or "") for n in claim.get("sources") or []]
    urls = [u for u in urls if u.startswith("http")]
    if not urls:
        return "НЕ ПРОВЕРИТЬ", "у источника нет адреса"
    reasons = []
    # Первые две ссылки, а не все: утверждение обычно опирается на один-два
    # источника, а каждая загрузка страницы — это секунды. Проверять пятую
    # ссылку смысла мало, а общий бюджет скрипта она съедает заметно.
    for url in urls[:2]:
        text, err = fetch_source_text(url)
        if err:
            reasons.append(f"{registrable_domain(url)}: {err}")
            continue
        if literal_present(core, text):
            return "ЕСТЬ", f"число найдено на {registrable_domain(url)}"
        reasons.append(f"{registrable_domain(url)}: числа на странице нет")
    if all("числа на странице нет" in r for r in reasons) and reasons:
        return "НЕТ", "; ".join(reasons)
    return "НЕ ПРОВЕРИТЬ", "; ".join(reasons) or "страницу не открыть"


def significant_tokens(text: str) -> set[str]:
    """Слова, по которым можно узнать утверждение среди чужих текстов."""
    words = re.findall(r"[А-Яа-яЁёA-Za-z][А-Яа-яЁёA-Za-z-]+", str(text or "").lower())
    return {w for w in words if len(w) >= MIN_TOKEN_LEN and w not in STOPWORDS}


def supporting_domains(results: list, claim_text: str, figure: str) -> list[str]:
    """Домены, которые НА САМОМ ДЕЛЕ подтверждают утверждение.

    Раньше считались все домены из выдачи, и порог «не меньше двух» не
    проверял ничего: на утверждение про диплом приходило 15 доменов, среди
    которых книжный магазин, музей вычислительной техники и Газпром. Пятнадцать
    нерелевантных проходили порог так же, как два релевантных, и вся тяжесть
    решения ложилась на суждение модели.

    Теперь домен засчитывается, только если в его сниппете есть чем
    подтвердить: для числа — само число, для факта — минимум два значимых
    слова утверждения. Это и есть перекрёстная проверка: повторение в разных
    независимых источниках, а не совпадение в поисковой выдаче.
    """
    core = numeric_core(figure) if figure else ""
    tokens = significant_tokens(claim_text)
    good: dict[str, str] = {}
    for r in results:
        if not isinstance(r, dict):
            continue
        dom = registrable_domain(str(r.get("url") or ""))
        if not dom or dom in good:
            continue
        snippet = f"{r.get('title') or ''} {r.get('snippet') or ''}"
        if not snippet.strip():
            continue
        if core:
            if literal_present(core, snippet):
                good[dom] = "число в сниппете"
            continue
        hit = tokens & significant_tokens(snippet)
        if len(hit) >= 2:
            good[dom] = ", ".join(sorted(hit)[:3])
    return sorted(good)


def ask_sonar(claim_text: str, *, key: str, model: str, timeout: float,
              figure: str = "") -> dict:
    """Один проверочный вопрос к Sonar. Возвращает вердикт, домены и доказательства."""
    if figure:
        # Для числа спрашиваем ПРО ЧИСЛО, а не про смысл фразы. Разница
        # решающая: на вопрос «верно ли, что она отвечает за аналитику для
        # 1 млн+ частных инвесторов» Sonar дважды из трёх отвечал
        # «подтверждено» — он подтверждал аналитику, а величину проглатывал.
        prompt = (
            "Проверь ТОЛЬКО числовую величину в утверждении, не общий смысл. "
            "Если источники подтверждают суть, но НЕ называют именно это число — "
            "это НЕ ПОДТВЕРЖДЕНО. Ответь СТРОГО в формате:\n"
            "ВЕРДИКТ: ПОДТВЕРЖДЕНО | НЕ ПОДТВЕРЖДЕНО | ЧАСТИЧНО\n"
            "ПОЧЕМУ: одно предложение\n\n"
            f"Проверяемая величина: {figure}\n"
            f"Утверждение целиком: {claim_text}"
        )
    else:
        prompt = (
            "Проверь утверждение по открытым источникам. Ответь СТРОГО в формате:\n"
            "ВЕРДИКТ: ПОДТВЕРЖДЕНО | НЕ ПОДТВЕРЖДЕНО | ЧАСТИЧНО\n"
            "ПОЧЕМУ: одно предложение\n\n"
            f"Утверждение: {claim_text}"
        )
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Ты проверяешь факты. Отвечай на русском, кратко, только по источникам."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0,
    }
    last = ""
    for attempt in range(3):
        per_try = min(timeout, time_left())
        if per_try < 5:
            last = last or "не хватило времени до дедлайна"
            return {"verdict": "НЕ ПРОВЕРЕНО (время)", "why": last, "domains": [], "urls": [],
                    "evidence": ""}
        # Запрос создаётся заново на каждой попытке: тело уже отправленного
        # объекта прочитано, и повтор ушёл бы пустым.
        req = urllib.request.Request(
            SONAR_URL, data=json.dumps(body).encode(),
            headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=per_try) as resp:
                payload = json.load(resp)
            break
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "ignore")[:160]
            if exc.code in (401, 403):
                raise SystemExit(
                    f"[!] Sonar отказал по ключу (HTTP {exc.code}): {detail}\n"
                    f"    Проверьте PERPLEXITY_API_KEY. Без него триангуляция невозможна,\n"
                    f"    и собирать досье нельзя: непроверенные факты уйдут владельцу.")
            last = f"HTTP {exc.code}: {detail}"
        except Exception as exc:  # noqa: BLE001
            last = f"{type(exc).__name__}: {str(exc)[:120]}"
        if attempt < 2 and time_left() > 10:
            time.sleep(2)
    else:
        return {"verdict": "СБОЙ", "why": last, "domains": [], "urls": [], "evidence": ""}

    answer = str((payload.get("choices") or [{}])[0].get("message", {}).get("content") or "")
    results = payload.get("search_results") or []
    urls = [str(r.get("url") or "") for r in results if r.get("url")]
    for u in payload.get("citations") or []:
        if isinstance(u, str):
            urls.append(u)
        elif isinstance(u, dict) and u.get("url"):
            urls.append(str(u["url"]))
    domains = sorted({d for d in (registrable_domain(u) for u in urls) if d})
    # ВАЖНО: ответ модели в доказательства НЕ входит. Sonar пересказывает
    # проверяемое утверждение вместе с числом, и число начинает подтверждать
    # само себя: на выдуманном «1 млн+» так проходило два прогона из пяти.
    # Доказательство — только текст, пришедший из найденных источников.
    evidence = " ".join(
        [str(r.get("snippet") or "") for r in results]
        + [str(r.get("title") or "") for r in results]
    )

    upper = answer.upper()
    if "НЕ ПОДТВЕРЖДЕНО" in upper:
        verdict = "НЕ ПОДТВЕРЖДЕНО"
    elif "ЧАСТИЧНО" in upper:
        verdict = "ЧАСТИЧНО"
    elif "ПОДТВЕРЖДЕНО" in upper:
        verdict = "ПОДТВЕРЖДЕНО"
    else:
        verdict = "НЕЯСНО"
    why = ""
    m = re.search(r"ПОЧЕМУ:\s*(.+)", answer)
    if m:
        why = " ".join(m.group(1).split())[:160]
    return {"verdict": verdict, "why": why,
            "domains": supporting_domains(results, claim_text, figure),
            "all_domains": domains, "urls": urls[:6], "evidence": evidence}


MAX_ROWS_PRINTED = 150


def preflight_sonar(timeout: float = 8.0) -> str:
    """Дешёвая проверка, что API Sonar вообще достижим — до запуска потоков.

    Без неё сетевой сбой проявлялся восемью параллельными таймаутами по 45
    секунд. Любой HTTP-ответ (даже 401/404/405) означает, что сеть есть;
    ошибка соединения — что нет. Возвращает пустую строку или причину.
    """
    req = urllib.request.Request("https://api.perplexity.ai/", method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=timeout):
            return ""
    except urllib.error.HTTPError:
        return ""
    except Exception as exc:  # noqa: BLE001
        return f"{type(exc).__name__}: {str(exc)[:120]}"


def main() -> int:
    args = [a for a in sys.argv[1:]]
    if "--explain" in args:
        print(__doc__)
        return 0
    dry = "--dry-run" in args
    fresh = "--fresh" in args
    paths = [a for a in args if not a.startswith("--") and not a.isdigit()]
    if not paths:
        return _die("[!] Укажите файл досье: verify_facts.py <абсолютный путь>/dossier.json")
    src, tried = resolve_input(paths[0])
    if src is None:
        return _die(f"[!] Нет файла {paths[0]}. Искал:\n    " + "\n    ".join(tried)
                    + "\n    Передайте АБСОЛЮТНЫЙ путь к dossier.json в каталоге задачи.")
    try:
        data = json.loads(src.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return _die(f"[!] {src} — не JSON: {exc}")
    if not isinstance(data, dict):
        return _die(f"[!] {src}: ожидается JSON-объект досье (см. render_dossier.py --schema)")

    srcmap = sources_by_number(data)
    claims = collect_claims(data)
    if not claims:
        print("Проверять нечего: в досье нет ни чисел, ни фраз со ссылкой на источник.")
        print("Это само по себе подозрительно — досье без фактов не бывает.")
        print("\nНЕ ГОДИТСЯ: нечего проверять.")
        return 1

    print(f"Файл: {src}")
    print(f"Утверждений к проверке: {len(claims)}")
    print("Проверяется КАЖДОЕ. Предела нет, пропусков нет.")
    print()

    if dry:
        for i, c in enumerate(claims, 1):
            exempt = primary_only(c, srcmap)
            mark = f"первоисточник {exempt}" if exempt else "идёт в Sonar"
            print(f"  {i:2d}. [{c['kind']}] {c['text'][:96]}")
            print(f"      источники {c['sources'] or '—'} · {mark}")
        print("\nЭто план. Обращений к сети не было.")
        return 0

    key = (os.environ.get("PERPLEXITY_API_KEY") or "").strip()
    if not key:
        write_status("no_key", "PERPLEXITY_API_KEY не передан скрипту", src)
        return _die(
            "[!] PERPLEXITY_API_KEY не передан скрипту.\n"
            "    Навык объявляет его в env_from_settings; проверьте, что ключ есть в\n"
            "    настройках и владелец выдал доступ в карточке навыка. Без ключа\n"
            "    триангуляции нет, а без триангуляции досье собирать нельзя.")
    model = env_first("DOSSIER_SONAR_MODEL", "OUROBOROS_SONAR_MODEL", default="sonar")
    try:
        timeout = float(env_first("DOSSIER_VERIFY_TIMEOUT_SEC", "OUROBOROS_VERIFY_TIMEOUT_SEC",
                                  default=str(DEFAULT_REQUEST_TIMEOUT_SEC)))
        deadline = float(env_first("DOSSIER_VERIFY_DEADLINE_SEC", default=str(DEFAULT_DEADLINE_SEC)))
    except ValueError:
        timeout, deadline = DEFAULT_REQUEST_TIMEOUT_SEC, DEFAULT_DEADLINE_SEC
    # Дедлайн не может быть позже платформенного предела в 300 секунд.
    _DEADLINE_AT[0] = time.time() + max(30.0, min(deadline, 270.0))

    GOOD = ("ПОДТВЕРЖДЕНО", "ПЕРВОИСТОЧНИК", "ПОДТВЕРЖДЕНО (источник не открылся)")
    cache = {} if fresh else load_cache()

    reason = preflight_sonar()
    if reason:
        write_status("network", f"api.perplexity.ai недоступен: {reason}", src)
        return _die(
            f"[!] API Sonar (api.perplexity.ai) недоступен: {reason}\n"
            "    Проверить факты нечем — досье не отдаётся. Повторите позже или\n"
            "    проверьте сетевой доступ навыка (разрешение net).")

    def verify_one(claim: dict) -> tuple:
        """Проверка одного утверждения. Возвращает (статус, домены, пояснение)."""
        exempt = primary_only(claim, srcmap)
        if exempt:
            return "ПЕРВОИСТОЧНИК", [exempt], f"уникальный источник {exempt}"
        ck = claim_key(claim, srcmap)
        hit = cache.get(ck)
        if isinstance(hit, dict) and hit.get("status") in GOOD:
            return hit["status"], list(hit.get("domains") or []), "из кэша прошлой проверки"
        if time_left() < 8:
            return "НЕ ПРОВЕРЕНО (время)", [], "не хватило времени до дедлайна — повторите вызов"
        figure = claim.get("value") or ""
        res = ask_sonar(claim["text"], key=key, model=model, timeout=timeout, figure=figure)
        if res["verdict"] == "НЕ ПРОВЕРЕНО (время)":
            return res["verdict"], [], res["why"]
        doms = res["domains"]
        ok = res["verdict"] == "ПОДТВЕРЖДЕНО" and len(doms) >= 2
        status = "ПОДТВЕРЖДЕНО" if ok else res["verdict"]
        if res["verdict"] == "ПОДТВЕРЖДЕНО" and len(doms) < 2:
            # Ноль и один — разные факты, и называть их одинаково нечестно:
            # «один источник» при нуле подтверждений вводит в заблуждение
            # ровно там, где нужна точность.
            status = "ОДИН ИСТОЧНИК" if doms else "НЕТ ПОДТВЕРЖДЕНИЙ"
        # Вердикт модели — мнение, и оно гуляет: на выдуманном «1 млн+» Sonar
        # дважды из трёх отвечал «подтверждено», подтверждая суть фразы и
        # проглатывая величину. Поэтому для чисел последнее слово за тупой
        # сверкой с САМОЙ цитируемой страницей.
        if figure:
            cited, why_cited = check_cited_source(claim, srcmap)
            if cited == "НЕТ":
                return "ЧИСЛА НЕТ В ЦИТИРУЕМОМ ИСТОЧНИКЕ", doms, why_cited
            if cited == "НЕ ПРОВЕРИТЬ":
                core = numeric_core(figure)
                if core and not literal_present(core, res.get("evidence", "")):
                    return "ЧИСЛА НЕТ В НАЙДЕННЫХ ИСТОЧНИКАХ", doms, res["why"]
                if ok:
                    return "ПОДТВЕРЖДЕНО (источник не открылся)", doms, res["why"]
        return status, doms, res["why"]

    def safe_verify(claim: dict) -> tuple:
        # Ошибка в одном утверждении не должна ронять проверку остальных и
        # тем более выглядеть как «всё прошло».
        try:
            return verify_one(claim)
        except SystemExit:
            raise
        except Exception as exc:  # noqa: BLE001
            return "СБОЙ", [], f"{type(exc).__name__}: {str(exc)[:100]}"

    # Считаем параллельно. Последовательный проход упирался в лимит скрипта на
    # полутора десятках утверждений — и это была единственная причина, по
    # которой хотелось ограничить их число. Ограничивать проверку нельзя,
    # ускорить её можно.
    from concurrent.futures import ThreadPoolExecutor

    workers = max(1, min(VERIFY_WORKERS, len(claims)))
    started = time.time()
    pool = ThreadPoolExecutor(max_workers=workers)
    try:
        outcomes = list(pool.map(safe_verify, claims))
    except BaseException as exc:
        if isinstance(exc, SystemExit) and "ключу" in str(exc):
            write_status("auth", str(exc).splitlines()[0][:200], src)
        # Прерывание (SIGTERM/KeyboardInterrupt): не ждём зависшие запросы.
        try:
            pool.shutdown(wait=False, cancel_futures=True)  # Python 3.9+
        except TypeError:
            pool.shutdown(wait=False)  # Python 3.8: без отмены очереди
        save_cache(cache)
        raise
    pool.shutdown(wait=True)

    rows, failed, timed_out = [], 0, 0
    for i, (claim, (status, doms, why)) in enumerate(zip(claims, outcomes), 1):
        if status in GOOD:
            cache[claim_key(claim, srcmap)] = {"status": status, "domains": doms,
                                               "text": claim["text"][:200]}
        else:
            failed += 1
            if status == "НЕ ПРОВЕРЕНО (время)":
                timed_out += 1
        rows.append((claim, status, doms, why))
        if i > MAX_ROWS_PRINTED:
            continue
        if status == "ПЕРВОИСТОЧНИК":
            print(f"  {i:2d}. ПЕРВОИСТОЧНИК  {claim['text'][:80]}")
            continue
        print(f"  {i:2d}. {status:<16} доменов {len(doms):>2}  {claim['text'][:66]}")
        if why:
            print(f"      {why[:110]}")
        if doms:
            print(f"      источники: {', '.join(doms[:5])}")
    if len(claims) > MAX_ROWS_PRINTED:
        print(f"  … подробности ещё {len(claims) - MAX_ROWS_PRINTED} утверждений не печатаются; "
              f"неподтверждённые перечислены ниже.")
    save_cache(cache)
    print(f"\nПроверено {len(claims) - timed_out} из {len(claims)} за "
          f"{time.time() - started:.0f}с в {workers} потоков.")
    print()
    if failed:
        if timed_out:
            print(f"НЕ ГОДИТСЯ — проверка не завершена: {timed_out} утверждений не успели "
                  f"проверить. Подтверждённое сохранено; повторите ТОТ ЖЕ вызов — "
                  f"проверится только остаток.")
        print(f"НЕ ГОДИТСЯ: {failed} из {len(claims)} утверждений без подтверждения.")
        print()
        for claim, status, doms, why in rows:
            if status in GOOD:
                continue
            print(f"  [{status}] {claim['text'][:100]}")
            if status == "НЕ ПРОВЕРЕНО (время)":
                print("     Повторите вызов — проверка продолжится с этого места.")
            elif claim["kind"] == "число":
                print("     Уберите число из текста или найдите второй независимый источник.")
            else:
                print("     Перенесите в «Не подтверждено» или найдите подтверждение.")
        print()
        print("Досье с неподтверждёнными утверждениями не собирается. Это отказ,")
        print("а не предупреждение: документ уносят на встречу.")
        bad = [status for _c, status, _d, _w in rows if status not in GOOD]
        if bad and all(s == "СБОЙ" for s in bad):
            write_status("network", "все непроверенные утверждения — сбой запроса к Sonar", src)
        else:
            write_status("claims_failed", f"{failed} из {len(claims)} без подтверждения", src)
        return 1

    write_status("ok", f"все {len(claims)} утверждений подтверждены", src)
    print(f"ГОДНО: все {len(claims)} утверждений подтверждены. Можно рендерить.")
    return 0


def _die(message: str) -> int:
    """Отказ печатаем в stderr, а не в stdout.

    Stdout — это результат проверки, его модель читает как отчёт. Сообщение
    о том, что проверка вообще не началась, в отчёт попадать не должно:
    иначе «нет ключа» выглядит как строка отчёта, а не как срыв запуска.
    """
    print(message, file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())

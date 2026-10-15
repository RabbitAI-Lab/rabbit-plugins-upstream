#!/usr/bin/env python3
"""Инструкция навыка dossier — без сети и без записи на диск.

    guide.py             ПОЛНАЯ инструкция навыка: тот же текст, что SKILL.md,
                         с короткой памяткой для этой установки сверху
    guide.py flow        порядок вызовов скриптов с готовыми аргументами
    guide.py playbook    поисковый справочник: слои, готовые запросы, стоп-условия
    guide.py checklist   stop-gate перед сдачей досье

Зачем инструкция печатается скриптом. В системе, где методика отлажена,
агент читал SKILL.md навыка целиком и работал по нему. В установке с
ClawHub агент видит в каталоге только строку описания и сразу вызывает
скрипты — текст SKILL.md до него не доходил ни в одном из прогонов: он
начинал с guide.py и дальше импровизировал. Поэтому первый вызов отдаёт ту
же инструкцию целиком — модель получает то же, что получала локально.
"""
from __future__ import annotations

import pathlib
import sys

sys.dont_write_bytecode = True

ROOT = pathlib.Path(__file__).resolve().parent.parent

MEMO = """ИНСТРУКЦИЯ НАВЫКА dossier — целиком, тот же текст, что SKILL.md.
Прочитайте её до первого поиска: досье собирается строго по ней.

Памятка — как навык работает в этой установке:

1. Поиск — ТОЛЬКО скриптом search.py этого навыка: он ходит в Perplexity Sonar.
   Встроенный поиск агента (gigasearch, web_search) здесь — другой движок, не Sonar;
   для досье его не используйте. Первые две волны — готовыми командами:
     skill_exec(skill="dossier", script="search.py",
                args=["--wave1", "<Имя Фамилия>", "--org", "<организация>", "--latin", "<Name Surname>"])
     skill_exec(skill="dossier", script="search.py",
                args=["--wave2", "<Имя Фамилия>", "--org", "<организация>", "--latin", "<Name Surname>"])
   Дальше так же --wave3 (связи) и --wave4 (свежая повестка и спорное), потом
   свои вопросы, до 8 за вызов: args=["вопрос 1", …]. Других флагов нет.
   Упал вызов — повторите ТОТ ЖЕ; встроенный поиск не замена.
   Без 6+ успешных запросов search.py с именем человека документ не соберётся,
   а источники досье берите из ответов search.py: не меньше половины.
2. Формат JSON и полный список того, на что сборка откажет, —
   render_dossier.py --schema. Пишите JSON сразу под эти правила.
   Сохраняйте его write_file(root="task_drive", path="dossier.json") и передавайте
   скриптам имя файла или абсолютный путь. Несколько человек в одной задаче —
   отдельный файл на каждого: dossier_<фамилия латиницей>.json.
   Оценки («крупнейший», «один из самых») не пишите — проверка их не подтвердит.
   Каждый раздел пишите на 10% короче его ЛИМИТА из --schema: «Кто он» 600 → ~540.
   Номер источника — у каждой фразы, в том числе перед «;» внутри строки.
3. Порядок проверок: сначала форма — render_dossier.py --check <dossier.json>
   (объём, числа, ссылки, частное), потом факты — verify_facts.py <dossier.json>
   без --dry-run, до текста в чат. Замечания обоих — полным списком: исправлять
   ВСЕ одним write_file (edit_text в этой установке часто заблокирован).
   «ЧАСТИЧНО» — убрать спорную часть или перенести в «Не подтверждено», не
   переформулировать и не дописывать новое взамен. «СБОЙ» — повторить тот же вызов.
   В «Не подтверждено» можно обе версии числа («200 [1] или 350 [2]») — не проверяется.
4. Документ — render_dossier.py <dossier.json> "Досье — <Фамилия Имя> — <ГГГГ-ММ-ДД>.docx".
   Скрипт напечатает «ТЕКСТ ДЛЯ ЧАТА»: отправьте его как есть вместе с файлом.
   Строку «Собрано: …» не дополняйте — модели в ней нет намеренно.
5. Шпаргалки: guide.py flow (вызовы), guide.py playbook (поисковый справочник),
   guide.py checklist (проверка перед сдачей).
"""

FLOW = """Порядок работы dossier (вызовы — через skill_exec):

0. Инструкция целиком (если ещё не читали) и поисковый справочник:
   skill_exec(skill="dossier", script="guide.py")
   skill_exec(skill="dossier", script="guide.py", args=["playbook"])

1. Поиск — волнами через Sonar, только search.py (всего не меньше 40 вопросов).
   Встроенный поиск агента — не замена: без 6+ запросов search.py с именем
   человека сборка (шаг 5) откажет.
   skill_exec(skill="dossier", script="search.py",
              args=["--wave1", "<Имя Фамилия>", "--org", "<организация>", "--latin", "<Name Surname>"])
   skill_exec(skill="dossier", script="search.py",
              args=["--wave2", "<Имя Фамилия>", "--org", "<организация>", "--latin", "<Name Surname>"])
   skill_exec(skill="dossier", script="search.py",
              args=["--wave3", "<Имя Фамилия>", "--org", "<организация>", "--latin", "<Name Surname>"])
   skill_exec(skill="dossier", script="search.py",
              args=["--wave4", "<Имя Фамилия>", "--org", "<организация>", "--latin", "<Name Surname>"])
   skill_exec(skill="dossier", script="search.py", args=["<Имя>: вопрос 1", "вопрос 2", …])  # добор
   skill_exec(skill="dossier", script="search.py", args=["--log"])                           # счётчик

2. Формат JSON, лимиты и всё, на что сборка откажет:
   skill_exec(skill="dossier", script="render_dossier.py", args=["--schema"])
   → источники — из ответов search.py (не меньше половины, иначе сборка откажет)
   → write_file(root="task_drive", path="dossier.json", …); каждое число — в figures
     (quote = дословная цитата источника на его языке: «$10 млрд» = «$10 billion»;
     или derived_from + «около» в тексте). Семья, здоровье, смерть близких —
     ни в одном разделе, включая «Чего не касаться».

3. Форма — объём, числа, ссылки, частное — ДО проверки фактов (она платная):
   skill_exec(skill="dossier", script="render_dossier.py", args=["--check", "dossier.json"])
   3а. Превышен объём → args=["--fit", "dossier.json"]
   → все замечания одним write_file; оценочные слова, которые покажет --check, — убрать.

4. Триангуляция фактов — ДО текста в чат и ДО документа:
   skill_exec(skill="dossier", script="verify_facts.py", args=["dossier.json"])
   → «НЕ ГОДИТСЯ» = убрать число / перенести утверждение в «Не подтверждено»
     (без новых формулировок взамен) и прогнать снова.
   → «проверка не завершена» или «СБОЙ» = повторить тот же вызов без правок.
   → План без сети: args=["dossier.json", "--dry-run"]

5. Сборка файла (имя БЕЗ пути):
   skill_exec(skill="dossier", script="render_dossier.py",
              args=["dossier.json", "Досье — <Фамилия Имя> — <ГГГГ-ММ-ДД>.docx"])
   → скрипт печатает полный путь готового файла и блок «ТЕКСТ ДЛЯ ЧАТА».

6. send_file(<путь из шага 5>) и тем же ходом — в чат блок «ТЕКСТ ДЛЯ ЧАТА»
   КАК ЕСТЬ, без единой правки (суммы уже записаны без «$»).
   Первая строка — полнота данных, последняя — «Собрано: dossier v… · … ·
   вёрстка render_dossier». Модель в неё НЕ дописывать: скрипт её не знает,
   и подпись по памяти в прогонах оказывалась неверной.

Вместо «dossier.json» можно передавать абсолютный путь из ответа write_file.
"""


def skill_body(path: pathlib.Path) -> str:
    """Текст SKILL.md без шапки-манифеста: шапка — для движка, не для работы."""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("\n---", 1)
        if len(parts) == 2:
            text = parts[1].split("\n", 1)[1] if "\n" in parts[1] else ""
    return text.strip()


def section_of(path: pathlib.Path, heading: str) -> str:
    """Раздел markdown-файла от заголовка до следующего заголовка того же уровня."""
    lines = path.read_text(encoding="utf-8").splitlines()
    level = len(heading) - len(heading.lstrip("#"))
    out, inside = [], False
    for line in lines:
        if line.strip().startswith(heading):
            inside = True
        elif inside and line.startswith("#" * level + " ") and not line.startswith("#" * (level + 1)):
            break
        if inside:
            out.append(line)
    return "\n".join(out).strip()


def main() -> int:
    topic = (sys.argv[1] if len(sys.argv) > 1 else "").strip().lower().lstrip("-")
    skill_md = ROOT / "SKILL.md"
    try:
        if topic == "flow":
            print(FLOW)
            return 0
        if topic == "playbook":
            print((ROOT / "references" / "search-playbook.md").read_text(encoding="utf-8"))
            return 0
        if topic == "checklist":
            text = section_of(skill_md, "## Stop-gate")
            print(text or "[!] Раздел Stop-gate не найден в SKILL.md")
            return 0 if text else 1
        # Без аргумента и с любым другим — полная инструкция. Ошибка на
        # незнакомый аргумент стоила ход и выглядела в журнале как сбой навыка.
        if topic and topic not in ("full", "all", "help", "h", "instruction", "skill"):
            print(f"[i] Раздела «{topic}» нет — печатаю инструкцию целиком. "
                  f"Разделы: flow, playbook, checklist.\n")
        print(MEMO)
        print("=" * 30 + " SKILL.md " + "=" * 30 + "\n")
        print(skill_body(skill_md))
        return 0
    except OSError as exc:
        print(f"[!] Не удалось прочитать файл навыка: {exc}")
        print(f"    Каталог навыка: {ROOT}")
        print("    Похоже, навык установлен в нестандартной раскладке — сообщите владельцу.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

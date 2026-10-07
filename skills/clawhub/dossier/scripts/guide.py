#!/usr/bin/env python3
"""Справочник навыка dossier — без сети и без записи на диск.

Зачем скрипт, а не «прочитайте файл». Путь к каталогу навыка зависит от
установки (нативный навык, ClawHub, внешний репозиторий), и агент тратил
ходы на угадывание, где лежит `references/search-playbook.md`. Скрипт знает
свой каталог сам и печатает нужное одним вызовом.

    guide.py playbook    поисковый справочник: слои, готовые запросы, стоп-условия
    guide.py checklist   stop-gate перед сдачей досье
    guide.py flow        порядок вызовов скриптов с готовыми аргументами
    guide.py             список разделов
"""
from __future__ import annotations

import pathlib
import sys

sys.dont_write_bytecode = True

ROOT = pathlib.Path(__file__).resolve().parent.parent

FLOW = """Порядок работы dossier (вызовы — через skill_exec):

0. Справочник поиска (один раз перед сбором):
   skill_exec(skill="dossier", script="guide.py", args=["playbook"])

0а. Поиск — волнами через Sonar (до 8 вопросов за вызов, всего не меньше 40).
    Встроенный поиск агента — не замена: без запросов search.py с именем
    человека сборка (шаг 4) откажет.
   skill_exec(skill="dossier", script="search.py", args=["<Имя Фамилия>: вопрос 1", "вопрос 2", ...])
   skill_exec(skill="dossier", script="search.py", args=["--log"])  # счётчик запросов

1. Формат JSON с лимитами разделов:
   skill_exec(skill="dossier", script="render_dossier.py", args=["--schema"])
   → сохранить dossier.json в каталог задачи; каждое число — в figures
     (quote = дословная цитата источника на его языке: «$10 млрд» = «$10 billion»;
     или derived_from + «около» в тексте). Семья, здоровье, смерть близких —
     ни в одном разделе, включая «Чего не касаться».

2. Триангуляция фактов — ДО текста в чат и ДО документа:
   skill_exec(skill="dossier", script="verify_facts.py",
              args=["<абсолютный путь>/dossier.json"])
   → «НЕ ГОДИТСЯ» = убрать число / перенести утверждение в «Не подтверждено»
     и прогнать снова. «проверка не завершена» = повторить тот же вызов.
   → План без сети: args=["<путь>/dossier.json", "--dry-run"]

3. Объём и числа:
   skill_exec(skill="dossier", script="render_dossier.py",
              args=["--check", "<абсолютный путь>/dossier.json"])
   3а. Превышен объём → args=["--fit", "<абсолютный путь>/dossier.json"]

4. Сборка файла (имя БЕЗ пути):
   skill_exec(skill="dossier", script="render_dossier.py",
              args=["<абсолютный путь>/dossier.json",
                    "Досье — <Фамилия Имя> — <ГГГГ-ММ-ДД>.docx"])
   → скрипт печатает полный путь готового файла и блок «ТЕКСТ ДЛЯ ЧАТА».

5. send_file(<путь из шага 4>) и тем же ходом — в чат блок «ТЕКСТ ДЛЯ ЧАТА»
   КАК ЕСТЬ (заменить только <МОДЕЛЬ>). Первая строка — полнота данных,
   последняя — «Собрано: dossier v… · … · модель …». Ничего не дописывать.
"""


def section_of(path: pathlib.Path, heading: str) -> str:
    """Раздел markdown-файла от заголовка до следующего заголовка того же уровня."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
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
    topic = (sys.argv[1] if len(sys.argv) > 1 else "").strip().lower()
    if topic in ("playbook", "checklist") and not (ROOT / "SKILL.md").is_file():
        print(f"[!] Не найден SKILL.md в каталоге навыка {ROOT}.")
        print("    Похоже, навык установлен в нестандартной раскладке — сообщите владельцу.")
        return 1
    try:
        if topic == "playbook":
            print((ROOT / "references" / "search-playbook.md").read_text(encoding="utf-8"))
            return 0
        if topic == "checklist":
            text = section_of(ROOT / "SKILL.md", "## Stop-gate")
            if not text:
                print("[!] Раздел Stop-gate не найден в SKILL.md")
                return 1
            print(text)
            return 0
        if topic == "flow":
            print(FLOW)
            return 0
    except OSError as exc:
        print(f"[!] Не удалось прочитать файл навыка: {exc}")
        print(f"    Каталог навыка: {ROOT}")
        return 1
    print(__doc__)
    return 0 if not topic else 64


if __name__ == "__main__":
    sys.exit(main())

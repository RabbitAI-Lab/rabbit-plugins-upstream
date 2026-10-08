# Job Application Skill für OpenClaw

[English documentation](README.en.md)

Dieser Skill erzeugt aus strukturierten Profildaten einen zugeschnittenen Lebenslauf, ein Anschreiben und eine Bewerbung im Textformat. Alle mitgelieferten Personen-, Arbeitgeber- und Bewerbungsdaten sind fiktiv.

Das mitgelieferte Portrait von Mira Hoffmann wurde künstlich generiert und zeigt keine reale Person. Für Bewerbungen kann `profile_picture` in `assets/profile/master_profile.json` entfernt oder auf ein eigenes Bild gesetzt werden.

## Voraussetzungen

- OpenClaw mit Unterstützung für lokale Skills
- Python 3.10 oder neuer; zusätzliche Python-Pakete werden nicht benötigt
- Eine LaTeX-Distribution, die `pdflatex` auf dem `PATH` bereitstellt
- Für den optionalen Linux/macOS-Wrapper: Bash

Geeignete LaTeX-Distributionen sind beispielsweise:

- Linux: TeX Live über die Paketverwaltung der Distribution
- Windows: MiKTeX oder TeX Live
- macOS: MacTeX oder BasicTeX mit den benötigten Paketen

Die Vorlagen verwenden verbreitete Pakete: `geometry`, `fontenc`, `inputenc`, `lmodern`, `xcolor`, `graphicx`, `tikz`/PGF, `textpos`, `ragged2e` und `hyperref`. Bei einer minimalen LaTeX-Installation müssen diese gegebenenfalls ergänzt werden. MiKTeX kann fehlende Pakete auf Wunsch beim ersten Lauf installieren.

Installation prüfen:

```text
python3 --version
pdflatex --version
```

Unter Windows heißt der Python-Befehl häufig `py -3` statt `python3`.

## Private Daten updatefest speichern

Speichere echte Profildaten und erzeugte Bewerbungen außerhalb des installierten Skill-Ordners. Der Skill unterstützt dafür zwei optionale Umgebungsvariablen:

```text
JOB_APPLICATION_PROFILE_DIR=/pfad/zum/privaten/profil
JOB_APPLICATION_OUTPUT_DIR=/pfad/zu/applications
```

In OpenClaw können diese unter `skills.entries.job-application.env` gesetzt werden. ClawHub-Updates ersetzen dann nur Skill-Code, Vorlagen und fiktive Beispiele. Profil, eigenes Foto und Bewerbungen bleiben unverändert. Ohne Konfiguration verwendet der Skill das fiktive Beispielprofil und `./applications`.

## Funktioniert der Skill unter Linux und Windows?

Ja. Die Generatoren und der PDF-Renderer sind in Python implementiert und verwenden plattformunabhängige Pfade. Getestet wurde die vollständige PDF-Erzeugung unter Linux. Unter Windows muss Python sowie MiKTeX oder TeX Live installiert und in `PATH` verfügbar sein. Das Bash-Skript ist nur ein Komfort-Wrapper für Linux und macOS; unter Windows wird direkt `scripts\render_application.py` aufgerufen.

Die erzeugten PDF-Dateien können sich zwischen LaTeX-Distributionen geringfügig bei Schriftmetriken oder Metadaten unterscheiden. Inhalt und Layout bleiben grundsätzlich gleich.

## Schnelltest

Linux/macOS, im Skill-Verzeichnis:

```bash
python3 scripts/prepare_application.py --slug 2026-09-example-demo
cp examples/*.json applications/2026-09-example-demo/
python3 scripts/generate_cv_selection.py --job applications/2026-09-example-demo/job.json --output applications/2026-09-example-demo/cv_selection.json
python3 scripts/generate_cv.py --selection applications/2026-09-example-demo/cv_selection.json --output applications/2026-09-example-demo/CV.tex
python3 scripts/generate_cover_letter.py --content applications/2026-09-example-demo/cover_letter.json --output applications/2026-09-example-demo/cover_letter.tex
python3 scripts/generate_plain_text.py --content applications/2026-09-example-demo/indeed_text.json --output applications/2026-09-example-demo/indeed_text.txt
python3 scripts/render_application.py applications/2026-09-example-demo
```

Windows PowerShell, im Skill-Verzeichnis:

```powershell
py -3 scripts\prepare_application.py --slug 2026-09-example-demo
Copy-Item examples\*.json applications\2026-09-example-demo\
py -3 scripts\generate_cv_selection.py --job applications\2026-09-example-demo\job.json --output applications\2026-09-example-demo\cv_selection.json
py -3 scripts\generate_cv.py --selection applications\2026-09-example-demo\cv_selection.json --output applications\2026-09-example-demo\CV.tex
py -3 scripts\generate_cover_letter.py --content applications\2026-09-example-demo\cover_letter.json --output applications\2026-09-example-demo\cover_letter.tex
py -3 scripts\generate_plain_text.py --content applications\2026-09-example-demo\indeed_text.json --output applications\2026-09-example-demo\indeed_text.txt
py -3 scripts\render_application.py applications\2026-09-example-demo
```

Die Ergebnisse liegen anschließend in `applications/2026-09-example-demo/`. Fertig erzeugte Beispiele befinden sich unter `examples/generated/`.

## Eigene Daten verwenden

Belasse die fiktiven Dateien in `assets/profile/` als öffentliche Beispieldaten. Lege eigene, strukturgleiche JSON-Dateien und das optionale Profilbild in einem privaten Verzeichnis außerhalb des Skills ab und setze `JOB_APPLICATION_PROFILE_DIR` auf dieses Verzeichnis. Relative Bildpfade werden vom Profilverzeichnis aus aufgelöst. So werden persönliche Daten weder veröffentlicht noch von einem Skill-Update überschrieben.

Projekte können optional einer Organisation und einem beruflichen Kontext zugeordnet werden. `context` dient als stabiler maschinenlesbarer Wert; `context_label` wird im Lebenslauf ausgegeben:

```json
{
  "organization": "Beispielunternehmen GmbH",
  "context": "employment",
  "context_label": "Im Rahmen der Anstellung"
}
```

Für Projekte des eigenen Unternehmens kann entsprechend `own_company` mit dem sichtbaren Label `Eigenes Unternehmen` verwendet werden. Fehlen diese Felder, wird weiterhin nur der vorhandene Projektuntertitel dargestellt.

Der Skill verschickt oder veröffentlicht keine Bewerbung automatisch. Eine externe Übermittlung benötigt immer eine ausdrückliche Freigabe für das konkrete Ziel.

## Entwicklung mit OpenSpec

Die ausgelieferten Verhaltensverträge liegen unter `openspec/specs/`. OpenSpec-Änderungen werden getrennt von den aktuellen Spezifikationen unter `openspec/changes/` geplant und nach der Umsetzung archiviert.

Voraussetzung ist Node.js 20.19 oder neuer. Installation und Prüfung:

```bash
npm install -g @fission-ai/openspec
openspec --version
openspec validate --specs --strict
```

Eine neue Änderung kann mit `openspec new change <change-id>` begonnen werden. Vor der Implementierung sollten Proposal, Spezifikations-Delta, Design und Tasks geprüft werden. Nach Umsetzung und Validierung wird die Änderung mit `openspec archive <change-id>` in die Hauptspezifikationen übernommen.

Die Repo verwendet absichtlich die tool-neutrale OpenSpec-Initialisierung. Dadurch werden keine zusätzlichen Agent-Skills in das veröffentlichte ClawHub-Paket aufgenommen.

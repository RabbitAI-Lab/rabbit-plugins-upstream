---
name: ClawSheet Wizard
slug: clawsheet-wizard
version: 1.0.0
description: "Opret, inspicér og rediger Excel/XLSX-filer med pålidelige formler, formatering og skabelon-bevarelse. PLUS unik feature: formel-tjekker der finder og retter #REF!/#DIV/0!-fejl automatisk + data-kvalitetsrapport."
metadata: {"clawdbot":{"emoji":"📗","requires":{"bins":["python3"]}}}
---

# ClawSheet Wizard

Excel-værktøj baseret på velafprøvede mønstre (pandas, openpyxl), **forbedret med unikke features**:

## 🆕 Unikke features (findes ikke i originalen)

### Feature 1: Formel-tjekker & auto-retter
Scanner hele workbook'en for `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, cirkulære referencer
og forskudte formel-områder — og foreslår/udfører rettelser:

```bash
python3 scripts/formula_checker.py bog.xlsx --fix --out bog-rettet.xlsx
python3 scripts/formula_checker.py bog.xlsx --report rapport.md
```

### Feature 2: Data-kvalitetsrapport
Genererer en rapport over: duplikater, tomme celler, tekst-tallene, afkortede ID'er
(>15 cifre), blandede typer og dato-fælder:

```bash
python3 scripts/data_quality.py kunder.xlsx --out kvalitet.md
```

### Feature 3: Skabelon-diff
Sammenligner en redigeret fil med originalen og viser præcis hvad der ændrede sig
(celler, formler, formatering, skjulte ark) — perfekt til audit:

```bash
python3 scripts/template_diff.py original.xlsx redigeret.xlsx
```

---

## Standard-operationer (arvet + forbedret)

### Vælg værktøj efter job
- `pandas` — analyse, reshaping, CSV-lignende opgaver
- `openpyxl` — formler, stilarter, kommentarer, merged cells, skabelon-bevarelse

### Datoer er serienumre med arv
- Excel bruger 1900-datessystemet med falsk skuddag; nogle bruger 1904
- Tid er brøkdele af dage — formatering og konvertering begge vigtige

### Hold beregninger i Excel
- Skriv formler ind i celler i stedet for hårdkodede resultater
- Tjek kopierede formler for forkerte områder, ark og off-by-one
- Lever ALTID uden formel-fejl

### Beskyt datatyper
- Lange ID'er, telefonnumre, postnumre og foranstillede nuller = tekst
- Excel afkorter numerisk præcision over 15 cifre
- Blandede tekst-tal-kolonner kræver eksplicit håndtering

### Bevar struktur
- Eksisterende skabeloner vinder over generiske stilarter
- Skjulte rækker/kolonner, navngivne områder og eksterne referencer påvirker output
- Match stilarter for nye celler

### Genberegn og gennemgå
- `openpyxl` bevarer formler, men beregner dem IKKE — brug `formula_checker.py`
- Visuel gennemgang hvis layout betyder noget

## Almindelige fælder
- Type-inference ved læsning kan ødelægge ID'er
- Kolonne-indeksering varierer — off-by-one i formler
- `.xlsm` kan indeholde makroer; `.xls` er et stramt legacy-format
- Store filer: brug streaming/chunked reads
- `FILTER`, `XLOOKUP`, `SORT`, `SEQUENCE` fejler i ældre visere

## Feedback
- Hjælpsom? → `clawhub star clawsheet-wizard`

---
name: ClawCode Lens
slug: clawcode-lens
version: 1.0.0
description: "Forklar kode i ethvert sprog med struktureret syntaks/logik-gennemgang — PLUS unik feature: lokal kode-analyse uden ekstern API + sikkerheds-scanning af koden for sårbarheder og forbedringsforslag."
metadata: {"clawdbot":{"emoji":"💻","requires":{"bins":["python3"]}}}
---

# ClawCode Lens

Kode-forklarings- og analyseværktøj — inspireret af Dify Code Interpreter, **men forbedret**:

## 🆕 Unikke features (findes ikke i originalen)

### Feature 1: Kører 100% LOKALT — ingen ekstern API krævet
Originalen kræver en Dify-server + Ollama-model + API-nøgle. ClawCode Lens analyserer
koden direkte med strukturerede regler — virker offline, gratis og øjeblikkeligt:

```bash
python3 scripts/explain.py kode.py --lang python
python3 scripts/explain.py main.js --lang javascript --detail
```

### Feature 2: Sikkerheds-scanning
Finder sårbarheder: hardcodede nøgler, SQL-injektion, `eval()`-misbrug, usikre
`exec`-kald, svage adgangskoder, usikre imports:

```bash
python3 scripts/security_scan.py kode.py --out rapport.md
```

### Feature 3: Forbedrings-forslag
Giver konkrete, prioriterede forslag: kompleksitet, gentaget kode, manglende fejlhåndtering,
performance-flaskehalse og bedste-praksis — med kode-eksempler:

```bash
python3 scripts/improve.py kode.py --out forslag.md
```

---

## Sådan bruges det

### Forklar kode (struktureret)
```bash
python3 scripts/explain.py fil.py --lang python
# Output: oversigt → nøglefunktioner → logik-flow → edge cases
```

### Understøttede sprog
Python, JavaScript/TypeScript, C/C++, Java, C#, Go, Rust, SQL, Bash, PHP, Ruby — auto-detekteret fra filtype.

### Kombiner alt i ét kald
```bash
python3 scripts/explain.py app.py --security --improve --out fuld-rapport.md
```

## Eksempel-output (sikkerhedsscan)

```text
🔒 Sikkerheds-scan: app.py
  [KRITISK] Linje 12: API-nøgle hardcoded — brug env-var
  [HØJ]    Linje 45: SQL-streng bygges med f-string — risiko for injektion
  [INFO]   Linje 78: eval() — undgå med mindre strengt nødvendigt
```

## Feedback
- Hjælpsom? → `clawhub star clawcode-lens`

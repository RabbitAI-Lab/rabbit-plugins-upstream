---
name: "mt5-headless-automation"
description: "Kør MetaTrader 5 (MT5) fuldt headless på Linux/VPS: Wine + Xvfb + xdotool + OCR. Installér, log ind, attach EA'er, deploy eksperter, overvåg heartbeat og genstart automatisk. Bygget fra rigtig drift-erfaring (Vantage, 17 symboler, DRT-Axe EA). Perfekt til tradere der vil køre EA'er 24/7 uden skærm."
---

# MT5 Headless Automation 🖥️🤖

Få MetaTrader 5 til at køre på en server UDEN skærm — fuld EA-automation 24/7.

## Hvad skill'en gør

1. **Installér MT5 + Wine + Xvfb** (headless display)
2. **Log ind på broker-konto** (terminal64.exe via Wine)
3. **Attach EA'er** via Navigator (Ctrl+N → OCR → dobbeltklik → Enter)
4. **Deploy EA-ændringer** med 1 kommando (kopiér → kompilér → genstart → verificér)
5. **Overvåg heartbeat** — hvis EA'en hænger: genstart automatisk
6. **Undgå de 5 klassiske fælder** (dokumenteret nedenfor)

## Hurtig start

```bash
# 1) Miljø
sudo apt install wine xvfb xdotool tesseract-ocr scrot
Xvfb :99 -screen 0 1280x720x24 &
export DISPLAY=:99

# 2) Installér MT5 (Windows-installeren via Wine)
wine "mt5setup.exe" /auto

# 3) Attach EA (scripts/attach_ea.sh)
bash scripts/attach_ea.sh "DRT-Axe"

# 4) Deploy ny EA-version (scripts/deploy_ea.sh)
bash scripts/deploy_ea.sh
```

## De 5 klassiske fælder (vi har ramt dem ALLE)

| # | Fælde | Symptom | Fix |
|---|-------|---------|-----|
| 1 | **ArraySetAsSeries mangler** | EA læser historik baglæns → 0 handler | `ArraySetAsSeries(rates, true)` efter hvert CopyRates |
| 2 | **EA unloades ved MT5-genstart** | "EA kører" men HB-fil frosset | Attach MANUELT efter hver genstart (auto-attach svigter) |
| 3 | **Log-friskhed ≠ EA kører** | Falsk positiv i monitor | Tjek HB-filens mtime, ikke log-linjer |
| 4 | **pkill -f dræber sig selv** | Script dør pludseligt | `pkill -f "pa[t]tern"` eller `kill $(lsof -ti:PORT)` |
| 5 | **xdotool koordinater ændrer sig** | Klik på forkert sted | OCR-find elementet hver gang (tesseract + tsv) |

## Filer

```
mt5-headless-automation/
├── SKILL.md
└── scripts/
    ├── attach_ea.sh     # OCR-guided EA-attach via Navigator
    ├── deploy_ea.sh     # 1-kommando: kopiér → kompilér → genstart → verificér
    ├── watchdog.sh      # Heartbeat-tjek + auto-genstart
    └── ea_fix.py        # Diagnosticér hvorfor EA'en ikke handler
```

## Verifikation (altid!)

- EA-log: `MQL5/Files/<EA>_Log.txt` (server-tid GMT+3)
- Heartbeat: `<EA>_HB.txt` — mtime skal være < 60 sek gammel
- Data: `<EA>_Data.json` (realtids-klines hvert 60s)
- ex5 MD5 skal matche workspace-kopi efter deploy

## Betaling (x402)
Premium: live EA-data + signals via x402 pay-per-call API.

# EA-Upload & Opsætning (DRT-Axe på MT5/Vantage) 🪓

**Formål:** Standardiseret EA-upload → kompilér → genstart → attach → verificér. Skrevet 19/8 2026 efter gentagne fejl (Boss: "du har lavet samme nummer flere gange"). **FØLG DENNE SKILL — ALTID — når EA'en skal ændres.**

## 🚨 De 3 fejl vi HAR lavet (lær af dem!)
1. **`ArraySetAsSeries` manglede** → CopyRates uden `ArraySetAsSeries(rates, true)` giver arrayet ÆLDST-FØRST. Koden antager rates[0]=nyeste → læser historikken baglæns → scannet finder KUN gamle sweeps (fx 13/8) → alder-gaten dropper ALT → 0 handler. **Tjek ALTID: efter hvert CopyRates/CopyClose-kald skal `ArraySetAsSeries(arr, true)` stå (gælder også DRT.mqh's DRT_ICTBias + DRT_DailyBias + SilverBullet-scan).**
2. **OCR-fumleri i stedet for DevOps' scripts** → brug ALDRIG xdotool/OCR til at finde Algo-knappen manuelt. Kør `mt5-ea-fix.py` (DevOps' script) — og hvis en EA-dialog står åben, tryk `Enter` (OK).
3. **Tokens spildt på kodegennemgang** → ændringen er typisk 1-4 linjer. Ret → kør deploy → verificér. Læs IKKE hele koden først.

## ⚡ Standard-procedure (1 kommando)
```bash
bash /home/openclaw/.openclaw/workspace/tradevault/ea/deploy_ea.sh
```
Scriptet: kopierer .mqh+.mq5 → MT5 → kompilerer (MetaEditor64 via wine+xvfb) → genstarter mt5.service → verificerer "DRT-Axe startet" i loggen.
- ✅ SUCCESS = "EA KØRER" + heartbeat frisk
- ⚠️ "ikke bekræftet efter 5 min" = en dialog venter → `xdotool key Return` (med korrekt DISPLAY/XAUTHORITY)
- ❌ kompileringsfejl = ret koden, kør igen

## 🛠️ Manuel kæde (hvis deploy fejler)
```bash
MT5="/home/openclaw/.wine-mt5/drive_c/Program Files/MetaTrader 5"
EA="/home/openclaw/.openclaw/workspace/tradevault/ea"
# 1) Kopiér
cp "$EA"/DRT.mqh "$MT5/MQL5/Include/DRT.mqh"
cp "$EA"/SilverBullet.mqh "$MT5/MQL5/Include/SilverBullet.mqh"
cp "$EA"/Risk.mqh "$MT5/MQL5/Include/Risk.mqh"
cp "$EA"/TimeFilter.mqh "$MT5/MQL5/Include/TimeFilter.mqh"
cp "$EA"/News.mqh "$MT5/MQL5/Include/News.mqh"
cp "$EA"/Notify.mqh "$MT5/MQL5/Include/Notify.mqh"
cp "$EA"/AntiFlag.mqh "$MT5/MQL5/Include/AntiFlag.mqh"
cp "$EA"/DRT-Axe.mq5 "$MT5/MQL5/Experts/DRT-Axe.mq5"
# 2) Kompilér (0 fejl = OK)
cd "$MT5/MQL5/Experts"
WINEPREFIX=/home/openclaw/.wine-mt5 WINEDLLOVERRIDES=mscoree,mshtml= HOME=/home/openclaw \
  xvfb-run -a wine "$MT5/MetaEditor64.exe" /compile:"DRT-Axe.mq5" /log:"compile_deploy.log" >/dev/null 2>&1
sleep 12
iconv -f UTF-16LE -t UTF-8 compile_deploy.log | grep "Result:"
# 3) Genstart + verificér
sudo systemctl restart mt5.service
sleep 150   # login ~60s + attach
tail -5 "$MT5/MQL5/Files/DRT-Axe_Log.txt"   # skal vise "DRT-Axe startet — 17 symboler"
```

## 🔍 Verifikation (ALTID efter deploy)
| Tjek | Kommando | OK-tegn |
|---|---|---|
| EA kører | `grep "startet" DRT-Axe_Log.txt \| tail -1` | dags dato + "17 symboler" |
| Heartbeat frisk | `stat -c %y DRT-Axe_HB.txt` | < 2 min gammel |
| Scanner friskt | `tail DRT-Axe_Log.txt` | sweeps med DAGENS priser (ikke 13/8-niveau) |
| Algo ON | `mt5-algo-ensure.py` | "EA-heartbeat frisk — Algo er ON" |

## 🪟 Hvis dialog venter (EA-egenskaber)
- Symptom: EA loadet men "startet" mangler / HB frosset
- Fix: find DISPLAY+XAUTHORITY, tryk Enter:
```bash
export DISPLAY=:99 XAUTHORITY=$(ps aux | grep 'Xvfb :99' | grep -v grep | grep -oE '\-auth [^ ]+' | awk '{print $2}' | head -1)
xdotool key Return
```

## 📁 Faste stier
- EA-kode (KUN ret her): `/home/openclaw/.openclaw/workspace/tradevault/ea/`
- MT5-mappe: `/home/openclaw/.wine-mt5/drive_c/Program Files/MetaTrader 5`
- EA-log: `$MT5/MQL5/Files/DRT-Axe_Log.txt` (server-tid GMT+3 = UTC+3)
- Heartbeat: `$MT5/MQL5/Files/DRT-Axe_HB.txt`
- Data til botten: `$MT5/MQL5/Files/DRT-Axe_Data.json` (skrives hvert 60s)
- DevOps' scripts: `/home/openclaw/.local/bin/mt5-ea-fix.py`, `mt5-ea-attach.sh`, `mt5-login-helper.sh`, `mt5-algo-ensure.py` (cron hver 2. min)

## ⏰ Tidsvinduer (handler)
London 09-11 · NY open 14:30-17:00 · SB PM 19:30-21:00 (DK-tid). Nat-pause 23-08.
**Udenfor vinduer = ingen entries** — det er by design, ikke en fejl. Forvent handler i NY/PM-vinduerne.

## 📌 Regler for EA-ændringer (Boss 19/8)
1. Lav ÆNDRINGEN (typisk få linjer) — læs ikke hele koden
2. Kør `deploy_ea.sh` — ikke manuel OCR-fumleri
3. Verificér med tabellen ovenfor
4. Commit: `git add tradevault/ea/ && git commit -m "EA fix: ..."` (medarbejder i workspace-repo)
5. Rapportér kort: hvad der blev ændret + bevis på at den kører

# Agent-Durchführungsablauf und Skript-Vertrag — powpow-register

Ausführungsdetails zu den einzelnen Schritten aus SKILL.md. Alle Befehle haben die Form `node scripts/powpow-register.mjs <Unterbefehl> [Parameter]`;
das Skript hat **null Abhängigkeiten** und benötigt **Node ≥ 18**; alle Anfragen gehen ausschließlich an `https://global.powpow.online`.

## Sicherheitsdesign (warum so konzipiert)

| Design | Grund |
|---|---|
| Das Passwort wird ausschließlich über die Umgebungsvariable `POWPOW_REGISTER_PASSWORD` übergeben | Kommandozeilen-Argumente eines Prozesses sind für andere Prozesse auf demselben Rechner sichtbar (argv-Leckfläche); eine Umgebungsvariable wird im Skript gelesen und sofort verwendet |
| Das Passwort wird **niemals in die Statusdatei geschrieben** und erscheint niemals in Logs | Die Statusdatei kann auf der Festplatte zurückbleiben; die einmalige Anzeige im Generierungsmodus im Chat dient nur dazu, dass der Nutzer es speichert |
| Die Statusdatei liegt im temporären Systemverzeichnis (`os.tmpdir()/powpow-register-state.json`, 0600) | Enthält nur die fünf Felder email / username / nickname / token / outTradeNo; `cleanup` entfernt sie mit einem einzigen Befehl |
| Das vom agent erhaltene JWT wird über den offiziellen `me?token=`-Endpunkt in ein Browser-Cookie umgetauscht | Offizielle, von der Plattform für die HarmonyOS-WebView konzipierte Brücke; die Signaturprüfung prüft nur Signatur + Gültigkeitsdauer, kein Geräte-Fingerprint — der Browser des Nutzers funktioniert |
| Bei der Zahlung nur create-order / query / Kasse öffnen | Die Zahlungshandlung und die Zahlungs-Credentials bleiben immer zwischen dem Nutzer und der offiziellen Alipay-Kasse; der agent fasst sie nie an |

## Befehlsreferenz

| Befehl | Schlüsselparameter | Funktion / Zeitpunkt |
|---|---|---|
| `status` | —— | Ablauffortschritt ansehen (liest die Statusdatei); nach einem Chat-Abbruch zuerst diesen Befehl ausführen |
| `gen-password` | —— | Erzeugt ein starkes 24-Zeichen-Passwort (Groß-/Kleinbuchstaben + Zahlen); stdout zeigt es **nur dieses eine Mal** |
| `prepare-suggest` | `--username --nickname --email` | Trägt die bestätigten Angaben in die Statusdatei ein (danach muss `register` sie nicht erneut übergeben) |
| `send-code` | `--email` | Löst den Versand des 6-stelligen Verifizierungscodes durch die Plattform aus (10 Minuten gültig, 60 s Abklingzeit) |
| `register` | `--code` (Pflicht); `--username --nickname --avatar --phone` (optional; wenn in der Statusdatei vorhanden, keine erneute Übergabe nötig) | Legt ein pending-Konto an; das Passwort läuft über die Umgebungsvariable `POWPOW_REGISTER_PASSWORD`; nach Erfolg wird das JWT automatisch in der Statusdatei gespeichert |
| `login-link` | `--target pending` oder `--target home` | Erzeugt einen Ein-Klick-Login-Link (Dual-Link-Design, siehe unten) |
| `create-order` | `--package monthly\|quarterly\|yearly` (Standard: Alipay)<br>`--provider alipay\|paypal` | Legt die Zahlungsbestellung an; Alipay liefert den Dateipfad der Zahlungsseite + outTradeNo, PayPal den Dateipfad der Autorisierungsseite + subscriptionId (automatisch in die Statusdatei eingetragen) |
| `query` | —— | Fragt den Status von Bestellung/Abo ab. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; alle 10–15 s pollen |
| `refresh-login` | Passwort über Umgebungsvariable | Erneutes Login für ein **neues JWT** (der Abo-Anspruch wechselt von NONE zu ACTIVE); nach dem Zahlungseingang zwingend ausführen |
| `whoami` | —— | Prüft mit dem Token aus der Statusdatei Konto- und Abo-Status (verifiziert, ob die Aktivierung gegriffen hat) |
| `cleanup` | —— | Löscht die Statusdatei (zum Abschluss zwingend ausführen) |

**Übergabe über Umgebungsvariablen** (das Passwort kommt niemals auf die Kommandozeile):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<Passwort>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<Passwort>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<Passwort> && node scripts/powpow-register.mjs register --code 123456
```

## Dual-Link-Mechanismus (Kern-Design)

Der Login-Status der Plattform ist ein HttpOnly-Cookie; der agent kann dem Browser nicht direkt ein Cookie untersetzen. Die Brücke ist der offizielle
Endpunkt `/api/auth/me?token=<JWT>&redirect=<interner Pfad>`: Signaturprüfung → für pending-Nutzer wird automatisch eine
session nachgebaut → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 Tage) → Prüfung des
redirect (nur mit einfachem Schrägstrich beginnend; `//` und Backslash verboten; nach dem Auflösen muss die Origin identisch sein) → 307 temporäre Weiterleitung auf die Zielseite.

- **Link 1 (direkt nach erfolgreicher Registrierung aushändigen)**: `--target pending` → Landung auf `/subscription`.
  Der Browser des Nutzers tritt in den „halben Login"-Zustand: Abo-Seite und Alipay-Rückkehrseite sind sichtbar und bedienbar; Inhaltsseiten werden von der Paywall
  weiterhin auf die Abo-Seite zurückgeleitet (dreistufige Absicherung: JWT-claims-Prüfung im Gateway → DB-Nachprüfung → Prüfung in den Kern-APIs; normales Verhalten).
- **Link 2 (nach der Bestätigung von paid aushändigen)**: zuerst `refresh-login` für ein neues JWT (die Zahlung aktualisiert nur die DB, nicht die
  claims des bereits ausgestellten JWT; ohne Erneuerung wirkt es wie „bezahlt, aber kein Mitglied"), dann `--target home` → Landung auf der Startseite,
  vollständiger Mitgliedsstatus.

## Vollständige Sequenz (Normalpfad)

```
1.  status                          # Umgebungs-Selbstprüfung
2.  (Schritt 2: Angaben im Chat bestätigen, Passwort als Entweder-oder; Generierungsmodus: gen-password → den Nutzer sofort speichern lassen)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → der Nutzer holt den Code im Postfach ab (einziges Verlassen des Chats, Stelle ①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → Link 1 an den Nutzer senden
7.  (der Nutzer wählt die Zahlungsart)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <Zahlungsseitendatei>     # Windows; macOS: open, Linux: xdg-open
    # → der Nutzer schließt Zahlung/Autorisierung an der Alipay-/PayPal-Kasse ab (Verlassen des Chats, Stelle ②)
9.  query (alle 10–15 s) bis paid / ACTIVE
10. refresh-login                   # neues JWT mit ACTIVE-Anspruch holen
11. login-link --target home        # → Link 2 an den Nutzer senden
12. whoami                          # subscriptionStatus: ACTIVE bestätigen (optional)
13. cleanup                         # Statusdatei löschen
```

## Zuordnung Befehl → Plattform-API

| Skript-Befehl | Plattform-Endpunkt |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart, Avatar-Direktupload) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (der Link selbst; wird beim Klick im Browser wirksam) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

Quellen der Regeln: Registrierungsfelder und Rate Limits siehe `registration-flow.md`; Pläne und Aktivierungskette siehe
`payment-and-activation.md` (beide mit Angabe der Plattform-Quelldateien).

## Fehlerbehandlung auf Skript-Ebene

| Symptom | Behandlung |
|---|---|
| `Node 版本过低` (Node-Version zu niedrig) | In den reinen Anleitungsmodus zurückfallen, nicht gewaltsam weiterprobieren |
| Netzwerkfehler / Timeout | Einmal wiederholen; wenn es weiterhin scheitert, den Nutzer das Netzwerk prüfen lassen und dann weitermachen (die Statusdatei ist noch da — mit `status` von vorn herstellen) |
| `register` meldet einen Business-Fehler (「用户名已存在」(Der Benutzername existiert bereits) usw.) | Nach der Tabelle in SKILL.md Schritt 5 behandeln; **den Verifizierungscode nicht erneut senden** (innerhalb von 10 Minuten weiterhin gültig) |
| `register` meldet 「邮箱验证码错误或已过期」(Der E-Mail-Verifizierungscode ist falsch oder abgelaufen) | Abgelaufen → `send-code` erneut |
| Nach `create-order` hat der Nutzer die Zahlungsseite geschlossen | Einfach erneut `create-order` (die alte Bestellung schließt sich nach 2 h automatisch; PayPal-PENDING-Abos laufen nach 1 h ab) |
| `create-order --provider paypal` meldet 409 | Es gibt schon ein unfertiges PayPal-Abo; 1 h warten, bis es abläuft, oder die alte Autorisierung im Browser abschließen |
| `query` bleibt dauerhaft pending / PENDING | Der Nutzer hat eventuell nicht bezahlt; kurz nachfragen. Wirklich bezahlt → nach der Troubleshooting-Tabelle in payment-and-activation.md vorgehen |
| `refresh-login` 403 `pending_payment` | Die Zahlung/Autorisierung ist noch nicht eingegangen; zurück zu Schritt 9 und weiter pollen |
| Statusdatei verloren (versehentlich gelöscht / Rechnerwechsel) | `whoami`/`refresh-login` funktionieren nicht; den Nutzer im Browser, in dem Link 1 geöffnet wurde, die Abo-Seite neu laden und den Status prüfen lassen — oder neu einloggen (Web-Modus) |

## Rückfallmodus (reine Anleitung)

Sobald einer der folgenden Fälle eintritt, sofort in die reine Anleitung im Stil von v1 zurückfallen und das Skript nicht weiter herumquälen:

- Kein Node ≥ 18 oder zweimal in Folge derselbe Skriptfehler;
- Der Nutzer sagt ausdrücklich „Ich mache das selbst auf der Webseite";
- Firmen-/Geräterichtlinien untersagen dem Skript den Netzzugriff.

Nach dem Rückfall: die Registrierungsseite https://global.powpow.online/register und die Abo-Seite
https://global.powpow.online/subscription geben, nach den Regeln aus `registration-flow.md` begleiten und gemeinsam Fehler suchen,
Ton unverändert, jede Runde endet weiterhin mit einem „Nächster Schritt"-Block.

---
name: powpow-register
description: Hilft Nutzer:innen, PowPow- (Bubble-)Registrierung, Alipay-/PayPal-Abonnement-Aktivierung und Ein-Klick-Login komplett im Chat abzuschließen. Der agent füllt Formulare (inkl. Avatar-Upload), sendet den E-Mail-Verifizierungscode, erstellt den Zahlungsauftrag und verfolgt den Zahlungseingang; die Nutzer:innen geben nur Basisinformationen an, rufen einmal den Verifizierungscode ab und zahlen an der Alipay-/PayPal-Kasse — ohne den Chat zu verlassen. Auslöser: „Bubble registrieren", „PowWow-Konto registrieren", „Wie registriere ich mich bei Bubble?", „Hilf mir, ein powpow-Konto anzulegen", „sign up powpow"; behandelt auch Feststeckendes bei der Registrierung (kein Verifizierungscode, Benutzername/E-Mail vergeben) und Aktivierungsprobleme (Login meldet „Konto nicht aktiviert" / pending_payment, wie abonnieren/bezahlen). Benötigt Node ≥ 18; falls nicht verfügbar, automatischer Rückfall in den reinen Anleitungsmodus. Keine Beiträge/kein Erstellen digitaler Menschen (das macht powpow-simple), keine Code-Entwicklung.
version: 2.1.0
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (Bubble-Registrierungsassistent)

Führt neue Nutzer:innen von „Ich weiß nicht, was Bubble ist" bis zu „Konto aktiviert, Ein-Klick-Login, loslegen" — alles im Chat. Nur zweimal muss der Chat kurz verlassen werden: **um im Postfach den Verifizierungscode zu suchen** und **um an der Kasse zu zahlen** (Alipay oder PayPal — der agent öffnet die Kassenseite automatisch).

**Version 2.1.0** · 2026-10-11 (ab v2 agent-gestützter Modus: Skript-Vertrag und vollständige Sequenz siehe `references/agent-flow.md`; Feldregeln, Rate Limits und Fehlerbehebung siehe `references/registration-flow.md`; Zahlungskanäle siehe `references/payment-and-activation.md`; Screenshot-Liste siehe `references/screenshots.md`. Ab v2.1.0 kann der agent auch PayPal-Abos übernehmen, als Option neben Alipay)

## Laufzeitumgebung

- Kernskript `scripts/powpow-register.mjs`: **null Abhängigkeiten**, benötigt **Node ≥ 18**. Vor dem Start einmal `node scripts/powpow-register.mjs status` ausführen, um die Umgebung zu prüfen.
- Alle Anfragen des Skripts gehen ausschließlich an die offizielle Domain `https://global.powpow.online`.
- **Ohne Node / bei Skriptfehlern**: automatischer Rückfall in den reinen Anleitungsmodus — dem Nutzer die Registrierungsseite https://global.powpow.online/register und die Abo-Seite https://global.powpow.online/subscription geben und nach `references/registration-flow.md` begleiten. Das Skript nicht wiederholt erzwingen.
- Nach einem Chat-Abbruch: zuerst mit `status` prüfen, wo der Ablauf steht, dann weitermachen.

## Trigger-Bedingungen

- Registrierungsabsicht: „Bubble registrieren", „ein powpow-Konto registrieren", „Wie registriere ich mich bei Bubble?", „sign up powpow"
- Registrierung hakt: „keine Verifizierungs-E-Mail erhalten", „Benutzername angeblich schon vergeben", „Passwort wird ständig abgelehnt"
- Probleme nach der Registrierung: „Login meldet Konto nicht aktiviert", „403 pending_payment", „Wie bezahle bzw. abonniere ich Bubble?"

**Kein Trigger**: Beiträge veröffentlichen/digitale Menschen erstellen (→ powpow-simple); Web-Code-Entwicklung (siehe die Entwicklungs-Skills). Möchte ein Nutzer sowohl registrieren als auch posten: erst diesen Skill durchlaufen, nach der Aktivierung an powpow-simple übergeben.

## Ablaufübersicht

| Schritt | Was der agent tut | Was die Nutzer:innen tun |
|---|---|---|
| 1 Produktvorstellung | Vorstellung + Screenshots senden | kurz anschauen |
| 2 Infos bestätigen | Benutzername/Spitzname aktiv vorschlagen, Passwort als Entweder-oder, E-Mail erfragen | bestätigen, angeben |
| 3 Code senden | `send-code` | —— |
| 4 Code zurückmelden | —— | 6-stelligen Code im Postfach suchen und zurückmelden |
| 5 Registrierung absenden | `register` (inkl. Avatar-Direktupload), Fehler automatisch behandeln | —— |
| 6 Halbes Login + Zahlung | `login-link(pending)` → `create-order --provider alipay|paypal` → Kasse öffnen → `query` pollen | Link öffnen, zahlen |
| 7 Volles Login | `refresh-login` → `login-link(home)` | Link öffnen, zur Startseite |
| 8 Abschluss | `cleanup` + Kontokarte aushändigen + Einführung + Plugins empfehlen | loslegen |

## Schritt 1: Produktvorstellung + Screenshots (nicht überspringbar)

Die meisten Nutzer:innen haben Bubble noch nie gesehen. Als Erstes geht es nicht um den Ablauf, sondern darum, das Produkt **sichtbar** zu machen:

1. Stelle Bubble in ~120 Zeichen vor: Mach aus einem spontan aufgenommenen Foto einen Reisetagebuch-Eintrag, den du als „Blase" auf der öffentlichen Karte verankerst; Blasen verlieren mit der Zeit an Aktualität, aber Likes von anderen lassen sie wieder aufleben; auf der Karte gibt es außerdem „digitale Menschen", mit denen du chatten kannst. Plattform-Adresse https://global.powpow.online ; wer zuerst ein Video sehen möchte: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Screenshots senden**. Die Screenshots liegen dem Skill bereits unter `assets/screenshots/powpow-0N.jpg` bei — einfach als lokale Bilddatei senden, ganz ohne Netzverbindung. Liste, Inhalt und Einsatzzeitpunkt jeder Grafik siehe `references/screenshots.md`. Beste Einstiegskombination: Kartenseite (powpow-03) + Beitragsdetailseite (powpow-06).

Screenshot-Regeln (harte Regeln):

- Die Screenshots **liegen dem Skill bei** unter `assets/screenshots/` (`powpow-0N.jpg`) — direkt als lokale Bilddateien senden; in jeder Umgebung nutzbar, auch dort, wo GitHub nicht erreichbar ist.
- Pro Runde nur 1–3 Bilder passend zum aktuellen Thema senden, nicht alles auf einmal.
- Fehlen die Dateien im Paket unerwartet, auf die gehosteten Links aus `references/screenshots.md` zurückfallen (Achtung: aus Festlandchina evtl. nicht erreichbar).

Nach der Vorstellung die Entscheidung dem Nutzer überlassen: **„Wenn du registrieren möchtest, richten wir dein Konto in drei Minuten im Chat ein — du musst nur einmal den E-Mail-Verifizierungscode anschauen."**

## Schritt 2: Registrierungsinfos bestätigen (pro Runde eine Frage, nicht alles auf einmal)

- **Benutzername** (Pflicht): aus dem Gesprächskontext / dem Systembenutzernamen **aktiv einen vorschlagen** (2–50 Zeichen, Groß-/Kleinschreibung egal); wenn der Nutzer zustimmt, übernehmen, sonst ändern.
- **Passwort** (Pflicht, zuerst Entweder-oder anbieten):
  - Nutzer:in gibt es selbst an → danach per Umgebungsvariable an das Skript übergeben, **niemals in Kommandozeilen-Argumente schreiben**;
  - agent generiert es → `node scripts/powpow-register.mjs gen-password` ausführen und das generierte Passwort **sofort an den Nutzer senden, damit er es speichert** (wird nur dieses eine Mal angezeigt, danach nie wieder).
- **E-Mail** (Pflicht): muss die Nutzer:in selbst angeben — das ist der Identitätsanker des Kontos, **nicht raten**.
- **Spitzname** (optional): standardmäßig wie der Benutzername vorschlagen.
- **Avatar** (optional): Wenn ein lokaler Bildpfad genannt wird (≤5 MB, kein SVG), lädt das Skript ihn direkt hoch; sonst überspringen (die Plattform nutzt das Standard-Logo). Wenn du Bilder generieren kannst, kannst du auch eines anbieten.
- **Telefonnummer** (optional, Festlandchina): standardmäßig überspringen; erst auf Wunsch erfragen.

Nach der Bestätigung `prepare-suggest --username U --nickname N --email E` ausführen, um alles in der Statusdatei festzuhalten (dann muss `register` nichts wiederholen).

## Schritt 3–4: E-Mail-Verifizierungscode (einziger Moment, an dem der Chat verlassen werden muss)

```
node scripts/powpow-register.mjs send-code --email <E-Mail>
```

Der Nutzer:in klar sagen: **Such im Postfach den 6-stelligen Code — er ist 10 Minuten gültig; schau auch in den Spam-/Werbungsordner.** Danach zurückkommen und den Code schicken. Das Senden hat eine 60-Sekunden-Abklingzeit — nicht mehrfach hintereinander klicken.

## Schritt 5: Registrierung absenden (agent erledigt es)

```
POWPOW_REGISTER_PASSWORD=<Passwort> node scripts/powpow-register.mjs register --code <Verifizierungscode> [--username U] [--nickname N] [--avatar <lokaler Bildpfad>] [--phone P]
```

Bei Erfolg steht das Konto sofort (Status pending, inkl. 3 Start-Abzeichen). Häufige Fehler werden automatisch behandelt, ohne den Nutzer zu unterbrechen:

| Fehler | Behandlung |
|---|---|
| Benutzername existiert bereits (用户名已存在) | automatisch Variante vorschlagen (Benutzername + Zahl), nach Bestätigung direkt erneut versuchen (Code bleibt gültig, kein Neusenden nötig) |
| E-Mail bereits verwendet (邮箱已被使用) | nachfragen: andere E-Mail — oder gibt es doch schon ein Konto (dann Login/Passwort-vergessen) |
| E-Mail-Verifizierungscode falsch oder abgelaufen (邮箱验证码错误或已过期) | älter als 10 Minuten → `send-code` erneut |
| Senden/Registrieren zu häufig (429) | 1 Minute warten und erneut versuchen; der Nutzer:in kurz Bescheid geben |

## Schritt 6: Ein-Klick-Login (Link 1) + Zahlung

1. Direkt nach erfolgreicher Registrierung:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Link an den Nutzer senden: **Nach dem Öffnen landet der Browser direkt auf der Abo-Seite und ist bereits eingeloggt** — so zeigt die Rückkehrseite nach der Zahlung korrekt „Zahlung erfolgreich". (In diesem Zustand werden Inhaltsseiten weiterhin auf die Abo-Seite umgeleitet — das ist die Paywall der Plattform, die normal arbeitet; kein Bug, und die internen Mechanismen müssen nicht erklärt werden.)
2. **Lass den Nutzer die Zahlungsart wählen** — zeig beide Kanäle:
   - **Alipay (China / Nutzer:innen mit Alipay)**: Einmalkauf der entsprechenden Laufzeit, **keine automatische Verlängerung**
     - Monatlich **¥6.99** (zum Ausprobieren empfohlen) / Quartal **¥19.99** / Jahr **¥69.99**
   - **PayPal (Ausland / ohne Alipay)**: monatliche automatische Verlängerung, jederzeit kündbar
     - Premium Monthly, ca. **$1/Monat** (gemäß Anzeige auf der Abo-Seite; automatische Verlängerung)
3. Sobald gewählt wurde:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Das Skript liefert den Dateipfad der Zahlungsseite — **direkt per Systembefehl öffnen** (Windows: `start <Datei>`; macOS: `open <Datei>`; Linux: `xdg-open <Datei>`). Der Browser springt automatisch zur offiziellen Kasse von Alipay oder PayPal; der Nutzer schließt dort die Zahlung oder die Einzugsermächtigung ab.
4. Alle 10–15 Sekunden `query` ausführen, bis `paid` oder `ACTIVE` zurückkommt (Zahlung/Autorisierung meist in wenigen Sekunden bis einer Minute). Schließt der Nutzer die Zahlungsseite zwischendurch → einfach erneut `create-order` (alte Bestellungen bzw. offene Abos schließen bzw. laufen nach 2 Stunden automatisch ab; nicht darum kümmern).
5. Der WeChat-QR-Kanal wird manuell bestätigt, der Zahlungseingang kann sich verzögern; Huawei IAP gibt es nur in der HarmonyOS-App. Diese beiden macht der Skill nicht — nach der Zahlung geht es ganz normal mit Schritt 7 weiter.

## Schritt 7: Volles Login (Link 2)

Nach bestätigtem Zahlungseingang zuerst den Login-Status mit der aktuellen Abo-Angabe tauschen, dann den Link direkt zur Startseite erzeugen:

```
POWPOW_REGISTER_PASSWORD=<Passwort> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

Link an den Nutzer senden: **Nach dem Öffnen direkte Landung auf der Startseite mit vollständigem Mitgliedsstatus** — damit ist der komplette Registrierungsablauf abgeschlossen.

## Schritt 8: Abschluss

1. `node scripts/powpow-register.mjs cleanup` — die temporäre Statusdatei (Sitzungs-Credentials) auf diesem Rechner löschen.
2. Eine „Kontokarte" aushändigen: Benutzername, E-Mail, Mitglieds-Ablaufdatum (das Passwort nicht erneut anzeigen — im Generierungsmodus wurde es beim Generieren gespeichert; ein selbst gewähltes kennt die Nutzer:in ohnehin).
3. Zum Ausprobieren anleiten: Karte erkunden, ersten Reisetagebuch-Eintrag posten (→ an powpow-simple übergeben).
4. Erweiterungen empfehlen: der Skill `@durenzidu/powpow-integration` und das Plugin `@durenzidu/openclaw-channel-powpow` — Bubble in den eigenen agent des Nutzers integrieren; auf Wunsch die Installationsbefehle geben.
5. Mit einem „Nächster Schritt"-Block abschließen.

## Conversation-UX

Übernimm den serviceorientierten Ton, der bei powpow üblich ist:

- **Der Nutzer ist das Subjekt des Satzes** — „Du kannst …" schlägt „Ich brauche dich, …"; keine Belehrungen, keine Herablassung.
- **Pro Runde nur eine Entscheidung vorantreiben**; bevor du Informationen anforderst, erst den Grund nennen.
- **Jede Antwort endet** mit einem festen „Nächster Schritt"-Block (Trennlinie + 👉 + eine einzelne Aktion + ein Satz „Sobald du das erledigt hast, werde ich …"), z. B.:
  ```
  ────────────────────
  👉 Das musst du jetzt tun: Such im Postfach den 6-stelligen Verifizierungscode und schick ihn mir direkt
     (sobald er da ist, lege ich dein Konto sofort an)
  ```
- **Keine unaufgeforderte Sicherheitspredigt zum Passwort**; interne Mechanismen, Rate Limits oder Sicherheitsdesign nur auf Nachfrage erklären.
- Gerade wenn der agent etwas erledigt: Fortschritt melden — nach jedem Skriptschritt in einem Satz sagen, was gerade passiert ist („Das Konto steht", „Die Zahlungsseite ist geöffnet").

## Harte Regeln

- **Credential-Sicherheit**: Das Passwort wird ausschließlich über die Umgebungsvariable `POWPOW_REGISTER_PASSWORD` an das Skript übergeben, **niemals** in Kommandozeilen-Argumente (in der Prozessliste sichtbar) und in keine Datei geschrieben (die einmalige Anzeige im Generierungsmodus dient nur dazu, dass der Nutzer es speichert; danach wird es nicht wiederholt). Der Verifizierungscode wird nur für die offizielle Registrierungs-API verwendet und danach verworfen.
- **Offizielle Grenze**: Alle Anfragen gehen ausschließlich an `https://global.powpow.online` (im Skript fest eingebaut); Nutzerdaten gehen niemals an Drittadressen.
- **Zahlungsgrenze**: Der agent erstellt nur Aufträge, öffnet die Kasse und prüft den Zahlungseingang; er fasst **niemals** das Alipay-/PayPal-Konto/Zahlungs-Credentials des Nutzers an und verspricht kein „Bezahlen für dich".
- **Die Paywall ist kein Bug**: Dass pending-Konten die Abo-/Rückkehrseite sehen dürfen, ist eingeplante Freigabe; dass Inhaltsseiten blockiert werden, ist die normal arbeitende Paywall der Plattform — nicht umgehen.
- **Rückfallfreiheit**: Sobald der Nutzer etwas selbst machen will oder die Umgebung das Skript nicht hergibt, jederzeit in den reinen Anleitungsmodus zurückfallen — Links geben, Regeln erklären, gemeinsam Fehler suchen.
- Keine Plattformregeln erfinden: Feldregeln, Fehlermeldungen und Rate-Limit-Parameter stammen alle aus dem Plattformcode (`references/registration-flow.md` nennt die Quellen); bei Plattform-Updates zählt das tatsächliche Verhalten.
- Für Bilder ausschließlich die Screenshots aus dem Paket unter `assets/screenshots/` verwenden (Einsatzzwecke siehe `references/screenshots.md`).
- Jede Runde mit einem „Nächster Schritt"-Block beenden, damit der Nutzer immer weiß, was gerade zu tun ist.

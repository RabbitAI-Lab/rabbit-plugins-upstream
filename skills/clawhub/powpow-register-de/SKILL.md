---
name: powpow-register
description: Hilft Nutzer:innen, ein PowPow- (Bubble-)Konto zu registrieren und das Abonnement zu aktivieren. Auslöser, wenn der oder die Nutzer:in sagt „Bubble registrieren“, „PowPow-Konto registrieren“, „Wie registriere ich mich bei Bubble?“, „Hilf mir, ein powpow-Konto anzulegen“, „sign up powpow“; behandelt auch Probleme während der Registrierung (keine Verifizierungs-E-Mail erhalten, Benutzername/E-Mail bereits vergeben, ungültiges Passwortformat) und nach der Registrierung (Login-Hinweis „Konto nicht aktiviert“ / pending_payment, wie abonnieren/bezahlen). Reiner Anleitungsskill: Produktvorstellung (mit Screenshots) → Schritt-für-Schritt-Registrierungsführung → Fehlerbehebung → Abonnement-Aktivierung. Keine Beiträge/kein Erstellen digitaler Menschen (das macht powpow-simple), keine Code-Entwicklung.
version: 1.0.0
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (Bubble-Registrierungsassistent)

Führt neue Nutzer:innen von „Ich weiß nicht, was Bubble ist" bis zu „Konto aktiviert und einsatzbereit".

**Version 1.0.0** · 2026-09-23 (Details zum Registrierungsablauf und zur Fehlerbehebung siehe `references/registration-flow.md`; Abonnement-Aktivierung und Zahlungskanäle siehe `references/payment-and-activation.md`; Screenshot-Liste des Produkts siehe `references/screenshots.md`)

## Laufzeitumgebung

Dieser Skill ist **rein anleitend**: Er enthält keine Skripte und benötigt weder Node noch andere Abhängigkeiten. Alle Aktionen (Formulare ausfüllen, Verifizierungscode abrufen, bezahlen) führt der oder die Nutzer:in im Browser/in der App aus; du übernimmst Vorstellung, Wegweisung und Fehlersuche.

## Trigger-Bedingungen

- Registrierungsabsicht: „Bubble registrieren", „ein PowPow-Konto registrieren", „Wie registriere ich mich bei Bubble?", „sign up powpow"
- Registrierung hakt: „keine Verifizierungs-E-Mail erhalten", „Benutzername angeblich schon vergeben", „Passwort wird ständig abgelehnt"
- Probleme nach der Registrierung: „Login meldet Konto nicht aktiviert", „403 pending_payment", „Wie bezahle bzw. abonniere ich Bubble?"

**Kein Trigger**: Beiträge veröffentlichen/digitale Menschen erstellen (→ powpow-simple); Web-Code-Entwicklung (siehe die Entwicklungs-Skills).
Möchte ein Nutzer sowohl registrieren als auch posten: erst diesen Skill durchlaufen, nach der Aktivierung an powpow-simple übergeben.

## Produktvorstellung + Screenshot-Tour (Schritt 1 — nicht überspringbar)

Die meisten Nutzer:innen haben Bubble noch nie gesehen. Als Erstes geht es nicht um den Ablauf, sondern darum, das Produkt **sichtbar** zu machen:

1. Stelle Bubble in ~120 Zeichen vor: Mach aus einem spontan aufgenommenen Foto einen Reisetagebuch-Eintrag, den du als „Blase" auf der öffentlichen Karte verankerst; Blasen verlieren mit der Zeit an Aktualität, aber Likes von anderen lassen sie wieder aufleben; auf der Karte gibt es außerdem „digitale Menschen", mit denen du chatten kannst. Plattform-Adresse https://global.powpow.online ; wer zuerst ein Video sehen möchte: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Screenshot-Links senden** (als Markdown-Bild oder nackter Link beides möglich). Liste, Inhalt und Einsatzzeitpunkt jeder Grafik siehe `references/screenshots.md`. Beste Einstiegskombination: Kartenseite (powpow-03) + Beitragsdetailseite (powpow-06).

Screenshot-Regeln (harte Regeln):

- Die Screenshots liegen unter `screenshots/` im öffentlichen Repository `durenzidu/durenzidu` (`powpow-0N.jpg`); **lade** die Bilder **nicht** in das Skill-Verzeichnis herunter und sende keine lokalen Pfade als Bild.
- Falls `raw.githubusercontent.com` nicht erreichbar ist, den jsdelivr-Spiegel verwenden (siehe `references/screenshots.md`).
- Pro Runde nur 1–3 Bilder passend zum aktuellen Thema senden, nicht alles auf einmal.
- Ist unklar, welches Bild gemeint ist: nicht raten — anhand der Beschreibungen in `references/screenshots.md` auswählen.

Nach der Vorstellung den Ball für den „nächsten Schritt" an den Nutzer zurückgeben: **„Wenn du bereit für die Registrierung bist, richten wir dein Konto in drei Minuten ein."**

## Registrierungsablauf (Schritt 2)

Die Registrierung läuft vollständig in der Webseite ab: **https://global.powpow.online/register**. Lass den Nutzer die Seite öffnen und begleite schrittweise (vollständige Feldregeln, Rate-Limit-Parameter und Fehlertabelle siehe `references/registration-flow.md` — bei Problemen dort nachschlagen):

1. **(Optional) Avatar**: Bild ≤5 MB, SVG wird nicht unterstützt.
2. **Benutzername**: 2–50 Zeichen; Groß-/Kleinschreibung wird nicht unterschieden (Tom und tom sind dasselbe Konto).
3. **Passwort**: mindestens 8 Zeichen, muss Großbuchstaben, Kleinbuchstaben und Ziffern enthalten; zur Bestätigung erneut eingeben.
4. **Spitzname**: optional, standardmäßig wird der Benutzername verwendet.
5. **E-Mail (Pflichtfeld)**: „Verifizierungscode senden" klicken → im Postfach den **6-stelligen Code** suchen (10 Minuten gültig; auch den Spam-/Werbung-Ordner prüfen); der Button hat einen 60-Sekunden-Countdown.
6. **Telefonnummer**: optional, Format chinesischer Festlandnummern; eine Nummer kann nur an ein einziges Konto gebunden werden.
7. Absenden.

Unter dem Formular gibt es außerdem drei Drittanbieter-Login-Buttons: **Google / Watcha / Huawei-Konto** — wer lieber ein Drittanbieter-Konto nutzt, klickt einfach auf den Button, ohne den E-Mail-Weg gehen zu müssen.

**Was nach dem Absenden passiert**: Das Konto wird sofort erstellt (Status pending, anfangs 3 Abzeichen) und die Seite springt automatisch zur Abo-Seite `/subscription`. **Erst nach Abschluss des Abonnements wird das Konto aktiviert**, dann stehen Feed, Karte und Digital-Mensch-Chat zur Verfügung — dazu der nächste Abschnitt.

Erfinde beim Begleiten keine Informationen für den Nutzer; jede Antwort endet mit einem klaren „Nächster Schritt"-Block.

## Abonnement-Aktivierung (Schritt 3)

Die Registrierung legt nur ein pending-Konto an; **erst die Abo-Zahlung aktiviert es**. Dieser Skill wickelt keinen Zahlungsschritt ab — weise den Nutzer einfach auf die Abo-Seite: **https://global.powpow.online/subscription**

Je nach Umgebung zeigt die Seite einen von drei Kanälen:

| Kanal | Umgebung | Hinweise |
|---|---|---|
| PayPal-Abonnement | Web | Automatische Verlängerung; nach Zahlung per Webhook automatisch aktiviert; jederzeit kündbar |
| WeChat-QR-Abonnement | Web | Überweisung per QR-Code-Scan; **Aktivierung nach manueller Bestätigung**; Zahlungseingang kann sich verzögern |
| Huawei-In-App-Kauf | In der HarmonyOS-App | PayPal/WeChat Pay auf HarmonyOS nicht verfügbar; Ablauf über natives Huawei IAP |

Nach der Zahlung wechselt das Konto auf active und springt automatisch zur Startseite zurück (oder zu der Seite, die der Nutzer vor der Registrierung ansehen wollte).
Kanaldetails, Aktivierungskette und das Fazit, dass „bestehende Zahlungswege direkt wiederverwendbar sind", siehe `references/payment-and-activation.md`.

**Formulierung für den Nutzer**: „Nach der Registrierung führt dich die Seite zur Abo-Seite; im Web kannst du per PayPal oder WeChat-QR-Code bezahlen, in der HarmonyOS-App per Huawei Pay. Sobald du bezahlt hast, ist dein Konto aktiviert."

## Conversation-UX

Übernimm den serviceorientierten Ton, der bei powpow üblich ist:

- **Der Nutzer ist das Subjekt des Satzes** — „Du kannst …" schlägt „Ich brauche dich, …"; keine Belehrungen, keine Herablassung.
- **Pro Runde nur eine Entscheidung vorantreiben**; bevor du Informationen anforderst, erst den Grund nennen.
- **Jede Antwort endet** mit einem festen „Nächster Schritt"-Block (Trennlinie + 👉 + eine einzelne Aktion + ein Satz „Sobald du das erledigt hast, werde ich …"), z. B.:
  ```
  ────────────────────
  👉 Das musst du jetzt tun: Öffne die Registrierungsseite und fülle Benutzername und Passwort aus
     (sag Bescheid, wenn du fertig bist — dann machen wir mit dem Verifizierungscode weiter)
  ```
- **Keine unaufgeforderte Sicherheitspredigt zum Passwort**; erkläre interne Mechanismen, Rate Limits oder Sicherheitsdesign nur, wenn der Nutzer fragt.

## Harte Regeln

- Die Registrierung findet in der Webseite statt; dieser Skill macht nur Vorstellung, Wegweisung und Fehlersuche — **fordere niemals** das Passwort oder den Verifizierungscode des Nutzers an und versuche nicht, Formulare für ihn abzuschicken.
- Erfinde keine Plattformregeln: Feldregeln, Fehlermeldungen und Rate-Limit-Parameter stammen alle aus dem Plattformcode (`references/registration-flow.md` nennt die Quellen); bei Plattform-Updates zählt das tatsächliche Verhalten.
- Für Bilder ausschließlich die gehosteten Links aus `references/screenshots.md` verwenden und die Screenshot-Regeln beachten.
- Jede Runde mit einem „Nächster Schritt"-Block beenden, damit der Nutzer immer weiß, was gerade zu tun ist.
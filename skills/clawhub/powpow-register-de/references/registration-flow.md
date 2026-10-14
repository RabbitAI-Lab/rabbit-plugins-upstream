# Registrierungsablauf im Detail — powpow-register

Zum Nachschlagen bei der Fehlerbehebung. Alle Regeln stammen aus dem Plattform-Quellcode (Next.js — Frontend und Backend validieren konsistent); die Quellen sind angegeben.
Bei Plattform-Updates zählt das tatsächliche Online-Verhalten.

## Einstiege

- Registrierungsseite: https://global.powpow.online/register
- Login-Seite: https://global.powpow.online/login
- Abo-Seite: https://global.powpow.online/subscription
- Wer über einen Share-Link o. Ä. mit `?next=...` hereinkommt, wird nach Registrierung + Zahlung automatisch zur ursprünglichen Seite zurückgeleitet.

## Formularfelder und Regeln

| Feld | Pflicht | Regeln | Quellcode-Stelle |
|---|---|---|---|
| Avatar | optional | Bild ≤5 MB, SVG wird nicht unterstützt; serverseitige automatische Komprimierung (>100 KB: auf 400×400 / Qualität 90 komprimiert) | `src/app/api/auth/register/route.ts` |
| Benutzername | Pflicht | 2–50 Zeichen; nach trim **kleingeschrieben** gespeichert (Tom und tom gelten als derselbe Benutzername; Registrierungs- wie Login-Seite sind case-insensitiv) | wie oben (zod schema) |
| Passwort | Pflicht | 8–100 Zeichen; muss Großbuchstaben, Kleinbuchstaben und Zahlen zugleich enthalten | wie oben |
| Passwort bestätigen | Pflicht | muss mit dem Passwort übereinstimmen (nur Frontend-Prüfung) | `src/app/(public)/register/page.tsx` |
| Spitzname | optional | ≤100 Zeichen; wenn nicht ausgefüllt, wird standardmäßig der Benutzername genommen | register route |
| E-Mail | **Pflicht** | gültiges E-Mail-Format, ≤255 Zeichen; mit einer E-Mail kann nur ein Konto registriert werden | register route |
| E-Mail-Verifizierungscode | **Pflicht** | 6-stellige Zahl; **10 Minuten gültig**; wird bei erfolgreicher Prüfung sofort ungültig; beim erneuten Senden wird der alte Code als verwendet markiert | `src/lib/email-verification.ts` |
| Telefonnummer | optional | Festlandchina-Nummer: beginnt mit `1[3-9]`, insgesamt 11 Stellen; eine Telefonnummer lässt sich nur an ein Konto binden | register route |

Die Seite bietet außerdem drei Drittanbieter-Login-Buttons: **Google, Watcha, Huawei-Konto** (`GoogleSignInButton` /
`WatchaLoginButton` / `HuaweiLoginButton`). Drittanbieter-Konten haben kein lokales Passwort; ein späterer Login per Passwort liefert
「该账号未设置密码，请使用其他方式登录」 (Für dieses Konto ist kein Passwort festgelegt; bitte melde dich auf andere Weise an).

## Rate-Limit- und Brute-Force-Schutz-Parameter

| Aktion | Limit | Quelle |
|---|---|---|
| Registrierung absenden | **3 mal/Minute/IP**, darüber 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Verifizierungscode senden | pro IP 1 mal/Minute **und** pro E-Mail 1 mal/Minute, darüber 429; Frontend-Button mit 60-Sekunden-Countdown | `src/app/api/auth/register/send-code/route.ts` |
| Verifizierungscode prüfen | pro E-Mail höchstens **5 Versuche** innerhalb von 10 Minuten; am Limit wird selbst bei richtigem Code abgelehnt — der Code muss neu angefordert werden | `src/lib/email-verification.ts` |
| Code bei vergessenem Passwort | 1 mal/Minute/IP | `src/app/api/auth/forgot-password/route.ts` |
| Login | 5 mal/Minute/IP; dasselbe Konto nach **5 Fehlversuchen in Folge 30 Minuten gesperrt** (423), mit Anzeige der abnehmenden Restversuche | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Privacy-Verhalten**: Beim Senden des Verifizierungscodes / bei vergessenem Passwort geben die Endpunkte — ob die E-Mail bereits registriert ist oder nicht existiert —
einheitlich eine Erfolgsmeldung zurück und verraten nicht, ob die E-Mail bereits registriert ist.

## Gleichwertigkeit von Agent-Durchführungsmodus und Web-Registrierung

Das Skill-Skript ruft **dieselben öffentlichen APIs** auf (`/api/auth/register`, `send-code`, `login`,
`/api/auth/me`) und durchläuft damit exakt dieselben Prüf-, Rate-Limit- und Fehlerpfade wie das Absenden des Registrierungsformulars — alle Regeln dieser
Datei gelten für beide Modi gleichermaßen. Skript-Sequenz und Befehls-Vertrag siehe `references/agent-flow.md`.

## Statusübergänge nach erfolgreicher Registrierung

1. Der Nutzer wird mit `accountStatus: 'pending'` in der Datenbank angelegt, inklusive der anfänglichen **3 Abzeichen** (register route).
2. Der Server setzt gleichzeitig zwei HttpOnly-Cookies: JWT (direkter Zugriff auf `/subscription` möglich) und
   pendingUserToken (Identitätsnachweis für den Abo-Ablauf).
3. Die Registrierungsseite erkennt `pending_payment` → Weiterleitung auf `/subscription` (der `next`-Rückkehrparameter bleibt erhalten);
   im Agent-Durchführungsmodus erzielt `me?token=…&redirect=/subscription` denselben Effekt.
4. Zahlung abgeschlossen → `accountStatus` wechselt zu `active` (**Alipay: serverseitige automatische Aktivierung über notify**;
   PayPal: automatische Aktivierung über Webhook; WeChat-QR: manuelle Bestätigung; Huawei IAP über `activate-huawei`).
   Details siehe `payment-and-activation.md`.

Nicht aktivierte (pending) Nutzer erhalten beim Aufruf der Kern-APIs (Feed, Karte, Gespräche mit digitalen Menschen, Check-in usw.) durchgängig 403;
ausgenommen sind Links auf geteilte Beiträge (bleiben öffentlich zugänglich).

## Troubleshooting-Tabelle häufiger Fehler

| Symptom | Ursache | Was tun |
|---|---|---|
| 「用户名已存在」 (Der Benutzername existiert bereits) | Benutzername vergeben (case-insensitiv) | einen anderen Benutzernamen wählen |
| 「邮箱已被使用」 (Die E-Mail ist bereits in Verwendung) | E-Mail schon registriert | E-Mail wechseln; oder stattdessen Login + 「忘记密码」 (Passwort vergessen), um das alte Konto zurückzuholen |
| 「邮箱验证码错误或已过期」 (Der E-Mail-Verifizierungscode ist falsch oder abgelaufen) | Code falsch eingegeben / älter als 10 Minuten / nach mehr als 5 Fehlversuchen abgelehnt | 「重新发送」 (Erneut senden) anklicken und den Code aus der **neuesten** E-Mail verwenden |
| Verifizierungscode kommt nicht an | 60-Sekunden-Rate-Limit; oder im Spam-/Werbungsordner gelandet | Countdown abwarten und erneut senden; Spam-Ordner durchforsten |
| 「手机号已被使用」 (Die Telefonnummer ist bereits in Verwendung) | Telefonnummer bereits an ein anderes Konto gebunden | Telefonnummer weglassen (optional) oder Nummer wechseln |
| 「注册请求过于频繁」 (Registrierungsanfragen zu häufig) / 429 | Registrierungslimit 3 mal/Minute/IP erreicht | ein paar Minuten warten und erneut versuchen |
| 409 「用户名或邮箱已被注册」 (Benutzername oder E-Mail bereits registriert) | beim Absenden zeitgleich mit jemand anderem kollidiert (Concurrency-Fallback) | Benutzername oder E-Mail ändern und erneut versuchen |
| 「图片大小不能超过5MB」 (Das Bild darf 5 MB nicht überschreiten) / 「不支持 SVG」 (SVG wird nicht unterstützt) | Avatar regelwidrig | Bild wechseln oder Avatar überspringen |
| Registrierung erfolgreich, aber Login 403 「请完成订阅以激活账户」 (Bitte schließe das Abonnement ab, um dein Konto zu aktivieren) | Konto ist noch pending (erwarteter Zustand vor der Zahlung) | Vor der Zahlung: normal — zuerst das Abo abschließen; nach der Zahlung weiterhin 403: es wurde ein altes JWT verwendet — im Skript-Modus zuerst `refresh-login` für einen neuen Login-Status |
| Login 423 「账户已锁定」 (Das Konto ist gesperrt) | 5× in Folge ein falsches Passwort | 30 Minuten warten |
| Login 401 「还剩 N 次尝试机会」 (Noch N Versuche übrig) | falsches Passwort, kurz vor der Sperre | in Ruhe nochmal versuchen — oder direkt über 「忘记密码」 (Passwort vergessen) gehen |
| 「该账号未设置密码，请使用其他方式登录」 (Für dieses Konto ist kein Passwort festgelegt; bitte melde dich auf andere Weise an) | Drittanbieter-Konto (Google/Watcha/Huawei) | mit dem ursprünglichen Drittanbieter-Button einloggen |
| 「该账号已注销」 (Dieses Konto wurde deaktiviert) | Konto wurde deaktiviert (deactivate) | erneut registrieren |

## Login-Wissenswertes (für die gelegentliche Fehlersuche)

Der Login akzeptiert **Benutzername / E-Mail / Telefonnummer** als kombinierte Eingabe (jede der drei Angaben taugt als Kontoname).
Passwort vergessen: Login-Seite → 「忘记密码」 (Passwort vergessen) → Registrierungs-E-Mail eingeben, den 6-stelligen Code empfangen → zurücksetzen.

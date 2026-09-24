# Registrierungsablauf im Detail — powpow-register

Nachschlagewerk für die Fehlerbehebung. Alle Regeln stammen aus dem Plattform-Quellcode (konsistente Next.js-Validierung von Frontend und Backend), mit Quellenangabe.
Bei Plattform-Updates zählt das tatsächliche Verhalten.

## Einstieg

- Registrierungsseite: https://global.powpow.online/register
- Login-Seite: https://global.powpow.online/login
- Abo-Seite: https://global.powpow.online/subscription
- Wer über einen geteilten Link mit `?next=...` kommt, wird nach Registrierung + Bezahlung automatisch zur ursprünglichen Seite zurückgeführt.

## Formularfelder und Regeln

| Feld | Pflicht | Regel | Quelle |
|---|---|---|---|
| Avatar | Optional | Bild ≤5 MB, SVG wird nicht unterstützt; serverseitig automatische Komprimierung (>100 KB wird auf 400×400 / Qualität 90 komprimiert) | `src/app/api/auth/register/route.ts` |
| Benutzername | Pflicht | 2–50 Zeichen, nach Trim in **Kleinschreibung** gespeichert (Tom und tom gelten als derselbe Benutzername; Registrierung und Login unterscheiden nicht zwischen Groß-/Kleinschreibung) | wie oben (zod Schema) |
| Passwort | Pflicht | 8–100 Zeichen, muss Großbuchstaben, Kleinbuchstaben und Ziffern enthalten | wie oben |
| Passwort bestätigen | Pflicht | Muss mit dem Passwort übereinstimmen (nur Frontend-Prüfung) | `src/app/(public)/register/page.tsx` |
| Spitzname | Optional | ≤100 Zeichen; Standard ist der Benutzername | register route |
| E-Mail | **Pflicht** | Gültiges E-Mail-Format, ≤255 Zeichen; mit einer E-Mail kann nur ein Konto registriert werden | register route |
| E-Mail-Verifizierungscode | **Pflicht** | 6-stellige Zahl; **10 Minuten gültig**; nach erfolgreicher Prüfung ungültig; erneutes Senden markiert den alten Code als verwendet | `src/lib/email-verification.ts` |
| Telefonnummer | Optional | Festland-China-Nummer, beginnt mit `1[3-9]`, insgesamt 11 Ziffern; eine Nummer kann nur an ein Konto gebunden werden | register route |

Die Seite bietet außerdem drei Drittanbieter-Login-Buttons: **Google, Watcha, Huawei-Konto** (`GoogleSignInButton` / `WatchaLoginButton` / `HuaweiLoginButton`). Drittanbieter-Konten haben kein lokales Passwort; wer später mit einem Passwort einloggen will, erhält „该账号未设置密码，请使用其他方式登录" (Für dieses Konto wurde kein Passwort festgelegt, bitte melde dich mit einer anderen Methode an).

## Rate-Limits und Anti-Brute-Force-Parameter

| Verhalten | Limit | Quelle |
|---|---|---|
| Registrierungs-Submit | **3×/Minute/IP**, darüber 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Verifizierungscode senden | Gleiche IP 1×/Minute **und** gleiche E-Mail 1×/Minute, darüber 429; Frontend-Button mit 60-Sekunden-Countdown | `src/app/api/auth/register/send-code/route.ts` |
| Code-Prüfung | Maximal **5 Versuche** pro E-Mail innerhalb von 10 Minuten; ab der Obergrenze wird auch ein richtiger Code abgelehnt, neuer Code nötig | `src/lib/email-verification.ts` |
| Passwort-vergessen-Code | 1×/Minute/IP | `src/app/api/auth/forgot-password/route.ts` |
| Login | 5×/Minute/IP; **5 Fehlversuche in Folge sperren das Konto für 30 Minuten** (423), währenddessen Hinweis mit abnehmender Versuchszahl | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Privatsphäre-Schutz**: Beim Senden des Verifizierungscodes / Passwort-vergessen-Codes liefert die Schnittstelle unabhängig davon, ob die E-Mail registriert ist oder nicht, dieselbe Erfolgsmeldung zurück — es wird nicht verraten, ob eine E-Mail existiert.

## Statusablauf nach erfolgreicher Registrierung

1. Der Nutzer wird mit `accountStatus: 'pending'` gespeichert, anfangs **3 Abzeichen** (register route).
2. Der Server setzt zugleich zwei HttpOnly-Cookies: JWT (ermöglicht direkten Zugriff auf `/subscription`) und pendingUserToken (Identitätsnachweis für den Abo-Ablauf).
3. Die Registrierungsseite erkennt `pending_payment` → Sprung zu `/subscription` (der `next`-Rücksprungparameter bleibt erhalten).
4. Zahlung abgeschlossen → `accountStatus` wird `active` (PayPal aktiviert automatisch per Webhook; WeChat-QR-Code per manueller Bestätigung; Huawei IAP über `activate-huawei`). Siehe `payment-and-activation.md`.

Aufrufe der Kern-APIs (Feed, Karte, Digital-Mensch-Chat, Check-ins usw.) durch nicht aktivierte (pending) Nutzer liefern durchgängig 403; ausgenommen sind geteilte Beitragslinks (bleiben öffentlich zugänglich).

## Tabelle häufiger Fehler

| Meldung | Ursache | Was tun |
|---|---|---|
| 「用户名已存在」(Benutzername existiert bereits) | Benutzername vergeben (ohne Groß-/Kleinschreibung) | Anderen Benutzernamen wählen |
| 「邮箱已被使用」(E-Mail bereits verwendet) | E-Mail bereits registriert | Andere E-Mail verwenden; oder per Login + „Passwort vergessen" das alte Konto wiederherstellen |
| 「邮箱验证码错误或已过期」(E-Mail-Verifizierungscode falsch oder abgelaufen) | Code falsch eingegeben / über 10 Minuten / nach mehr als 5 Versuchen abgelehnt | „Erneut senden" klicken und den Code aus der **neuesten** E-Mail verwenden |
| Kein Verifizierungscode erhalten | 60-Sekunden-Limit; oder im Spam-/Werbung-Ordner gelandet | Countdown abwarten und erneut senden; Spam-Ordner prüfen |
| 「手机号已被使用」(Telefonnummer bereits verwendet) | Nummer an ein anderes Konto gebunden | Telefonnummer entfernen (optional) oder andere Nummer verwenden |
| 「注册请求过于频繁」/ 429 (Registrierungsanfragen zu häufig) | Limit von 3 Registrierungen/Minute/IP erreicht | Ein paar Minuten warten und erneut versuchen |
| 409「用户名或邮箱已被注册」(Benutzername oder E-Mail bereits registriert) | Beim Absenden mit anderem Nutzer kollidiert (Concurrency-Fallback) | Benutzername oder E-Mail ändern und erneut versuchen |
| 「图片大小不能超过5MB」/「不支持 SVG」(Bild darf 5 MB nicht überschreiten / SVG wird nicht unterstützt) | Avatar entspricht nicht den Regeln | Anderes Bild verwenden oder Avatar überspringen |
| Registrierung erfolgreich, aber Login 403「请完成订阅以激活账户」(Bitte schließe dein Abonnement ab, um dein Konto zu aktivieren) | Konto ist noch pending | Nach dem Login dem Hinweis auf der Seite folgen und auf `/subscription` das Abonnement abschließen |
| Login 423「账户已锁定」(Konto gesperrt) | Passwort 5-mal falsch eingegeben | 30 Minuten warten |
| Login 401「还剩 N 次尝试机会」(Noch N Versuche übrig) | Falsches Passwort, kurz vor der Sperrung | Erst überlegen, dann versuchen; oder direkt „Passwort vergessen" nutzen |
| 「该账号未设置密码，请使用其他方式登录」(Für dieses Konto wurde kein Passwort festgelegt, bitte melde dich mit einer anderen Methode an) | Drittanbieter-Konto (Google/Watcha/Huawei) | Mit dem ursprünglichen Drittanbieter-Button anmelden |
| 「该账号已注销」(Dieses Konto wurde deaktiviert) | Konto wurde deaktiviert | Neues Konto registrieren |

## Login-Wissen (nützlich auch bei der Fehlersuche)

Der Login akzeptiert eine kombinierte Eingabe aus **Benutzername / E-Mail / Telefonnummer** (jede der drei Varianten funktioniert als Kontoname).
Passwort vergessen: Login-Seite → „Passwort vergessen" → registrierte E-Mail eingeben, 6-stelligen Code erhalten → zurücksetzen.
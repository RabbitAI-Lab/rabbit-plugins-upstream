# Abo-Aktivierung und Zahlung — powpow-register

## Fazit (zuerst die Antwort)

**Der Alipay-Kanal ist live (ab 2026-10-07) und ist der von diesem Skill bevorzugte Zahlungsweg; der agent kann Bestellung und Verfolgung des Zahlungseingangs übernehmen.**
Nutzer im Ausland / ohne Alipay fallen auf PayPal zurück; WeChat-QR (manuelle Bestätigung) und Huawei IAP gibt es weiterhin, sie werden vom Skill aber nicht stellvertretend ausgeführt.

Die Verantwortlichkeitsgrenze im Zahlschritt: Der agent darf **Bestellungen erstellen, die Kasse öffnen und den Zahlungseingang abfragen**; er kommt **niemals** mit dem Alipay-Konto /
den Zahlungs-Credentials des Nutzers in Berührung und verspricht niemals „Ich zahle für dich". Die Zahlungshandlung führt immer der Nutzer selbst an der offiziellen Alipay-Kasse aus.

## Alipay-Kanal (vibepay, bevorzugt)

Einmalkauf-Modell: einmal zahlen, die entsprechende Laufzeit wird freigeschaltet, **keine automatische Verlängerung**. Die Pläne sind fest in
`src/lib/alipay-vibepay.ts` hinterlegt (`ALIPAY_PACKAGES`):

| key | planId | Name | Preis | Laufzeit |
|---|---|---|---|---|
| `monthly` | alipay-monthly | Monats-Mitgliedschaft | ¥6.99 | 30 Tage |
| `quarterly` | alipay-quarterly | Quartals-Mitgliedschaft | ¥19.99 | 90 Tage |
| `yearly` | alipay-yearly | Jahres-Mitgliedschaft | ¥69.99 | 365 Tage |

### Endpunkt-Vertrag (vom Skill-Skript bereits gekapselt; der agent baut keine Anfragen selbst)

| Endpunkt | Methode | Beschreibung |
|---|---|---|
| `/api/payment/alipay/create-order` | POST | Benötigt `Authorization: Bearer <JWT>` (ein pending-Nutzer genügt). body `{package}` → Rückgabe `{paymentHtml, outTradeNo, amount, planName}`; `paymentHtml` ist eine Formularseite, die sich automatisch an das Alipay-Gateway absendet |
| `/api/payment/alipay/query` | GET `?outTradeNo=` | Ebenfalls Bearer-Authentifizierung. Rückgabe `paid` / `pending` / `closed` / `unknown` |
| `/api/payment/alipay/notify` | POST (Server-Callback von Alipay) | Prüfung der fünf Signatur-Elemente (Signatur, app_id, Betrag stimmt überein, TRADE_SUCCESS/TRADE_FINISHED, Händler-Eindeutigkeit) → **idempotentes** Aktualisieren der Bestellung + Abo anlegen + Konto aktivieren. Der Skill rührt diesen Endpunkt niemals an |
| `/payment/alipay/return` | Browser-Rückkehrseite | Öffentlicher Pfad; zeigt nach der Zahlung die Bestätigung 「支付成功」 (Zahlung erfolgreich) und pollt innerhalb der Seite den echten Backend-Status |

- Unbezahlte Bestellungen **schließen sich nach 2 Stunden automatisch**; bricht der Nutzer mittendrin ab → einfach erneut `create-order`, um die alte Bestellung braucht man sich nicht zu kümmern.
- Das Skript schreibt `paymentHtml` in eine temporäre HTML-Datei; der agent öffnet sie per Systembefehl, und der Nutzer gelangt direkt in die Alipay-Kasse
  (per QR-Code scannen oder per Alipay-Login zahlen).

### Aktivierungskette (automatisch, kein manueller Schritt nötig)

notify-Signaturprüfung bestanden → `paymentOrders` als bezahlt markiert → `user_subscriptions` anlegen/verlängern
(`planId`, `currentPeriodEnd` werden nach durationDays berechnet; eine Verlängerung rechnet ab dem ursprünglichen Ablaufdatum weiter) →
`users.accountStatus: active` + `subscriptionStatus: ACTIVE` → die Rückkehrseite pollt paid und zeigt den Erfolg an.

### Nach der Zahlung zwingend den Login-Status erneuern (wichtig)

Im JWT steckt der Abo-Anspruch (bei pending-Konten `NONE`). **Der Zahlungseingang aktualisiert nur die Datenbank, nicht das bereits ausgestellte
JWT** — der Anspruch des alten Tokens bleibt weiterhin NONE; damit direkt einen Login-Link zu erzeugen, wirkt wie „kein Mitglied".
Deshalb führt der Skill nach Bestätigung von `paid` zuerst `refresh-login` aus (erneutes Login für ein neues JWT, der Anspruch wird ACTIVE)
und erzeugt erst danach Link 2. Das ist Design-Verhalten, keine Fehlerbehebung.

## Die vier Kanäle der Abo-Seite

Die Abo-Seite `src/app/(public)/subscription/page.tsx` zeigt je nach Laufzeitumgebung:

| Kanal | Umgebung | Mechanismus | Aktivierung |
|---|---|---|---|
| **Alipay (bevorzugt)** | Web | `AlipayPaymentSection` über die vibepay-Endpunkte (Tabelle oben) | serverseitige automatische Aktivierung über notify, sekundenschnell |
| PayPal-Abo | Web (nicht HarmonyOS) | `/api/subscription/create` → Weiterleitung zur PayPal-Autorisierung; monatliche automatische Verlängerung, jederzeit kündbar (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) setzt automatisch active |
| WeChat-QR-Abo | Web (nicht HarmonyOS) | unten auf der Seite 「微信扫码订阅」 (WeChat-QR-Abonnement): QR-Code scannen und überweisen | **manuelle Bestätigung**, der Eingang kann sich verzögern; nach der Zahlung nicht vorschnell auf Fehlschlag schließen |
| Huawei-In-App-Kauf | in der HarmonyOS-App | nativ `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` aktiviert nach Prüfung der Huawei-Bestellung |

PayPal-Pläne und -Preise werden dynamisch aus `/api/subscription/plans` gelesen; fester Text auf der Seite: Auto-renews. Cancel anytime.

## Status und Weiterleitungen

- Alipay bezahlt → die Rückkehrseite zeigt den Erfolg; PayPal erfolgreich → `/subscription/success` → Konto active →
  automatische Rückleitung zur ursprünglichen Seite aus dem `next`-Parameter (ohne Parameter: Startseite).
- Wer bereits abonniert hat und die Abo-Seite erneut besucht → Anzeige "You're All Set!", nach 3 Sekunden automatisch zurück zur Startseite.
- Zahlung fehlgeschlagen/abgebrochen (PayPal) → `/subscription/cancel`; kann neu angestoßen werden.

## Troubleshooting

| Symptom | Behandlung |
|---|---|
| Alipay bezahlt, `query` bleibt trotzdem pending | notify verzögert sich nur äußerst selten; 30 Sekunden warten und erneut abfragen. Klappt es weiterhin: den Nutzer im Browser den Status der Rückkehrseite prüfen lassen; hilft das auch nicht, den Plattform-Support kontaktieren (dongtao@outlook.com) und die `outTradeNo` nennen |
| Alipay bezahlt, aber mit Link 2 weiterhin blockiert | `refresh-login` wurde ausgelassen (der Anspruch des alten JWT ist nicht aktualisiert) — zuerst `refresh-login`, dann `login-link` |
| Nach der Zahlung weiterhin 403 (PayPal) | Webhooks verzögern sich gelegentlich; neu einloggen und den Status auffrischen |
| Mit WeChat bezahlt, aber nicht freigeschaltet | Die manuelle Bestätigung läuft asynchron; erst nach mehreren Stunden ohne Freischaltung den Plattform-Support kontaktieren |
| Die Abo-Seite meldet "No subscription plans available" | `/api/subscription/plans` hat keine verfügbaren PayPal-Pläne — Konfigurationsproblem auf Plattformseite; Nutzer in Festlandchina nehmen einfach den Alipay-Weg |

## Historische Anmerkung

Im Code existiert außerdem ein **alter** Alipay-Web-Zahlungsweg (`src/lib/alipay.ts`, `/api/payment/create-order`,
¥9.90/¥99 Einmalkauf; ohne konfigurierte Sandbox-Keys Rückfall auf eine simulierte Zahlung); er wurde nie in die Abo-Seiten-UI integriert und hat mit vibepay
nichts zu tun. Der Skill rührt ihn grundsätzlich nicht an; `alipay-vibepay.ts` ist der aktuell gültige Kanal.

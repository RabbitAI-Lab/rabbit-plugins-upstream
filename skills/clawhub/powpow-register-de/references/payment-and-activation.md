# Abonnement-Aktivierung und Bezahlung — powpow-register

## Fazit (erst die Antwort)

**Bestehende Zahlungswege sind direkt wiederverwendbar — der Registrierungsassistent braucht null Zahlungs-Entwicklung.**

Gründe:

1. Die Registrierungsschnittstelle (`src/app/api/auth/register/route.ts`) stellt beim Anlegen des pending-Kontos bereits ein JWT-Cookie + pendingUserToken-HttpOnly-Cookie aus, sodass der Nutzer beim Eintreffen auf `/subscription` schon eingeloggt ist — alle drei Zahlungskanäle hängen an dieser Abo-Seite und aktivieren dasselbe pending-Konto.
2. Die Login-Schnittstelle liefert für pending-Konten 403 + `redirectTo: '/subscription'` und setzt die Cookies genauso — ein Nutzer, der später nachzahlt, wird immer zurück auf dieselbe Seite geführt.
3. Damit ist die Aufgaben-Grenze eines Registrierungs-Assistenz-Skills schlicht „den Nutzer zu /subscription führen"; keine neue Zahlungsschnittstelle, kein neues Bestellmodell, keine Backend-Änderungen nötig.

Zugleich ist zu beachten: Der Zahlungsschritt (PayPal-JS-SDK-Button, WeChat-QR-Code mit manueller Bestätigung, natives Huawei IAP) **macht es unmöglich und unangebracht, per Kommandozeilen-/Chat-Skill für den Nutzer zu zahlen**. Versuche nicht, Zahlungsschnittstellen per Skript anstelle des Nutzers aufzurufen, und fordere keine Zahlungsnachweise des Nutzers an.

## Die drei Kanäle auf der Abo-Seite

Die Abo-Seite `src/app/(public)/subscription/page.tsx` zeigt automatisch den passenden Kanal je nach Laufzeitumgebung:

| Kanal | Umgebung | Mechanismus | Aktivierung |
|---|---|---|---|
| PayPal-Abonnement | Web (nicht HarmonyOS) | `/api/subscription/create` erstellt ein PayPal-Abonnement → Weiterleitung zur PayPal-Autorisierung; monatliche automatische Verlängerung, jederzeit kündbar (`/api/subscription/manage`) | PayPal-Webhook (`BILLING.SUBSCRIPTION.*`) setzt `accountStatus` automatisch auf active |
| WeChat-QR-Abonnement | Web (nicht HarmonyOS) | Bereich „Per WeChat scannen und abonnieren" unten auf der Seite: Überweisung per Scan, **Aktivierung nach manueller Bestätigung** (`WechatQrPaymentSection`) | Manuelle Bestätigung; Zahlungseingang kann sich verzögern — direkt nach der Zahlung nicht vorschnell auf Fehler schließen |
| Huawei-In-App-Kauf (IAP) | In der HarmonyOS-App | In der HarmonyOS-WebView sind PayPal/WeChat Pay nicht verfügbar, die Seite nutzt stattdessen natives `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` prüft die Huawei-Bestellung und aktiviert dann |

Pläne und Preise werden dynamisch von `/api/subscription/plans` gelesen (PayPal-Pläne); der feste Text auf der Seite: Auto-renews. Cancel anytime.

## Status und Weiterleitungen

- Zahlung erfolgreich → `/subscription/success` (PayPal-Callback trägt `subscriptionId`) → Konto active → automatische Rückkehr zur ursprünglichen Seite aus dem `next`-Parameter (sonst Startseite).
- Bereits abonnierte Nutzer, die die Abo-Seite besuchen → zeigt "You're All Set!", nach 3 Sekunden automatisch zurück zur Startseite.
- Zahlungsfehler/Abbruch → `/subscription/cancel`, ein neuer Versuch ist möglich.

## Fehlersuche

| Meldung | Behandlung |
|---|---|
| Nach der Zahlung immer noch 403 | PayPal: der Webhook hängt gelegentlich — aus- und wieder einloggen, um den Status zu aktualisieren (beim Login wird der aktuelle DB-Status erneut geprüft); WeChat: manuelle Bestätigung noch nicht abgeschlossen, etwas warten; Huawei: prüfen, ob die In-App-Zahlungserfolgsseite erschienen ist |
| Abo-Seite zeigt "No subscription plans available" | Auf `/api/subscription/plans` sind keine nutzbaren PayPal-Pläne — ein Konfigurationsproblem auf Plattformseite; den Nutzer bitten, es später erneut zu versuchen |
| Per WeChat bezahlt, aber nicht aktiviert | Die manuelle Bestätigung läuft asynchron; wenn es nach einigen Stunden nicht aktiviert ist, Plattform-Support kontaktieren (dongtao@outlook.com) |

## Hinweis: Alipay

Im Code existiert ein Satz Alipay-Webzahlungen (`src/lib/alipay.ts`, `/api/payment/create-order`, Einmalkauf-Modell: normale Mitgliedschaft ¥9,90 / Premium-Mitgliedschaft ¥99; ohne konfigurierten Sandbox-Schlüssel automatische Degradierung zur simulierte Zahlung), **es ist jedoch nicht in die Abo-Seiten-UI eingebunden** — ungenutzter/vorgesehener Code. Falls Alipay künftig auf der Abo-Seite aktiviert werden soll, lässt sich dieser fertige Code anschließen — das betrifft diesen Skill nicht und dient hier nur als Referenz für plattformseitige Entscheidungen.
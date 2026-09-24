# powpow-register

Der Bubble-Registrierungsassistent für PowPow (OpenClaw-Ausgabe): führt neue Nutzer:innen von „Ich weiß nicht, was Bubble ist" bis zu „Konto aktiviert und einsatzbereit" — Produktvorstellung (mit UI-Screenshots), Schritt-für-Schritt-Registrierungsführung, Fehlerbehebung und Erklärung der Abonnement-Aktivierung.

Reiner Anleitungsskill, ohne Skripte und ohne Abhängigkeiten; alle Registrierungsaktionen führt der oder die Nutzer:in im Browser/in der App durch.

## Installation

```
openclaw skills install @durenzidu/powpow-register
```

## Funktionen

1. **Produktvorstellung**: Einstieg mit ~120 Zeichen + Screenshot-Links aus einem öffentlichen GitHub-Repository (6 Grafiken: Kartenseite, Beitragsdetailseite usw.; je nach Szenario 1–3 senden).
2. **Registrierungsführung**: Feldregeln (Benutzername/Passwort/E-Mail-Verifizierungscode/Telefonnummer/Avatar), Drittanbieter-Login (Google/Watcha/Huawei), Rate-Limit-Parameter — alles aus dem Plattform-Quellcode, mit Quellenangabe.
3. **Fehlerbehebung**: 13 häufige Probleme, darunter keine Verifizierungs-E-Mail, Benutzername/E-Mail vergeben, 403 nicht aktiviert, Konto gesperrt.
4. **Abonnement-Aktivierung**: drei Kanäle — PayPal (Web) / WeChat-QR-Code (manuelle Bestätigung) / Huawei IAP (HarmonyOS) — mit Erklärungen und Fehlersuche; die bestehende Zahlungskette wird direkt wiederverwendet, der Skill weist nur den Weg.

## Dateistruktur

```
powpow-register/
├── SKILL.md                            # Hauptanleitung (Trigger, Ablauf, Ton-Regeln)
├── README.md
├── .clawhubignore
└── references/
    ├── registration-flow.md            # Feldregeln, Rate Limits, Fehlertabelle (mit Quellenangabe)
    ├── payment-and-activation.md       # Abo-Aktivierung, Zahlungskanäle, Wiederverwendungs-Fazit
    └── screenshots.md                  # Gehostete Screenshot-Liste + Szenario-Schnellübersicht
```

## Sicherheit

- Enthält keine Geheimnisse; keine Skripte, kommt nie mit Nutzer-Zugangsdaten in Berührung.
- **Fordere niemals** Passwort, Verifizierungscode oder Zahlungsnachweise des Nutzers an; Registrierung und Bezahlung laufen vollständig auf den Plattformseiten.

## Lizenz

MIT-0 (einheitliche ClawHub-Lizenz).

## Links

- Offizielle Website: https://global.powpow.online
- Registrierung: https://global.powpow.online/register
- Bubble kennenlernen (Video): https://www.bilibili.com/video/BV1Wu826UEVz/
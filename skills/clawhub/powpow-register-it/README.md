# powpow-register

L'assistente alla registrazione Bubble di PowPow (edizione OpenClaw): porta un nuovo utente da « non so cosa sia Bubble » a « account attivato e pronto all'uso » — presentazione del prodotto (con screenshot dell'interfaccia), guida passo passo alla registrazione, risoluzione errori e spiegazione dell'attivazione dell'abbonamento.

Skill puramente indicativo, senza script né dipendenze; tutte le azioni di registrazione vengono svolte dall'utente nel browser/App.

## Installazione

```
openclaw skills install @durenzidu/powpow-register
```

## Funzionalità

1. **Presentazione del prodotto**: introduzione di ~120 caratteri + link agli screenshot ospitati in un repository pubblico GitHub (6 immagini: pagina mappa, pagina dettaglio post, ecc.; inviane 1–3 a seconda dello scenario).
2. **Guida alla registrazione**: regole dei campi (nome utente/password/codice di verifica e-mail/telefono/avatar), login di terze parti (Google/Watcha/Huawei), parametri di rate limit — tutto tratto dal codice sorgente della piattaforma con le fonti citate.
3. **Risoluzione errori**: 13 problemi comuni, tra cui codice di verifica non ricevuto, nome utente/e-mail già in uso, 403 non attivato, account bloccato.
4. **Attivazione dell'abbonamento**: tre canali — PayPal (web) / QR code WeChat (conferma manuale) / IAP Huawei (HarmonyOS) — con spiegazioni e risoluzione errori; la catena di pagamento esistente è riutilizzata così com'è, lo skill indica solo la strada.

## Struttura dei file

```
powpow-register/
├── SKILL.md                            # Guida principale (trigger, flusso, regole di tono)
├── README.md
├── .clawhubignore
└── references/
    ├── registration-flow.md            # Regole dei campi, rate limit, tabella errori (con fonti)
    ├── payment-and-activation.md       # Attivazione abbonamento, canali di pagamento, conclusione riutilizzo
    └── screenshots.md                  # Elenco screenshot ospitati + riferimento rapido per scenario
```

## Sicurezza

- Non contiene segreti; senza script, non tocca mai le credenziali dell'utente.
- **Non chiedere mai** la password, il codice di verifica o i giustificativi di pagamento dell'utente; registrazione e pagamento avvengono interamente sulle pagine della piattaforma.

## Licenza

MIT-0 (licenza unificata ClawHub).

## Link

- Sito ufficiale: https://global.powpow.online
- Registrazione: https://global.powpow.online/register
- Scoprire Bubble (video): https://www.bilibili.com/video/BV1Wu826UEVz/
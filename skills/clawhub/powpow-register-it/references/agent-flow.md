# Flusso delegato all'agent e contratto dello script — powpow-register

Dettagli esecutivi dei singoli passi di SKILL.md. Tutti i comandi sono `node scripts/powpow-register.mjs <sottocomando> [parametri]`,
lo script è a **zero dipendenze**, richiede **Node ≥ 18**, e tutte le richieste vanno solo a `https://global.powpow.online`.

## Progettazione della sicurezza (perché è fatta così)

| Scelta | Motivo |
|---|---|
| La password passa solo tramite la variabile d'ambiente `POWPOW_REGISTER_PASSWORD` | I parametri a riga di comando del processo sono visibili agli altri processi sulla stessa macchina (superficie di fuga argv), la variabile d'ambiente viene letta e usata subito dentro lo script |
| La password **non finisce mai nel file di stato**, mai nei log | Il file di stato può restare sul disco; in modalità generata la si mostra una sola volta in conversazione perché l'utente la salvi |
| File di stato nella cartella temporanea di sistema (`os.tmpdir()/powpow-register-state.json`, 0600) | Contiene solo i cinque campi email / username / nickname / token / outTradeNo, `cleanup` li cancella con un comando |
| Il JWT ottenuto dall'agent viene scambiato in cookie del browser tramite l'endpoint ufficiale `me?token=` | Ponte ufficiale della piattaforma pensato per la WebView HarmonyOS; la verifica firma controlla solo firma + scadenza, non lega l'impronta del dispositivo, quindi il browser dell'utente può usarlo |
| Il pagamento si limita a create-order / query / aprire la cassa | L'atto di pagare e le credenziali di pagamento restano sempre tra l'utente e la cassa ufficiale Alipay, l'agent non ci passa mai in mezzo |

## Riferimento dei comandi

| Comando | Parametri chiave | Funzione / occasione |
|---|---|---|
| `status` | —— | Vedere l'avanzamento del flusso (legge il file di stato); dopo un'interruzione della conversazione eseguire prima questo |
| `gen-password` | —— | Genera una password robusta di 24 caratteri (maiuscole + minuscole + cifre), stdout la mostra **una sola volta** |
| `prepare-suggest` | `--username --nickname --email` | Segna nel file di stato le informazioni confermate (dopo, register non dovrà ripeterle) |
| `send-code` | `--email` | Fa scattare l'invio da parte della piattaforma del codice a 6 cifre (valido 10 minuti, cooldown 60s) |
| `register` | `--code` (obbligatorio); `--username --nickname --avatar --phone` (facoltativi, se già nel file di stato si omettono) | Crea l'account pending; la password passa per la variabile d'ambiente `POWPOW_REGISTER_PASSWORD`; riuscito, il JWT viene salvato automaticamente nel file di stato |
| `login-link` | `--target pending` oppure `--target home` | Genera il link di accesso con un clic (design a doppio link, vedi sotto) |
| `create-order` | `--package monthly\|quarterly\|yearly` (Alipay predefinito)<br>`--provider alipay\|paypal` | Crea l'ordine di pagamento; Alipay restituisce il percorso del file della pagina di pagamento + outTradeNo; PayPal restituisce il percorso del file della pagina di autorizzazione + subscriptionId (registrato automaticamente nel file di stato) |
| `query` | —— | Interroga lo stato dell'ordine/abbonamento. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; polling ogni 10–15s |
| `refresh-login` | password via variabile d'ambiente | Rieffettua il login per un **nuovo JWT** (la dichiarazione di abbonamento passa da NONE ad ACTIVE), da eseguire obbligatoriamente dopo l'accredito |
| `whoami` | —— | Con il token nel file di stato verifica account e stato abbonamento (per controllare che l'attivazione sia avvenuta) |
| `cleanup` | —— | Elimina il file di stato (da eseguire obbligatoriamente in chiusura) |

**Passaggio della variabile d'ambiente** (la password non va mai in riga di comando):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<password>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<password>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<password> && node scripts/powpow-register.mjs register --code 123456
```

## Meccanismo del doppio link (progetto centrale)

Lo stato di accesso della piattaforma è un cookie HttpOnly, e l'agent non può piantare direttamente un cookie nel
browser altrui; il ponte è l'endpoint ufficiale `/api/auth/me?token=<JWT>&redirect=<percorso del sito>`: verifica
firma → l'utente pending riceve automaticamente una sessione → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax /
7 giorni) → validazione del redirect (solo iniziante con uno slash, vietati `//` e backslash, dopo risoluzione deve
essere same-origin) → redirect temporaneo 307 alla pagina di destinazione.

- **Link 1 (dato subito dopo la registrazione riuscita)**: `--target pending` → atterra su `/subscription`.
  Il browser dell'utente entra nello stato di «semi-sessione»: pagina abbonamento e pagina di ritorno Alipay sono
  visibili e operabili; le pagine di contenuto restano respinte dal paywall verso la pagina abbonamento (triplo
  filtro: controllo del gateway sulle claims JWT → ricontrollo su DB → controllo delle API centrali, comportamento
  normale).
- **Link 2 (dato dopo la conferma di paid)**: prima `refresh-login` per un nuovo JWT (il pagamento aggiorna solo il
  DB, non modifica le claims del JWT già emesso; senza rinnovo sembrerebbe «ho pagato ma non sono membro»), poi
  `--target home` → atterra in home, stato membro completo.

## Sequenza completa (percorso normale)

```
1.  status                          # Autoverifica ambiente
2.  (passo 2: conferma informazioni in conversazione, password doppia scelta; modalità generata: gen-password → far salvare subito all'utente)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → l'utente va nell'email a leggere il codice (unica uscita dalla conversazione ①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → link 1 da mandare all'utente
7.  (l'utente sceglie il metodo di pagamento)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <file pagina pagamento>   # Windows; macOS usa open, Linux usa xdg-open
    # → l'utente completa pagamento/autorizzazione alla cassa Alipay/PayPal (uscita dalla conversazione ②)
9.  query (ogni 10–15s) finché non è paid / ACTIVE
10. refresh-login                   # nuovo JWT con dichiarazione ACTIVE
11. login-link --target home        # → link 2 da mandare all'utente
12. whoami                          # confermare subscriptionStatus: ACTIVE (facoltativo)
13. cleanup                         # ripulire il file di stato
```

## Mappatura comandi → API della piattaforma

| Comando script | Interfaccia piattaforma |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart, caricamento diretto avatar) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (il link in sé, efficace al click del browser) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

Fonte delle regole: campi di registrazione e limiti di frequenza in `registration-flow.md`; pacchetti e catena di
attivazione in `payment-and-activation.md` (entrambi con i file sorgente della piattaforma citati).

## Gestione degli errori a livello di script

| Sintomo | Gestione |
|---|---|
| `Versione di Node troppo bassa` | Tornare alla modalità di sola guida, non insistere |
| Errore di rete / timeout | Riprovare una volta; se fallisce ancora, far controllare la rete all'utente e riprendere (il file di stato esiste, rieseguire `status` per ripartire) |
| register restituisce un errore di business (nome utente esistente ecc.) | Gestire secondo la tabella del passo 5 di SKILL.md, **il codice di verifica non va reinviato** (resta valido per 10 minuti) |
| register restituisce 「邮箱验证码错误或已过期」 (codice errato o scaduto) | Scaduto → eseguire di nuovo `send-code` |
| L'utente chiude la pagina di pagamento dopo `create-order` | Eseguire subito di nuovo `create-order` (il vecchio ordine si chiude da solo dopo 2h; gli abbonamenti PENDING PayPal scadono dopo 1h) |
| `create-order --provider paypal` restituisce 409 | Esiste già un abbonamento PayPal non completato; attendi 1h perché scada o completa la vecchia autorizzazione nel browser |
| `query` resta sempre pending / PENDING | Forse l'utente non ha pagato; chiedere. Se ha pagato davvero → seguire la tabella in payment-and-activation.md |
| `refresh-login` 403 `pending_payment` | Il pagamento o l'autorizzazione non è ancora accreditato, tornare al passo 9 e continuare il polling |
| File di stato perso (cancellato per sbaglio / cambio macchina) | `whoami`/`refresh-login` non utilizzabili; far riaprire all'utente la pagina abbonamento nel browser dove ha già aperto il link 1 per confermare lo stato, oppure rifare il login (modalità web) |

## Modalità di ripiego (sola guida)

In uno qualunque di questi casi si rientra subito nella sola guida in stile v1, senza più tormentare lo script:

- Niente Node ≥ 18 oppure due fallimenti consecutivi dello stesso tipo;
- L'utente dice esplicitamente «faccio io dal browser»;
- Politiche aziendali/di dispositivo che impediscono allo script di uscire in rete.

Dopo il ripiego: fornire la pagina di registrazione https://global.powpow.online/register e la pagina abbonamento
https://global.powpow.online/subscription , accompagnare la diagnosi secondo le regole di `registration-flow.md`,
tono invariato, ogni turno si chiude comunque con il blocco «prossimo passo».

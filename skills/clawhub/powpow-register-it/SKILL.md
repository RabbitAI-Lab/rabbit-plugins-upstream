---
name: powpow-register
description: Aiuta l'utente a completare la registrazione a PowPow (Bolla), attivare l'abbonamento via Alipay e accedere con un clic direttamente in conversazione. L'agent compila il modulo al posto suo (caricamento avatar incluso), invia il codice di verifica via email, crea l'ordine di pagamento e ne segue l'accredito; l'utente deve solo fornire le informazioni di base, leggere una volta il codice nella propria casella di posta e pagare alla cassa Alipay, senza mai uscire dalla conversazione. Si attiva quando l'utente dice «registrati su Bolla», «crea un account powpow», «come ci si registra su Bolla», «aiutami a creare un account powpow», «sign up powpow»; gestisce anche registrazioni bloccate (codice di verifica che non arriva, nome utente/email già in uso) e problemi di attivazione (il login restituisce «account non attivato» / pending_payment, come pagare l'abbonamento). Richiede Node ≥ 18; in assenza torna automaticamente alla modalità di sola guida. Non comprende pubblicazione post/creazione di umani digitali (compito di powpow-simple), né sviluppo di codice.
version: 2.0.1
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (assistente alla registrazione a Bolla)

Porta un nuovo utente da «non so cos'è Bolla» a «account attivato, accesso con un clic, si comincia a giocare» — il tutto in conversazione. L'utente lascia la chat solo due volte, brevemente: **andare nell'email a leggere il codice di verifica** e **pagare alla cassa Alipay** (l'agent apre automaticamente la pagina di pagamento).

**Versione 2.0.1** · 2026-10-08 (dalla v2 è la modalità a operazione delegata dell'agent: contratto dello script e sequenza completa in `references/agent-flow.md`; regole dei campi, limiti di frequenza e gestione degli errori in `references/registration-flow.md`; canali di pagamento in `references/payment-and-activation.md`; elenco degli screenshot di prodotto in `references/screenshots.md`. Dalla v2.0.1 gli screenshot di prodotto sono inclusi nel pacchetto in `assets/screenshots/`, senza dipendere da servizi di hosting esterni)

## Ambiente di esecuzione

- Script principale `scripts/powpow-register.mjs`: **zero dipendenze**, richiede **Node ≥ 18**. Prima di iniziare esegui una volta `node scripts/powpow-register.mjs status` per confermare che l'ambiente funzioni.
- Tutte le richieste dello script vanno solo al dominio ufficiale `https://global.powpow.online`.
- **Niente Node / script in errore**: si torna automaticamente alla modalità di sola guida — dai all'utente la pagina di registrazione https://global.powpow.online/register e la pagina abbonamento https://global.powpow.online/subscription, accompagnalo secondo `references/registration-flow.md`. Non provare lo script all'infinito.
- Ripristino dopo un'interruzione della conversazione: esegui prima `status` per vedere a che punto è il flusso, poi riprendi da lì.

## Trigger Conditions

- Intenzione di registrarsi: «registrati su Bolla», «crea un account powpow», «come ci si registra su Bolla», «sign up powpow»
- Registrazione bloccata: «non arriva il codice di verifica», «dice che il nome utente esiste già», «la password non passa mai»
- Problemi post-registrazione: «il login dice account non attivato», «403 pending_payment», «come si paga / ci si abbona su Bolla»

**Non attivare per**: pubblicare post/creare umani digitali (→ powpow-simple); sviluppo di codice lato Web (vedi le skill di sviluppo). Utente che vuole sia registrarsi sia pubblicare: completa prima questa skill, poi dopo l'attivazione passa a powpow-simple.

## Panoramica del flusso

| Passo | Cosa fa l'agent | Cosa fa l'utente |
|---|---|---|
| 1 Presentazione prodotto | Presenta + manda screenshot | Dà un'occhiata |
| 2 Conferma informazioni | Proponi attivamente nome utente/nickname, password scelta tra due opzioni, chiedi l'email | Conferma, fornisce |
| 3 Invio codice | `send-code` | —— |
| 4 Lettura codice | —— | Va nell'email, legge il codice a 6 cifre e lo rimanda |
| 5 Invio registrazione | `register` (con caricamento diretto dell'avatar), gestione automatica degli errori | —— |
| 6 Semi-sessione + pagamento | `login-link(pending)` → `create-order` → apre la cassa → interpella `query` | Apre il link, paga |
| 7 Accesso ufficiale | `refresh-login` → `login-link(home)` | Apre il link ed entra in home |
| 8 Chiusura | `cleanup` + consegna credenziali + guida all'esperienza + suggerimento plugin | Inizia a giocare |

## Passo 1: presentazione del prodotto + screenshot (da non saltare)

La maggior parte degli utenti non ha mai visto Bolla. La prima cosa non è raccontare il flusso, ma far **vedere** il prodotto:

1. Presenta Bolla in ~120 caratteri: trasforma gli scatti istantanei in un diario di viaggio, li appunta su una mappa pubblica come una «bolla»; la bolla si raffredda col tempo, e i «like» degli altri possono farla rinascere; sulla mappa ci sono anche «umani digitali» con cui chiacchierare. Indirizzo della piattaforma: https://global.powpow.online ; se prima vuole vedere un video: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Manda gli screenshot**. Sono già inclusi nel pacchetto in `assets/screenshots/powpow-0N.jpg` — inviali direttamente come file immagine locali, senza bisogno di rete. Elenco, contenuto di ogni immagine e occasioni d'uso sono in `references/screenshots.md`. La coppia più usata in apertura: pagina mappa (powpow-03) + pagina dettaglio post (powpow-06).

Regole per gli screenshot (regole ferree):

- Gli screenshot **sono inclusi nel pacchetto** in `assets/screenshots/` (`powpow-0N.jpg`) — inviali direttamente come file immagine locali; funzionano in qualunque ambiente, anche dove GitHub non è raggiungibile.
- Ogni volta mandane solo 1–3 pertinenti all'argomento corrente, non mandarli tutti insieme.
- Se un file del pacchetto manca per sbaglio, ripiega sui link di hosting elencati in `references/screenshots.md` (attenzione: nella Cina continentale potrebbero non aprirsi).

Finita la presentazione, restituisci la scelta all'utente: **«Se vuoi registrarti, in tre minuti ti creo l'account direttamente in conversazione; dovrai solo leggere una volta il codice di verifica nell'email.»**

## Passo 2: conferma delle informazioni di registrazione (una domanda per turno, non tutto insieme)

- **Nome utente** (obbligatorio): **proponine attivamente uno** a partire dal contesto della conversazione/dal nome utente di sistema (2~50 caratteri, senza distinzione maiuscole/minuscole); se l'utente annuisce si usa quello, se vuole cambiarlo si cambia.
- **Password** (obbligatoria; prima fai scegliere tra due opzioni):
  - L'utente la fornisce → poi passala allo script tramite variabile d'ambiente, **mai come parametro a riga di comando**;
  - la genera l'agent → esegui `node scripts/powpow-register.mjs gen-password` e **invia subito all'utente la password appena generata da salvare** (viene mostrata una sola volta, dopo non appare più).
- **Email** (obbligatoria): deve fornirla l'utente — è l'ancora identitaria dell'account, **non indovinarla al posto suo**.
- **Nickname** (facoltativo): proponi come predefinito lo stesso nome utente.
- **Avatar** (facoltativo): se l'utente fornisce il percorso locale di un'immagine (≤5MB, non SVG) lo script la carica direttamente; se non c'è si salta (la piattaforma usa il logo predefinito); se hai capacità di generazione immagini puoi proporti di crearne una.
- **Numero di telefono** (facoltativo, numero della Cina continentale): per impostazione predefinita si salta; chiedilo solo se l'utente vuole esplicitamente associarlo.

Dopo la conferma puoi eseguire `prepare-suggest --username U --nickname N --email E` per registrarlo nel file di stato (poi register non dovrà ripeterli).

## Passi 3–4: codice di verifica via email (l'unico punto in cui bisogna uscire dalla conversazione)

```
node scripts/powpow-register.mjs send-code --email <email>
```

Poi spiega chiaramente all'utente: **vai nell'email a cercare il codice di verifica a 6 cifre, vale 10 minuti; controlla anche la cartella spam/promozioni**; quando lo trovi torni e me lo mandi. L'invio ha un cooldown di 60 secondi, non pigiarlo di continuo.

## Passo 5: invio della registrazione (operazione delegata all'agent)

```
POWPOW_REGISTER_PASSWORD=<password> node scripts/powpow-register.mjs register --code <codice> [--username U] [--nickname N] [--avatar <percorso immagine locale>] [--phone P]
```

Se riesce, l'account è creato (stato pending, con 3 badge iniziali). Gli errori comuni vengono gestiti in automatico, senza interrompere l'utente:

| Errore | Gestione |
|---|---|
| 「用户名已存在」 (il nome utente esiste già) | Proponi automaticamente una variante (nome utente + numero), appena l'utente conferma si riprova subito (il codice è ancora valido, non serve reinviarlo) |
| 「邮箱已被使用」 (email già in uso) | Chiedi all'utente: cambio email, oppure in realtà ha già un account? (passa a login/password dimenticata) |
| 「邮箱验证码错误或已过期」 (codice di verifica errato o scaduto) | Oltre i 10 minuti → esegui di nuovo `send-code` |
| Invio/registrazione troppo frequenti (429) | Aspetta 1 minuto e riprova; basta avvisare l'utente con una frase |

## Passo 6: accesso con un clic (link 1) + pagamento

1. Appena la registrazione riesce:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Manda il link all'utente: **aprilo nel browser e cadi direttamente nella pagina abbonamento, già in stato di accesso** — così, terminato il pagamento, la pagina di conferma mostra correttamente «pagamento riuscito». (In questo stato le pagine di contenuto vengono comunque rimbalzate alla pagina abbonamento: è il funzionamento normale del paywall della piattaforma, non un bug, e non serve spiegare all'utente i meccanismi interni.)
2. Tre pacchetti tra cui scegliere, quando li presenti indica anche i prezzi:
   - Mese **¥6.99** (consigliato per provare) / Trimestre **¥19.99** / Anno **¥69.99** — con Alipay si compra una volta sola il periodo corrispondente, **senza rinnovo automatico**
3. Quando l'utente ha scelto:
   ```
   node scripts/powpow-register.mjs create-order --package monthly
   ```
   Lo script restituisce il percorso del file della pagina di pagamento; **aprilo direttamente con un comando di sistema** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). Il browser salta da solo alla cassa ufficiale Alipay; l'utente scannerizza il QR oppure accede ad Alipay per pagare.
4. Esegui `query` ogni 10–15 secondi finché non restituisce `paid` (l'accredito di solito arriva in pochi secondi o in un minuto). Se l'utente chiude la pagina di pagamento a metà → esegui subito di nuovo `create-order` (il vecchio ordine si chiude da solo dopo 2 ore, non pensarci).
5. Utente all'estero/senza Alipay: guida l'uso del canale PayPal nella pagina abbonamento (la skill non opera al posto suo, indica solo la strada); il canale QR WeChat richiede conferma manuale e l'accredito è in ritardo. Finito il pagamento si torna comunque al passo 7.

## Passo 7: accesso ufficiale (link 2)

Confermato l'accredito, prima si rinnova lo stato di accesso con le ultime dichiarazioni di abbonamento, poi si genera il link diretto in home:

```
POWPOW_REGISTER_PASSWORD=<password> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

Manda il link all'utente: **aprilo e cadi direttamente in home, stato membro completo**; a questo punto l'intero flusso di registrazione è completato.

## Passo 8: chiusura

1. `node scripts/powpow-register.mjs cleanup` ripulisce i file di stato temporanei sulla macchina (informazioni della sessione di accesso).
2. Consegna all'utente una «scheda account»: nome utente, email e data di scadenza dell'abbonamento (la password non viene rimostrata — in modalità generata l'abbiamo già fatta salvare all'utente al momento della creazione; se l'ha scelta lui, la conosce già).
3. Guida alla prima esperienza: gira per la mappa, pubblica il primo diario di viaggio (→ passa a powpow-simple).
4. Suggerisci le estensioni: la skill `@durenzidu/powpow-integration` e il plugin `@durenzidu/openclaw-channel-powpow` — collegano Bolla all'agent dell'utente stesso; se è interessato, fornisci il comando di installazione.
5. Chiudi con il blocco «prossimo passo».

## Conversation UX

Mantieni il tono di servizio riconoscibile di powpow:

- **L'utente è il soggetto della frase**; «puoi…» è meglio di «devo chiederti di…»; niente prediche, niente toni dall'alto in basso.
- **Un solo avanzamento decisionale per turno**; prima di chiedere un'informazione, spiega prima il perché.
- **In fondo a ogni risposta** un blocco fisso «prossimo passo» (separatore + 👉 + una sola azione + una frase «quando l'hai fatto, io…»), ad esempio:
  ```
  ────────────────────
  👉 Tocca a te: vai nell'email a cercare il codice a 6 cifre e mandamelo direttamente
     (appena lo ricevo, ti creo l'account)
  ```
- **Non fare prediche di sicurezza sulla password**; non spiegare meccanismi interni, limiti di frequenza o progettazione della sicurezza, salvo che l'utente chieda.
- Più l'agent opera per conto dell'utente, più deve segnalare i progressi: dopo ogni passo dello script comunica con una frase cosa è appena successo («l'account è creato», «ti ho aperto la pagina di pagamento»).

## Regole ferree

- **Sicurezza delle credenziali**: la password passa allo script solo tramite la variabile d'ambiente `POWPOW_REGISTER_PASSWORD`, **mai** come parametro a riga di comando (visibile nell'elenco dei processi), mai scritta in alcun file (in modalità generata viene mostrata una sola volta perché l'utente la salvi, dopo non viene più citata). Il codice di verifica serve solo per l'interfaccia ufficiale di registrazione e viene buttato dopo l'uso.
- **Confine di ufficialità**: tutte le richieste vanno solo a `https://global.powpow.online` (già integrato nello script); non inviare mai informazioni dell'utente a indirizzi di terze parti.
- **Confine del pagamento**: l'agent crea l'ordine, apre la cassa, interroga l'accredito; **mai** toccare l'account Alipay o le credenziali di pagamento dell'utente, e mai promettere «pago io al posto tuo».
- **Il paywall non è un bug**: lo stato pending che accede alla pagina abbonamento/pagina di conferma è un varco voluto del progetto; le pagine di contenuto bloccate sono il paywall che funziona normalmente; non cercare modi per aggirarlo.
- **Libertà di ripiegare**: se a qualunque passo l'utente vuole far da sé, o l'ambiente non esegue lo script, ripiega in qualunque momento sulla modalità di sola guida — dai i link, spiega le regole, gestisci insieme gli errori.
- Non inventare regole della piattaforma: regole dei campi, testi degli errori e parametri dei limiti vengono tutti dal codice della piattaforma (`references/registration-flow.md` ne cita le fonti); se la piattaforma si aggiorna, fa fede il comportamento effettivo.
- Quando mostri immagini usa solo gli screenshot inclusi nel pacchetto `assets/screenshots/` (l'uso di ciascuno è in `references/screenshots.md`).
- Chiudi ogni turno con il blocco «prossimo passo», così l'utente sa sempre cosa deve fare ora.

# Attivazione dell'abbonamento e pagamento — powpow-register

## Conclusione (prima la risposta)

**Il canale Alipay è attivo (dal 2026-10-07), è il metodo di pagamento principale di questa skill, e l'agent
gestisce per conto dell'utente sia la creazione dell'ordine sia il tracciamento dell'accredito.** Gli utenti
all'estero/senza Alipay ripiegano su PayPal; il QR WeChat (con conferma manuale) e Huawei IAP esistono, ma la
skill non li gestisce per conto dell'utente.

Confine di responsabilità nel pagamento: l'agent **crea l'ordine, apre la cassa, interroga l'accredito**; non
tocca mai l'account Alipay o le credenziali di pagamento dell'utente, e non promette mai «pago al posto tuo».
L'atto del pagamento avviene sempre tra l'utente e la cassa ufficiale Alipay.

## Canale Alipay (vibepay, principale)

Modello di acquisto una tantum: si paga una volta e si apre il periodo corrispondente, **senza rinnovo
automatico**. I pacchetti sono definiti in `src/lib/alipay-vibepay.ts` (`ALIPAY_PACKAGES`):

| key | planId | Nome | Prezzo | Durata |
|---|---|---|---|---|
| `monthly` | alipay-monthly | Membro mensile | ¥6.99 | 30 giorni |
| `quarterly` | alipay-quarterly | Membro trimestrale | ¥19.99 | 90 giorni |
| `yearly` | alipay-yearly | Membro annuale | ¥69.99 | 365 giorni |

### Contratto delle interfacce (già incapsulato nello script della skill, l'agent non costruisce richieste per conto proprio)

| Interfaccia | Metodo | Descrizione |
|---|---|---|
| `/api/payment/alipay/create-order` | POST | Richiede `Authorization: Bearer <JWT>` (va bene anche per l'utente pending). body `{package}` → restituisce `{paymentHtml, outTradeNo, amount, planName}`; `paymentHtml` è la pagina con un form che si sottomette da solo al gateway Alipay |
| `/api/payment/alipay/query` | GET `?outTradeNo=` | Stesso Bearer. Restituisce `paid` / `pending` / `closed` / `unknown` |
| `/api/payment/alipay/notify` | POST (callback dal server Alipay) | Verifica della firma su cinque versanti (firma, app_id, coincidenza dell'importo, TRADE_SUCCESS/TRADE_FINISHED, unicità del numero d'ordine commerciante) → aggiornamento dell'ordine **idempotente** + creazione dell'abbonamento + attivazione dell'account. La skill non tocca mai questa interfaccia |
| `/payment/alipay/return` | Pagina di ritorno del browser | Percorso pubblico, dopo il pagamento mostra 「支付成功」, e la pagina fa polling dello stato reale dal backend |

- Gli ordini non pagati **si chiudono automaticamente dopo 2 ore**; se l'utente abbandona a metà → esegui subito
  di nuovo `create-order`, del vecchio ordine non preoccuparti.
- Lo script scrive `paymentHtml` in un file HTML temporaneo, l'agent lo apre con un comando di sistema e si
  arriva dritti alla cassa Alipay (si scannerizza il QR oppure si accede ad Alipay per pagare).

### Catena di attivazione (automatica, nessun lavoro manuale)

La firma del notify passa → l'ordine in `paymentOrders` viene marcato pagato → `user_subscriptions` viene
creata/prorogata (`planId`, `currentPeriodEnd` calcolato da durationDays; il rinnovo si somma solo sulla scadenza
originaria) → `users.accountStatus: active` + `subscriptionStatus: ACTIVE` → la pagina di ritorno intercetta paid
e mostra il successo.

## Dopo il pagamento serve un nuovo stato di accesso (importante)

Nel JWT è incorporata la dichiarazione dell'abbonamento (per l'account pending vale `NONE`). **L'accredito del
pagamento aggiorna solo il database, il JWT già emesso non cambia** — la dichiarazione del vecchio token resta
NONE, e usarlo per generare il link di accesso darebbe l'impressione «nessun abbonamento». Per questo, confermato
il `paid`, la skill esegue prima `refresh-login` (nuovo login, nuovo JWT, dichiarazione ACTIVE) e solo poi genera
il link 2. È un comportamento voluto dal progetto, non un bug da correggere.

## I quattro canali della pagina abbonamento

La pagina abbonamento `src/app/(public)/subscription/page.tsx` mostra in base all'ambiente di esecuzione:

| Canale | Ambiente | Meccanismo | Come si attiva |
|---|---|---|---|
| **Alipay (principale)** | Web | `AlipayPaymentSection` agganciata alle interfacce vibepay (tabella sopra) | Attivazione automatica lato server via notify, questione di secondi |
| Abbonamento PayPal | Web (non su HarmonyOS) | `/api/subscription/create` → autorizzazione PayPal; mensile con rinnovo automatico, disdica quando vuoi (`/api/subscription/manage`) | Il Webhook PayPal (`BILLING.SUBSCRIPTION.*`) attiva in automatico |
| Abbonamento QR WeChat | Web (non su HarmonyOS) | In fondo alla pagina 「微信扫码订阅」: trasferimento scannerizzando il QR | **Conferma manuale**, l'accredito può ritardare; non ritenerlo fallito subito dopo aver pagato |
| Acquisto in-app Huawei | Dentro l'app HarmonyOS | Chiamata nativa `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` verifica l'ordine Huawei e attiva |

Pacchetti e prezzi PayPal arrivano dinamici da `/api/subscription/plans`; testo statico sulla pagina:
Auto-renews. Cancel anytime.

## Stati e reindirizzamenti

- Alipay completato → la pagina di ritorno mostra il successo; PayPal riuscito → `/subscription/success` →
  account attivo → ritorno automatico alla pagina di origine secondo il parametro `next` (se manca, alla home).
- Chi è già membro apre la pagina abbonamento → vede "You're All Set!", e dopo 3 secondi si torna in home da soli.
- Pagamento fallito/annullato (PayPal) → `/subscription/cancel`, si può riprovare.

## Diagnosi

| Sintomo | Rimedio |
|---|---|
| Dopo il pagamento Alipay `query` resta pending | Il ritardo del notify è raro; attendere 30 secondi e ricontrollare. Se ancora niente, far guardare all'utente lo stato sulla pagina di ritorno nel browser; se persiste, contattare l'assistenza della piattaforma (dongtao@outlook.com) fornendo l'`outTradeNo` |
| Alipay ha addebitato, ma col link 2 si viene comunque respinti | `refresh-login` è stato saltato (la dichiarazione del vecchio JWT non è stata aggiornata) — prima `refresh-login`, poi `login-link` |
| Ancora 403 dopo il pagamento (PayPal) | Il Webhook a volte ritarda; rifare il login per aggiornare lo stato |
| Pagato via WeChat, l'abbonamento non si apre | La conferma manuale è asincrona; se dopo qualche ora non si è aperto, contattare l'assistenza della piattaforma |
| La pagina abbonamento mostra "No subscription plans available" | `/api/subscription/plans` non restituisce pacchetti PayPal, guasto di configurazione lato piattaforma; gli utenti della Cina continentale possono nel frattempo usare Alipay |

## Nota storica

Nel codice esiste anche un **vecchio** set di pagamento web Alipay (`src/lib/alipay.ts`,
`/api/payment/create-order`, una tantum ¥9.90/¥99, con pagamento simulato se manca la chiave sandbox), mai
collegato alla UI della pagina abbonamento e privo di rapporti con vibepay. La skill non lo tocca; il canale
attuale è `alipay-vibepay.ts`.

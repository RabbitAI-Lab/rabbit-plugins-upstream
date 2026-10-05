# Attivazione dell'abbonamento e pagamento — powpow-register

## Conclusione (prima la risposta)

**I metodi di pagamento esistenti sono direttamente riutilizzabili — lo skill assistente alla registrazione non richiede alcuno sviluppo di pagamento.**

Motivi:

1. L'interfaccia di registrazione (`src/app/api/auth/register/route.ts`) emette già un cookie JWT + un cookie HttpOnly pendingUserToken alla creazione dell'account pending, così quando l'utente arriva su `/subscription` ha già la sessione attiva — i tre canali di pagamento pendono tutti da questa pagina abbonamento e attivano lo stesso account pending.
2. L'interfaccia di login restituisce 403 + `redirectTo: '/subscription'` per gli account pending e imposta i cookie allo stesso modo — un utente che paga in ritardo viene sempre riportato alla stessa pagina.
3. Quindi il confine di responsabilità di uno skill di guida alla registrazione è semplicemente « portare l'utente su /subscription »; nessuna nuova interfaccia di pagamento, nessun nuovo modello di ordine, nessuna modifica al backend.

Da notare anche: il passaggio di pagamento (pulsante PayPal JS SDK, conferma manuale del QR code WeChat, IAP nativo Huawei) **rende impossibile e inappropriato che uno skill da riga di comando/chat paghi al posto dell'utente**. Non tentare di chiamare interfacce di pagamento da uno script per pagare per l'utente, e non chiedere i suoi giustificativi di pagamento.

## I tre canali della pagina abbonamento

La pagina abbonamento `src/app/(public)/subscription/page.tsx` mostra automaticamente il canale adatto in base all'ambiente di esecuzione:

| Canale | Ambiente | Meccanismo | Attivazione |
|---|---|---|---|
| Abbonamento PayPal | Web (non HarmonyOS) | `/api/subscription/create` crea un abbonamento PayPal → reindirizza all'autorizzazione PayPal; rinnovo automatico mensile, annullabile in qualsiasi momento (`/api/subscription/manage`) | Il Webhook PayPal (`BILLING.SUBSCRIPTION.*`) imposta automaticamente `accountStatus` su active |
| Abbonamento con QR code WeChat | Web (non HarmonyOS) | Sezione « Abbonati scansionando WeChat » in fondo alla pagina: bonifico con scansione, **attivazione dopo conferma manuale** (`WechatQrPaymentSection`) | Conferma manuale; l'accredito può richiedere tempo — non concludere subito che sia fallito dopo il pagamento |
| Acquisto in-app Huawei (IAP) | Dentro l'App HarmonyOS | Nella WebView HarmonyOS PayPal/WeChat Pay non sono disponibili; la pagina usa il nativo `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` verifica l'ordine Huawei e poi attiva |

Piani e prezzi vengono letti dinamicamente da `/api/subscription/plans` (piani PayPal); il testo fisso della pagina: Auto-renews. Cancel anytime.

## Stati e reindirizzamenti

- Pagamento riuscito → `/subscription/success` (il callback PayPal porta `subscriptionId`) → account active → ritorno automatico alla pagina originale indicata dal parametro `next` (home se assente).
- Un utente già abbonato che visita la pagina abbonamento → mostra "You're All Set!", torna alla home dopo 3 secondi.
- Pagamento fallito/annullato → `/subscription/cancel`, si può ritentare.

## Risoluzione dei problemi

| Messaggio | Trattamento |
|---|---|
| Ancora 403 dopo il pagamento | PayPal: il Webhook a volte è in ritardo — fai logout e login per aggiornare lo stato (il login ricontrolla l'ultimo stato nel DB); WeChat: la conferma manuale non è conclusa, attendi un po'; Huawei: verifica se è apparsa la pagina di successo del pagamento in-app |
| La pagina abbonamento mostra "No subscription plans available" | Nessun piano PayPal utilizzabile su `/api/subscription/plans` — un problema di configurazione lato piattaforma; chiedi all'utente di riprovare più tardi |
| Pagato con WeChat ma non attivato | La conferma manuale è asincrona; se entro qualche ora non si attiva, contatta il supporto della piattaforma (dongtao@outlook.com) |

## Nota: Alipay

Nel codice esiste un insieme di pagamenti web Alipay (`src/lib/alipay.ts`, `/api/payment/create-order`, un modello di acquisto singolo: iscrizione normale ¥9,90 / iscrizione premium ¥99; degrada automaticamente a pagamento simulato se la chiave sandbox non è configurata), **ma non è collegato alla UI della pagina abbonamento** — è codice inattivo/di riserva. Se in futuro si volesse abilitare Alipay sulla pagina abbonamento, basta collegare questo codice già pronto — non riguarda questo skill ed è annotato solo come riferimento per decisioni lato piattaforma.
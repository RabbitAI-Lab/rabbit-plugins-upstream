# Dettaglio del flusso di registrazione — powpow-register

Da consultare quando si diagnosticano problemi. Tutte le regole vengono dal codice sorgente della piattaforma
(validazione coerente frontend-backend in Next.js), con fonte citata. Se la piattaforma si aggiorna, fa fede il
comportamento effettivo online.

## Punti d'ingresso

- Pagina di registrazione: https://global.powpow.online/register
- Pagina di login: https://global.powpow.online/login
- Pagina abbonamento: https://global.powpow.online/subscription
- Se si entra da un link di condivisione con `?next=...`, dopo registrazione + pagamento si torna automaticamente
  alla pagina di origine.

## Campi del modulo e regole

| Campo | Obbligatorio | Regola | Fonte nel codice |
|---|---|---|---|
| Avatar | Facoltativo | Immagine ≤5MB, SVG non supportato; il server la comprime automaticamente (se >100KB la porta a 400×400 / qualità 90) | `src/app/api/auth/register/route.ts` |
| Nome utente | Obbligatorio | 2~50 caratteri, dopo il trim viene salvato in **minuscolo** (Tom e tom sono lo stesso nome utente; sia lato registrazione sia lato login non si distingue maiuscole/minuscole) | Idem (zod schema) |
| Password | Obbligatoria | 8~100 caratteri, deve contenere insieme maiuscola, minuscola e cifra | Idem |
| Conferma password | Obbligatoria | Uguale alla password (solo validazione frontend) | `src/app/(public)/register/page.tsx` |
| Nickname | Facoltativo | ≤100 caratteri; se vuoto prende il nome utente | register route |
| Email | **Obbligatoria** | Formato email valido, ≤255 caratteri; una email può registrare un solo account | register route |
| Codice di verifica email | **Obbligatorio** | 6 cifre; **valido 10 minuti**; appena la verifica riesce viene invalidato; il reinvio marca il vecchio codice come usato | `src/lib/email-verification.ts` |
| Numero di telefono | Facoltativo | Numero della Cina continentale, 11 cifre iniziante con `1[3-9]`; un numero si lega a un solo account | register route |

La pagina offre inoltre tre pulsanti di login di terze parti: **Google, Watcha, account Huawei**
(`GoogleSignInButton` / `WatchaLoginButton` / `HuaweiLoginButton`). Gli account di terze parti non hanno password
locale: chi prova poi il login con password riceve «questo account non ha una password impostata, usa un altro
metodo di accesso».

## Limiti di frequenza e protezione antiforza bruta

| Comportamento | Limite | Fonte |
|---|---|---|
| Invio della registrazione | **3 volte/minuto/IP**, oltre 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Invio codice di verifica | Stesso IP 1 volta/minuto **e** stessa email 1 volta/minuto, oltre 429; pulsante frontend con countdown di 60 secondi | `src/app/api/auth/register/send-code/route.ts` |
| Verifica del codice | Per email, massimo **5 tentativi** in 10 minuti; al tetto il codice viene rifiutato anche se corretto, serve un nuovo invio | `src/lib/email-verification.ts` |
| Invio codice password dimenticata | 1 volta/minuto/IP | `src/app/api/auth/forgot-password/route.ts` |
| Login | 5 volte/minuto/IP; stesso account con **5 fallimenti consecutivi si blocca per 30 minuti** (423), con avviso dei tentativi residui decrescenti | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Comportamento di tutela della privacy**: quando si invia il codice / la password dimenticata, se l'email è già
registrata o non esiste, l'interfaccia restituisce comunque lo stesso messaggio di successo, senza rivelare se
l'email sia già registrata.

## Equivalenza tra modalità delegata all'agent e registrazione via web

Lo script della skill chiama **lo stesso set di API pubbliche** (`/api/auth/register`, `send-code`, `login`,
`/api/auth/me`), passando per controlli, limiti di frequenza ed errori identici a quelli dell'invio del modulo
della pagina di registrazione — tutte le regole di questo file valgono allo stesso modo per le due modalità.
Sequenza e contratto dei comandi dello script in `references/agent-flow.md`.

## Transizioni di stato dopo la riuscita della registrazione

1. L'utente viene salvato con `accountStatus: 'pending'` e **3 badge** iniziali (register route).
2. Il server pianta contestualmente due cookie HttpOnly: il JWT (che dà accesso diretto a `/subscription`) e il
   pendingUserToken (credenziale d'identità per il flusso di abbonamento).
3. La pagina di registrazione rileva `pending_payment` → reindirizza a `/subscription` (conservando il parametro
   di ritorno `next`); nella modalità delegata all'agent si ottiene lo stesso effetto con `me?token=…&redirect=/subscription`.
4. Pagamento completato → `accountStatus` diventa `active` (**Alipay via notify, attivazione automatica lato
   server**; PayPal via Webhook, attivazione automatica; QR WeChat conferma manuale; Huawei IAP via
   `activate-huawei`). Dettagli in `payment-and-activation.md`.

Gli utenti non attivati (pending) che chiamano le API centrali (feed, mappa, dialoghi con umani digitali, check-in
ecc.) ricevono tutti 403; fa eccezione il link di condivisione dei post (che resta accessibile pubblicamente).

## Tabella di diagnosi degli errori comuni

| Sintomo | Causa | Cosa fare |
|---|---|---|
| 「用户名已存在」 (il nome utente esiste già) | Nome utente occupato (indipendente da maiuscole/minuscole) | Cambiare nome utente |
| 「邮箱已被使用」 (email già in uso) | Email già registrata | Cambiare email; oppure passare al login + «password dimenticata» per recuperare il vecchio account |
| 「邮箱验证码错误或已过期」 (codice di verifica errato o scaduto) | Codice sbagliato / oltre 10 minuti / oltre 5 tentativi falliti rifiutato | Premere «reinvia» e usare il codice **dell'ultimo messaggio** ricevuto |
| Il codice non arriva | Limite dei 60 secondi; oppure finito in spam/promozioni | Aspettare la fine del countdown prima di reinvitare; controllare la cartella spam |
| 「手机号已被使用」 (numero di telefono già in uso) | Numero già legato a un altro account | Togliere il numero (facoltativo) oppure cambiarlo |
| 「注册请求过于频繁」 (richieste di registrazione troppo frequenti) / 429 | Tetto dei 3 registrazioni/minuto/IP raggiunto | Aspettare qualche minuto e riprovare |
| 409 「用户名或邮箱已被注册」 (nome utente o email già registrati) | Collisione con altri proprio nell'istante dell'invio (rete di sicurezza per concorrenza) | Cambiare nome utente o email e riprovare |
| 「图片大小不能超过5MB」 (l'immagine non può superare 5MB) / 「不支持 SVG」 (SVG non supportato) | Avatar non conforme | Cambiare immagine o saltare l'avatar |
| Registrazione riuscita ma login 403 「请完成订阅以激活账户」 (completa l'abbonamento per attivare l'account) | L'account è ancora pending (stato previsto prima del pagamento) | Prima del pagamento: è normale, completa prima l'abbonamento; dopo il pagamento ancora 403: significa che si è usato un vecchio JWT, in modalità script eseguire prima `refresh-login` per rinnovare lo stato di accesso |
| Login 423 「账户已锁定」 (account bloccato) | Password sbagliata 5 volte di fila | Aspettare 30 minuti |
| Login 401 「还剩 N 次尝试机会」 (restano N tentativi) | Password errata, vicino al blocco | Pensare bene prima di riprovare, oppure andare direttamente su «password dimenticata» |
| 「该账号未设置密码，请使用其他方式登录」 (questo account non ha una password impostata, usa un altro metodo di accesso) | Account di terze parti (Google/Watcha/Huawei) | Effettuare il login con il pulsante di terze parti originario |
| 「该账号已注销」 (questo account è stato cancellato) | Account disattivato | Serve una nuova registrazione |

## Nozioni utili sul login (per la diagnosi, già che ci si è)

Il login supporta l'input tre-in-uno **nome utente / email / numero di telefono** (qualsiasi dei tre vale come
nome account).
Password dimenticata: pagina di login → «Password dimenticata» → inserire l'email di registrazione per ricevere un
codice a 6 cifre → reimpostarla.

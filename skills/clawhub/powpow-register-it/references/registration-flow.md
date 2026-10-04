# Flusso di registrazione in dettaglio — powpow-register

Riferimento per la risoluzione dei problemi. Tutte le regole provengono dal codice sorgente della piattaforma (validazione coerente Next.js lato frontend e backend), con le fonti citate.
Quando la piattaforma si aggiorna, conta il comportamento reale online.

## Accessi

- Pagina di registrazione: https://global.powpow.online/register
- Pagina di login: https://global.powpow.online/login
- Pagina abbonamento: https://global.powpow.online/subscription
- Chi arriva da un link condiviso con `?next=...`, dopo registrazione + pagamento viene riportato automaticamente alla pagina originale.

## Campi del modulo e regole

| Campo | Obbligatorio | Regola | Fonte |
|---|---|---|---|
| Avatar | Opzionale | Immagine ≤5MB, SVG non supportato; compressione automatica lato server (>100KB compressa a 400×400 / qualità 90) | `src/app/api/auth/register/route.ts` |
| Nome utente | Obbligatorio | 2–50 caratteri, salvato in **minuscolo** dopo il trim (Tom e tom sono lo stesso nome utente; registrazione e login non distinguono maiuscole/minuscole) | ídem (schema zod) |
| Password | Obbligatorio | 8–100 caratteri, deve contenere lettere maiuscole, lettere minuscole e cifre | ídem |
| Conferma password | Obbligatorio | Deve coincidere con la password (solo validazione frontend) | `src/app/(public)/register/page.tsx` |
| Soprannome | Opzionale | ≤100 caratteri; se vuoto, si usa il nome utente | register route |
| E-mail | **Obbligatoria** | Formato e-mail valido, ≤255 caratteri; un'e-mail può registrare un solo account | register route |
| Codice di verifica e-mail | **Obbligatorio** | 6 cifre; **valido 10 minuti**; esaurito dopo la verifica; un nuovo invio marca il codice precedente come usato | `src/lib/email-verification.ts` |
| Numero di telefono | Opzionale | Numero per la Cina continentale che inizia con `1[3-9]`, 11 cifre in totale; un numero può essere legato a un solo account | register route |

La pagina offre anche tre pulsanti di login di terze parti: **Google, Watcha, account Huawei** (`GoogleSignInButton` / `WatchaLoginButton` / `HuaweiLoginButton`). Gli account di terze parti non hanno password locale; provare a fare login con password più tardi restituisce « 该账号未设置密码，请使用其他方式登录 » (Questo account non ha una password impostata, usa un altro metodo di accesso).

## Rate limit e parametri anti forza bruta

| Comportamento | Limite | Fonte |
|---|---|---|
| Invio registrazione | **3 volte/min/IP**, 429 oltre il limite | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Invio codice di verifica | Stessa IP 1 volta/min **e** stessa e-mail 1 volta/min, 429 oltre il limite; countdown di 60 secondi sul pulsante frontend | `src/app/api/auth/register/send-code/route.ts` |
| Verifica del codice | Massimo **5 tentativi** per e-mail entro 10 minuti; raggiunto il tetto, rifiutato anche se il codice è giusto — serve un nuovo codice | `src/lib/email-verification.ts` |
| Codice password dimenticata | 1 volta/min/IP | `src/app/api/auth/forgot-password/route.ts` |
| Login | 5 volte/min/IP; **5 errori consecutivi bloccano l'account per 30 minuti** (423), con avviso decrescente dei tentativi rimasti | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Comportamento di protezione della privacy**: all'invio del codice di verifica / password dimenticata, l'interfaccia restituisce lo stesso messaggio di successo sia che l'e-mail sia registrata sia che non lo sia, senza rivelare se esiste un account.

## Transizione di stato dopo una registrazione riuscita

1. L'utente viene salvato con `accountStatus: 'pending'` e **3 badge iniziali** (register route).
2. Il server imposta anche due cookie HttpOnly: JWT (consente l'accesso diretto a `/subscription`) e pendingUserToken (credenziale di identità per il flusso di abbonamento).
3. La pagina di registrazione rileva `pending_payment` → salto a `/subscription` (conservando il parametro di ritorno `next`).
4. Pagamento completato → `accountStatus` diventa `active` (PayPal attiva automaticamente via Webhook; QR code WeChat con conferma manuale; IAP Huawei tramite `activate-huawei`). Vedi `payment-and-activation.md`.

Le chiamate di un utente non attivato (pending) alle API principali (feed, mappa, chat con umani digitali, check-in, ecc.) restituiscono sempre 403; fanno eccezione i link dei post condivisi (restano accessibili pubblicamente).

## Tabella degli errori comuni

| Messaggio | Causa | Cosa fare |
|---|---|---|
| 「用户名已存在」(Il nome utente esiste già) | Nome utente occupato (senza distinzione maiuscole/minuscole) | Scegli un altro nome utente |
| 「邮箱已被使用」(L'e-mail è già in uso) | E-mail già registrata | Usa un'altra e-mail; oppure passa dal login + « Password dimenticata » per recuperare il vecchio account |
| 「邮箱验证码错误或已过期」(Il codice di verifica e-mail è errato o scaduto) | Codice sbagliato / oltre 10 minuti / rifiutato dopo più di 5 tentativi | Clicca su « Invia di nuovo » e usa il codice dell'**ultima** e-mail |
| Codice di verifica non ricevuto | Rate limit di 60 secondi; oppure finito nello spam/promozioni | Aspetta la fine del countdown prima di rinviare; controlla la cartella spam |
| 「手机号已被使用」(Il numero di telefono è già in uso) | Numero legato a un altro account | Rimuovi il numero (campo opzionale) o usa un altro numero |
| 「注册请求过于频繁」/ 429 (Troppe richieste di registrazione) | Raggiunto il tetto di 3 registrazioni/min/IP | Aspetta qualche minuto e riprova |
| 409「用户名或邮箱已被注册」(Nome utente o e-mail già registrati) | Collisione con un altro utente all'invio (fallback di concorrenza) | Cambia nome utente o e-mail e riprova |
| 「图片大小不能超过5MB」/「不支持 SVG」(La dimensione dell'immagine non può superare 5MB / SVG non supportato) | Avatar non conforme | Cambia immagine o salta l'avatar |
| Registrazione riuscita ma login 403「请完成订阅以激活账户」(Completa il tuo abbonamento per attivare l'account) | L'account è ancora pending | Dopo il login, segui l'avviso sulla pagina e vai su `/subscription` per completare l'abbonamento |
| Login 423「账户已锁定」(Account bloccato) | Password sbagliata 5 volte | Aspetta 30 minuti |
| Login 401「还剩 N 次尝试机会」(Rimangono N tentativi) | Password errata, vicino al blocco | Pensa bene prima di riprovare, oppure vai diretto a « Password dimenticata » |
| 「该账号未设置密码，请使用其他方式登录」(Questo account non ha una password impostata, usa un altro metodo di accesso) | Account di terze parti (Google/Watcha/Huawei) | Accedi con il pulsante di terze parti originale |
| 「该账号已注销」(Questo account è stato disattivato) | Account disattivato | Serve una nuova registrazione |

## Curiosità sul login (utile anche per risolvere problemi)

Il login accetta un campo combinato **nome utente / e-mail / telefono** (uno qualsiasi dei tre funziona come nome account).
Password dimenticata: pagina di login → « Password dimenticata » → inserisci l'e-mail di registrazione, ricevi un codice a 6 cifre → reimposta.
# Activation ya abonnement na kofuta — powpow-register

## Conclusion (reponse liboso)

**Nzela ya Alipay ezali en ligne (uta 2026-10-07), ezali nzela ya kofuta monene ya skill oyo, agent ekoki kosala commande na kolandela mbongo ekota.**
Mosaleli ya mboka mosusu/azali na Alipay te ezonga na PayPal; scan WeChat (confirmation ya moto) na Huawei IAP ezali naino, kasi skill esala yango te.

Ndelo ya responsabilité na se ya kofuta: agent ekoki **sala commande, fungola caisse, tuna mbongo**; **jamais** ekanga compte ya Alipay ya mosaleli / identite ya kofuta, jamais epromettre «kofuta na esika ya mosaleli». Action ya kofuta mbala nionso esalaka na mosaleli moko moko na caisse officielle ya Alipay.

## Nzela ya Alipay (vibepay, monene)

Systeme ya achat mbala moko: futa mbala moko mpo ofungola duree ekokani, **ko-renouveler automatiquement te**. Plans ekangami na
`src/lib/alipay-vibepay.ts` (`ALIPAY_PACKAGES`):

| key | planId | Nkomba | Motango | Duree |
|---|---|---|---|---|
| `monthly` | alipay-monthly | Membre ya mois | ¥6.99 | jours 30 |
| `quarterly` | alipay-quarterly | Membre ya trimestre | ¥19.99 | jours 90 |
| `yearly` | alipay-yearly | Membre ya annee | ¥69.99 | jours 365 |

### Contract ya interfaces (script ya skill ekanga deja, agent assembla requete directement te)

| Interface | Methode | Explication |
|---|---|---|
| `/api/payment/alipay/create-order` | POST | Esengi `Authorization: Bearer <JWT>` (mosaleli pending ekoki). body `{package}` → ezongisa `{paymentHtml, outTradeNo, amount, planName}`; `paymentHtml` ezali lokasa ya fome etindaka automatiquement na passerelle ya Alipay |
| `/api/payment/alipay/query` | GET `?outTradeNo=` | Ndenge moko auth ya Bearer. Ezongisa `paid` / `pending` / `closed` / `unknown` |
| `/api/payment/alipay/notify` | POST (callback ya serveur Alipay) | Verification ya signature ya elements misato (signature, app_id, montant ekokana, TRADE_SUCCESS/TRADE_FINISHED, unicite ya marchand) → **idempotent** mise a jour ya commande + kosala abonnement + ko-activer kompte. Skill jamais etuna interface oyo |
| `/payment/alipay/return` | Lokasa ya retour ya navigateur | Chemin public, nsima ya kofuta elakisa confirmation «支付成功» (kofuta esilama), lokasa epoller etat reel ya backend |

- Commande non payée **efungwama automatiquement nsima ya heures 2**; mosaleli abwaka na katikati → directement sala lisusu `create-order`, commande ya kala likambo te.
- Script ekoma `paymentHtml` na fichier HTML temporaire, agent esalela commande ya systeme mpo efungola na caisse ya Alipay (scan to akota na Alipay afuta).

### Molongo ya activation (automatique, moto esengi te)

notify verification ya signature eleki → `paymentOrders` elakisa payé → `user_subscriptions` esala/etindaka liboso
(`planId`, `currentPeriodEnd` calculer na durationDays, renouvellement etindaka liboso na date ya expiration ya kala) →
`users.accountStatus: active` + `subscriptionStatus: ACTIVE` → lokasa ya retour epoller kino paid elakisa succes.

### Nsima ya kofuta esengi echangala etat ya koneksione sika (monene)

JWT ezali na declaration ya abonnement (kompte pending ezali `NONE`). **Kofuta ekota echangaka base de donnees kaka, echangaka JWT déjà signe te** — declaration ya token ya kala naino NONE, osalela directement mpo sala lien ya koneksione ekomonana «membre te».
Ndenge wana skill nsima ya confirmation `paid` liboso esala `refresh-login` (koneksione lisusu echangala JWT sika, declaration ekomi ACTIVE), nsima sala lien 2. Yango ezali comportement ya design, ezali correction ya bug te.

## Nzela nionso ya lokasa ya abonnement

Lokasa ya abonnement `src/app/(public)/subscription/page.tsx` elakisa selon environnement ya kosala:

| Nzela | Environnement | Mecanisme | Ndenge ya activation |
|---|---|---|---|
| **Alipay (monene)** | Web | `AlipayPaymentSection` na interfaces ya vibepay (table oyo na se) | notify serveur activation automatique, secondes |
| Abonnement PayPal | Web (te Harmony) | `/api/subscription/create` → kende na autorisation ya PayPal; renouvellement ya chaque mois ekoki annuler mbala nionso (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) ekoma active automatiquement |
| Abonnement «微信扫码订阅» (scan WeChat) | Web (te Harmony) | na se ya lokasa: scan transfert ya mbongo | **confirmation ya moto**, mbongo ekoki kuchelewa; nsima ya kofuta juger echec mbala moko te |
| Achat na kati ya app Huawei | Na kati ya app Harmony | Natif `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` everifier commande ya Huawei nsima activer |

Plans na motango ya PayPal ewuti dynamique na `/api/subscription/plans`; texte fixe ya lokasa: Auto-renews. Cancel anytime.

## Etat na redirection

- Alipay nsima ya kofuta → lokasa ya retour elakisa succes; PayPal succes → `/subscription/success` → kompte active →
  redirection automatique na lokasa ya libanda oyo parametre `next` elobi (ezali te lokasa ya libanda).
- Mosaleli déjà abonné afika lokasa ya abonnement → elakisa "You're All Set!", nsima ya secondes 3 ezonga lokasa ya libanda automatiquement.
- Kofuta echec/annulé (PayPal) → `/subscription/cancel`, ekoki lancer lisusu.

## Kotunga

| Tukio | Kosunga |
|---|---|
| Alipay nsima ya kofuta `query` naino pending | notify kuchelewa mingi mingi te; zela secondes 30 nsima tuna lisusu. Bado ezali te pesa mosaleli ezonga navigateur komona etat ya lokasa ya retour, bado ezali te contacter support ya plateforme (dongtao@outlook.com), pesa `outTradeNo` |
| Alipay nsima ya kofuta, lien 2 ekota naino ebombama | elibi `refresh-login` (declaration ya JWT ya kala misajour te) — liboso `refresh-login` nsima `login-link` |
| Nsima ya kofuta naino 403 (PayPal) | Webhook mbala mosusu kuchelewa, koneksione lisusu mpo refresh etat |
| WeChat efuti kasi efungolami te | confirmation ya moto ezali asynchrone, na kati ya heures ebele efungolami te contacter support ya plateforme |
| Lokasa ya abonnement elakisa "No subscription plans available" | `/api/subscription/plans` ezali na plan PayPal disponible te, likambo ya configuration ya plateforme; mosaleli ya Chine abadila na Alipay kaka |

## Note ya histoire

Na code ezali na ensemble **ya kala** ya paiement web Alipay (`src/lib/alipay.ts`, `/api/payment/create-order`,
¥9.90/¥99 achat mbala moko, sandbox na cle te ekita na paiement ya simulation), jamais ekangami na UI ya lokasa ya abonnement, ezali na lien na vibepay te. Skill jamais etuna yango; `alipay-vibepay.ts` nde nzela oyo ezali kosalelama sikoyo.

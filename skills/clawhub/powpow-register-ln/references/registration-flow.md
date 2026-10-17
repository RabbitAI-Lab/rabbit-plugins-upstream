# Detail ya mosala ya inscription — powpow-register

Mpo na koluka ntango ya kotunga makambo. Mangonga nionso ewuti na code source ya plateforme (verification ya coherence Next.js liboso na nsima), source elakisami. Plateforme ntango esali mise a jour, landa comportement reel ya ligne.

## Entrée

- Lokasa ya inscription: https://global.powpow.online/register
- Lokasa ya koneksione: https://global.powpow.online/login
- Lokasa ya abonnement: https://global.powpow.online/subscription
- Soki okoti uta lien ya partage na `?next=...`, nsima ya inscription + kofuta esila, ekozonga automatiquement na lokasa ya libanda.

## Champs ya fome na mangonga

| Champ | Obligatoire | Mangonga | Source ya code |
|---|---|---|---|
| Lilinzo ya profil | Optionnel | Lilinzo <=5MB, esupporte SVG te; serveur ecompresser automatiquement (soki >100KB ecompresser na 400×400 / qualite 90) | `src/app/api/auth/register/route.ts` |
| Kombo ya mosaleli | Obligatoire | 2~50 caracteres, nsima ya trim ekoma na **minuscule** (Tom na tom bazali kombo moko ya mosaleli, na inscription na koneksione minuscule/MAJUSCULE esengeli te) | ndenge moko (zod schema) |
| Password | Obligatoire | 8~100 caracteres, esengi ezala na lettres majuscules, lettres minuscules na nombo ensemble | ndenge moko |
| Confirmer password | Obligatoire | Ekokana na password (verification frontend kaka) | `src/app/(public)/register/page.tsx` |
| Surnom | Optionnel | <=100 caracteres; soki ezali te par default ezali kombo ya mosaleli | register route |
| Imele | **Obligatoire** | Format ya imele malamu, <=255 caracteres; imele moko ekoki inscription kompte moko kaka | register route |
| Kodi ya ndingisa ya imele | **Obligatoire** | Nombo 6; **valide na kati ya miniti 10**; nsima ya verification succes ebwakama; kotinda lisusu ekanga kodi ya kala comme déjà utilisé | `src/lib/email-verification.ts` |
| Nombo ya telephone | Optionnel | Nombo ya telephone ya Chine ebanda na `1[3-9]` jumla nombo 11; nombo ya telephone moko ekoki kanga kompte moko kaka | register route |

Lokasa mpe ezali na boutons misato ya koneksione ya bato ya misato: **Google, Watcha, Huawei** (`GoogleSignInButton` /
`WatchaLoginButton` / `HuaweiLoginButton`). Kompte ya bato ya misato ezali na password local te, nsima kosalela password mpo koneksione ekopesa
`该账号未设置密码，请使用其他方式登录` (kompte oyo ezali na password te, salela nzela mosusu ya koneksione).

## Limites na protection ya brute force

| Action | Limite | Source |
|---|---|---|
| Kotinda inscription | **mbala 3/minute/IP**, eleki 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Kotinda kodi ya ndingisa | IP moko mbala 1/minute **mpe** imele moko mbala 1/minute, eleki 429; bouton frontend compte a rebours secondes 60 | `src/app/api/auth/register/send-code/route.ts` |
| Verification ya kodi | chaque imele na kati ya miniti 10 essais kino **mbala 5**, kofika limite ata kodi ezali malamu ekatali, esengi kotinda kodi ya sika | `src/lib/email-verification.ts` |
| Kotinda kodi ya password oublié | mbala 1/minute/IP | `src/app/api/auth/forgot-password/route.ts` |
| Koneksione | mbala 5/minute/IP; kompte moko echec continu **mbala 5 efungama minutes 30** (423), na ntango yango bato oyo esengeli ezalaki ekiti kolakisa | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Comportement ya protection ya vie privee**: ntango ya kotinda kodi ya ndingisa / password oublié, soki imele déjà inscrit to ezali te, API ezongisa reponse ya succes moko moko, elakisi imele déjà inscrit te.

## Ekokana ya mode agent na inscription web

Scripts ya skill ezali kobenga **API publiques moko moko** (`/api/auth/register`, `send-code`, `login`,
`/api/auth/me`), na fome ya lokasa ya inscription ekota na verification, limites na nzela ya mbeba moko moko — mangonga nionso ya fichier oyo ezali ndenge moko mpo na modes mibale. Molongo na contract ya commandes tala `references/agent-flow.md`.

## Etat nsima ya inscription succes

1. Mosaleli akota na base na `accountStatus: 'pending'`, **badges 3 ya ebandeli** (register route).
2. Serveur mpe ekanda cookie mibale ya HttpOnly: JWT (ekoki kota directement `/subscription`) na
   pendingUserToken (identite ya mosala ya abonnement).
3. Lokasa ya inscription emoni `pending_payment` → ekende na `/subscription` (ebombi parametre `next` ya retour);
   mode ya agent esalela `me?token=…&redirect=/subscription` mpo ezala resultat ndenge moko.
4. Kofuta esila → `accountStatus` ekomi `active` (**Alipay na notify serveur activation automatique**;
   PayPal na Webhook activation automatique; scan WeChat confirmation ya moto; Huawei IAP na `activate-huawei`).
   Detail tala `payment-and-activation.md`.

Mosaleli non-active (pending) abenga API core (feed, mapa, lisolola na moto numerique, check-in, nsn.) nionso ezongisa 403;
lien ya post partagé ezali exception (ezali public, ekoki kofungwama).

## Table ya kotunga mbeba ya mbala mingi

| Tukio | Tina | Kosala nini |
|---|---|---|
| 「用户名已存在」 (kombo ya mosaleli ezali deja) | Kombo ya mosaleli déjà pris (minuscule/MAJUSCULE esengeli te) | Changer kombo ya mosaleli |
| 「邮箱已被使用」 (imele esalelamaka deja) | Imele déjà inscrit | Changer imele; to abadila nzela ya koneksione + «忘记密码» mpo ozwa kompte ya kala |
| 「邮箱验证码错误或已过期」 (kodi ya ndingisa ya imele mbeba to ekufi) | Kodi mbeba / eleki miniti 10 / essais eleki mbala 5 ekatali | Beta «重新发送» (tinda lisusu), salela kodi ya imele **ya sika** |
| Kodi ya ndingisa ekomi te | Limite ya secondes 60; to ekoti na spam/promotions | Zela compte a rebours esila nsima tinda; luka dossier ya spam |
| 「手机号已被使用」 (nombo ya telephone esalelamaka deja) | Nombo ya telephone déjà kanga kompte mosusu | Facer nombo ya telephone (optionnel) to changer nombo |
| 「注册请求过于频繁」/ 429 (demande ya inscription mingi mingi / 429) | Inscription mbala 3/minute/IP efika kilele | Zela minutes moke nsima meka |
| 409「用户名或邮箱已被注册」 (409 kombo ya mosaleli to imele déjà inscrit) | Na ntango ya kutinda ekangani na moto mosusu (protection ya concurrence) | Changer kombo ya mosaleli to imele nsima meka lisusu |
| 「图片大小不能超过5MB」/「不支持 SVG」 (lilinzo monene koleka 5MB / esupporte SVG te) | Lilinzo ya profil ezali malamu te | Changer lilinzo to bwaka lilinzo ya profil |
| Inscription succes kasi koneksione 403「请完成订阅以激活账户」 (sila kosala abonnement mpo activer kompte) | Kompte naino pending (etat ya ko attendre liboso ya kofuta) | Liboso ya kofuta: yango normal, liboso sila abonnement; nsima ya kofuta naino 403: elobi osalelaki JWT ya kala, mode script liboso `refresh-login` echangala etat ya koneksione sika |
| Koneksione 423「账户已锁定」 (kompte efungami) | Password mbeba continu mbala 5 | Zela minutes 30 |
| Koneksione 401「还剩 N 次尝试机会」 (bado N ya essais ekoki) | Password mbeba, peneza efungama | Kanisa malamu nsima meka, to directement na «忘记密码» |
| 「该账号未设置密码，请使用其他方式登录」 (kompte oyo ezali na password te, salela nzela mosusu ya koneksione) | Kompte ya bato ya misato (Google/Watcha/Huawei) | Salela bouton ya bato ya misato ya liboso mpo koneksione |
| 「该账号已注销」 (kompte efacer) | Kompte deactivate | Esengi inscription ya sika |

## Yeba ya koneksione (mpo kotunga na ndenge moko)

Koneksione esupporta entrée **kombo ya mosaleli / imele / nombo ya telephone** moko (misato nionso ekoki kosalela comme kombo ya kompte).
Password oublié: lokasa ya koneksione → «忘记密码» → koma imele ya inscription mpo ozwa kodi ya nombo 6 → reset.

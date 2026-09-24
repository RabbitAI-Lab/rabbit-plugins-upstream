# Détail ya Processus ya Inscription — powpow-register

Tala yangó ntango okoluka mokakatano. Ba règles nyonso ewuti na code ya source ya platforme (vérification ya ndenge ya sika ya Next.js na libosó/mosala ya nsima), origine emonisami. Ntango platforme ebongwanaka, landa nzéla ya solo ya site.

## Ba Lupapɛ

- Lupapɛ ya inscription: https://global.powpow.online/register
- Lupapɛ ya kokɔta: https://global.powpow.online/login
- Lupapɛ ya souscription: https://global.powpow.online/subscription
- Soki okoti na lien ya kozabana mosusu na `?next=...`, nsima ya inscription + kofuta esili, ekokende na lupapɛ ya libosó na yo automatiquement.

## Ba Champ ya Formulaire mpe Ba Règles

| Champ | Esengeli | Règle | Origine ya Code |
|---|---|---|---|
| Elilingi ya profil | Lipono | Elilingi ≤5MB, SVG esalaka te; serveur ekotia yangó automatiquement (soki >100KB e comprimer na 400×400 / qualité 90) | `src/app/api/auth/register/route.ts` |
| Kombo ya mosaleli | Esengeli | 2~50 mokanda, nsima ya trim ekomama na **mokanda ya moke** (Tom mpe tom ezali kombo moko; inscription mpe kokɔta batyolaka te mokanda ya monene/moke) | Na likoló (schema zod) |
| Password | Esengeli | 8~100 mokanda, esengeli kozala na mokanda ya monene, mokanda ya moke mpe nimero | Na likoló |
| Vérification ya password | Esengeli | Esengeli kozala ndenge moko na password (vérification ya libosó kaka) | `src/app/(public)/register/page.tsx` |
| Surnom | Lipono | ≤100 mokanda; soki etiaki te, kombo ya mosaleli nde ekozala | register route |
| Imɛli | **Esengeli** | Format ya imɛli ya solo, ≤255 mokanda; imɛli moko ekoki kosala inscription ya compte moko kaka | register route |
| Kode ya vérification ya imɛli | **Esengeli** | Nimero 6; **esalaka mpo na miniti 10**; e elimwa nsima ya vérification oyo elongi; soki batindi lisusu, kode ya libosó ekokoma inutile | `src/lib/email-verification.ts` |
| Niméro ya telefɔ́ne | Lipono | Niméro ya Chine oyo ebandaka na `1[3-9]`, nimero 11 na mobimba; niméro moko ekokani na compte moko kaka | register route |

Na likoló ya yangó, lupapɛ ezali mpe na ba butɔ misato ya kokɔta na compagnie mosusu: **Google, Watcha, Compte ya Huawei** (`GoogleSignInButton` / `WatchaLoginButton` / `HuaweiLoginButton`). Ba compte ya compagnie mosusu ezali na password ya kati te; soki otiki nsima kokɔta na password, okomona erreur «该账号未设置密码，请使用其他方式登录» (compte oyo etiaki password te, kosengeli kokɔta na nzela mosusu).

## Ba Limite ya Fréquence mpe Protection contre Explosion

| Mosala | Limite | Origine |
|---|---|---|
| Kotinda inscription | **Mbala 3 / miniti / IP**; 429 soki eleki | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Kotinda kode ya vérification | Mbala 1 / miniti na IP moko mpe mbala 1 / miniti na imɛli moko; 429 soki eleki; butɔ ya libosó ezali na compteur ya sɛkɔnd 60 | `src/app/api/auth/register/send-code/route.ts` |
| Vérification ya kode | Na mingi **mbala 5 ya komeka** na miniti 10 mpo na imɛli moko; soki limite ekomi, kode ekokoma inutile ata soki ezalaki ya solo, esengeli kotinda ya sika | `src/lib/email-verification.ts` |
| Kotinda kode ya kobosana password | Mbala 1 / miniti / IP | `src/app/api/auth/forgot-password/route.ts` |
| Kokɔta | Mbala 5 / miniti / IP; compte moko soki ekisaki **mbala 5 na molongo e klama mpo na miniti 30** (423), na ntango yango ekotalisaka ndenge bantango ya komeka ezali kokita | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Ezaleli ya bobombami**: ntango ya kotinda kode ya vérification / kobosana password, ata imɛli esali inscription to te, interface ekozongisa message ya elonga ndenge moko, elakisi te soki imɛli esali inscription.

## Bongwana ya État Nsima ya Inscription ya Kolonga

1. Mosaleli abombamaka na `accountStatus: 'pending'` na base ya ba données, na **ba badge 3 ya libosó** (register route).
2. Serveur atiaka cookies HttpOnly mibale na mbala moko: JWT (mpo na kokende na `/subscription` mbala moko) mpe pendingUserToken (identité ya processus ya souscription).
3. Lupapɛ ya inscription soki emoni `pending_payment` → ekokende na `/subscription` (ekobomba paramètre ya retour `next`).
4. Kofuta esukisi → `accountStatus` ekokoma `active` (PayPal e activer automatiquement na Webhook; QR ya WeChat esengeli kolakisa na moto; Huawei IAP ekendaka na `activate-huawei`). Tala `payment-and-activation.md` mpo na détail.

Mosaleli oyo azali nanu activé te (pending) soki asaleli ba API ya libosó (liste ya ba post, carte, kofandela na bato ya digital, check-in, bongo bongo) akomona 403 ntango nyonso; ba liens ya ba post oyo bapanzani kaka ekosala (batikaka yangó polele mpo na bato nyonso).

## Table ya Koluka Ba Erreurs ya Mbalakaka

| Emonani (messages ya système) | Ntina | Nini kosala |
|---|---|---|
| 「用户名已存在」 (Kombo ya mosaleli esili kozala) | Kombo yangó ezali na mosaleli mosusu (batyolaka mokanda ya monene/moke te) | Bongola kombo ya mosaleli |
| 「邮箱已被使用」 (Imɛli esili kosalela) | Imɛli yangó esali inscription libosó | Bongola imɛli; to kokɔta + «Nabosani password» mpo na kozongisa compte ya libosó |
| 「邮箱验证码错误或已过期」 (Kode ya vérification ya imɛli ezangi to esili koleka) | Kode ekomami mabe / eleki miniti 10 / eleki mbala 5 ya komeka mabe | Pésa «Tinda lisusu», salela kode ya vérification ya **sika** |
| Kode ya vérification ezwámí te | Limite ya sɛkɔnd 60; to ekoti na spam/publicité | Zela ete compteur esukisa mpe tinda lisusu; tala box ya spam |
| 「手机号已被使用」 (Niméro ya telefɔ́ne esili kosalela) | Niméro yangó esili kokangama na compte mosusu | Kolongola niméro ya telefɔ́ne (lipono) to bongola niméro |
| 「注册请求过于频繁」 / 429 (Mposa ya inscription eleki mingi) | Eleki limite ya mbala 3 / miniti / IP | Zela miniti mwa moke mpe meka lisusu |
| 409「用户名或邮箱已被注册」 (Kombo ya mosaleli to imɛli esili kosala inscription) | Kobombana na kombo ya moto mosusu na ntango ya kotinda (protection ya kowelela) | Bongola kombo ya mosaleli to imɛli mpe meka lisusu |
| 「图片大小不能超过5MB」 / 「不支持 SVG」 (Elilingi esengeli te koleka 5MB / SVG esalaka te) | Elilingi ya profil ezali malamu te | Bongola elilingi to longola elilingi ya profil |
| Inscription elongi kasi kokɔta elobi 403「请完成订阅以激活账户」 (Sukisa souscription mpo na activer compte na yo) | Compte ezali nanu pending | Nsima ya kokɔta, landa ndimbola ya lupapɛ kende na `/subscription` mpe sukisa souscription |
| Kokɔta 423「账户已锁定」 (Compte eklami) | Password ekisaki mbala 5 na molongo | Zela miniti 30 |
| Kokɔta 401「还剩 N 次尝试机会」 (Bantango ya komeka N etikali) | Password ezangi, ezali pembeni ya koklama | Kanisa malamu mpe meka, to kende na «Nabosani password» mbala moko |
| 「该账号未设置密码，请使用其他方式登录」 (Compte oyo etiaki password te, kosengeli kokɔta na nzela mosusu) | Ezali compte ya compagnie mosusu (Google/Watcha/Huawei) | Kokɔta na butɔ ya compagnie mosusu oyo osalelaki libosó |
| 「该账号已注销」 (Compte eklami) | Compte deactivate esalemaki | Esengeli kosala inscription lisusu |

## Koyeba Moke ya Kokɔta (esalaka mpe mpo na koluka mokakatano)

Kokɔta **esalelaka kombo ya mosaleli / imɛli / niméro ya telefɔ́ne** nyonso (moko kati na yangó ekoki kozala identité ya compte). Kobosana password: lupapɛ ya kokɔta → «Nabosani password» → pesa imɛli oyo esalaki inscription mpo na kozwa kode ya nimero 6 → tia password ya sika.
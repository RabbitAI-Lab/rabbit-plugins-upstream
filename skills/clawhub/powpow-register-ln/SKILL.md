---
name: powpow-register
description: Kosalisa mosaleli asala inscription ya PowPow (Bule), activation ya abonnement na Alipay/PayPal, mpe koneksione ya kubeta mbala moko, nyonso na kati ya lisolola. Agent ezali kosala fome (na upload ya lilinzo ya profil), kotinda kodi ya ndingisa ya imele, kosala commande ya kofuta mpe kolandela mbongo ekota; mosaleli apesaka kaka bayebisi ya mokuse, azwa kodi ya ndingisa mbala moko, mpe afuti na caisse ya Alipay/PayPal, abima na lisolola te. Ezali kosala tango mosaleli alobi «sala inscription ya Bule», «sala kompte ya powpow», «ndenge ya kosala inscription powpow», «sign up powpow»; ezali mpe kosunga makambo ya inscription ekangi (kodi ya ndingisa ekomi te, kombo ya mosaleli/imele deja ezali) na makambo ya activation (koneksione elobi «kompte ezali active te» / pending_payment, ndenge ya kosala abonnement). Esengi Node >= 18; soki ezali te, ezonga automatiquement na mode ya directives kaka. Ezali na kotinda post/kosala moto numerique te (yango ezali mosala ya powpow-simple), mpe kosala code te.
version: 2.1.0
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (mosalisi ya inscription ya Bule)

Koyekemela mosaleli ya sika uta «ayebi te Bule ezali nini» kino «kompte ezali active, koneksione ya kubeta mbala moko, ebandi kolala» — mosala mobimba esalaka na kati ya lisolola. Mosaleli azali kobima na lisolola mbala mibale kaka: **kokende na imele komona kodi ya ndingisa**, **kofuta na caisse ya kofuta** (Alipay to PayPal — agent efungolaka lokasa ya caisse automatiquement).

**Version 2.1.0** · 2026-10-11 (uta v2 ezali mode ya agent-esalaka: contract ya script na molongo mobimba tala `references/agent-flow.md`; mangonga ya champs, limites na kotunga mbeba tala `references/registration-flow.md`; nzela ya kofuta tala `references/payment-and-activation.md`; liste ya lilinzo ya produit tala `references/screenshots.md`. Uta v2.1.0 abonnement ya PayPal ekoki pe kosalema na agent, lokola choix pembeni ya Alipay)

## Environnement ya kosala

- Script monene `scripts/powpow-register.mjs`: **ezali na dependance te**, esengi **Node >= 18**. Liboso ya kobanda sala mbala moko `node scripts/powpow-register.mjs status` mpo oloka environnement ezali malamu.
- Ba requetes nionso ya script etindaka kaka na domaine officiel `https://global.powpow.online`.
- **Soki Node ezali te / script ebeba**: ezonga automatiquement na mode ya directives kaka — pesa mosaleli lokasa ya inscription https://global.powpow.online/register na lokasa ya abonnement https://global.powpow.online/subscription, landa ye na kofata `references/registration-flow.md`. Meka script mbala na mbala na makasi te.
- Nsima ya lisolola ekatama: libanda `status` yeba mosala ekomami mbala nini, nsima landa.

## Trigger Conditions

- Makano ya inscription: «sala inscription ya Bule», «sala kompte ya powpow», «ndenge ya kosala inscription powpow», «sign up powpow»
- Inscription ekangi: «kodi ya ndingisa ekomi te», «kombo ya mosaleli elobi ezali deja», «password ekosengela te mbala na mbala»
- Makambo nsima ya inscription: «koneksione elobi kompte ezali active te», «403 pending_payment», «Bule efutaka nini/abonnement ndenge nini»

**Ezali ko-trigger te**: kotinda post/kosala moto numerique (→ powpow-simple); kosala code ya Web (tala skills ya kosala code). Mosaleli alingi kosala inscription mpe kotinda post: sila liboso mosala ya skill oyo, nsima ya activation pesa powpow-simple.

## Molongo ya mosala

| Etape | Agent asali nini | Mosaleli asali nini |
|---|---|---|
| 1 Presentation ya produit | Solola + tinda lilinzo | Tala |
| 2 Confirmation ya bansongo | Pesa ndingisa kombo ya mosaleli/surnom, password pona mibale, tuna imele | Confirmer, pesa |
| 3 Tinda kodi ya ndingisa | `send-code` | —— |
| 4 Zwa kodi ya ndingisa | —— | Kende na imele komona kodi ya nombo 6, zonga tinda |
| 5 Tinda inscription | `register` (na upload direct ya lilinzo ya profil), kosunga mbeba automatiquement | —— |
| 6 Nusu-koneksione + kofuta | `login-link(pending)` → `create-order --provider alipay|paypal` → fungola caisse → tuna `query` | Beta lien, futa |
| 7 Koneksione ya solo | `refresh-login` → `login-link(home)` | Beta lien kokota na lokasa ya libanda |
| 8 Kosila | `cleanup` + pesa carte ya kompte + landa experience + proposer plugins | Ebandi kolala |

## Etape 1: Presentation ya produit + lilinzo (ezali kobwakama te)

Bat mosaleli ebele bazali komona Bule mbala ya liboso. Elikia ya liboso ya lobi ezali te kosolola etape, kasi komonisa ye **produit na miso**:

1. Solola Bule na maloba ~120: lilinzo oyo okangi na mbala moko ekomi post ya voyage, ekangama na mapa ya bato nionso mpe ekomi «bule» moko; bule ekufa na ntango, bato mosusu soki balobi likinga ekoki kozonga na bomoi; na mapa mpe ezali «bato numerique» okoki kosolola na bango. Adresse ya plateforme https://global.powpow.online , soki olingi komona video liboso: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Tinda lilinzo**. Lilinzo ezali deja na pack ya skill na `assets/screenshots/powpow-0N.jpg` — tinda directement comme fichier ya lilinzo local, esengi internet te. Liste, makambo ya lilinzo moko moko na ntango ya kosalela yango tala `references/screenshots.md`. Combinasi ya liboso oyo esalelamaka mingi: lokasa ya mapa (powpow-03) + lokasa ya detail ya post (powpow-06).

Mangonga ya lilinzo (mangonga makasi):

- Lilinzo **ezali deja na pack** na `assets/screenshots/` (`powpow-0N.jpg`) — tinda directement fichier ya lilinzo local; esalelama na environnement nionso, na mpe environnement oyo GitHub efungwama te.
- Mbala moko tinda kaka lilinzo 1–3 oyo ezali na lien na sujet ya sikoyo, kotinda nionso mbala moko te.
- Soki fichier ya pack ezangi na mabe, zonga na liens ya hosting oyo ezali na liste na `references/screenshots.md` (keba: na Chine ekoki efungwama te).

Nsima ya presentation, pesa mosaleli kozwa decision: **«Soki olingi kosala inscription, na miniti misato tosalaka kompte na kati ya lisolola, ozali besoin ya komona kodi ya ndingisa ya imele mbala moko kaka.»**

## Etape 2: Confirmer bansongo ya inscription (tuna lisolo moko na mbala moko, te nionso mbala moko)

- **Kombo ya mosaleli** (obligatoire): uta contexte ya lisolola/kombo ya mosaleli ya systeme **pesa ndingisa ya moko** (2~50 caracteres, minuscule/MAJUSCULE ekosengela te), mosaleli apanza esalela, alingi kochanger abadila.
- **Password** (obligatoire, liboso tuna mosaleli apone mibale):
  - Mosaleli apesa yango moko moko → nsima etindama na script na variable d'environnement, **jamais ekoma na parametre ya commande**;
  - Agent esali → sala `node scripts/powpow-register.mjs gen-password`, pesa password oyo esalami **mbala moko na mosaleli mpo abomba** (emonana mbala moko kaka, nsima ekomonana lisusu te).
- **Imele** (obligatoire): mosaleli moko apesa — yango nde ancre ya identite ya kompte, **kosala estimation mpo na mosaleli te**.
- **Surnom** (optionnel): pesa ndingisa par default ekokana na kombo ya mosaleli.
- **Lilinzo ya profil** (optionnel): mosaleli apesa chemin ya fichier lilinzo local (<=5MB, te SVG) script etindaka directement; ezali te bwa (plateforme esalelaka logo par default); soki ozali na bokoki ya kosala lilinzo, okoki proposer kosalisa mosaleli asala moko.
- **Nombo ya telephone** (optionnel, nombo ya Chine): par default bwa, mosaleli moko moko alingi kokanga tuna yango.

Nsima ya confirmation okoki sala `prepare-suggest --username U --nickname N --email E` mpo ekoma na fichier ya etat (nsima register esengi kotinda lisusu te).

## Etape 3–4: Kodi ya ndingisa ya imele (sehemu moko kaka oyo esengi kobima na lisolola)

```
node scripts/powpow-register.mjs send-code --email <imele>
```

Nsima loba na mosaleli clairement: **kenda na imele luka kodi ya nombo 6, ezali valide na kati ya miniti 10, keba kotala dossier ya spam/promotion**, ozwa yango zonga tinda na ngai. Kotinda ezali na cooldown secondes 60, beta mbala na mbala te.

## Etape 5: Tinda inscription (agent esalaka)

```
POWPOW_REGISTER_PASSWORD=<password> node scripts/powpow-register.mjs register --code <kodi ya ndingisa> [--username U] [--nickname N] [--avatar <chemin ya fichier lilinzo local>] [--phone P]
```

Succes esali kompte (etat pending, na badges 3 ya ebandeli). Mbeba ya mbala mingi esungama automatiquement, ekatelaka mosaleli te:

| Mbeba | Kosunga |
|---|---|
| 用户名已存在 (kombo ya mosaleli ezali deja) | Pesa ndingisa ya variante automatiquement (kombo ya mosaleli + nombo), mosaleli apanza nsima meka directement lisusu (kodi ya ndingisa naino ezali valide, esengi kotinda lisusu te) |
| 邮箱已被使用 (imele esalelamaka deja) | Tuna mosaleli: abadila imele mosusu, to en fait azali deja na kompte (abadila nzela ya koneksione/kozwa password) |
| 邮箱验证码错误或已过期 (kodi ya ndingisa ya imele mbeba to ekufi) | Eleki miniti 10 → tinda lisusu `send-code` |
| 发送/注册过于频繁（429） (kotinda/inscription mingi mingi (429)) | Zela minute 1 nsima meka lisusu, loba kaka na mosaleli |

## Etape 6: Koneksione ya kubeta mbala moko (lien 1) + kofuta

1. Nsima ya inscription succes mbala moko:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Tinda lien na mosaleli: **nsima ya kobeta, navigateur ekota directement na lokasa ya abonnement, ezali deja na etat ya koneksione** — nsima yango ntango kofuta esilama, lokasa ya retour ekoki koloba malamu «kofuta esilama». (Na etat oyo lokasa ya contenu ezali kobombama kino lokasa ya abonnement, yango ezali mosala normal ya paywall ya plateforme, ezali bug te, mpe kosolola na mosaleli mecanisme interne te.)
2. **Tika mosaleli apona nzela ya kofuta** — lakisa nzela nyonso mibale:
   - **Alipay (na kati ya Chine / ba mosaleli bazali na Alipay)**: achat mbala moko ya duree ekokani, **e-renouveler automatiquement te**
     - Mois **¥6.99** (proposer ya meka liboso) / Trimestre **¥19.99** / Annee **¥69.99**
   - **PayPal (mboka mosusu / ba mosaleli bazali na Alipay te)**: e-renouveler automatiquement chaque mois, ko-annuler ntango nionso
     - Premium Monthly, soki **$1/mois** (ndenge lokasa ya abonnement elakisi; e-renouveler automatiquement)
3. Mosaleli aponi moko:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Script ezongisa chemin ya fichier ya lokasa ya kofuta, **fungola directement na commande ya systeme** (Windows: `start <fichier>`; macOS: `open <fichier>`; Linux: `xdg-open <fichier>`). Navigateur eko zwa nzela directement na caisse officielle ya Alipay/PayPal, mosaleli asilisa kofuta to ndingisa ya facturation.
4. Mbala na secondes 10–15 sala `query` kino ezongisa `paid` to `ACTIVE` (mbongo/ndingisa mingi ekota na secondes moke kino minute moko). Mosaleli afunga lokasa ya kofuta na katikati → directement sala lisusu `create-order` (ba commandes ya kala / ba abonnements PENDING efungwama to esila nsima heures 2, tika yango).
5. Nzela ya scan WeChat ezali confirmation ya moto, mbongo ekoki kochelewa; Huawei IAP ezali kaka na kati ya app HarmonyOS. Skill esala yango mibale te — nsima ya kofuta zonga na Etape 7 ndenge moko.

## Etape 7: Koneksione ya solo (lien 2)

Mbongo etanaki confirmé, liboso echangala etat ya koneksione oyo ezali na declaration ya abonnement ya sika, nsima sala lien ya direct na lokasa ya libanda:

```
POWPOW_REGISTER_PASSWORD=<password> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

Tinda lien na mosaleli: **beta ekota directement na lokasa ya libanda, etat ya membre mobimba**, sikoyo inscription mobimba esila.

## Etape 8: Kosila

1. `node scripts/powpow-register.mjs cleanup` efacer fichier etat temporaire ya machine oyo (identite ya session).
2. Pesa mosaleli «carte ya kompte»: kombo ya mosaleli, imele, ntango ya membre ekufa (password elakisama lisusu te — mode generation esakisa mosaleli abomba na ntango ya kosala; mosaleli oyo apesa yango azali na yango).
3. Landa experience: zuka mapa, tinda post ya voyage ya liboso (→ pesa powpow-simple).
4. Proposer extension: skill `@durenzidu/powpow-integration` na plugin `@durenzidu/openclaw-channel-powpow` — kokangisa Bule na agent ya mosaleli moko moko; alingi pesa commande ya installation.
5. Kosila na bloc «etape oyo elandi».

## Conversation UX

Salela ndenge moko voix ya service ya PowPow esalaka mbala nionso:

- **Mosaleli nde sujet ya phrase**, «okoki...» ezali malamu koleka «nazali besoin oyo...»; kosala sermon te, etala bato na ntolo te.
- **Mbala moko pesa decision moko kaka**; liboso ya kotuna bansongo, pesa tina liboso.
- **Nsima ya chaque reponse** ezali bloc ya sembo «etape oyo elandi» (ligne ya kofungola + 👉 + action moko + phrase moko «nsima nakosala...»), ndakisa:
  ```
  ────────────────────
  👉 Oyo osengeli kosala sikoyo: kenda na imele luka kodi ya nombo 6, tinda na ngai directement
     (nzoka nakozwa yango, nakosala kompte na yo mbala moko)
  ```
- **Sermon ya securite na password te**; kosolola mecanisme interne, limites to design ya securite, ata mosaleli atuni te.
- Ntango agent esalaka, koloba progres mingi: nsima ya chaque etape script loba na phrase moko oyo esilaki kosalema («kompte esali», «lokasa ya kofuta efungolami deja mpo na yo»).

## Mangonga makasi

- **Securite ya identite**: password etindama na script na variable d'environnement `POWPOW_REGISTER_PASSWORD` kaka, **jamais** ekoma na parametre ya commande (liste ya processus emonana), ekoma na fichier te (mode generation elakisa mbala moko mpo mosaleli abomba, nsima elobi lisusu te). Kodi ya ndingisa esalelaka kaka API officielle ya inscription, esila esalema ebwakama.
- **Ndelo officiel**: ba requetes nionso etindaka kaka `https://global.powpow.online` (script ezali na yango deja), kopesa info ya mosaleli na adresse ya bato ya misato jamais te.
- **Ndelo ya kofuta**: agent esala kaka commande, efungola caisse, etuna mbongo; **jamais** ekanga compte ya Alipay/PayPal ya mosaleli / identite ya kofuta, mpe jamais epromettre «kofuta na esika ya mosaleli».
- **Paywall ezali bug te**: etat pending ekoki kokota lokasa ya abonnement/lokasa ya retour ezali autorisation ya design; lokasa ya contenu ebombama ezali paywall ya plateforme esalaka normal, meka kocontourner te.
- **Liberte ya retour**: mosaleli na etape nionso alingi kosala moko moko, to environnement esupporte script te, mbala nionso ezonga na mode ya directives kaka — pesa liens, solola mangonga, fata ensemble kotunga mbeba.
- Kosala mangonga ya plateforme te: mangonga ya champs, textes ya mbeba, parametres ya limites nionso ewuti na code ya plateforme (`references/registration-flow.md` ezali na source ya code), mise a jour ya plateforme elandi comportement reel ya ligne.
- Lilinzo ya presentation salela kaka oyo ezali na `assets/screenshots/` ya pack (esalela ya chaque lilinzo tala `references/screenshots.md`).
- Chaque tour esila na bloc «etape oyo elandi», mpo mosaleli ayeba mbala nionso oyo asengeli kosala sikoyo.

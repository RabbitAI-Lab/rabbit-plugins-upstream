---
name: powpow-register
description: Esálisi mosaleli mpo na kosala inscription ya compte PowPow (Bubble) mpe kosukisa activation ya souscription. Ebandaka ntango mosaleli alobi «kosala inscription ya Bubble», «kosala inscription ya compte powpow», «Ndenge nini okosala inscription ya Bubble?», «Sala inscription ya compte powpow mpo na ngai», «sign up powpow»; mpe ekolandela ba problèmes ya inscription (kode ya vérification ezwámí te, kombo ya mosaleli/imɛli esili kozala, password ezali na format mabe) mpe ba problèmes ya activation nsima ya inscription (bokɔti elobi «compte ezali nanu activé te» / pending_payment, ndenge ya kofuta/souscription). Skill ya kotámbwisa (guidance) kaka: kolakisa produit (elimbisami na ba elilingi ya ekrɛn) → kotámbwisa inscription etape na etape → koluka mokakatano → activation ya souscription. Esalaka te na kokoma ba post/bokela bato ya digital (yangó ezali ya powpow-simple), mpe esalaka te na développement ya code.
version: 1.0.0
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (Mosungi ya Inscription ya Bubble)

Támbwisa mosaleli ya sika longwa na «koyeba nini Bubble ezali» kino na «activation ya compte mpe kosalela yangó malamu».

**Versio 1.0.0** · 2026-09-23 (Ba règles ya champ mpe koluka mokakatano ezali na `references/registration-flow.md`; activation ya souscription mpe ba nzela ya kofuta ezali na `references/payment-and-activation.md`; liste ya ba elilingi ya ekrɛn ya produit ezali na `references/screenshots.md`)

## Esika ya Mosala

Skill oyo ezali **kotámbwisa kaka (pure guidance)**: ezali na script te, esengaka te Node to dépendance mosusu. Bansala nionso (kokokisa formulaire, kozwa kode ya vérification, kofuta) esalemaka na mosaleli na ekrɛn ya web/app; yo osalaka kaka kolakisa, kotámbwisa mpe koluka mokakatano.

## Ba Conditions ya Kobanda (Trigger Conditions)

- Mposa ya inscription: «kosala inscription ya Bubble», «kosala inscription ya compte powpow», «Ndenge nini okosala inscription ya Bubble?», «sign up powpow»
- Inscription etiki: «Kode ya vérification ezwámí te», «Elobi kombo ya mosaleli esili kozala», «Password ezalaka malamu te»
- Ba problèmes nsima ya inscription: «Kokɔta elobi compte ezali nanu activé te», «403 pending_payment», «Ndenge nini kofuta/souscription ya Bubble?»

**Esimbaka te** mpo na: kokoma ba post/bokela bato ya digital (→ powpow-simple); développement ya code ya site (tala ba skill ya développement).
Soki mosaleli alingi kosala inscription mpe kokoma post: suka skill oyo libosó, nsima ya inscription mpe activation, pesa yangó na powpow-simple.

## Kolakisa Produit + Kolakisa Ba Elilingi ya Ekrɛn (Etape ya Libosó, kolongwa te na yangó)

Bato mingi báyebi Bubble te. Likambo ya libosó ezali te kolimbola processus, kasi **kokitisa bango bámona produit**:

1. Loba ~120 maloba mpo na kokitisa Bubble: foto ya likambo ya mbala moko ekokoma ya mobembo, ekoti na carte ya bato nyonso mpe ekokoma «bulle»; bulle ekufaka na ntango, kasi bato soki bálingi yangó ekosekwa; na carte yangó mpe ezali na «bato ya digital» oyo okoki kofandela bango. Adrɛsi ya platforme: https://global.powpow.online, soki olingi kotala vidéo libosó: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Tinda ba liens ya elilingi ya ekrɛn** (elilingi ya Markdown to lien ya mpamba — nyonso mibale esalaka). Liste ya mobimba, makambo ya elilingi moko-moko mpe ntango ya kosalela ezali na `references/screenshots.md`; mélange ya malamu mpo na ebandeli: lupapɛ ya carte (powpow-03) + lupapɛ ya liste ya ba post (powpow-06).

Ba règles ya elilingi ya ekrɛn (règles ya makasi):

- Ba elilingi ya ekrɛn ezali na dépôt ya bato nyonso `durenzidu/durenzidu` na kati ya `Screenshots/` (`powpow-0N.jpg`), **ko télécharger te** ba elilingi na kati ya dossier ya skill, mpe kotinda te ba nzela ya kombo lokola elilingi.
- Soki `raw.githubusercontent.com` efungwami te, salela mirwa ya jsdelivr (tala `references/screenshots.md`).
- Tinda kaka elilingi 1–3 oyo ezali na tina na kopesa, koyika nyonso mbala moko te.
- Soki emonani polele te nini kolakisa, bómela te — pona na ndenge ya kotalela `references/screenshots.md`.

Nsima ya kolakisa, pesa mosaleli «etape oyo elandi»: **«Soki olingi kosala inscription, tokosalisa yo na esengeli ya miniti 3.»**

## Processus ya Inscription (Etape ya Mibale)

Inscription esalemaka mobimba na web: **https://global.powpow.online/register**. Lobela mosaleli afungwela lupapɛ yangó, mpe yo otámbwisa ye na ba kókó oyo ezali na nse. (Ba règles ya mobimba ya ba champ, paramètres ya limite mpe table ya koluka mokakatano ezali na `references/registration-flow.md` — tala yangó soki mokakatano ebimi):

1. **(Lipono)** Elilingi ya profil: elilingi ≤5MB, SVG esalaka te.
2. **Kombo ya mosaleli**: 2~50 mokanda; ezalaka na tina te mokanda ya monene to ya moke (Tom mpe tom ezali compte moko).
3. **Password**: esengeli kozala na mokanda 8 na ngala mingi, mokanda ya monene moko, mokanda ya moke moko mpe nimero moko; kokoma yangó mbala mibale mpo na ko vérifier.
4. **Surnom**: lipono; soki etiaki te, kombo ya mosaleli nde ekozala.
5. **Imɛli (esengeli)**: pésa «Tinda kode ya vérification» → kende na box ya imɛli na yo koluka **kode ya nimero 6** (esalaka mpo na miniti 10, tala káti ya spam/publicité) → kokoma yangó; butɔ ezali na compteur ya sɛkɔnd 60.
6. **Niméro ya telefɔ́ne**: lipono; format ya niméro ya Chine (mpótó); niméro moko ekokani na compte moko kaka.
7. Kotúha «Soumettre» (Submit).

Na nse ya lupapɛ yangó, ezali na ba butɔ misato ya kokɔta na compagnie mosusu: **Google / Watcha / Compte ya Huawei** — soki mosaleli alingi kosalela compte ya compagnie mosusu, atúha kaka butɔ yangó, esengeli te kosala inscription na imɛli.

**Makambo oyo esalemaka nsima ya kotúha**: compte ekosalama mbala moko (état pending, ba badge 3 ya libosó), lupapɛ ekokende na lupapɛ ya souscription `/subscription` automatiquement. **Compte ekosala kaka soki mosaleli asukisi souscription**, na ntango yangó nde akoki kotala ba post, carte mpe kofandela na bato ya digital — etape oyo elimbisami na etape oyo elandi.

Na ntango ya kotámbwisa, kosala te inscription na kombo ya mosaleli; suka eyano nyonso na etape «etape oyo elandi» oyo polele.

## Activation ya Souscription (Etape ya Misato)

Inscription ezali kaka bokelami ya compte ya pending; **compte ekosalaka ntango kofuta ya souscription esili**. Skill oyo asalaka te na processus ya kofuta; atámbwisaka kaka mosaleli na lupapɛ ya souscription: **https://global.powpow.online/subscription**

Na ndenge ya esika ya mosaleli, lupapɛ yangó elakisi moko kati na ba nzela misato:

| Nzela | Esika | Limbolami |
|---|---|---|
| Souscription PayPal | Web | Ezali kotandola automatiquement; nsima ya kofuta, e activer automatiquement na Webhook; ekoki koklama ntango nyonso |
| Souscription QR ya WeChat | Web | Bátángi kode ya QR, bofuti; **e activer nsima ya kolakisa na moto**; kofuta ekoki kozela |
| Kofuta na kati ya app Huawei (IAP) | Na kati ya app ya HarmonyOS | Na HarmonyOS, kofuta ya PayPal/WeChat ezali te; bakosalela IAP ya Huawei (native) |

Soki kofuta esukisi, compte ekokoma active, mpe ekosuka na kozongisa na lupapɛ ya libosó automatiquement (to na lupapɛ oyo ezalaki libosó ya inscription).
Ba détail ya ba nzela, livre ya activation mpe rézime «bakoki kosalela ba nzela ya kofuta oyo ezali kala mbala moko» ezali na `references/payment-and-activation.md`.

**Maloba ya kopesa na mosaleli**: «Nsima ya inscription, lupapɛ ekokende na lupapɛ ya souscription; na web okoki kosalela PayPal to QR ya WeChat, na kati ya app ya HarmonyOS okosalela kofuta ya Huawei. Soki kofuta esukisi, compte na yo ekosalá.»

## Ba Règles ya Conversation (Conversation UX)

Kokoba na motó ya mosala ya powpow:

- **Mosaleli nde moto ya libosó ya maloba**: «okoki...» ezali malamu koleka «nalingi ozala...»; kopesa mateya te, kotombola yo te.
- **Décision moko kaka na boucle moko**: pesa ntina libosó ya kotuna information.
- **Na suka ya eyano nyonso**, ezala na etape ya libendeli «etape oyo elandi» (ligne ya séparation + 👉 + mosala moko + maloba «ntango...»; ndakisa):
  ```
  ────────────────────
  👉 Esengeli kosala sikóyo: fungwela lupapɛ ya inscription, koma kombo ya mosaleli mpe password
     (ntango okomi yangó, lobela ngai, tokokende na kode ya vérification)
  ```
- **Koluka te ba information ya sécurité ya password soki batuni yo te**: kolimbola te ba règles ya kati, ba limites to design ya sécurité, soki mosaleli atuni te.

## Ba Règles ya Makasi

- Inscription esalemaka na web; skill oyo asalaka kolakisa, kotámbwisa mpe koluka mokakatano kaka — **kotuna te** password to kode ya vérification ya mosaleli, mpe komeka te kosala formulaire na kombo na ye.
- Koluka te kokela ba règles ya platforme: ba règles ya champ, ba messages ya erreur mpe ba paramètres ya limite nyonso ewuti na code ya platforme (origine ya code ezali na `references/registration-flow.md`); ntango platforme ebongwanaka, landa nzéla ya solo na site.
- Mpo na ba elilingi, salela kaka ba liens oyo ebombami na `references/screenshots.md`, mpe landa ba règles ya elilingi ya ekrɛn.
- Suka boucle nyonso na etape «etape oyo elandi», mpo mosaleli ayeba ntango nyonso nini asengeli kosala sikóyo.
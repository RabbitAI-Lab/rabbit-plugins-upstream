# powpow-register

Mosungi ya inscription ya PowPow Bubble (version ya OpenClaw): támbwisa mosaleli ya sika longwa na «koyeba nini Bubble ezali» kino na «activation ya compte mpe kosalela yangó malamu» — kolakisa produit (elimbisami na ba elilingi ya ekrɛn), kotámbwisa inscription etape na etape, koluka mokakatano mpe limbolami ya activation ya souscription.

Skill ya kotámbwisa kaka, ezali na script to dépendance te; bansala nyonso ya inscription esalemaka na mosaleli na ekrɛn ya web/app.

## Kosalela

```
openclaw skills install @durenzidu/powpow-register
```

## Misala

1. **Kolakisa produit**: kokɔtɔ ~120 maloba + ba liens ya elilingi ya ekrɛn oyo ebombami na dépôt ya bato nyonso ya GitHub (lupapɛ ya carte, lupapɛ ya liste ya ba post, bongo bongo — 6 nionso, tinda 1–3 na ndenge ya likambo).
2. **Kotámbwisa inscription**: ba règles ya champ (kombo ya mosaleli/password/kode ya vérification ya imɛli/niméro ya telefɔ́ne/elilingi ya profil), kokɔta na compagnie mosusu (Google/Watcha/Huawei) mpe ba paramètres ya limite — nyonso ewuti na code ya source ya platforme, origine emonisami.
3. **Koluka mokakatano**: kode ya vérification ezwámí te, kombo ya mosaleli/imɛli esili kozala, 403 ya kozala activé te, compte e klámí, bongo bongo — 13 ba erreurs ya mbalakaka.
4. **Activation ya souscription**: ba nzela misato — PayPal (web) / QR ya WeChat (kolakisa na moto) / Huawei IAP (HarmonyOS) — limbolami mpe koluka mokakatano; bakoki kosalela ba nzela ya kofuta oyo ezali kala mbala moko, skill asalaka kotámbwisa kaka.

## Structure ya Fichier

```
powpow-register/
├── SKILL.md                            # Matéya ya libosó (ba conditions ya kobanda, processus, ba règles ya ezaleli)
├── README.md
├── .clawhubignore
└── references/
    ├── registration-flow.md            # Ba règles ya champ ya formulaire, limite, table ya koluka mokakatano (na origine ya code)
    ├── payment-and-activation.md       # Activation ya souscription, ba nzela ya kofuta, rézime ya kosalela lisusu
    └── screenshots.md                  # Liste ya ba elilingi ya ekrɛn + guide ya mbala moko ya situation
```

## Sécurité

- Ezali na clé te; script te; esimbaka te ba identifiants ya mosaleli.
- **Kotuna te** password, kode ya vérification to ba moyens ya kofuta ya mosaleli; inscription mpe kofuta nyonso esalemaka na ba lupapɛ ya platforme.

## Licence

MIT-0 (Licence commune ya ClawHub).

## Ba Liens

- Site officiel: https://global.powpow.online
- Inscription: https://global.powpow.online/register
- Koyeba mingi na tina ya Bubble (vidéo): https://www.bilibili.com/video/BV1Wu826UEVz/
# Molongo ya agent esalaka na contract ya script — powpow-register

Detail ya execution ya etapes nionso ya SKILL.md. Commandes nionso ezali `node scripts/powpow-register.mjs <commande> [params]`, script **ezali na dependance te**, esengi **Node >= 18**, ba requetes nionso etindaka kaka `https://global.powpow.online`.

## Design ya securite (mbala nini esali ndenge wana)

| Design | Tina |
|---|---|
| Password etindaka kaka na variable d'environnement `POWPOW_REGISTER_PASSWORD` | parametres ya commande ya processus emonana na processus mosusu ya machine oyo (surface ya fuite argv), variable d'environnement na kati ya script esomaka mpe esalelama mbala moko |
| Password **jamais ekoma na fichier etat**, jamais emonana na logs | fichier etat ekoki kofanda na disque; mode generation elakisa mbala moko kaka mpo mosaleli abomba |
| Fichier etat ezali na repertoire temporaire ya systeme (`os.tmpdir()/powpow-register-state.json`, 0600) | ezali na champs tano kaka: email / username / nickname / token / outTradeNo, `cleanup` efaceraka mbala moko |
| JWT oyo agent azwa echangama na cookie ya navigateur na pont officiel `me?token=` | pont officiel oyo plateforme esali mpo na WebView ya Harmony; verification ya signature etala kaka signature + validite, ekanga empreinte ya appareil te, navigateur ya mosaleli ekoki kosalela |
| Kofuta esala kaka create-order / query / kofungola caisse | action ya kofuta na identite ya kofuta mbala nionso ezali na kati ya mosaleli na caisse officielle ya Alipay, agent apasi te |

## Reference ya commandes

| Commande | Params monene | Mosala / ntango |
|---|---|---|
| `status` | —— | Tala progres ya mosala (soma fichier etat); nsima lisolola ekatama sala yango liboso |
| `gen-password` | —— | Sala password ya makasi ya caracteres 24 (MAJUSCULE+minuscule+nombo), emonana na stdout **mbala moko kaka** |
| `prepare-suggest` | `--username --nickname --email` | Koma bansongo oyo epanzani na fichier etat (nsima register esengi kotinda lisusu te) |
| `send-code` | `--email` | Peser plateforme etinda kodi ya nombo 6 (valide miniti 10, cooldown secondes 60) |
| `register` | `--code` (obligatoire); `--username --nickname --avatar --phone` (optionnel, soki fichier etat ezali na yango esengi te) | Sala kompte pending; password na variable d'environnement `POWPOW_REGISTER_PASSWORD`; nsima succes JWT ekanda automatiquement na fichier etat |
| `login-link` | `--target pending` to `--target home` | Sala lien ya koneksione ya kubeta mbala moko (design ya liens mibale, tala se) |
| `create-order` | `--package monthly\|quarterly\|yearly` | Sala commande Alipay; ezongisa chemin ya fichier ya lokasa ya kofuta + outTradeNo (ekanda automatiquement na fichier etat) |
| `query` | —— | Tuna etat ya commande `paid / pending / closed / unknown` (outTradeNo ewuti na fichier etat), poller chaque secondes 10–15 |
| `refresh-login` | Password na variable d'environnement | Koneksione lisusu mpo azwa **JWT sika** (declaration ya abonnement echangaka uta NONE kino ACTIVE), obligatoire nsima mbongo ekota |
| `whoami` | —— | Salela token ya fichier etat tona etat ya kompte na abonnement (verifier activation esalaka) |
| `cleanup` | —— | Facera fichier etat (obligatoire na nsila) |

**Etinda variable d'environnement** (password jamais na commande):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<password>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<password>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<password> && node scripts/powpow-register.mjs register --code 123456
```

## Mecanisme ya liens mibale (design ya kati)

Etat ya koneksione ya plateforme ezali cookie HttpOnly, agent ekoki kanda cookie na navigateur directement te; pont ezali endpoint officiel
`/api/auth/me?token=<JWT>&redirect=<chemin interne>`: verification signature → mosaleli pending efungolaka session automatiquement → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / jours 7) → verification redirect (ebanda na slash moko kaka, interdit `//` na backslash, nsima ya resolution esengi ezala origine moko moko) → redirection temporaire 307 na lokasa cible.

- **Lien 1 (pesa mbala moko nsima inscription succes)**: `--target pending` → ekota `/subscription`.
  Navigateur ya mosaleli ekota etat «nusu-koneksione»: lokasa ya abonnement, lokasa ya retour ya Alipay emonana mpe esalelama; lokasa ya contenu ebombama nsima kino lokasa ya abonnement (protection ya niveaux misato: verification ya claims ya JWT na porte → verification DB → verification API core, ezali comportement normal).
- **Lien 2 (pesa nsima confirmation paid)**: liboso `refresh-login` mpo azwa JWT sika (kofuta echangaka DB kaka, echangaka claims ya JWT deja signe te, soki echangisami te ekomonana «ofuti kasi membre te»), nsima `--target home` → ekota lokasa ya libanda, etat ya membre mobimba.

## Molongo mobimba (nzela normal)

```
1.  status                          # Verification ya environnement
2.  (Etape 2 lisolola confirmer bansongo, password pona mibale; mode generation: gen-password → pesa mosaleli abomba mbala moko)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → mosaleli kende na imele komona kodi (sehemu moko kaka ya kobima na lisolola①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → lien 1 na mosaleli
7.  (Mosaleli aponi plan) create-order --package monthly
8.  start <fichier ya lokasa ya kofuta>              # Windows; macOS esalela open, Linux esalela xdg-open
    # → mosaleli afuta na caisse ya Alipay (sehemu ya kobima na lisolola②)
9.  query (chaque secondes 10–15) kino paid
10. refresh-login                   # echangala JWT sika na declaration ACTIVE
11. login-link --target home        # → lien 2 na mosaleli
12. whoami                          # confirmer subscriptionStatus: ACTIVE (optionnel)
13. cleanup                         # facera fichier etat
```

## Commande → API ya plateforme

| Commande ya script | Interface ya plateforme |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart, upload direct ya lilinzo ya profil) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (lien moko moko, esalaka ntango mosaleli abeta) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

Source ya mangonga: mangonga ya champs na limites ya inscription tala `registration-flow.md`; plans na molongo ya activation tala
`payment-and-activation.md` (nionso ezali na fichier source ya plateforme elakisami).

## Kotunga mbeba ya niveau script

| Tukio | Kosunga |
|---|---|
| `Node 版本过低` (Node version moke koleka) | Zonga na mode ya directives kaka, meka na makasi te |
| Mbeba ya reseau / timeout | Meka mbala moko; bado ebebi pesa mosaleli atala reseau nsima alanda (fichier etat ezali naino, sala `status` uta liboso mpo ezonga) |
| register elobi mbeba ya business (kombo ya mosaleli ezali deja, nsn.) | Landa table ya Etape 5 ya SKILL.md, **kodi ya ndingisa esengi kotinda lisusu te** (valide naino na kati ya miniti 10) |
| register elobi `邮箱验证码错误或已过期` (kodi ya ndingisa ya imele mbeba to ekufi) | Ekufi na ntango → tinda lisusu `send-code` |
| Nsima ya `create-order` mosaleli afunga lokasa ya kofuta | Sala directement lisusu `create-order` (commande ya kala efungwama automatiquement nsima heures 2) |
| `query` ezali kofanda pending | Ekoki kozala mosaleli afuti te; tuna moko. Asili afuti → landa table ya kotunga ya payment-and-activation.md |
| `refresh-login` 403 `pending_payment` | Kofuta naino ekomi te, zonga Etape 9 landa poller |
| Fichier etat etangami te (efacami na mabe / ekoti na machine mosusu) | `whoami`/`refresh-login` esalelama te; pesa mosaleli na navigateur oyo efungolaki lien 1 abandisa lokasa ya abonnement mpo aconfirmer etat, to koneksione lisusu (mode web) |

## Mode ya retour (directives kaka)

Na cas nionso oyo elandi, zonga mbala moko na mode ya directives kaka ya v1, souffrir script lisusu te:

- Node >= 18 ezali te to script ebeba mbala mibale moko moko na ndenge moko;
- Mosaleli alobi clairement «ngai moko nakosala na web»;
- Politique ya entreprise/appareil peki script ekende na internet.

Nsima ya retour: pesa lokasa ya inscription https://global.powpow.online/register na lokasa ya abonnement
https://global.powpow.online/subscription, landa mangonga ya `registration-flow.md` mpo kosunga na ye, voix
echangama te, chaque tour esila na bloc «etape oyo elandi».

# Activation ya Souscription mpe Kofuta — powpow-register

## Rézime (Eyano ya Libosó)

**Bakoki kosalela ba nzela ya kofuta oyo ezali kala mbala moko; skill ya mosungi ya inscription esengaka développement ya kofuta te.**

Ba ntina:

1. Interface ya inscription (`src/app/api/auth/register/route.ts`) esili kotia JWT cookie + pendingUserToken HttpOnly cookie ntango ekelaki compte ya pending; boye ntango mosaleli akomaki na `/subscription`, azali kala na état ya kokɔta — ba nzela misato ya kofuta ezali na lupapɛ ya souscription, mpe nyonso e activeraka compte ya pending yango moko.
2. Interface ya kokɔta ekozongisaka 403 + `redirectTo: '/subscription'` mpo na compte ya pending, mpe e tia cookie na ndenge moko — soki mosaleli asukisaki kofuta oyo etikalaki ntango nyonso, akokende na lupapɛ yango moko.
3. Boye, limite ya mosala ya skill ya inscription ezali «kotámbwisa mosaleli na /subscription»; esengaka te kokela interface ya kofuta ya sika, modèle ya ordre ya sika to libongwani ya backend moko.

Na ntango moko, zwa likebi: processus ya kofuta (butɔ ya PayPal JS SDK, kolakisa na moto ya QR ya WeChat, IAP native ya Huawei) **ekoki te, mpe esengeli te**, ete efutama na kombo ya mosaleli na script ya ligne de commande / skill ya conversation. Komeka te kobenga interface ya kofuta na script mpo na kofutela mosaleli, mpe kotuna te ba moyens ya kofuta na ye.

## Ba Nzela Misato ya Lupapɛ ya Souscription

Lupapɛ ya souscription `src/app/(public)/subscription/page.tsx` elakisi automatiquement na ndenge ya esika:

| Nzela | Esika | Processus | Nzela ya Activation |
|---|---|---|---|
| Souscription PayPal | Web (HarmonyOS te) | `/api/subscription/create` ekelaka souscription ya PayPal → kokɔta na permission ya PayPal; e tandolaka mokolo na mokolo, ekoki koklama ntango nyonso (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) e activeraka `accountStatus` automatiquement |
| Souscription QR ya WeChat | Web (HarmonyOS te) | Libándá ya nse ya lupapɛ «Souscription QR ya WeChat»: bátángi QR, bofuti, **e activer nsima ya kolakisa na moto** (`WechatQrPaymentSection`) | Kolakisa na moto; kofuta ekoki kozela; lobela te «esili» mbala moko sima ya kofuta |
| Kofuta na kati ya app Huawei (IAP) | Na kati ya app ya HarmonyOS | Na WebView ya HarmonyOS, kofuta PayPal/WeChat ezali te; lupapɛ ekokende na native `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` e activeraka nsima ya ko vérifier ordre ya Huawei |

Ba plans mpe ba prix balukamaka na ndenge ya dynamique na `/api/subscription/plans` (ba plans ya PayPal); maloba ya libendeli ya lupapɛ: Auto-renews. Cancel anytime.

## État mpe Bokende (Redirect)

- Kofuta esukisi → `/subscription/success` (kape ya retour ya PayPal ebombi `subscriptionId`) → compte ekomi active → e zongisaka na lupapɛ ya libosó oyo `next` emonisi automatiquement (soki te, lupapɛ ya libosó).
- Mosaleli oyo asalaki inscription libosó soki apekisi lisusu lupapɛ ya souscription → akomona "You're All Set!", sima ya sɛkɔnd 3 ekozonga na lupapɛ ya libosó automatiquement.
- Kofuta elongi te/eklami → `/subscription/cancel`, ekoki kobanda lisusu.

## Koluka Mokakatano

| Emonani | Nini kosala |
|---|---|
| Nsima ya kofuta ezali nanu 403 | PayPal: Webhook ekoki kozela mwa moke, kokɔta lisusu mpo na kobongisa état (kokɔta e zongisaka état ya base ya ba données ya sika); WeChat: kolakisa na moto esili te, zela; Huawei: vérifier ete lupapɛ ya elonga ya kofuta na kati ya app emonani |
| Lupapɛ ya souscription elobi "No subscription plans available" | `/api/subscription/plans` ezali na plan ya PayPal te; ezali problème ya configuration ya platforme, lobela mosaleli ameka lisusu na ntango mosusu |
| WeChat afuti kasi e activé te | Kolakisa na moto ezali kozwa ntango; soki na ngonga mwa moke e activé te, kende na service ya platforme (dongtao@outlook.com) |

## Likebi: Alipay

Na kati ya code, ezali na système ya kofuta ya web ya Alipay (`src/lib/alipay.ts`, `/api/payment/create-order`, modèle ya kosomba mbala moko: membre ya katikati ¥9.90 / membre ya likolo ¥99, soki clé ya sandbox ezali te ekokita na kofuta ya simulation automatiquement), **kasi esangani te na UI ya lupapɛ ya souscription** — ezali code oyo basalelaki te / babombaki mpo na mikolo ekoya. Soki balingi activer Alipay na lupapɛ ya souscription na mikolo ekoya, ekosalema na kosangisa code oyo esili kotalisama — yango ezali na tina na skill oyo te, ezali kaka référence ya décision ya équipe ya platforme.
# Ìmúṣiṣẹ́ Ìforúkọsílẹ̀ àti Ìsanwó — powpow-register

## Ìpinnu (Ìdáhùn Àkọ́kọ́)

**A lè lo àwọn ọ̀nà ìsanwó tó wà lọ́wọ́ taara; skill olùrànlọ́wọ́ ìforúkọsílẹ̀ kò ní láti ṣe àgbékalẹ̀ ìsanwó kankan.**

Àwọn ìdí:

1. Interface ìforúkọsílẹ̀ (`src/app/api/auth/register/route.ts`) ti fi JWT cookie + pendingUserToken HttpOnly cookie sílẹ̀ nígbà tí ó bá dá àkọọlẹ̀ pending; nítorí náà, nígbà tí olùmúlò dé `/subscription`, ó ti wà ní ipò ìwọlé tẹ́lẹ̀ — àwọn ọ̀nà ìsanwó mẹ́tẹ̀ẹ̀ta ní ojú-ìwé ìforúkọsílẹ̀, gbogbo wọ́n sì ń mú àkọọlẹ̀ pending kanna ṣiṣẹ́.
2. Interface ìwọlé dá 403 + `redirectTo: '/subscription'` padà fún àkọọlẹ̀ pending, ó sì fi cookie sílẹ̀ ní ọ̀nà kanna — bí olùmúlò bá parí ìsanwó tó ṣẹ́kù nígbàkúgbà, yóò lọ sí ojú-ìwé kanna.
3. Nítorí náà, ààlà ojúṣe skill ìforúkọsílẹ̀ ni «dárí olùmúlò sí /subscription»; kò sí láti ṣẹ̀dá interface ìsanwó tuntun, àwoṣe àṣẹ tuntun tàbí àyípadà ẹ̀yìn-ọkàn kankan.

Ní àkókò kanna, ṣe àkíyèsí: ìlànà ìsanwó (bọ̀tìnì PayPal JS SDK, ìfọwọ́sowọ́pọ̀ ènìyàn QR WeChat, IAP ẹlẹ́yà Huawei) **kò ṣeé ṣe, kò sì yẹ kí ó di ìsanwó lórúkọ olùmúlò nípasẹ̀ ìkọ̀wé-ètò ìlà-àṣẹ / skill ìbánisọ̀rọ̀**. Má ṣe gbìyànjú láti pe interface ìsanwó nípasẹ̀ ìkọ̀wé-ètò láti sanwó fún olùmúlò, má sì béèrè àwọn ohun-èlò ìsanwó rẹ̀.

## Àwọn Ọ̀nà Mẹ́ta ojú-Ìwé Ìforúkọsílẹ̀

Ojú-ìwé ìforúkọsílẹ̀ `src/app/(public)/subscription/page.tsx` máa ń fi hàn fúnrarẹ̀ ní ìbámu pẹ̀lú àyíká:

| Ọ̀nà | Àyíká | Ìlànà | Ọ̀nà Ìmúṣiṣẹ́ |
|---|---|---|---|
| Ìforúkọsílẹ̀ PayPal | Ayélujára (kì í ṣe HarmonyOS) | `/api/subscription/create` dá ìforúkọsílẹ̀ PayPal → wọlé sí àṣẹ PayPal; ó máa ń tún ara rẹ̀ ṣe lóṣooṣù, ó ṣeé ṣe láti fagilé nígbàkúgbà (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) máa ń mú `accountStatus` ṣiṣẹ́ fúnrarẹ̀ |
| Ìforúkọsílẹ̀ QR WeChat | Ayélujára (kì í ṣe HarmonyOS) | Apá nísàlẹ̀ ojú-ìwé «Ìforúkọsílẹ̀ QR WeChat»: a kà kódì QR tán, a sanwó, **a máa ń ṣiṣẹ́ lẹ́yìn ìfọwọ́sowọ́pọ̀ ènìyàn** (`WechatQrPaymentSection`) | Ìfọwọ́sowọ́pọ̀ ènìyàn; ìsanwó lè sún ọ̀wọ́n; má ṣe kúkú sọ «ó parí» fún olùmúlò lẹ́sẹ̀kẹsẹ̀ lẹ́yìn tí ó sanwó |
| Rírà inú-app Huawei (IAP) | Nínú app HarmonyOS | Nínú WebView HarmonyOS, ìsanwó PayPal/WeChat kò sí; ojú-ìwé yóò lọ sí native `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` máa ń mú un ṣiṣẹ́ lẹ́yìn ìfọwọ́sí àṣẹ Huawei |

A máa ń ka àwọn ètò àti owó láti inú `/api/subscription/plans` ní ọ̀nà tó ń yí padà (àwọn ètò PayPal); ọ̀rọ̀ tó dúró ṣinṣin ní ojú-ìwé: Auto-renews. Cancel anytime.

## Ipò àti Ìyípadà (Redirect)

- Ìsanwó parí → `/subscription/success` (ìpèpadà PayPal pa `subscriptionId` mọ́) → àkọọlẹ̀ di active → ó padà sí ojú-ìwé àkọ́kọ́ tí `next` tọ́ka sí fúnrarẹ̀ (tí kò bá sí, ojú-ìwé àkọ́kọ́).
- Olùmúlò tí ó ti forúkọ sílẹ̀ tẹ́lẹ̀ tí ó bá tún wọ ojú-ìwé ìforúkọsílẹ̀ → yóò rí "You're All Set!", lẹ́yìn ìṣẹ́jú-àáyá mẹ́ta yóò padà sí ojú-ìwé àkọ́kọ́ fúnrarẹ̀.
- Ìsanwó kùnà/fagilé → `/subscription/cancel`, a lè bẹ̀rẹ̀ lẹ́ẹ̀kan sí i.

## Ìṣàwárí Ìṣòro

| Ìṣẹ̀lẹ̀ | Ohun tí ó ṣe |
|---|---|
| Lẹ́yìn ìsanwó ṣì ń rí 403 | PayPal: Webhook lè sún díẹ̀, wọlé lẹ́ẹ̀kan sí i láti tún ipò rẹ̀ ṣe (ìwọlé máa ń dá ipò ibùdó ìsọfúnni tuntun padà); WeChat: ìfọwọ́sowọ́pọ̀ ènìyàn kò tíì parí, dúró; Huawei: fi díi rí i pé ojú-ìwé àṣeyọrí ìsanwó inú-app hàn |
| Ojú-ìwé ìforúkọsílẹ̀ ń sọ "No subscription plans available" | `/api/subscription/plans` kò ní ètò PayPal kankan tó wà; àìṣedáradára ìtòlẹ́sẹẹsẹ pẹ̀pẹ̀ ni, sọ fún olùmúlò kí ó gbìyànjú lẹ́ẹ̀kan sí i nígbà mìíràn |
| WeChat sanwó ṣùgbọ́n kò tíì ṣiṣẹ́ | Ìfọwọ́sowọ́pọ̀ ènìyàn ń gba àkókò; bí kò bá ṣiṣẹ́ láàárín wákàtí díẹ̀, kan ẹgbẹ́ pẹ̀pẹ̀ (dongtao@outlook.com) |

## Àkíyèsí: Alipay

Nínú kóòdù, ètò ìsanwó Alipay ayélujára wà (`src/lib/alipay.ts`, `/api/payment/create-order`, àwoṣe rírà ẹ̀ẹ̀kan: ọmọ ẹgbẹ́ ìrọ̀rùn ¥9.90 / ọmọ ẹgbẹ́ gíga ¥99, bí kò bá sí bọ́tìnnì sandbox yóò wá sí ìsanwó afọwọ́ṣe fúnrarẹ̀), **ṣùgbọ́n kò so mọ́ UI ojú-ìwé ìforúkọsílẹ̀** — ó jẹ́ kóòdù tí a kò lò/tí a fi pamọ́ fún ọjọ́ ọ̀la. Bí a bá fẹ́ mú Alipay ṣiṣẹ́ lórí ojú-ìwé ìforúkọsílẹ̀ ní ọjọ́ iwájú, a lè ṣe é nípasẹ̀ sísopọ̀ kóòdù yìí tí a ti ṣètò — èyí kò ní í ṣe pẹ̀lú skill yìí, ó jẹ́ ìtọ́kasí ìpinnu ẹgbẹ́ pẹ̀pẹ̀ nìkan.
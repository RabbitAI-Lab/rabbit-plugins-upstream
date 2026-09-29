# Usajili, Uanzishaji na Malipo — powpow-register

## Hitimisho (Jibu kwanza)

**Njia zilizopo za malipo zinaweza kutumika tena moja kwa moja; skill ya msaidizi wa kujiandikisha haiitaji maendeleo yoyote ya malipo.**

Sababu:

1. Interface ya kujiandikisha (`src/app/api/auth/register/route.ts`) wakati wa kuunda akaunti ya pending tayari imetoa JWT cookie + pendingUserToken HttpOnly cookie, kwa hivyo mtumiaji anapofika `/subscription` tayari yuko katika hali ya kuingia (logged-in) — njia zote tatu za malipo zimeunganishwa kwenye ukurasa huu wa usajili, na zinamilisha akaunti hiyo hiyo ya pending.
2. Interface ya kuingia inarudisha 403 + `redirectTo: '/subscription'` kwa akaunti za pending, na huweka cookie sawa — mtumiaji akifanya malipo ya nyongeza wakati wowote ataelekezwa kwenye ukurasa huo huo.
3. Kwa hivyo mipaka ya wajibu wa skill ya kuongoza kujiandikisha ni «kumwelekeza mtumiaji kwenye /subscription»; haiitaji interface mpya ya malipo, haiitaji modeli mpya ya oda wala mabadiliko yoyote ya upande wa seva (backend).

Wakati huo huo zingatia: mchakato wa malipo (kitufe cha PayPal JS SDK, uthibitisho wa mtu wa kuchanganua msimbo wa WeChat, IAP asilia ya Huawei) **unamaanisha kwamba hauwezi na haupaswi kulipwa kwa niaba ya mtumiaji na skill ya mstari wa amri/mazungumzo**. Usijaribu kutumia skripti kuita interface ya malipo kulipa kwa niaba ya mtumiaji, wala usiombe hati za malipo za mtumiaji.

## Njia Tatu za Ukurasa wa Usajili

Ukurasa wa usajili `src/app/(public)/subscription/page.tsx` huonyesha kiotomatiki kulingana na mazingira ya uendeshaji:

| Njia | Mazingira | Mfumo | Njia ya uanzishaji |
|---|---|---|---|
| Usajili wa PayPal | Wavuti (si HarmonyOS) | `/api/subscription/create` inaunda usajili wa PayPal → inaruka kwa idhini ya PayPal; hujifanyia upya kila mwezi, unaweza kufuta wakati wowote (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) huweka `accountStatus` kuwa active kiotomatiki |
| Usajili wa kuchanganua msimbo wa WeChat | Wavuti (si HarmonyOS) | Kizuizi cha chini cha ukurasa «Usajili wa kuchanganua msimbo wa WeChat»: changanua msimbo uhamishe pesa, **hufunguliwa baada ya uthibitisho wa mtu** (`WechatQrPaymentSection`) | Uthibitisho wa mtu; kukamilika kwa malipo kunaweza kuchelewa; baada ya mtumiaji kulipa usiharakishe kuhukumu kwamba kumeshindwa |
| Ununuzi wa ndani ya App (IAP) wa Huawei | Ndani ya App ya HarmonyOS | Kwenye WebView ya HarmonyOS PayPal/WeChat hazipatikani; ukurasa hutumia `NativeBridge.purchaseSubscription()` asilia | `/api/subscription/activate-huawei` inathibitisha oda ya Huawei kisha inamilisha |

Mipango na bei husomwa kwa nguvu (dynamically) kutoka `/api/subscription/plans` (mipango ya PayPal); maandishi yasiyobadilika ya ukurasa: Auto-renews. Cancel anytime.

## Hali na Mabadiliko ya Ukurasa

- Malipo yamefanikiwa → `/subscription/success` (upokeaji wa PayPal unabeba `subscriptionId`) → akaunti active → inarudi kiotomatiki kwenye ukurasa wa awali uliowekwa na parameta ya `next` (kama hakuna, ukurasa wa mwanzo).
- Mtumiaji aliyekwisha usajili akifika tena kwenye ukurasa wa usajili → inaonyesha "You're All Set!", baada ya sekunde 3 inarudi kiotomatiki kwenye ukurasa wa mwanzo.
- Malipo yakishindwa/kufutwa → `/subscription/cancel`, yanaweza kuanzishwa upya.

## Utatuzi wa Matatizo

| Dalili | Nini cha kufanya |
|---|---|
| Bado 403 baada ya kulipa | PayPal: Webhook wakati mwingine huchelewa; ingia upya usasishe hali (kwenye kuingia inaangalia hali ya punde zaidi kwenye hifadhidata); WeChat: uthibitisho wa mtu haujakamilika, subiri; Huawei: thibitisha kama ukurasa wa mafanikio wa malipo ndani ya App umeonekana |
| Ukurasa wa usajili unaonyesha "No subscription plans available" | `/api/subscription/plans` haina mpango wa PayPal unaopatikana; ni tatizo la usanidi wa upande wa jukwaa, mwambie mtumiaji ajaribu baadaye |
| Amealipa kwa WeChat lakini haijafunguliwa | Uthibitisho wa mtu ni wa muda (asynchronous); ikiwa haijafunguliwa ndani ya masaa machache wasiliana na msaada wa jukwaa (dongtao@outlook.com) |

## Dokezo: Alipay

Kwenye msimbo kuna mfumo wa malipo ya wavuti ya Alipay (`src/lib/alipay.ts`, `/api/payment/create-order`, modeli ya ununuzi wa mara moja wa mwanachama wa kawaida ¥9.90 / mwanachama wa juu ¥99, na wakati sandbox haina funguo inapungua kiotomatiki hadi malipo ya simulizi), **lakini haijaunganishwa kwenye UI ya ukurasa wa usajili** — ni msimbo usiotumika/uliohifadhiwa. Iwapo siku zijazo unataka kuwezesha Alipay kwenye ukurasa wa usajili, unganisha kwa kutumia msimbo huu uliopo — hii haihusiani na skill hii, ni kwa ajili ya maamuzi ya upande wa jukwaa tu.
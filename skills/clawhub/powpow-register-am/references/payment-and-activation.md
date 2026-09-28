# የደንበኝነት ማንቃት እና ክፍያ — powpow-register

## መደምደሚያ (መጀመሪያ መልስ)

**ያሉት የክፍያ መንገዶች በቀጥታ እንደገና መጠቀም ይቻላል፤ የምዝገባ ረዳት skill ምንም የክፍያ ልማት አያስፈልገውም።**

ምክንያቶች፦

1. የምዝገባ interface (`src/app/api/auth/register/route.ts`) የpending መለያ ሲፈጥር ቀድሞውኑ JWT cookie + pendingUserToken HttpOnly cookie አውጥቷል፤ ስለዚህ ተጠቃሚው `/subscription` ሲደርስ ቀድሞውኑ በገብተኝነት (logged-in) ሁኔታ ላይ ነው — ሦስቱም የክፍያ መንገዶች በዚህ የደንበኝነት ገጽ ላይ የተንጠለጠሉ ሲሆን፣ ሁሉም የሚያነቁት ያንኑ የpending መለያ ነው።
2. የመግቢያ interface ለpending መለያ 403 + `redirectTo: '/subscription'` ይመልሳል፣ እንዲሁም cookie በተመሳሳይ ሁኔታ ያስቀምጣል — ተጠቃሚው በማንኛውም ጊዜ የጎደለውን ክፍያ ቢያከናውን ወደዚያው ገጽ ይመራል።
3. ስለዚህ የምዝገባ መምሪያ skill የኃላፊነት ድንበር «ተጠቃሚውን ወደ /subscription መምራት» ነው፤ አዲስ የክፍያ interface፣ አዲስ የትዕዛዝ ሞዴል ወይም ማንኛውም የኋላ-ጫፍ ለውጥ አያስፈልግም።

በተመሳሳይ ጊዜ ልብ ይበሉ፡ የክፍያ ሂደቱ (የPayPal JS SDK አዝራር፣ የWeChat QR የሰው ማረጋገጫ፣ የHuawei native IAP) **በትእዛዝ-መስመር/ውይይት skill በተጠቃሚ ስም መከፈል እንደማይችል እና እንደማይገባ ይወስናል**። በስክሪፕት የክፍያ interfaceን ጠርቶ ለተጠቃሚው ለመክፈል አትሞክር፣ የተጠቃሚውን የክፍያ ማረጋገጫዎችም አትጠይቅ።

## የደንበኝነት ገጽ ሦስት መንገዶች

የደንበኝነት ገጽ `src/app/(public)/subscription/page.tsx` እንደ አሰራር አካባቢው በራስ-ሰር ያሳያል፦

| መንገድ | አካባቢ | አሰራር | የማንቃት መንገድ |
|---|---|---|---|
| የPayPal ደንበኝነት | ድረ-ገጽ (HarmonyOS አይደለም) | `/api/subscription/create` የPayPal ደንበኝነት ይፈጥራል → ወደ PayPal ፈቃድ ይዘላል፤ በየወሩ በራስ-ሰር ይታደሳል፣ በማንኛውም ጊዜ መሰረዝ ይቻላል (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) በራስ-ሰር `accountStatus`ን active ያደርገዋል |
| የWeChat QR ቅኝት ደንበኝነት | ድረ-ገጽ (HarmonyOS አይደለም) | ከገጹ በታች «የWeChat QR ቅኝት ደንበኝነት» ክፍል፡ QR ተቃኝቶ ገንዘብ ይዛወራል፣ **በሰው ከተረጋገጠ በኋላ ይከፈታል** (`WechatQrPaymentSection`) | የሰው ማረጋገጫ፤ ገንዘቡ ለመድረስ ሊዘገይ ይችላል፤ ተጠቃሚው ከከፈለ በኋላ በፍጥነት «ተሳነፈ» አትይዘው |
| የHuawei በ-App ግዢ (IAP) | በHarmonyOS App ውስጥ | በHarmonyOS WebView ውስጥ PayPal/WeChat ክፍያ አይገኝም፤ ገጹ ወደ native `NativeBridge.purchaseSubscription()` ይሄዳል | `/api/subscription/activate-huawei` የHuawei ትዕዛዝ ካረጋገጠ በኋላ ያነቃል |

ዕቅዶች እና ዋጋዎች ከ `/api/subscription/plans` በተለዋዋጭ ሁኔታ ይነበባሉ (የPayPal ዕቅዶች)፤ የገጹ ቋሚ ጽሑፍ፡ Auto-renews. Cancel anytime.

## ሁኔታ እና ዝላይ (Redirect)

- ክፍያ ተሳክቷል → `/subscription/success` (የPayPal መልሶ-ጥሪ `subscriptionId` ይይዛል) → መለያ active → በ`next` መለኪያ ወደተጠቀሰው የመጀመሪያ ገጽ በራስ-ሰር ይመለሳል (ከሌለ ወደ መነሻ ገጽ)።
- ቀድሞ የተመዘገበ ተጠቃሚ የደንበኝነት ገጹን እንደገና ሲጎበኝ → "You're All Set!" ያሳያል፣ ከ3 ሰከንድ በኋላ በራስ-ሰር ወደ መነሻ ገጽ ይመለሳል።
- ክፍያ ተሳነፈ/ተሰረዘ → `/subscription/cancel`፣ እንደገና መጀመር ይቻላል።

## መፈተሻ

| ክስተት | ምን ማድረግ |
|---|---|
| ከከፈለ በኋላ አሁንም 403 | PayPal፡ Webhook አልፎ አልፎ ይዘገያል፣ እንደገና ግባ ሁኔታውን ለማደስ (በመግቢያ ጊዜ አዲሱን የመረጃ ቋት ሁኔታ ይመለሳል)፤ WeChat፡ የሰው ማረጋገጫ አልተጠናቀቀም፣ ጠብቅ፤ Huawei፡ በ-App ውስጥ የክፍያ ስኬት ገጽ መታየቱን አረጋግጥ |
| የደንበኝነት ገጽ "No subscription plans available" ይላል | `/api/subscription/plans` ምንም የሚገኝ የPayPal ዕቅድ የለውም፤ የመድረክ ወገን አወቃቀር ችግር ነው፣ ተጠቃሚው ትንሽ ቆይቶ እንዲሞክር ንገረው |
| WeChat ከፍሏል ግን አልተከፈተም | የሰው ማረጋገጫ ጊዜ የሚወስድ ነው፤ በጥቂት ሰዓታት ውስጥ ካልተከፈተ የመድረክ ድጋፍን አግኝ (dongtao@outlook.com) |

## ማስታወሻ፡ Alipay

በኮዱ ውስጥ የAlipay ድረ-ገጽ ክፍያ ስርዓት አለ (`src/lib/alipay.ts`፣ `/api/payment/create-order`፣ ተራ አባል ¥9.90 / የላቀ አባል ¥99 የአንድ-ጊዜ ግዢ ሞዴል፣ sandbox ቁልፍ ከሌለው በራስ-ሰር ወደ ማስመሰል ክፍያ ይወርዳል)፣ **ነገር ግን ከደንበኝነት ገጽ UI ጋር አልተገናኘም** — ያልተጠቀመ/ለወደፊት የተቀመጠ ኮድ ነው። ወደፊት በደንበኝነት ገጽ ላይ Alipayን ማንቃት ከተፈለገ፣ ይህን የዘጋጀውን ኮድ በማገናኘት ይሰራል — ይህ ከዚህ skill ጋር አይገናኝም፣ ለመድረክ ወገን ውሳኔ ማጣቀሻ ብቻ ነው።
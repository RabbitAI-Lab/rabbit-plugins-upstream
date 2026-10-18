# ایجنٹ معاون عمل تے سکرپٹ معاہدہ — powpow-register

SKILL.md دے قدم دے عمل دیاں تفصیلاں۔ ساریاں کمانڈاں `node scripts/powpow-register.mjs <ذیلی کمانڈ> [پیرامیٹر]` نیں، سکرپٹ **انحصار توں آزاد** اے، **Node >= 18** لوڑ اے، ساریاں درخواستاں صرف `https://global.powpow.online` تے جاندیاں نیں۔

## سلامتی ڈیزائن (ایوں کیوں بنایا گیا)

| ڈیزائن | کارن |
|---|---|
| پاس ورڈ صرف ماحول متغیر `POWPOW_REGISTER_PASSWORD` راہیں جاندا اے | پروسیس کمانڈ لائن آرگومنٹ اسی مشین دے ہور پروسیساں نوں دکھ سکدے نیں (argv لیک سطح)، ماحول متغیر سکرپٹ وچ پڑھ کے فوراً ورتیا جاندا اے |
| پاس ورڈ **کدے سٹیٹ فائل وچ نہیں لکھیا**، لاگ وچ کدے نہیں آؤندا | سٹیٹ فائل ڈسک تے رہ سکدی اے؛ گفتگو وچ بناون والے موڈ وچ اک واری دکھانا صرف اس لئی اے کہ صارف محفوظ کر لے |
| سٹیٹ فائل سسٹم عارضی ڈائریکٹری وچ (`os.tmpdir()/powpow-register-state.json`, 0600) | صرف email / username / nickname / token / outTradeNo پنج فیلڈز، `cleanup` اک کلک وچ صاف |
| ایجنٹ کول آیا JWT سرکاری `me?token=` اینڈپوائنٹ راہیں براؤزر cookie وچ بدلدا اے | ہارمونی WebView لئی بنایا گیا پلیٹ فارم دا سرکاری پل؛ سائنئچر دی جانچ صرف سائن + مہلت، ڈیوائس فنگرپرنٹ نہیں بنھدا، صارف دا براؤزر ورت سکدا اے |
| پیمنٹ صرف create-order / query / کیشیئر کھولھنا | ادا کرن دا عمل تے پیمنٹ کریڈینشل ہمیشہ صارف تے Alipay سرکاری کیشیئر دے وچکار، ایجنٹ وچ نہیں لنگھدا |

## کمانڈ حوالہ

| کمانڈ | اہم پیرامیٹر | کم / ویلہ |
|---|---|---|
| `status` | —— | عمل دی ترقی ویکھو (سٹیٹ فائل پڑھو)؛ گفتگو رک جان تے پہلے ایہ چلاؤ |
| `gen-password` | —— | 24 حروف دا مضبوط پاس ورڈ بناوے (کیپس+سمال+نمبر)، stdout تے **صرف اک واری** دکھدا اے |
| `prepare-suggest` | `--username --nickname --email` | تصدیق شدہ معلومات سٹیٹ فائل وچ لکھو (بعد وچ register نوں دوبارہ بھیجن دی لوڑ نہیں) |
| `send-code` | `--email` | پلیٹ فارم نوں 6 ہندسے دا تصدیقی کوڈ بھیجن لئی کہو (10 منٹ چلدا اے، 60s کول ڈاؤن) |
| `register` | `--code` (لازمی)؛ `--username --nickname --avatar --phone` (اختیاری، سٹیٹ فائل وچ ہووے تاں دین دی لوڑ نہیں) | pending اکاؤنٹ بناؤ؛ پاس ورڈ `POWPOW_REGISTER_PASSWORD` ماحول متغیر راہیں؛ کامیابی تے JWT خود سٹیٹ فائل وچ محفوظ |
| `login-link` | `--target pending` یا `--target home` | اک کلک لاگ ان لنک بناؤ (دو لنک ڈیزائن، تھلے ویکھو) |
| `create-order` | `--package monthly\|quarterly\|yearly` (Alipay ڈیفالٹ) <br>`--provider alipay\|paypal` | پیمنٹ آرڈر بناوے؛ Alipay پیمنٹ صفہہ فائل راہ + outTradeNo دیندا اے؛ PayPal اجازت صفہہ فائل راہ + subscriptionId دیندا اے (خود سٹیٹ فائل وچ لکھیا جاندا اے) |
| `query` | —— | آرڈر/سبسکرپشن حالت پچھو۔ Alipay: `paid / pending / closed / unknown`؛ PayPal: `ACTIVE / PENDING`, 10–15s پولنگ |
| `refresh-login` | پاس ورڈ ماحول متغیر راہیں | دوبارہ لاگ ان کے **نواں JWT** لو (سبسکرپشن دعوا NONE توں ACTIVE)، پیمنٹ آؤن تے لازمی چلاؤ |
| `whoami` | —— | سٹیٹ فائل دے token نال اکاؤنٹ تے سبسکرپشن حالت پچھو (ایکٹویشن کم کر رہیا اے پکا کرو) |
| `cleanup` | —— | سٹیٹ فائل مٹاؤ (اختتام تے لازمی) |

**ماحول متغیر پچھارنا** (پاس ورڈ کدے کمانڈ لائن تے نہیں):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<پاس ورڈ>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<پاس ورڈ>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<پاس ورڈ> && node scripts/powpow-register.mjs register --code 123456
```

## دو لنک نظام (بنیادی ڈیزائن)

پلیٹ فارم دی لاگ ان حالت HttpOnly cookie اے، ایجنٹ براؤزر لئی سدھا cookie نہیں لگا سکدا؛ پل سرکاری
`/api/auth/me?token=<JWT>&redirect=<سائٹ دے اندر راہ>` اینڈپوائنٹ اے: سائنئچر جانچ → pending صارف لئی خودکار
session بناوے → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 دن) →
redirect دی جانچ (صرف اک سلیش نال شروع، `//` تے بیک سلیش منع، حل کرن تے اسی origin ہونا چاہیدا) → 307 عارضی redirect متعلقہ صفہے تے۔

- **لنک 1 (رجسٹریشن کامیاب تے فوری دو)**: `--target pending` → `/subscription` تے لنگھدا اے۔
  صارف دا براؤزر «اادھا لاگ ان» حالت وچ آ جاندا اے: سبسکرپشن صفہہ، Alipay واپسی صفہہ ویکھ سکدا اے تے استعمال کر سکدا اے؛ مواد صفے اجے وی پے وال سبسکرپشن صفہے تے واپس دھکیلدے نیں (تن پرتاں دا بچاؤ: JWT claims گیٹ وے جانچ → DB دوبارہ جانچ → کور API جانچ، عام سلوک اے)۔
- **لنک 2 (paid دی تصدیق تے دو)**: پہلے `refresh-login` نواں JWT لو (پیمنٹ صرف DB اپڈیٹ کردی اے، پہلے توں جاری JWT دے claims نہیں بدلدی، نہ بدلو تے «پیسے دتے پر ممبر نہیں» لگدا اے)، فیر `--target home` → ہوم پیج تے لنگھدا اے،
  مکمل ممبر حالت۔

## پورا سلسلہ (عام راہ)

```
1.  status                          # ماحول خود جانچ
2.  (قدم 2 گفتگو وچ معلومات دی تصدیق، پاس ورڈ لئی دو وِکھپ؛ بناون والے موڈ: gen-password → صارف نوں فوری محفوظ کرواؤ)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → صارف ای میل تے جا کے کوڈ ویکھے (گفتگو چھوڑن دا پہلا قدم①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → لنک 1 صارف نوں
7.  (صارف ادائیگی دا طریقہ چوندا اے)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <پیمنٹ صفہہ فائل>              # Windows; macOS open ورتدا اے، Linux xdg-open
    # → صارف Alipay/PayPal کیشیئر تے ادا کردا اے یا اجازت دیندا اے (گفتگو چھوڑن دا دوجا قدم②)
9.  query (ہر 10–15s) جدوں تک paid / ACTIVE
10. refresh-login                   # ACTIVE دعوا والا نواں JWT
11. login-link --target home        # → لنک 2 صارف نوں
12. whoami                          # subscriptionStatus: ACTIVE پکا کرو (اختیاری)
13. cleanup                         # سٹیٹ فائل صاف
```

## کمانڈ → پلیٹ فارم API نقشہ

| سکرپٹ کمانڈ | پلیٹ فارم انٹرفیس |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart، پروفائل تصویر سدھا اپلوڈ) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (لنک خود، صارف کلک کرن تے کم کردا اے) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

قاعدے دا سورس: رجسٹریشن فیلڈ تے رفتار حد ویکھن لئی `registration-flow.md`؛ پیک تے ایکٹویشن چین ویکھن لئی
`payment-and-activation.md` (دوہاں وچ پلیٹ فارم سورس فائل درج اے)۔

## سکرپٹ سطح دی غلطی دی سنھال

| واقعہ | حل |
|---|---|
| `Node 版本过低` (Node ورژن بہت پرانا اے) | صرف ہدایت والے موڈ تے واپس، زبردستی نہ کرو |
| نیٹ ورک غلطی / ٹائم آؤٹ | اک واری دوبارہ کوشش؛ اجے فیل ہووے تاں صارف نوں نیٹ ورک چیک کرن دو تے اگے ودھو (سٹیٹ فائل اجے اے، شروع توں `status` چلا کے واپس لو) |
| register بزنس غلطی دے (یوزرنیم پہلے توں موجود وغیرہ) | SKILL.md قدم 5 دے جدول مطابق سنھالو، **تصدیقی کوڈ دوبارہ بھیجن دی لوڑ نہیں** (10 منٹ وچ اجے چلدا اے) |
| register «邮箱验证码错误或已过期» دے (ای میل تصدیقی کوڈ غلط یا مہلت ختم) | مہلت پار → دوبارہ `send-code` |
| `create-order` توں بعد صارف نے پیمنٹ صفہہ بند کیتا | سدھا دوبارہ `create-order` (پرانا آرڈر 2h وچ خود بند؛ PayPal PENDING سبسکرپشن 1h بعد خودکار میاڈ) |
| `create-order --provider paypal` توں 409 آوے | نامکمل PayPal سبسکرپشن اے؛ 1 گھنٹے انتظار کرو خودکار میاڈ لئی، یا براؤزر وچ پرانی اجازت مکمل کرو |
| `query` ہمیشہ pending / PENDING | شاید صارف نے ادا نہیں کیتا؛ اک سوال پچھو۔ واقعی ادا کیتا اے → payment-and-activation.md جانچ جدول مطابق جاؤ |
| `refresh-login` 403 `pending_payment` | پیمنٹ/اجازت اجے آئی نہیں، قدم 9 تے واپس پولنگ جاری رکھو |
| سٹیٹ فائل گم (غلطی نال مٹ گئی / مشین بدلی) | `whoami`/`refresh-login` نہیں چل سکدے؛ صارف نوں لنک 1 کھولھے براؤزر وچ سبسکرپشن صفہہ ریفریش کر کے حالت پکاؤن دو، یا دوبارہ لاگ ان کرو (ویب موڈ) |

## واپس جان دا موڈ (صرف ہدایت)

ہیٹھاں دیاں وچوں کوئی وی حالت، فوراً v1 طرز دے صرف ہدایت والے موڈ تے واپس، سکرپٹ نال ہور دشواری نہ کرو:

- Node >= 18 نہیں یا سکرپٹ اکو طرح دو واری لگاتار فیل؛
- صارف صاف کہندا اے «میں خود ویب تے کراں گا»؛
- کمپنی/ڈیوائس پالیسی سکرپٹ نوں نیٹ ورک توں روکدی اے۔

واپس آؤن تے: رجسٹریشن صفہہ https://global.powpow.online/register تے سبسکرپشن صفہہ
https://global.powpow.online/subscription دو، `registration-flow.md` دے قاعدے مطابق غلطیاں نال رہو،
وائس نہیں بدلدا، ہر واری اجے وی «اگلا قدم» بلاک نال ختم کرو۔

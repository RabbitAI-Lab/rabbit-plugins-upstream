# Agent-सहायता प्रक्रिया आ स्क्रिप्ट कॉन्ट्रैक्ट — powpow-register

SKILL.md के हर कदम के अंजाम देवे के ब्यौरा। सगरी कमांड `node scripts/powpow-register.mjs <सबकमांड> [आर्ग्युमेंट]` बा,
स्क्रिप्ट **बिना डिपेंडेंसी** बा, **Node >= 18** चाहीं, सगरी रिक्वेस्ट सिर्फ `https://global.powpow.online` पर जाला।

## सुरक्षा डिज़ाइन (एह तरह काहे बनावल बा)

| डिज़ाइन | कारण |
|---|---|
| पासवर्ड सिर्फ एनवायरनमेंट वेरिएबल `POWPOW_REGISTER_PASSWORD` से जाला | प्रोसेस के कमांड-लाइन आर्ग्युमेंट एही मशीन के दूसर प्रोसेस के दिखाई देला (argv लीक के रास्ता), एनवायरनमेंट वेरिएबल स्क्रिप्ट के भीतर पढ़ला पर तुरंत इस्तेमाल हो जाला |
| पासवर्ड **कभो स्टेट फाइल में ना**, कभो लॉग में ना दिखला | स्टेट फाइल डिस्क पर रह सकत बा; गप्पा में बनावे मोड एक बेर दिखावल यूज़र सांभरे खातिर बा |
| स्टेट फाइल सिस्टम के टेम्प डायरेक्टरी में (`os.tmpdir()/powpow-register-state.json`, 0600) | ई में खाली पाँच गो फील्ड बा: email / username / nickname / token / outTradeNo, `cleanup` एक क्लिक में साफ कर देला |
| agent के मिलल JWT आधिकारिक `me?token=` एंडपॉइंट से ब्राउज़र cookie बन जाला | प्लेटफॉर्म के Harmony WebView खातिर बनवल आधिकारिक पुल; सिग्नेचर जाँच सिर्फ सिग्नेचर+मेयाद देखेला, डिवाइस फिंगरप्रिंट से ना बांधला, यूज़र के ब्राउज़र में चली |
| पेमेंट में खाली create-order / query / कैशियर खोले | पैसा देवे के काम आ पेमेंट क्रेडेंशियल सदा यूज़र आ Alipay आधिकारिक कैशियर के बीचे रहेला, agent के हाथ ना लागेला |

## कमांड रेफरेंस

| कमांड | मुख्य आर्ग्युमेंट | काम / कब |
|---|---|---|
| `status` | —— | प्रक्रिया के प्रगति देखे (स्टेट फाइल पढ़े); गप्पा टूटला के बाद पहिले ई चलाईं |
| `gen-password` | —— | 24 अक्षर के मजबूत पासवर्ड बनावे (छोटा-बड़ा अक्षर+अंक सहित), stdout पर **खाली एह बेर** दिखाई देला |
| `prepare-suggest` | `--username --nickname --email` | पक्का कइल जानकारी स्टेट फाइल में दर्ज करे (बाद में register में फेर ना भेजे पड़ी) |
| `send-code` | `--email` | प्लेटफॉर्म से 6 अंक के सत्यापन कोड भेजवावे (10 मिनट चालू, 60s कूलडाउन) |
| `register` | `--code` (अनिवार्य); `--username --nickname --avatar --phone` (वैकल्पिक, स्टेट फाइल में बा त ना भेजीं) | pending खाता बनावे; पासवर्ड `POWPOW_REGISTER_PASSWORD` एनवायरनमेंट वेरिएबल से; सफलता पर JWT अपने-आप स्टेट फाइल में रह जाला |
| `login-link` | `--target pending` या `--target home` | एक क्लिक लॉगिन लिंक बनावे (दू लिंक डिज़ाइन, नीचे देखीं) |
| `create-order` | `--package monthly\|quarterly\|yearly` (Alipay डिफ़ॉल्ट)<br>`--provider alipay\|paypal` | पेमेंट ऑर्डर बनावे; Alipay पेमेंट पेज फाइल पाथ + outTradeNo लवटावे; PayPal अनुमति पेज फाइल पाथ + subscriptionId लवटावे (अपने-आप स्टेट फाइल में दर्ज) |
| `query` | —— | ऑर्डर/सदस्यता हालत पूछे। Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; 10–15s में पूछीं |
| `refresh-login` | पासवर्ड एनवायरनमेंट वेरिएबल से | फेर लॉगिन कर के **नवा JWT** लीं (सदस्यता वाला वादा NONE से ACTIVE हो जाला), पैसा जमा भइला पर जरूर चलाईं |
| `whoami` | —— | स्टेट फाइल के token से खाता आ सदस्यता हालत पूछे (एक्टिवेशन लागल-नईखे जाँचे) |
| `cleanup` | —— | स्टेट फाइल मिटावे (समेटत घरी जरूर चलाईं) |

**एनवायरनमेंट वेरिएबल से देवे के तरीका** (पासवर्ड कभो कमांड-लाइन पर ना):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<पासवर्ड>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<पासवर्ड>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<पासवर्ड> && node scripts/powpow-register.mjs register --code 123456
```

## दू लिंक तंत्र (मुख्य डिज़ाइन)

प्लेटफॉर्म के लॉगिन हालत HttpOnly cookie बा, agent ब्राउज़र के जगह सीधे cookie ना लगा सकत बा; पुल आधिकारिक
`/api/auth/me?token=<JWT>&redirect=<साइट के भीतर के रास्ता>` एंडपॉइंट बा: सिग्नेचर जाँच → pending यूज़र खातिर
अपने-आप session बनावे → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 दिन) → redirect के जाँच
(खाली एगो स्लैश से शुरू, `//` आ बैकस्लैश मना, पार्स कइला पर एही साइट होवे के चाहीं) → 307 अस्थायी रीडायरेक्ट लक्ष्य पेज पर।

- **लिंक 1 (रजिस्टर सफल होत ही दीं)**: `--target pending` → `/subscription` पर पहुँची।
  यूज़र के ब्राउज़र "आधा-लॉगिन" हालत में जाई: सदस्यता पेज, Alipay वापसी पेज खुलत-चलत बा; कंटेंट पेज फिर भी पेवॉल
  से सदस्यता पेज पर रोकल जाई (तीन कठबेड़ी: JWT claims गेटवे जाँच → DB दोबारा जाँच → मुख्य API जाँच, ई सामान्य व्यवहार बा)।
- **लिंक 2 (paid पक्का भइला पर दीं)**: पहिले `refresh-login` से नवा JWT लीं (पेमेंट खाली DB बदलेला, दिहल गइल
  JWT के claims ना बदलेला, ना बदलवा त "पैसा दिहल पर मेंबर नईखे" दिखी), फिर `--target home` → होमपेज पर,
  पूरा मेंबर हालत।

## पूरा क्रम (सामान्य रास्ता)

```
1.  status                          # माहौल के आत्म-जाँच
2.  (कदम 2 में गप्पा से जानकारी पक्का करे, पासवर्ड दू में से चुनवावे; बनावे मोड: gen-password → यूज़र से तुरंत सांभरे के कहीं)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → यूज़र ईमेल में जा के कोड देखे (गप्पा छोड़े के एकलौता जगह①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → लिंक 1 यूज़र के भेजीं
7.  (यूज़र पेमेंट के तरीका चुने)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <पेमेंट पेज फाइल>              # Windows; macOS में open, Linux में xdg-open
    # → यूज़र Alipay/PayPal कैशियर पर पैसा/अनुमति पूरा करे (गप्पा छोड़े के जगह②)
9.  query (हर 10–15s) जब ले paid / ACTIVE
10. refresh-login                   # ACTIVE वाला नवा JWT लीं
11. login-link --target home        # → लिंक 2 यूज़र के भेजीं
12. whoami                          # subscriptionStatus: ACTIVE पक्का करे (वैकल्पिक)
13. cleanup                         # स्टेट फाइल साफ करे
```

## कमांड → प्लेटफॉर्म API नक्शा

| स्क्रिप्ट कमांड | प्लेटफॉर्म इंटरफेस |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart, प्रोफाइल फोटो सीधे अपलोड) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (लिंक खुदे, यूज़र क्लिक करत घरी काम करेला) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

नियम के सोर्स: रजिस्टर फील्ड आ रेट-लिमिट खातिर `registration-flow.md` देखीं; पैकेज आ एक्टिवेशन श्रृंखला खातिर
`payment-and-activation.md` देखीं (दुनो में प्लेटफॉर्म के सोर्स फाइल निशान लगावल बा)।

## स्क्रिप्ट-स्तर के एरर संभाले

| लक्षण | का करीं |
|---|---|
| `Node 版本过低` (Node के वर्जन बहुत कम बा) | सिर्फ-निर्देश मोड में लौटीं, जोर-जबरदस्ती ना करीं |
| नेटवर्क एरर / टाइमआउट | एक बेर फेर कोशिश; फिर भी फेल त यूज़र से नेटवर्क जाँच करवा के आगे बढ़ाईं (स्टेट फाइल अभी बा, `status` से फेर शुरू करीं) |
| register बिजनेस एरर देला (用户名已存在 वगैरह) | SKILL.md कदम 5 के टेबल हिसाब से संभालीं, **सत्यापन कोड फेर ना भेजे पड़ी** (10 मिनट ले चालू रही) |
| register 「邮箱验证码错误或已过期」 देला | मेयाद पार → फेर `send-code` |
| `create-order` के बाद यूज़र पेमेंट पेज बंद कइ दिहलस | सीधे फेर `create-order` (पुरान ऑर्डर 2 घंटा में अपने-आप बंद हो जाई; PayPal PENDING सदस्यता 1 घंटा में खतम) |
| `create-order --provider paypal` 409 लवटावेला | एक गो अधूरा PayPal सदस्यता बा; 1 घंटा रुकीं जब ले खतम हो जाय, या पुरान अनुमति ब्राउज़र में पूरा करीं |
| `query` लगातार pending / PENDING | शायद यूज़र पैसा ना दिहलस; एक शब्द पूछीं। असल में दिहलस → payment-and-activation.md के पड़ताल टेबल अपनाईं |
| `refresh-login` 403 `pending_payment` | पैसा/अनुमति अभी जमा ना भइल, कदम 9 पर लौट के पूछत रहीं |
| स्टेट फाइल लुप्त (हाथ से मिट गइल / मशीन बदलल) | `whoami`/`refresh-login` ना चली; यूज़र से लिंक 1 खोलल ब्राउज़र में सदस्यता पेज रिफ्रेश करा के हालत पक्का करवाईं, या फेर लॉगिन कराईं (वेब मोड) |

## फॉलबैक मोड (सिर्फ-निर्देश)

नीचे कवनो एक हालत पर तुरंत v1 जैसन सिर्फ-निर्देश मोड में लौटीं, स्क्रिप्ट के चुनौती ना दीं:

- Node >= 18 नईखे या स्क्रिप्ट लगातार दू बेर एही तरह के एक गो एरर देला;
- यूज़र साफ कहेला "हम खुदे वेब पर करब";
- कंपनी/डिवाइस के नीति स्क्रिप्ट के नेटवर्क रोकत बा।

लौटला के बाद: रजिस्टर पेज https://global.powpow.online/register आ सदस्यता पेज
https://global.powpow.online/subscription दीं, `registration-flow.md` के नियम हिसाब से साथ-साथ एरर पड़ताल करीं,
स्वर ओही रही, हर राउंड "अगिला कदम" ब्लॉक से समेटीं।

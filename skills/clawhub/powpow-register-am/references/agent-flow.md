# የወኪል ተይዞ የሚሠራ ሂደትና የስክሪፕት ውል — powpow-register

የ SKILL.md እያንዳንዱ ደረጃ የአፈጻጸም ዝርዝር። ሁሉም ትዕዛዞች `node scripts/powpow-register.mjs <ንዑስ-ትዕዛዝ> [ክርክሮች]` ቅርጸት አላቸው፣ ስክሪፕቱ **ዜሮ ጥገኛነት** አለው፣ **Node ≥ 18** ያስፈልገዋል፣ ሁሉም ጥሪዎች ወደ `https://global.powpow.online` ብቻ ይሄዳሉ።

## የደህንነት ንድፍ (ለምን እንዲህ እንደተነደፈ)

| ንድፍ | ምክንያት |
|---|---|
| የመግቢያ ቃል በአካባቢ ተለዋዋጭ `POWPOW_REGISTER_PASSWORD` በኩል ብቻ ይገባል | የሂደቱ ትዕዛዝ መስመር ክርክሮች ለተመሳሳይ ማሽን ሌሎች ሂደቶች ይታያሉ (የ argv የፍልሰት ገጽታ)፤ የአካባቢ ተለዋዋጭ ስክሪፕቱ ካነበው ወዲያውኑ ይጠቀምበታል |
| የመግቢያ ቃል **በጭራሽ ወደ ሁኔታ ፋይል አይጻፍም**፣ በሎግ አይታይም | የሁኔታ ፋይል በዲስክ ላይ ሊቀር ይችላል፤ በውይይቱ ውስጥ በመፍጠሪያ ሁነታ አንዴ ብቻ መታየቱ ተጠቃሚው እንዲያስቀምጥ ነው |
| የሁኔታ ፋይል በስርዓቱ ጊዜያዊ ማውጫ (`os.tmpdir()/powpow-register-state.json`፣ 0600) | አምስቱን መስኮች ብቻ ይዟል email / username / nickname / token / outTradeNo፤ `cleanup` በአንድ ጠቅታ ያጽዳቸዋል |
| ወኪሉ የተቀበለው JWT በብዙሃን `me?token=` በር በኩል ወደ አሳሽ cookie ይቀየራል | መድረኩ ለሃርሞኒየስ (HarmonyOS) WebView ያዘጋጀው ይፋዊ ድልድይ ነው፤ የፊርማ ማረጋገጫው ፊርማ + የኃይል ጊዜ ብቻ ያረጋግጣል፣ የመሣሪያ አሻራ አያስተሳስርም፣ ስለዚህ የተጠቃሚው አሳሽ መጠቀም ይችላል |
| ክፍያ create-order / query / የክፍያ ገጽ መክፈት ብቻ ነው | የክፍያ ተግባርና የክፍያ ማረጋገጫ ለዘላለም በተጠቃሚውና በአሊፓይ ይፋዊ የክፍያ ገጽ መካከል ብቻ ናቸው፤ ወኪል አያነካቸውም |

## የትዕዛዞች ማጣቀሻ

| ትዕዛዝ | ቁልፍ ክርክሮች | ተግባር / ጊዜ |
|---|---|---|
| `status` | —— | የሂደቱን እድገት ማየት (የሁኔታ ፋይልን ማንበብ)፤ ውይይቱ ከተቋረጠ በኋላ መጀመሪያ ይህን ያሂዱ |
| `gen-password` | —— | 24 ፊደላት ጠንካራ የመግቢያ ቃል ይፈጥራል (ትላልቅ + ትንሽ ፊደላት + ቁጥሮች)፤ stdout **ይህን አንዴ ብቻ** ያሳያል |
| `prepare-suggest` | `--username --nickname --email` | የተረጋገጠውን መረጃ ወደ ሁኔታ ፋይል ያስገባል (ከዚያ በኋላ register ዳግም መላክ አያስፈልገውም) |
| `send-code` | `--email` | መድረኩ 6-አሃያ የማረጋጋጫ ኮድ እንዲልክ ያነቃቃል (10 ደቂቃ ይጸናል፣ 60s ቀዝቃዛ ጊዜ) |
| `register` | `--code` (ግዴታ)፤ `--username --nickname --avatar --phone` (አማራጭ፤ በሁኔታ ፋይል ላይ ካሉ መላክ አያስፈልግም) | pending መለያ ይፈጥራል፤ የመግቢያ ቃል በ `POWPOW_REGISTER_PASSWORD` የአካባቢ ተለዋዋጭ በኩል፤ ሲሳክ JWT በራስ-ሰር ወደ ሁኔታ ፋይል ይቀመጣል |
| `login-link` | `--target pending` ወይም `--target home` | የአንድ ጠቅታ መግቢያ አገናኝ ይፈጥራል (የጥንድ አገናኝ ንድፍ፣ ከታች ይመልከቱ) |
| `create-order` | `--package monthly\|quarterly\|yearly` | የአሊፓይ ትዕዛዝ ይፈጥራል፤ የክፍያ ገጽ ፋይል መንገድ + outTradeNo ይመልሳል (በራስ-ሰር ወደ ሁኔታ ፋይል ይግባል) |
| `query` | —— | የትዕዛዙን ሁኔታ `paid / pending / closed / unknown` ያረጋግጣል (outTradeNo ከሁኔታ ፋይል)፣ በየ 10–15s መጠየቅ |
| `refresh-login` | የመግቢያ ቃል በአካባቢ ተለዋዋጭ በኩል | ዳግም መግባት **አዲስ JWT** ለመቀየር (የደንበኝነት አባልነት ከ NONE ወደ ACTIVE ይቀየራል)፤ ገንዘብ ከገባ በኋላ መሮጥ አለበት |
| `whoami` | —— | በሁኔታ ፋይሉ ያለውን ቶከን በመጠቀም መለያና የደንበኝነት ሁኔታ ያረጋግጣል (ማንቃቱ እንደተሳካ ማረጋገጥ) |
| `cleanup` | —— | የሁኔታ ፋይል መሰረዝ (ሲዘጋ መሮጥ አለበት) |

**የአካባቢ ተለዋዋጭ ማስተላለፍ** (የመግቢያ ቃል በጭራሽ ወደ ትዕዛዝ መስመር አይደርስም)፦

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<የመግቢያ ቃል>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<የመግቢያ ቃል>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<የመግቢያ ቃል> && node scripts/powpow-register.mjs register --code 123456
```

## የጥንድ አገናኝ ሜካኒዝም (ዋና ንድፍ)

የመድረኩ የመግቢያ ሁኔታ HttpOnly cookie ነው፤ ወኪል ለአሳሽ cookie በቀጥታ መትከል አይችልም፤ ድልድዩ ደግሞ ይፋዊ
`/api/auth/me?token=<JWT>&redirect=<የውስጥ ገጽ መንገድ>` በር ነው፦ የፊርማ ማረጋገጫ → ለ pending ተጠቃሚ በራስ-ሰር ክፍለ-ጊዜ (session) መሙላት → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 ቀናት) → redirect ማረጋገጥ (በአንድ ስላሽ ብቻ መጀመር፣ `//` እና backslash እንደማይፈቀዱ፣ ከተተካ ተመሳሳይ ምንጭ መሆን አለበት) → 307 ጊዜያዊ መመለሻ ወደ ዒላማው ገጽ።

- **አገናኝ 1 (ምዝገባ ሲሳክ ወዲያውኑ ይሰጣል)**፦ `--target pending` → ወደ `/subscription` ይወርዳል።
  የተጠቃሚው አሳሽ «ግማሽ መግቢያ» ሁኔታ ይገባል፦ የደንበኝነት ገጽና የአሊፓይ መመለሻ ገጽ ይታያሉና ሊሠሩ ይቻላሉ፤ የይዘት ገጾች ግን አሁንም በየክፍያ ግድግዳ
  ወደ የደንበኝነት ገጽ ይመለሳሉ (ሦስት ደረጃ ጥበቃ፦ የ JWT claims በበር ውስጥ ፍተሻ → የመረጃ ቋት ዳግም ፍተሻ → የመሠረታዊ API ፍተሻ፤ ተራ ባህርይ ነው)።
- **አገናኝ 2 (paid ከተረጋገጠ በኋላ ይሰጣል)**፦ መጀመሪያ `refresh-login` በማሂድ አዲስ JWT ይቀያይሩ (ክፍያ የመረጃ ቋቱን ብቻ ያዘምናል፣ አስቀድሞ ለተሰጠው JWT claims አይነካም፤ ካልተቀየረ «ከፍለሀል ግን አባል አይደለም» ይመስላል)፣ ከዚያ `--target home` → ወደ መነሻ ገጽ ይወርዳል፣
  ሙሉ የአባልነት ሁኔታ።

## ሙሉ ቅደም ተከተል (መደበኛ መንገድ)

```
1.  status                          # የአካባቢ በራስ-ፍተሻ
2.  (ደረጃ 2፦ በውይይት መረጃ ማረጋገጥ፣ የመግቢያ ቃል ከሁለት አንዱን መምረጥ፤ የመፍጠሪያ ሁነታ፦ gen-password → ተጠቃሚው ወዲያውኑ እንዲያስቀምጥ)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → ተጠቃሚው ወደ ኢሜይል ገብቶ ኮዱን ማየት (ከውይይቱ ውጭ መውጣት ①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → አገናኝ 1 ለተጠቃሚው ተልኳል
7.  (ተጠቃሚው ጥቅል ይምረጣል) create-order --package monthly
8.  start <የክፍያ ገጽ ፋይል>          # Windows፤ macOS ላይ open፣ Linux ላይ xdg-open
    # → ተጠቃሚው በአሊፓይ የክፍያ ገጽ ላይ ይከፍላል (ከውይይቱ ውጭ መውጣት ②)
9.  query (በየ 10–15s) paid እስኪሆን ድረስ
10. refresh-login                   # ACTIVE አባልነት ያለው አዲስ JWT
11. login-link --target home        # → አገናኝ 2 ለተጠቃሚው ተልኳል
12. whoami                          # subscriptionStatus: ACTIVE ማረጋገጥ (አማራጭ)
13. cleanup                         # የሁኔታ ፋይል ማጽዳት
```

## ትዕዛዝ → የመድረክ API ካርታ

| የስክሪፕት ትዕዛዝ | የመድረክ በር |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart፣ የመገለጫ ምስል ቀጥታ ማስገባት) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (አገናኙ ራሱ፤ በአሳሽ ሲነካ ይሠራል) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

የሕጎች ምንጭ፦ የምዝገባ መስኮችና ገደቦች `registration-flow.md` ውስጥ፤ ጥቅሎችና የማንቃት ሰንሰለት `payment-and-activation.md` ውስጥ (ሁለቱም የመድረኩን የኮድ ፋይሎች ይጠቅሳሉ)።

## በስክሪፕት ደረጃ ስህተት አፈታት

| ምልክት | አፈታት |
|---|---|
| `Node 版本过低` (የ Node ስሪት በጣም ዝቅተኛ ነው) | ወደ ንጹህ መመሪያ ሁነታ ይመለሱ፣ አትገድዱ |
| የአውታረ መረብ ስህተት / ጊዜ መያዝ | አንዴ ይመንጨቱ፤ እንደቀጠለ ተጠቃሚው አውታረ መረቡን ካረጋገጠ በኋላ ይቀጥሉ (የሁኔታ ፋይሉ አለ፤ ከመጀመሪያው `status` ሮጦት ይመለሳል) |
| register የንግድ ስህተት ያሳያል (የተጠቃሚ ስም አስቀድሞ አለ ወዘተ) | በ SKILL.md ደረጃ 5 ሠንጠረዥ መሠረት ይፍቱ፣ **የማረጋጋጫ ኮዱን ዳግም መላክ አያስፈልግም** (በ 10 ደቂቃ ውስጥ አሁንም ይጸናል) |
| register 「邮箱验证码错误或已过期」 (የኢሜይል ማረጋጋጫ ኮድ ስህተት ወይም አልፏል) ያሳያል | ጊዜ ከማለፉ → ዳግም `send-code` |
| ከ `create-order` በኋላ ተጠቃሚው የክፍያ ገጹን ዘግቷል | በቀጥታ ዳግም `create-order` (አሮጌው ትዕዛዝ በ 2h በራስ ይዘጋል) |
| `query` በተከታታይ pending | ተጠቃሚው ሳይከፍል ይችላል፤ አንዴ ጠይቁት። በእውነት ከፈለክ በኋላ → በ payment-and-activation.md ያለውን የአፈታት ሠንጠረዥ ይከተሉ |
| `refresh-login` 403 `pending_payment` | ክፍያው ገና አልገባም፤ ወደ ደረጃ 9 ተመልሰው መጠየቁን ይቀጥሉ |
| የሁኔታ ፋይል መጥፋት (በአጣቃቂ ሲሰረዝ / ማሽን ሲቀየር) | `whoami`/`refresh-login` መጠቀም አይቻልም፤ ተጠቃሚው አገናኝ 1ን የከፈተበት አሳሽ ውስጥ የደንበኝነት ገጹን በቀጥታ በማደስ ሁኔታውን እንዲያረጋግጥ ይንገሩት፣ ወይም ዳግም ይግባ (የዌብ ሁነታ) |

## የመመለሻ ሁነታ (ንጹህ መመሪያ)

ከሚከተሉት አንዱ ከተከሰተ ወዲያውኑ ወደ v1 ዓይነቱ ንጹህ መመሪያ ይመለሱ እና ስክሪፕቱን ማለቀቀት ያቁሙ፦

- Node ≥ 18 ከሌለ ወይም ስክሪፕቱ በተከታታይ ሁለት ጊዜ ተመሳሳይ ዓይነት ስህተት ካሳየ፤
- ተጠቃሚው በግልጽ «በዌብ ላይ ራሴ እሠራለሁ» ካለ፤
- የኩባንያ/የመሣሪያ ፖሊሲ ስክሪፕቱ አውታረ መረብ እንዳይጠቀም ከገደበ።

ከተመለሱ በኋላ፦ የምዝገባ ገጹን https://global.powpow.online/register እና የደንበኝነት ገጹን https://global.powpow.online/subscription ይስጡ፣ በ `registration-flow.md` ሕጎች መሠረት አብረውት ስህተቶችን ይፍቱ፣ ቃለ-ጥምርታው አይቀየርም፣ እያንዳንዱ ዙር አሁንም በ«ቀጣዩ እርምጃ» ብሎክ ይዝጋል።


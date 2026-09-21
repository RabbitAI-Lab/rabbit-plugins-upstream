# i18n Catalog — 50+ Languages, Cultural POI, RTL (v2 NEW)

## Supported Languages (50)

| Code | Name | Native | Dir | Units | Region | Notes |
|------|------|--------|-----|-------|--------|-------|
| en | English | English | LTR | metric | US | fallback |
| en-GB | English (UK) | English | LTR | metric | GB | |
| en-US | English (US) | English | LTR | imperial | US | imperial default |
| ro | Romanian | Română | LTR | metric | RO | |
| de | German | Deutsch | LTR | metric | DE | |
| fr | French | Français | LTR | metric | FR | |
| fr-CA | French (Canada) | Français | LTR | metric | CA | |
| es | Spanish | Español | LTR | metric | ES | |
| es-MX | Spanish (Mexico) | Español | LTR | metric | MX | |
| it | Italian | Italiano | LTR | metric | IT | |
| pt | Portuguese | Português | LTR | metric | PT | |
| pt-BR | Portuguese (Brazil) | Português | LTR | metric | BR | |
| ru | Russian | Русский | LTR | metric | RU | |
| uk | Ukrainian | Українська | LTR | metric | UA | |
| pl | Polish | Polski | LTR | metric | PL | |
| hu | Hungarian | Magyar | LTR | metric | HU | |
| tr | Turkish | Türkçe | LTR | metric | TR | |
| ar | Arabic | العربية | RTL | metric | SA | RTL, bidi |
| fa | Persian | فارسی | RTL | metric | IR | RTL, bidi |
| he | Hebrew | עברית | RTL | metric | IL | RTL |
| hi | Hindi | हिन्दी | LTR | metric | IN | |
| bn | Bengali | বাংলা | LTR | metric | BD | |
| ur | Urdu | اردو | RTL | metric | PK | RTL |
| zh | Chinese | 中文 | LTR | metric | CN | |
| zh-TW | Chinese (Taiwan) | 中文 | LTR | metric | TW | |
| ja | Japanese | 日本語 | LTR | metric | JP | |
| ko | Korean | 한국어 | LTR | metric | KR | |
| th | Thai | ไทย | LTR | metric | TH | |
| vi | Vietnamese | Tiếng Việt | LTR | metric | VN | |
| id | Indonesian | Bahasa Indonesia | LTR | metric | ID | |
| ms | Malay | Bahasa Melayu | LTR | metric | MY | |
| nl | Dutch | Nederlands | LTR | metric | NL | |
| sv | Swedish | Svenska | LTR | metric | SE | |
| no | Norwegian | Norsk | LTR | metric | NO | |
| da | Danish | Dansk | LTR | metric | DK | |
| fi | Finnish | Suomi | LTR | metric | FI | |
| el | Greek | Ελληνικά | LTR | metric | GR | |
| cs | Czech | Čeština | LTR | metric | CZ | |
| sk | Slovak | Slovenčina | LTR | metric | SK | |
| bg | Bulgarian | Български | LTR | metric | BG | |
| hr | Croatian | Hrvatski | LTR | metric | HR | |
| sr | Serbian | Српски | LTR | metric | RS | |
| sl | Slovenian | Slovenščina | LTR | metric | SI | |
| et | Estonian | Eesti | LTR | metric | EE | |
| lv | Latvian | Latviešu | LTR | metric | LV | |
| lt | Lithuanian | Lietuvių | LTR | metric | LT | |
| ka | Georgian | ქართული | LTR | metric | GE | |
| am | Amharic | አማርኛ | LTR | metric | ET | |
| sw | Swahili | Kiswahili | LTR | metric | KE | |
| yo | Yoruba | Yorùbá | LTR | metric | NG | |
| zu | Zulu | isiZulu | LTR | metric | ZA | |
| af | Afrikaans | Afrikaans | LTR | metric | ZA | |

## RTL Handling

Languages with RTL: ar, fa, he, ur

- Bidi wrapping: `\u202B{text}\u202C` (RLE + PDF)
- UI flip: navigation instructions reverse left/right when RTL? No, keep LTR for map directions but wrap text bidi
- Accept-Language header: send `ar, en` etc to Nominatim/Photon/Wikipedia
- Valhalla language: `ar`, `fa`, etc via `directions_options.language`

## Units per Locale

- Imperial: en-US (US), en-GB partially (UK uses metric for most but imperial for distance? Use metric for UK per modern)
- Metric: all others
- Override: `umn config set units imperial|metric`
- Formatting: `format_distance()` in i18n.py handles per locale

## Date/Time Formatting

Per locale patterns (ICU-like, simplified):

- en: YYYY-MM-DD HH:mm:ss, 12h optional
- ro: DD.MM.YYYY HH:mm
- de: DD.MM.YYYY HH:mm
- fr: DD/MM/YYYY HH:mm
- ar: DD/MM/YYYY HH:mm (RTL)
- fa: YYYY/MM/DD HH:mm
- zh: YYYY年MM月DD日 HH时mm分
- ja: YYYY年MM月DD日 HH時mm分
- etc

Implemented via `Intl.DateTimeFormat` pattern stub in i18n.py — real formatting uses Python datetime + locale patterns.

## Cultural POI Mapping

Cultural categories → OSM tags:

| Category | OSM Tags | Cultures |
|----------|----------|----------|
| mosque | place_of_worship religion=muslim, building=mosque | Muslim majority, ar, tr, fa, ur, id, ms |
| church | place_of_worship religion=christian | Christian, en, de, fr, es, it, ro, ru, etc |
| temple | place_of_worship religion=buddhist|hindu|shinto | Buddhist/Hindu, hi, th, ja, zh, bn |
| shrine | historic=wayside_shrine | Global |
| synagogue | place_of_worship religion=jewish | Jewish, he |
| bazaar | shop=bazaar, marketplace | tr, fa, hi, ar |
| souk | shop=market, marketplace | ar |
| hammam | amenity=public_bath | tr, ar |
| onsen | public_bath bath:type=onsen, hot_spring | ja |
| izakaya | restaurant cuisine=japanese, bar | ja |
| tapas | restaurant cuisine=spanish | es, es-MX |
| halal | diet:halal=yes | ar, fa, ur, id, ms, tr |
| kosher | diet:kosher=yes | he |
| vegan | diet:vegan=yes | Global, en, de |
| pharmacy | amenity=pharmacy | Global |
| hospital | amenity=hospital|clinic | Global |
| shelter | amenity=shelter, emergency=assembly_point | Global — critical for survival |
| water | amenity=drinking_water | Global — critical for survival |
| police | amenity=police | Global |
| embassy | office=diplomatic | Global |

Usage:
```bash
umn poi "mosque" --near "Istanbul" --lang tr
umn poi "halal" --near "London" --lang en
umn poi "onsen" --near "Tokyo" --lang ja
umn poi "bazaar" --near "Tehran" --lang fa
```

## Translation Dictionary

Offline dictionary in `scripts/i18n.py` covers common navigation keys:

- route, distance, duration, from, to, navigate, nearby, search, save
- turn_left, turn_right, go_straight, arrive, depart, roundabout
- fuel, parking, hospital, pharmacy, shelter, water, danger, safe, emergency, help, sos

For full sentence translation, use `--lang` which sets Accept-Language for Nominatim/Photon/Wikipedia — they return localized names.

Future: integrate with `trans` CLI or offline MarianMT models (optional, not stdlib).

## Language Detection

Heuristic detection in `i18n.py`:

- Script detection: Arabic \u0600-\u06FF → ar/fa/ur, Hebrew \u0590-\u05FF → he, CJK \u4E00-\u9FFF → zh/ja, Hangul → ko, Thai, Devanagari → hi
- Word heuristics: " und ", " der " → de; " le ", " et " → fr; " el ", " y " → es; " și ", " din " → ro; " و ", " در " → fa
- Fallback: en

Accuracy ~80% for major languages, sufficient for routing to correct prompt template. For high accuracy, use fasttext or CLD3 (optional).

## Plural Rules

Stub: English 2 forms, Arabic 6 forms, etc. For future i18n expansion, use `i18n/<lang>/plurals.json` per CLDR.

## Testing

```bash
python3 scripts/i18n.py --test
umn i18n list
umn i18n detect "مرحبا"
umn i18n translate "shelter" --to ar
umn geocode "القاهرة" --lang ar --compact
umn poi "mosque" --near "Istanbul" --lang tr --json
```

## Compatibility

- Claude: uses `accept-language` header via tool definitions
- GPT: function calling with `lang` param
- Gemini: same
- All models: stdlib only, no external deps, fallback to en if lang unsupported

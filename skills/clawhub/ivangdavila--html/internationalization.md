# Language, Direction, Encoding

Four attributes and one meta tag decide whether a page is readable, pronounceable, translatable and sortable in the user's language. Defaults come from `document_lang`.

**Contents:** [Encoding](#encoding) · [`lang`](#lang) · [`dir`](#dir) · [`bdi` and Bidi Isolation](#bdi-and-bidi-isolation) · [`hreflang`](#hreflang) · [Translation Control](#translation-control) · [Text That Breaks in Other Languages](#text-that-breaks-in-other-languages) · [Forms and Locale](#forms-and-locale) · [CJK and Vertical Text](#cjk-and-vertical-text)

## Encoding

- UTF-8 for every document, always. Declare it in the first 1024 bytes: `<meta charset="utf-8">` (`head.md`).
- The HTTP `Content-Type` header wins over the meta tag. When they disagree, the page renders per the header and the meta looks like it is being ignored — check the header first when text is mojibake despite a correct meta.
- Mojibake decoder: `Ã©` for `é` means UTF-8 bytes read as Latin-1. `�` (U+FFFD) means the bytes are not valid UTF-8 at all — the file itself was saved in another encoding.
- Save source files as UTF-8 **without BOM**: a BOM before the doctype pushes some parsers into quirks mode and shows as a stray character in others.
- Do not escape non-ASCII text as character references. `é` is a character; `&eacute;` is noise that breaks search, copy-paste, and length calculations.

## `lang`

```html
<html lang="en">
  <p>The French call it <span lang="fr">un renard</span>.</p>
```

- `lang` on `<html>` is mandatory. It selects the screen reader's voice and pronunciation rules, the hyphenation dictionary, the quote characters `<q>` produces, spellcheck, the font fallback for CJK, and the language browsers offer to translate from.
- Mark inline foreign phrases with `lang` on a wrapping element. Without it, a French phrase is pronounced with English phonetics — the difference between comprehensible and not.
- BCP-47 values: language, optionally script and region — `en`, `en-GB`, `pt-BR`, `zh-Hans`, `sr-Latn`. Do not invent values, and do not use `lang="en-us"` casing rules as if they mattered (values are case-insensitive, but the conventional form is `en-US`).
- `lang=""` explicitly means "unknown" and is correct for user-generated content of unknown language — better than inheriting the wrong one.
- Proper nouns and product names do not need a `lang`; borrowed phrases assimilated into the page's language ("café") do not either.

## `dir`

| Value | Meaning |
|---|---|
| `ltr` | Left to right |
| `rtl` | Right to left — Arabic, Hebrew, Persian, Urdu |
| `auto` | The browser guesses from the first strongly-directional character |

- `dir` on `<html>` sets the base direction for the document; CSS logical properties (`margin-inline-start`, `inset-inline-end`) then mirror the layout automatically — that is the `css` skill's half of the work.
- Direction is **not** implied by `lang`. `lang="ar"` without `dir="rtl"` renders Arabic in a left-to-right layout.
- What mirrors: layout, text alignment, list markers, table column order, directional icons (back/forward arrows, indentation). What does not: clocks, media playback controls, logos, phone numbers, and code.
- Numbers and Latin-script fragments inside RTL text keep their own direction; the surrounding paragraph's base direction decides where the fragment lands, which is what makes bidi bugs look random.

## `bdi` and Bidi Isolation

```html
<li><bdi>ايتم</bdi> — 3 in stock</li>
```

- `<bdi>` isolates a run of unknown-direction text so it cannot reorder the text around it. It is the correct wrapper for **any user-supplied string interpolated into a sentence**: names, usernames, titles, search terms.
- Without it, an Arabic username in an English sentence can drag the following punctuation and numbers to the wrong side — a rendering bug that only appears for some users' data.
- `<bdo dir="rtl">` forces a direction override; it is for the rare case where the text really must be reversed, not for fixing bidi bugs.
- `dir="auto"` on an input or a `<bdi>` handles the common case of a field that may receive either direction.

## `hreflang`

```html
<link rel="alternate" hreflang="en-gb" href="https://example.co.uk/pricing">
<link rel="alternate" hreflang="es"    href="https://example.com/es/precios">
<link rel="alternate" hreflang="x-default" href="https://example.com/pricing">
```

- Every page in the set lists **every** version including itself. A missing self-reference or a one-way link invalidates the whole cluster.
- `x-default` marks the fallback for unmatched locales — typically a language selector or the primary market's page.
- Values are language, or language-region; region alone is invalid (`hreflang="uk"` is Ukrainian, not the United Kingdom).
- Every `hreflang` URL must be absolute, canonical, and self-canonical. Pointing an alternate at a page whose canonical is elsewhere collapses the cluster.
- `hreflang` on an `<a>` is a hint about the destination's language and is unrelated to the alternates cluster.
- **Before writing an `hreflang` set, read `~/Clawic/data/domains/domains.md`** for the locale→hostname map already agreed. Two pages that disagree about whether Spanish lives on a subdomain or a path produce a cluster that never validates.

## Translation Control

- `translate="no"` on brand names, code samples, and user identifiers keeps machine translation from mangling them; it is honored by browser translation and by translation services.
- `<code>`, `<samp>`, `<kbd>` and `<var>` are not automatically excluded — mark them explicitly when translation matters.
- Never build a sentence from concatenated fragments in the markup: word order differs by language and the translator sees only the pieces. One string per sentence, with placeholders.

## Text That Breaks in Other Languages

| Assumption | Reality |
|---|---|
| Text length is stable | German and Finnish routinely run 30–50% longer than English; Chinese is much shorter. Fixed-width buttons and single-line labels break |
| Words break at spaces | Thai and Khmer have no spaces; CJK wraps anywhere. `word-break` and `<wbr>` exist for the hard cases |
| Names have a first and last part | Many do not. One `name` field with `autocomplete="name"` is safer than two (`forms.md`) |
| Uppercase is reversible | `İ`/`i` in Turkish, `ß` in German. Never store an uppercased value |
| Dates are DD/MM or MM/DD | Use `<time datetime>` with an ISO value and render the localized string (`semantics.md`) |
| Sorting is alphabetical | Locale collation differs; do not sort in markup |
| Currency symbol position is fixed | Format server-side per locale, with the currency in the value |
| One font covers the page | CJK, Arabic and Devanagari need their own stacks, selected by `:lang()` |

## Forms and Locale

- `autocomplete` tokens are language-independent and work in every locale — the strongest reason to use them (`forms.md`).
- Address forms differ by country: field order, whether a region is required, postcode presence and format. Reorder the fields by country rather than validating a US shape everywhere.
- `<input type="date">` displays in the user's locale and always submits ISO — this is a feature, not a bug to work around.
- `inputmode` and `lang` on an input together decide the mobile keyboard's layout and language.
- Placeholders and error messages must be translated; `pattern` regexes usually must change too (postcodes, phone formats).

## CJK and Vertical Text

- `lang="ja"` vs `lang="zh-Hans"` vs `lang="zh-Hant"` selects different glyphs for the **same** code points — the wrong `lang` shows Chinese glyph forms to Japanese readers. This is the single most visible i18n error in CJK pages.
- Ruby annotations: `<ruby>漢字<rt>かんじ</rt></ruby>`, with `<rp>` fallback parentheses for browsers without ruby support.
- Vertical writing modes are CSS; the markup requirement is a correct `lang` and no hard-coded line breaks.
- `<wbr>` marks an optional break point in a long unbroken string (a URL, an identifier) without inserting a character.

**When a locale set is established for a site** — which languages, on which hostnames or paths, with which `x-default` — write the locale→hostname map to `~/Clawic/data/domains/domains.md` (one row per hostname, updated in place) and record the language list against the template row in `## Pages` of `memory.md` (`memory-template.md`). **If the user states a default language, region, or a translation constraint**, that is a declaration: record `document_lang` or the relevant key in `config.yaml`, never in `memory.md`.

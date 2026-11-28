# Writing the narration

Each page's narration is what a good presenter says while that page is on screen. It lives in the slide's `notes`, is read aloud by a voice, and is checked by `narrate.py check`.

## What to say

- **Explain, don't read.** The slide carries a few words; the narration gives the reasoning behind them: why the number moved, what it is compared with, what it means for the audience. Use the source for this context.
- **One page, one thread.** Open with the point of the page, support it with one to three facts, and close with a bridge to the next page ("That growth has a cost, which is the next question.").
- **Keep the source's qualifiers.** "Estimated", "according to the vendor", "in a survey of 300 people" stay in.
- **Cover and closing pages** can be short: a welcome and the promise of the talk; a recap and one call to action.
- Do not invent examples, quotes or numbers to fill time. A shorter page is better than a padded one.

## Length per page

| Language | Target per content page | Limit |
| --- | --- | --- |
| Chinese (zh, zh-tw) | 150–260 characters | 320 |
| Japanese | 180–320 characters | 380 |
| Korean | 160–280 characters | 340 |
| English, Spanish, Portuguese, German, French | 80–160 words | 190 |

Roughly one minute of listening per page. Over the limit, split the page.

## How it must sound

- Spoken sentences: 12–22 words (EN) or 25–45 characters (ZH) each. No lists, bullets, headings, Markdown, emoji, arrows or check marks.
- No "on this slide", "as you can see", no reading out symbols.
- No URLs. Say the site or organization name.
- Numbers exactly as in the source, written the way people say them. Chinese keeps Arabic digits (write 212%, not the number spelled out in characters); English may write "212 percent". Keep signs and decimals.
- Abbreviations: spell out on first use if listeners would not know them.
- Same language as the slides (`contentLocale`), unless the user asks otherwise. Translate wording, never figures, names or the meaning of quotes.

## Pronunciation

The voice reads the text as written. Terms it may misread (brand names, acronyms, people) go in `pronunciations.json`, applied only to the audio:

```json
{ "zh": { "Skillry": "\u65af\u5947\u5c14\u745e" }, "en": { "SQL": "sequel" } }
```

Values may use JSON \u escapes, as above. Chinese defaults for Skillry, Claude and Codex are built in. Longer terms are replaced first; Latin terms match whole words.

## Before recording

Generate nothing until the user has read `narration.md`. If they want to hear the tone first, voice two or three pages with `tts.mjs generate --only <id1,id2> --yes` (after the estimate), then the rest.

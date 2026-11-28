# Deck review: readability, crops and decorations

Run this review on every page after the style's own build and check, before showing the deck to the user. Each item below is a problem that real narrated decks have shipped with.

## 1. Text size for the content language

Styles are often tuned for English editorial type. The same 10px body copy that reads well in English is too small in Chinese, Japanese or Korean.

Open `presentation.html` over local HTTP in page view and run this in the browser console (or with the browser tool's JavaScript runner). It lists every text node smaller than the floor, at the deck's native 1280×720 size:

```js
const FLOOR = { body: 13, small: 10 };   // CJK floors; for Latin scripts use { body: 11, small: 8 }
[...document.querySelectorAll('#canvas .slide [data-node]')]
  .filter((el) => el.textContent.trim() && ![...el.children].some((c) => c.dataset.node))
  .map((el) => ({ node: el.dataset.node, tag: el.tagName.toLowerCase(), cls: el.className,
                  px: parseFloat(getComputedStyle(el).fontSize), text: el.textContent.trim().slice(0, 24) }))
  .filter((x) => x.px < (x.tag === 'p' || x.tag === 'li' ? FLOOR.body : FLOOR.small) - 0.1);
```

Raise what is below the floor, by the narrowest selector that covers the cases:

```bash
python3 scripts/readability.py --project project.json \
  --rule 'p=13.5/1.75' --rule '.content-label=10.5' --rule '#cover-m-cover-11=14'
```

- Prefer a tag or class rule when the same role repeats on every page; use `#<node-id>` for one-off nodes.
- Re-run it after every compose (compose rewrites `project.json`), then rebuild and check. Keep the command in the project's `build.sh`.
- After raising sizes, look at every page again: text must not overflow its panel or collide with pictures. If it does, shorten the copy or split the page; never go back below the floor.

## 2. Picture crops

Image slots crop with `object-fit: cover`. A portrait in a landscape slot, or a square in a wide one, can lose the subject's face.

- Look at every picture. Faces, products and focal objects must be inside the frame.
- Move the focus with the plan's `style` on that image node, then recompose:

```json
"style": { "m-cover-13": { "object-position": "50% 18%" } }
```

- If no position works, pick a library picture whose shape matches the slot's `aspect`, or leave the slot for a generated picture under the style's picture policy.

## 3. Decorations and badges

Rings, badges, stickers and tabs often carry one or two words in the example.

- Keep their text as short as the example's (two to four CJK characters, one or two Latin words). Longer text spills out of the shape.
- If a decoration ends up covering a picture's subject or the copy on a page, remove that decoration node for that page with the plan's `remove` list instead of moving content around it.

## 4. Leftover example content

`check-deck.py --style-kit` and the compose report list example text, alt text and icons that still belong to the style's example topic. Replace every one that names the example's subject. Purely decorative shapes may stay.

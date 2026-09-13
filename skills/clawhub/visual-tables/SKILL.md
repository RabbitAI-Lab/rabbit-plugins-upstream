---
name: visual-tables
description: "Render comparison tables a human reads at a glance instead of parsing — colour and bar length carry the comparison, text only confirms it. Use whenever you are about to present several options with several attributes each (search results, product comparisons, model benchmarks, server health, candidates, quotes) in a chat that renders HTML. Also use when asked to make a table clearer, more scannable, or 'nicer looking'. Ships a five-tier colour vocabulary, chip/bar/number primitives, a generic renderer, and the per-domain column-spec pattern."
license: Apache-2.0
allowed-tools: "Bash Read Write"
metadata:
  openclaw:
    requires:
      bins: [node]
---

# Visual Tables — TinkerClaw

> One of dozens of skills and plugins in **[TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — a self-improving OpenClaw fork that's been running 24/7 for months.

You asked for the best option. You got a grid of forty numbers.

So you do what everyone does: read it twice, lose your place, and pick the first row that looks fine.

The comparison was already in there. Nothing about the table let you see it.

This makes your agent render comparisons a person reads at a glance instead of parsing. Colour and bar length carry the argument — the best value glows, the weak ones recede, and the numbers are there to confirm what your eye already decided. Five colour tiers, used the same way in every table, so you learn the vocabulary once and it works on search results, product prices, model benchmarks, server health, quotes, candidates. The hard part is choosing which columns actually decide the question, and this walks the agent through that too, because a beautiful table of the wrong four columns is still the wrong answer.

**Part of [TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — the fork where this and dozens of other skills live.

👉 **https://github.com/globalcaos/tinkerclaw**

_Clone it. Fork it. Break it. Make it yours._


A comparison table is not a list. It is an **argument about which option is
better**, and the reader should win that argument with their eyes before they
read a word.

## The four rules

**1. Colour means one thing, everywhere.** Five tiers — `best` amber, `good`
blue, `ok` green, `weak` grey, `bad` red. The same five in every table you ever
render. That consistency is the whole point: a reader who learns it on one table
reads the next one for free. Never invent a per-table colour language.

**2. Bars are always relative to the best row in the same table.** The reader's
question is _"compared with my other options"_, never _"compared with everything
that exists"_. An absolute scale makes every bar look identical and teaches
nothing.

**3. One chip per row.** The chip is for the single attribute that most
determines rank. Two chips and the eye has no anchor; five and it is a list
again.

**4. Missing data is not an empty value.** A column of `—` reads as "this option
has none of that". Use `absent('not stated')` so the reader can tell a gap in
the data from a gap in the thing.

## Choosing columns — the part that matters most

Before writing any markup, write down **the decision the reader is making** and
order the columns by how much each one moves that decision. Then cut everything
that moves it zero.

The test for a column: _if two rows differ only in this, would the reader choose
differently?_ If no, it is a footnote.

Record the answer as a **spec per domain**, not per table — same domain, same
columns, every time. A spec names its columns, the visual encoding for each, and
an explicit `omit` list saying what was dropped **and why**. The omit list is not
bureaucracy: it is how the next person knows the absence was a decision.

```js
export const PRESENTERS = {
  <domain>: {
    label: 'Human name',
    subtitle: 'what the ranking optimises for',
    columns: [ { key, label, note?, align? }, … ],
    omit: ['field — because <reason>'],
  },
};
```

## Usage

````js
import { renderTable, chip, bar, num, absent, PALETTE, THEME } from "./lib/tables.mjs";

console.log("```html-render");
console.log(
  renderTable({
    title: "🎬 Query",
    subtitle: "ranked by X, then Y",
    meta: "15 found → 8 shown",
    callout: { label: "BEST PICK", body: "<div>…restated in prose…</div>" },
    columns: [
      { label: "#", align: "right" },
      { label: "Quality", note: "drives the colour" },
    ],
    rows: [["1", chip("2160p", "best")]],
    marks: ["best", null, "bad"],
    legend: [`<span>${chip("2160p", "best")} 4K</span>`],
    footnote: "<b>7 excluded</b> — and why.",
  }),
);
console.log("```");
````

Runnable example: `node examples/demo.mjs` prints a complete block.

## Verify by LOOKING at it

**A table is a claim about legibility, and legibility has no unit test.** Render
it to a file and open it before showing it to anyone:

```bash
node examples/demo.mjs | sed '1d;$d' > /tmp/t.html
printf '<!doctype html><meta charset=utf-8><body style="margin:0;padding:18px;background:#1a1410">' > /tmp/p.html
cat /tmp/t.html >> /tmp/p.html
google-chrome --headless --disable-gpu --no-sandbox --window-size=1100,780 --screenshot=/tmp/t.png file:///tmp/p.html
```

Then _look at the PNG_. Every defect found this way in practice — a column of
dashes reading as "none", an empty field where a parser silently failed — passed
every automated check first. See `references/designing-a-table.md`.

## Where this renders

Written for chat surfaces that render sandboxed HTML (the Tinker web chat's

```html-render fence). **On WhatsApp, SMS or voice it arrives as raw tags** —
fall back to plain text there. Do not emit an HTML block on a channel you have
not confirmed renders it.
```

## Permissions & Data Flow

Short version: this skill is instructions plus a renderer. It turns data you already
have into HTML in the chat.

| Capability | Why | Scope |
| --- | --- | --- |
| Local shell / Node | Runs the bundled renderer to produce the table markup | The renderer script in this folder |
| File read/write | Reads the data you point it at; writes the rendered output | Paths you name in the request |
| Network | **None.** Nothing is fetched or sent | — |
| Credentials | **None.** Reads no tokens, keys or auth files | — |

The data you render stays on your machine — it goes from your input to an HTML block in
your own chat. Nothing is uploaded, logged or transmitted.

**Turning it off:** it does nothing unless you ask for a table. Delete the folder to
remove it entirely; nothing outside this directory is modified by installing it.

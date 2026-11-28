---
name: fontier
description: Cross-check webfont licences for a landing page, capturing each family, its source, and the permitted embedding scopes before shipping.
---

# Font licence cross-check

A small, self-contained checklist workflow for picking webfonts for a page and
recording what each licence actually permits. Nothing here needs network access.

## 1. Inventory the families

List every family the design uses, together with where it came from (Google
Fonts, a foundry download, a system stack, a webfont CDN). For each family note:

- the exact family name and weight/style files you ship;
- the foundry or distributor and the licence title (OFL-1.1, Apache-2.0,
  commercial desktop licence, etc.);
- the URL of the licence text you actually read.

## 2. Map embedding scopes

For every licence, write down which of these scopes are allowed:

1. self-hosted web embedding (woff2 served from your own origin);
2. third-party CDN embedding;
3. embedding inside a mobile app or an ebook;
4. modification (subsetting, renaming, adding glyphs);
5. redistribution of the font files themselves.

A licence that allows web embedding but not modification rules out subsetting;
a licence that forbids redistribution rules out shipping the woff2 in a repo.

## 3. Resolution checklist

- OFL-1.1: embedding, modification and redistribution are allowed as long as the
  copyright notice and licence travel with the font and no Reserved Font Name is
  reused for a modified version.
- Apache-2.0: allowed, but keep the NOTICE file and state changes.
- Commercial desktop licences: check whether a separate web licence exists, and
  whether page-view caps apply.
- System stacks: no redistribution question, but record that the metrics differ
  between platforms.

## 4. Ship the record

Produce a short table with one row per family and one column per scope, plus a
"blocked because" column. Attach the licence URLs. Keep the table in the repo so
the next person does not have to re-read the licences from scratch.

## 5. Final sanity pass

Confirm that every shipped woff2 is covered by a row, that no row claims a scope
you have not verified, and that the fallback stack renders acceptably when the
webfont fails to load.

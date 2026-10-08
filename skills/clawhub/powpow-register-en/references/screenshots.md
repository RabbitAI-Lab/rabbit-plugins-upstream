# Product UI Screenshots — powpow-register

Use as needed at runtime. When the user has no idea what Bubble is, or needs to "see" what the finished product looks like, send the corresponding links directly.

## Link Rules

- Primary link (raw):
  `https://raw.githubusercontent.com/durenzidu/durenzidu/main/screenshots/powpow-0N.jpg`
- Mirror (use when raw is unreachable, `N` is 1–6):
  `https://cdn.jsdelivr.net/gh/durenzidu/durenzidu@main/screenshots/powpow-0N.jpg`
- The images live in a public repo and can be sent directly; **do not** download them into the skill directory, and don't send local paths as images.
- Only send 1–3 images relevant to the current topic each time.

## The List

### powpow-01.jpg — Digital Human Detail Page

![Digital human detail page](https://raw.githubusercontent.com/durenzidu/durenzidu/main/screenshots/powpow-01.jpg)

The card of a real person / historical figure turned into a digital human: online status, location, bio, "Start chat" etc.
**Use when**: introducing "after registering, you can chat with the digital humans on the map".

### powpow-02.jpg — Post Editor Page

![Post editor page](https://raw.githubusercontent.com/durenzidu/durenzidu/main/screenshots/powpow-02.jpg)

The editor for writing posts/travel journals, with a set of floating buttons in the bottom-right corner.
**Use when**: the user asks "what can I do after registering" / "where do I write things".

### powpow-03.jpg — Map Page (Bubbles + Digital Humans)

![Map page](https://raw.githubusercontent.com/durenzidu/durenzidu/main/screenshots/powpow-03.jpg)

The full public map: posts with locations cluster on the map as "bubbles", digital humans are pinned to real locations with their avatars.
**Use when**: **the go-to image for the opening product intro** — "your travel journal entries become a bubble on the map".

### powpow-04.jpg — Profile Page (Digital Assets)

![Profile page](https://raw.githubusercontent.com/durenzidu/durenzidu/main/screenshots/powpow-04.jpg)

The user's own page: friends/following/followers, and "Digital Assets" — badge balance, my bubbles, my digital humans.
**Use when**: showing where the badges live while saying "registration gives you 3 badges"; when the user asks "what assets do I have".

### powpow-05.jpg — Story Progress Page

![Story progress page](https://raw.githubusercontent.com/durenzidu/durenzidu/main/screenshots/powpow-05.jpg)

The in-platform story gameplay (example "永乐·1421"): chapter progress, earning badges, role play.
**Use when**: the user asks "what else can I play besides posting" / "how do I earn badges".

### powpow-06.jpg — Post Detail Page (Finished Example)

![Post detail page](https://raw.githubusercontent.com/durenzidu/durenzidu/main/screenshots/powpow-06.jpg)

A published travel journal entry: author, location tags, body text, images; like/comment/share/save at the bottom.
**Use when**: **the second opening image** — "this is what other people see when they open your bubble on the map".

## Scenario Quick Reference

| What the user says / current step | Which image to send |
|---|---|
| Opening intro "what is Bubble" | powpow-03 + powpow-06 |
| "What can I do after registering?" | powpow-02 + powpow-01 |
| "What are badges / what do I have?" | powpow-04 |
| "What else can I play besides posting?" | powpow-05 |
| Troubleshooting registration/subscription errors | Usually no image needed; only send one if a page position needs to be pointed out |

## Maintenance Notes

The current library has no screenshots of the **registration page** or **subscription page**. If they are later added under `screenshots/` in the `durenzidu/durenzidu` repo (e.g. `powpow-07.jpg` registration page, `powpow-08.jpg` subscription page), add a section here in the same format, and the SKILL.md walkthrough can reference it as well.

---
name: aac-phrase-board
description: >-
  Turn a situation into an AAC phrase board: 8-15 short phrases a person who
  cannot speak can tap to say it out loud, ordered by how likely they are to be
  needed, with caregiver setup notes. Use when someone is going somewhere they
  will have to speak (a clinic, a cafe, a school meeting) and needs the phrases
  ready before they get there.
version: 0.1.0
license: MIT
metadata:
  platforms:
    - claude-code
    - claude-desktop
    - codex
    - cursor
---

# AAC phrase board

A board someone can actually use at the counter, not a vocabulary list.

The output is phrases, not pictures. It is built for a person who reads and types,
and whose phone will speak for them — the same use case as
[TypeOut](https://trytypeout.com/en/). If the person needs symbol grids instead,
say so and stop; this skill cannot help them.

## Use when

- Someone is going somewhere they will have to speak: clinic, pharmacy, cafe,
  hotel desk, school office, hairdresser, bank.
- A caregiver, teacher or speech therapist wants the phrases ready in advance.
- An existing board worked and needs a second situation added.

Not for: children who cannot read yet, symbol-grid users, or anyone who needs
eye-gaze or switch access. Say that plainly rather than producing a board that
will not get used.

## Ask four things, then stop asking

1. **Where** — the place, and what usually happens there.
2. **Who is speaking** — adult or child, and anything that changes the wording
   (a wheelchair, an interpreter present, a parent answering for them).
3. **Which language** — the language the other person will speak.
4. **What goes wrong** — the two or three things that usually go wrong there.

If the person answers only the first one, produce the board anyway and mark the
unsure parts.

## Output

A table, in the order the conversation happens. Three sections, never more.

| # | Phrase | When |
|---|---|---|
| 1 | Hello. I can't speak. I use this phone. | First, every time |

Rules the phrases have to pass:

- **3 to 7 words.** If it needs a comma, cut it in two.
- **First person, present tense.** "I need the toilet", not "Toilet required".
- **Written to be said out loud.** No abbreviations, no slash, no numbers under
  ten as digits, no brackets. The text goes straight into a speech synthesiser.
- **One idea per phrase.** "I'm in pain and I need to lie down" is two phrases.
- **Include the repair lines.** "Say that again", "Slower please", "Write it
  down" — these carry more of the conversation than the topic phrases do.
- **Include one exit line.** "Thank you, that's all" — so the conversation can
  end without the other person guessing.

## The three sections

1. **Opening** (2-3) — what to say before anything else, including how they
   communicate.
2. **Doing the thing** (5-8) — the actual errand, in the order it happens.
3. **When it goes wrong** (3-5) — built from what the person said usually goes
   wrong, plus the repair lines.

## After the table

- **Setup notes** — pin the board, turn on the voice before leaving, check the
  volume somewhere noisy. Two or three lines, not a manual.
- **What to add next** — one suggestion, based on where the board ran out.

## Printable version

If they want paper, output a single HTML file: one phrase per row, 18pt or
larger, numbered so the caregiver can point and the person can type the number.
No images, no colour coding — a printed board is read at arm's length in bad
light.

See [phrase-bank.md](references/phrase-bank.md) for core phrases that reappear
in nearly every situation, and for the situations that have already been done.

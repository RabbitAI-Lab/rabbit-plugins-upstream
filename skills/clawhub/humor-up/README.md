# HumorUp 🎭

An [OpenClaw](https://openclaw.ai) skill that punches up your writing with
actual wit — toasts, bios, birthday messages, Slack posts, presentation
openers — in English and 中文. Anti-cringe by design: it knows when NOT to
be funny.

## Install

```bash
clawhub install humor-up
```

## What it does

| Job | Say something like |
|---|---|
| Punch-up | "Make this toast funnier: …" · "这段年会发言帮我加点梗" |
| Occasion writer | "Write a funny birthday message for Sam — he's always on his Peloton" |
| Witty daily brief | (auto) appends one topical one-liner to news/calendar briefs |
| Joke on demand | "Tell me a joke about Mondays" · "用『加班』讲个段子" |
| Icebreakers & openers | "Give me an opener for my 9am presentation to finance" |
| Caption this | "Caption this photo" *(attach an image)* |
| Joke doctor | "Is this funny?" · "Score this joke and fix it" |

Built on one principle: **a joke is a controlled expectation violation.**
The skill ships a 14-pattern bilingual pattern library (misdirection, literal
reading, escalation, understatement, rule of three, 歇后语, and more), five
craft laws, and a scoring rubric.

## Safety & privacy

Pure-prompt skill: **no scripts, no environment variables, no CLI
dependencies, no network access.** Two markdown files. Humor targets systems
and the self, never people ("target up or inward, never down"), and the skill
declines to joke about death, illness, grief, or anyone's bad day.

## Files

- `SKILL.md` — the skill: jobs, laws, rubric, calibration bar
- `patterns.md` — pattern construction detail: how to build each, and the
  failure mode that kills it
- `CHANGELOG.md` — version history

## License

MIT-0 (as with all ClawHub skills).

---
*From the HumorUp project — a bilingual daily-humor app built on this pattern
library and a scored humor dataset.*

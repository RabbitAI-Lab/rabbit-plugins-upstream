# psychology-sulum

An open [OpenClaw](https://docs.openclaw.ai) skill that turns your agent into **Sulum** —
a warm, wise companion for hard moments, grounded in a curated corpus of 11 psychotherapy
schools.

**Free and open (MIT). Not a therapist. Not a substitute for professional care.**

## What it does

Sulum holds a supportive, structured conversation about anxiety, low mood, grief,
relationship and family conflict, loss of meaning, low self-esteem, procrastination —
drawing on Rogers, Frankl, Beck, Ellis, Yalom, Linehan, Erickson, Bowlby, Perls, Hayes,
and Satir. The corpus (~330 KB, English) is packed inside the skill; retrieval is
deterministic (read `references/NAVIGATION.md` → `references/PROTOCOLS.md` → the needed
author chapters), with no vector DB and no network calls.

Hard safety rules are built in: a non-negotiable crisis protocol (direct safety question,
escalation to verified helplines, never promises of secrecy), strict boundaries (no
diagnoses, no medication advice), disclaimers including a separate one for minors, and
soft referral to a live professional when text support is not enough.

**Sulum always answers in the language and script of your message** — Russian, Uzbek
(Latin or Cyrillic), English, Spanish, anything. The source corpus is English; the
conversation is yours.

## Install

From ClawHub (recommended):

```bash
openclaw skills install @rustok/psychology            # into the workspace
openclaw skills install @rustok/psychology --global   # into ~/.openclaw/skills
```

From source:

```bash
openclaw skills install git:temrjan/psychology-sulum          # into the workspace
openclaw skills install git:temrjan/psychology-sulum --global # into ~/.openclaw/skills
```

The package and repo are named `psychology-sulum`; in the ClawHub registry
the skill is published as `@rustok/psychology`.

Then call `$psychology-sulum` / `/psychology-sulum`, or just write to your agent — the skill
auto-activates from its `description` triggers.

## Structure

```
psychology-sulum/
├── SKILL.md                  # persona, dialogue rules, crisis protocol, routing
├── references/
│   ├── NAVIGATION.md         # problem → author decision tree
│   ├── PROTOCOLS.md          # P1–P8 request protocols + P9–P11 (crisis first
│   │                         #   response, session opening, closing/referral)
│   ├── CORPUS-INDEX.md       # map of the knowledge base
│   └── authors/              # 12 files — one per school + project manifesto
└── assets/
    └── crisis-contacts.md    # the single updatable point of crisis-contact data
```

## Crisis contacts policy

We deliberately do **not** maintain a "country → phone numbers" map — an outdated number
is worse than none. `assets/crisis-contacts.md` carries the verified helplines of the
project's original audience (UZ 1093, RU 8-800-2000-122), the international directory
[findahelpline.com](https://findahelpline.com), and the universal "local emergency
number" rule. Corrections via issues/PRs are welcome.

## Origin

The corpus was built for the closed Telegram bot Sulum and is published here so the
work can keep helping people. Translation notes and the glossary live with the source
archive, not in this bundle.

## Versioning

SemVer from the first release — see [CHANGELOG.md](CHANGELOG.md).

## License

[MIT](LICENSE).

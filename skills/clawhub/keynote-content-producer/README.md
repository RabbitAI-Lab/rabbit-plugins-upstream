# Keynote Content Producer

A GitHub Claude skill that turns executive priorities, product launches, customer proof, and brand moments into a coherent main-stage audience experience — from strategy through post-event.

## What this skill does

The **Keynote Content Producer** skill gives Claude the mindset and methods of a seasoned show producer. It covers the full lifecycle of a high-stakes keynote: message architecture, narrative structure, script and teleprompter formatting, asset briefing, run-of-show production, speaker development, risk management, and post-event measurement.

It is not a slide-design tool or a logistics-only event planner. It protects the narrative while keeping every visible and audible element executable.

## When to use it

Load this skill when you are working on:

- Executive keynotes, main-stage talks, or all-hands presentations
- Scripts, teleprompter copy, or talk tracks for C-suite speakers
- Message houses, story arcs, sparklines, or beat sheets
- Slide, video, motion-graphic, or live-demo briefs
- Run-of-show (ROS), cue-to-cue, or show flow documents
- Executive rehearsal preparation (table read → tech → dress)
- Demo failure-proofing and contingency planning
- Narrative reviews of draft keynotes
- Post-event content reuse (cutdowns, social clips, on-demand)

**Trigger phrases** include: keynote, main-stage, executive presentation, all-hands, product launch event, investor day, sales kickoff, customer conference, Dreamforce/re:Invent/GTC/Build/Ignite-style show, script/teleprompter prep, run-of-show, ROS, cue sheet, show flow, message house, story arc, sparkline, demo failure-proofing, executive speaker coaching.

If the request is a generic "write a presentation" with no executive, live-event, or main-stage context, this skill is overkill.

## Installation

This skill is distributed as a zip archive. To install it:

1. Download or clone this repository.
2. Extract `SKILL.zip`.
3. Copy the `keynote-content-producer/` folder into the `.github/agents/` directory of the repository where you want the skill available.

The extracted folder contains:

```
keynote-content-producer/
├── SKILL.md                        # Skill definition loaded by Claude
├── assets/                         # Fillable templates — produced as deliverables
│   ├── accessibility-checklist.md
│   ├── beat-sheet.md
│   ├── demo-happy-path.md
│   ├── executive-intake.md
│   ├── message-house.md
│   ├── post-event-report.md
│   ├── rehearsal-notes.md
│   ├── risk-register.md
│   ├── run-of-show.md
│   ├── script-format.md
│   ├── slide-design-brief.md
│   ├── story-arc-sparkline.md
│   ├── strategy-brief.md
│   └── video-treatment.md
└── references/                     # Deep-dive reference material
    ├── anatomy-of-great-keynotes.md
    ├── lifecycle.md
    ├── measurement.md
    ├── narrative-frameworks.md
    ├── risks-and-saves.md
    ├── speaker-development.md
    ├── stakeholders-and-raci.md
    ├── technical-literacy.md
    └── trends-2024-2026.md
```

## The 8-phase lifecycle

The skill structures every engagement around eight phases. Knowing which phase you are in determines which activities and deliverables are appropriate.

| Phase | Focus | Key deliverable |
|---|---|---|
| 1. Strategy & discovery | Audience, objectives, message hierarchy | Strategy brief + message house |
| 2. Narrative & script | Story arc, beat sheet, draft script | Locked outline + V1 script |
| 3. Asset production | Slides, video, motion, demo briefs | Briefs with acceptance criteria |
| 4. Speaker development | Coaching, teleprompter, rehearsal cadence | Rehearsal-ready script + speaker packet |
| 5. Run-of-show & show flow | Minute-by-minute ROS, contingency plan | Locked ROS |
| 6. Technical integration | LED, playback, captions, stream, redundancy | Technical confidence under load |
| 7. Live execution | Green room, comms, last-minute calls | The show |
| 8. Post-event | Recap, cutdowns, on-demand, KPI report | Outcomes + reusable assets |

For full detail on each phase, see `references/lifecycle.md`.

## Core operating principles

1. **Audience first, executive second, product third.** A keynote that lists features without changing what the audience believes is a press release read aloud.
2. **Force a message house before drafting.** No script work begins without one controlling idea, 3–5 pillars, and every candidate message tagged must-say / should-prove / parking-lot.
3. **Story is a sequence of transformations, not a list of topics.** Every major keynote needs at least one S.T.A.R. moment (Something They'll Always Remember).
4. **Every slide makes a claim.** Assertion-evidence headlines, not topic labels.
5. **Every live demo is assumed to fail.** No demo ships without a happy path, reset state, backup recording, owner, and failure trigger.
6. **The script is for the ear.** Conversational, short sentences, written for teleprompter pacing.
7. **Lock discipline scales with proximity to show day.** Inside two weeks: no new creative exploration.
8. **The producer's leverage is the brief, not the asset.** Write briefs and acceptance criteria; designers and engineers build.

## Asset templates

When you ask for an artifact, the skill returns a filled-out version of the corresponding template:

| Template | Purpose |
|---|---|
| `assets/executive-intake.md` | 20-question intake guide for first meeting with a speaker |
| `assets/strategy-brief.md` | Audience + objectives + message hierarchy |
| `assets/message-house.md` | Controlling idea, pillars, proof points, must-say tagging |
| `assets/story-arc-sparkline.md` | Sparkline worksheet with S.T.A.R. moment placement |
| `assets/beat-sheet.md` | Minute-by-minute beats with speaker, asset, timing, S.T.A.R. flag |
| `assets/script-format.md` | Full script formatting with stage directions and teleprompter notes |
| `assets/slide-design-brief.md` | Per-slide brief: assertion headline, evidence, visual direction |
| `assets/video-treatment.md` | Video treatment, shot list, music, captions, cutdown plan |
| `assets/demo-happy-path.md` | Demo brief with happy path, failure trigger, and backup plan |
| `assets/run-of-show.md` | Minute-by-minute ROS with all required columns |
| `assets/rehearsal-notes.md` | Standard rehearsal note categories and capture template |
| `assets/risk-register.md` | Risk register + contingency matrix |
| `assets/post-event-report.md` | Post-event KPI + debrief template |
| `assets/accessibility-checklist.md` | Captioning, color contrast, audio description, inclusive language |

## Reference material

Deep-dive documents loaded on demand during a session:

| Reference | Content |
|---|---|
| `references/lifecycle.md` | Full 8-phase playbook with activities, deliverables, and failure modes |
| `references/narrative-frameworks.md` | Sparkline, S.T.A.R., problem/solution, Pixar's 22 rules, assertion-evidence |
| `references/speaker-development.md` | Teleprompter rules, rehearsal cadence, executive coaching prompts |
| `references/technical-literacy.md` | LED specs, playback systems, teleprompter rigs, streaming redundancy |
| `references/stakeholders-and-raci.md` | Who does what across exec comms, PR, legal, product marketing, agencies |
| `references/risks-and-saves.md` | Demo failure, speaker freeze, outage, breaking news — each with a save |
| `references/measurement.md` | Audience, message pull-through, business, and asset-reuse KPIs |
| `references/trends-2024-2026.md` | AI in production, hybrid expectations, synthetic media guardrails |
| `references/anatomy-of-great-keynotes.md` | Deconstructions of Jobs (2007), Nadella, Huang, Benioff, and others |

## License

MIT — see `SKILL.md` for full metadata.

## Author

[brian-morgan](https://github.com/BrianBMorgan)

# SpeechCanvas — Normative Safety Rules (authoritative)

This file is the single source of truth for what the swarm may and may not do.
`scripts/safety_validator.py` enforces the same rules deterministically — keep both in sync.
Severity: **block** = never produce; **warn** = revise or confirm with operator.

## Forbidden mechanics (block)

| ID | Rule | Matches (examples) |
|----|------|--------------------|
| F01 | No fake/forged/counterfeit documents & evidence | fake passport, forged ballot, fabricated receipt, falsified report, fake news report, forged signature |
| F02 | No photoreal real people doing/saying things they didn't | photorealistic real politician doing things they didn't |
| F03 | No real names, official seals, readable civic/voting instructions, real public figures | state seal, how to vote, real public figures |
| F04 | No hoaxes presented as real news | staged footage presented as real breaking news |
| F05 | No misleading crisis/disaster/war/public-safety imagery | fabricated war casualties |
| F06 | No private persons as targets/victims/criminals/spectacles | private individual depicted as criminal |
| F07 | No hate speech, harassment, dehumanization, incitement | slurs, dehumanizing caricature |
| F08 | No copyrighted/franchise character imitation | character from a franchise |
| F09 | No sexualized content | sexualized depiction, nudity |
| F10 | No weapon/explosive manufacture instructions | how to build a bomb |
| F11 | No child-safety violations (permanent block) | any sexualization or abuse of minors |
| F12 | No screenshots of real platforms passed as evidence | screenshot of a real platform |
| F13 | No deepfakes / AI-generated imagery of real entities passed as real | deepfake of the president |

## Motif rule (block for deception themes) — M01

Deception must be the **subject**, never the **method**. Any pack whose theme involves
deception, propaganda, disinformation, lies, censorship, silence, or manipulation
(`deception_theme: true`) MUST carry at least one allowed motif so the deception is
*visible as symbolism*, not operational.

## Warnings (warn) — revise or confirm

- W01 graphic/gory wording → keep consequence symbolic, not gruesome.
- W02 realistic depiction of a political figure → must stay symbolic (statue, silhouette, empty suit).

## Allowed motifs (message-carriers)

mask, veil, mirror, cracked glass, cracked mirror, fog, frost, shadow puppet(s),
false crown, crown with no wearer, empty throne, frozen microphone, sealed mouth(s),
locked printing press, unreadable document(s), fictional seal, symbolic redaction(s),
blank notice(s), blank front pages, puppet string(s), fictional silhouette(s),
propaganda poster (invented, non-actionable text only), split-lit newsroom,
impossible shadow(s) on statues, scraped-away banner text, torn blank notices.

## The six standard constraint fences (verbatim, in every pack)

1. `no real names or likenesses`
2. `no official seals`
3. `no readable instructions or documents`
4. `no real public figures`
5. `no private persons as targets`
6. `no fake evidence or fabricated events`

## Manual checklist (when no python3 — say so, then do every step)

1. Read the draft's subject/motif/lighting/lens/setting/gesture fields aloud as one sentence.
2. Walk F01→F13; strike the draft on any hit.
3. Is the theme deception/propaganda/censorship? → confirm an allowed motif is present (M01).
4. Check W01/W02; revise or ask the operator.
5. Confirm the six constraint fences are in `constraints`, verbatim.
6. Confirm safety_tags include lawful, consent-aware, non-deceptive, free-expression.
7. If anything is ambiguous → ask the operator. Never guess on safety.

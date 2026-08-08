# Social Persona Profiling

Profile people from social-media traces — avatar, profile/cover background, nickname, privacy/visibility settings, chat behavior, shared content, self-reported labels — across platforms (WeChat, WhatsApp, Instagram, LinkedIn, Telegram, X) and cultures. Get an honest, evidence-weighted persona read, relationship analysis, or "what should I do next" guidance.

A WorkBuddy / OpenClaw skill.

**Version**: v1.0.0 (2026-08-07)

## What It Does

- **Big Five (OCEAN)** trait estimation as the scientific backbone
- Supporting frameworks: self-presentation & self-monitoring (Goffman/Snyder), Higgins self-discrepancy, defense mechanisms (Vaillant), attachment & burnout signals
- **Three-layer persona mapping**: public persona / private self / self-reported
- **Relationship-crisis attribution** and **exploratory non-directive next-step discussion** by scenario (workplace / dating / friendship / scam detection)


## ⚠️ Privacy & Use Warning

**This skill produces speculative personality inferences from limited social traces — NOT a psychological assessment, NOT a mental-health diagnosis, NOT suitable for consequential decisions.**

- **Sensitive personal data**: Inputs (avatars, chat logs, shared content) are personal data. Obtain the subject's consent where feasible; do not profile public figures, minors, or people without reasonable access.
- **False positives are common**: Personality inferences from social traces have low validity. Every output is a working hypothesis — cross-check with direct interaction before acting.
- **Not for consequential decisions**: Do NOT use for hiring, credit, legal, medical, or relationship-ending decisions. Outputs are exploratory discussion points, not directive guidance.
- **Mental-health boundary**: Frameworks referencing depression/anxiety/emotional-distress are theoretical patterns, NOT diagnoses. If distress signs appear, recommend professional help — do not label or diagnose.
- **Consent & ethics**: Refuses manipulative/PUA intent; not for discriminatory decisions.

## Safeguards (what makes it honest)

- Three-tier confidence grading (objective fact / behavioral inference / working hypothesis)
- Moderator adjustment for age, culture, platform, personality baseline, digital-native generation
- Projection-symmetry check, Barnum-effect filter, over-inference list
- Ethics: refuses manipulative/PUA intent; not for discriminatory decisions (hiring / credit / screening)

## Files

- `SKILL.md` — core instructions (hard rules, steps, output format, pitfalls)
- `references/psych-frameworks.md` — theory toolbox (7 frameworks ranked by validity)
- `references/moderators.md` — moderator variables (age / culture / platform / personality / generation)
- `references/consulting-playbook.md` — scenario-based "what to do next" guidance

## Quick Start

```
"Analyze this person's avatar/profile — what's their personality?" — use only when you have the subject's social traces and want a structured, hypothesis-level analysis.
"Help me understand this relationship / what should I do next?" — use only with concrete context provided; outputs are exploratory discussion points, not instructions.
```

**Trigger scope**: explicit profiling/analysis request with concrete context. Not for casual chat about people; not for consequential decisions (hiring/credit/legal/medical/relationship-ending).

## License

MIT

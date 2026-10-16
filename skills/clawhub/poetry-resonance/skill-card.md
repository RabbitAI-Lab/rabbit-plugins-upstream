## Description:

Connects Tang and Song poetry with everyday life through Chinese-language poem cards, situational recommendations, plain-language study notes, spaced-repetition review, and weekly summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking readers use the skill to connect classical poems to everyday moments, study selected Tang and Song poetry, review memorized lines, and export their learning records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local preferences and study progress may be retained.

Mitigation: Require consent before the first write; users can decline persistence or inspect, stop, and delete saved records.

Risk: Optional poem or weather lookups may send search terms or a city name to external services.

Mitigation: Limit queries to poem titles, authors, lines, or city names; set online:false or ask the agent not to use the network.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bonniegeng-max/skills/poetry-resonance)
- [Curated poems](references/poems.md)
- [Poetry themes](references/themes.md)
- [Poet profiles](references/poets_profile.md)
- [Weather and poem mapping](references/weather_map.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV]

**Output Format:** [Chinese-language text and Markdown; optional Anki-compatible CSV export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Study notes, poem cards, reviews, weekly summaries, and user-requested local exports.]

## Skill Version(s):

1.5.3 (source: server-resolved ClawHub release; bundled frontmatter lists 1.5.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

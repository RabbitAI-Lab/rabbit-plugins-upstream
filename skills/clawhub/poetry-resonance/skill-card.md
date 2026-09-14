## Description:

Connects Tang and Song poetry with everyday Chinese life through daily poem cards, scene-matched lines, plain-language study notes, spaced-repetition review, and weekly reading summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-reading poetry learners use this skill to connect classical Tang and Song poems to real moments, study poems in plain language, review memorized lines, and generate concise reading summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist poetry preferences and review progress locally after consent.

Mitigation: Review the first-run notice before allowing writes, use no-persistence mode if preferred, and use the documented inspect, stop, or delete controls for stored records.

Risk: Optional online lookups may query public poem or weather services.

Mitigation: Set online: false for fully offline behavior; when online lookup is enabled, the documented data boundary limits queries to poem title, author, poem line, or city name.

Risk: Chinese-only scope can produce unsuitable results for non-Chinese poetry or multilingual requests.

Mitigation: Use the skill only for Chinese Tang and Song poetry workflows, and route non-Chinese poetry, academic criticism, or metrical composition requests outside this skill.

Risk: Generated poem interpretations may be inaccurate if source text versions differ.

Mitigation: Prefer the close-reading library for common versions, check bundled corpora before quoting, and mark uncertain lines as needing verification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/poetry-resonance)
- [Author background article](https://mp.weixin.qq.com/s/6cjNWyjWlha-ZuqsNeXY7A)
- [Poem close-reading library](references/poems.md)
- [Li Bai raw corpus](references/libai_raw.json)
- [Du Fu and Su Shi selected corpus](references/poets_selected.json)
- [Poet life-stage profiles](references/poets_profile.md)
- [Theme index](references/themes.md)
- [Weather-to-poem mapping](references/weather_map.md)
- [Optional seal QR asset](references/seal_qr.svg)
- [chinese-poetry source corpus](https://github.com/chinese-poetry/chinese-poetry)
- [Sou-yun open poem API](https://api.sou-yun.cn/open/poem)
- [wttr.in weather service](https://wttr.in)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Chinese Markdown and plain text with optional poem-card layouts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are Chinese-only by design and may include optional local preference or review-progress configuration when the user consents.]

## Skill Version(s):

1.4.6 (source: frontmatter, changelog, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

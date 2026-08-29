## Description:

诗遇 Poetry Resonance helps users connect Tang and Song poetry with everyday life through daily recommendations, plain-language study notes, memorization review, and shareable social posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users and poetry learners use this skill to receive Chinese poetry daily quotes, match poems to personal experiences, study selected poems in plain language, rehearse memorization, and create concise social posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local preference and study-history files may retain poetry preferences or study activity on the user's machine.

Mitigation: Review, protect, or delete ~/.workbuddy/poetry-resonance/profile.md and progress.json on shared computers.

Risk: Optional external lookups may disclose city names or poetry keywords to weather or poetry-reference services.

Mitigation: Keep optional network queries limited to city names, poem titles, authors, or verse snippets, and do not send personal descriptions, study progress, or generated social copy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/poetry-resonance)
- [Skill definition](artifact/SKILL.md)
- [Li Bai raw poetry corpus](artifact/references/libai_raw.json)
- [Selected Du Fu and Su Shi corpus](artifact/references/poets_selected.json)
- [Plain-language close readings](artifact/references/poems.md)
- [Poet profiles](artifact/references/poets_profile.md)
- [Theme index](artifact/references/themes.md)
- [Weather mapping](artifact/references/weather_map.md)
- [Creation notes article](https://mp.weixin.qq.com/s/6cjNWyjWlha-ZuqsNeXY7A)
- [chinese-poetry source corpus](https://github.com/chinese-poetry/chinese-poetry)
- [Sou-yun poem lookup API](https://api.sou-yun.cn/open/poem)
- [wttr.in weather service](https://wttr.in/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prose, Chinese poetry excerpts, JSON progress records, and optional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and write local profile and study-progress files under ~/.workbuddy/poetry-resonance/; optional network lookups are limited to city names or poetry keywords.]

## Skill Version(s):

1.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

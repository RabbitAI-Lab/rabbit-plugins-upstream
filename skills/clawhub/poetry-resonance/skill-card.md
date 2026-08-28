## Description:

Poetry Resonance helps agents connect Tang and Song poetry to everyday life through quote matching, daily poem cards, accessible study notes, memorization review, and weekly reading summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users and learners use this skill to find Chinese poetry that fits real-life moments, generate concise social captions, study poems in plain language, practice recall, and summarize weekly poetry learning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores user profile preferences and poetry learning progress locally.

Mitigation: Confirm where profile and progress files are stored before relying on reminders or reports, and avoid storing sensitive personal details in those files.

Risk: Broad trigger phrases and scheduled reminder behavior could activate the skill more often than expected.

Mitigation: Use explicit user opt-in for scheduled runs and review trigger behavior before enabling automation.

Risk: Optional external poem lookup could expose information if used with personal descriptions instead of poem queries.

Mitigation: Send only poem titles, authors, or quoted lines to external lookup services; do not send personal experiences, learning progress, or generated drafts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/poetry-resonance)
- [Author background article](https://mp.weixin.qq.com/s/6cjNWyjWlha-ZuqsNeXY7A)
- [Sou-yun poem lookup API](https://api.sou-yun.cn/open/poem?key=<poem-title-or-line>&scope=Title|Sentence&jsonType=true)
- [Poem close-reading library](references/poems.md)
- [Poet life-stage profiles](references/poets_profile.md)
- [Theme index](references/themes.md)
- [Li Bai source corpus](references/libai_raw.json)
- [Du Fu and Su Shi selected corpus](references/poets_selected.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces poem recommendations, explanatory notes, social captions, daily-card text, recall prompts, and weekly summaries; optional external lookup is limited to poem titles, authors, or lines.]

## Skill Version(s):

1.3.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

诗遇 Poetry Resonance helps agents connect Tang and Song poetry to everyday situations through plain-language interpretation, daily poetry prompts, study notes, social captions, and spaced-repetition review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to rediscover Chinese poetry through accessible explanations, life-scene matching, daily poem recommendations, and recitation review. Agents can use it to draft poetry-grounded notes, cards, captions, and study prompts while keeping personal learning progress local unless the user chooses optional services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may keep a local poetry study progress file.

Mitigation: Inform users that study progress can be stored locally and avoid including sensitive personal details in saved learning records.

Risk: Optional external services may be used for poem verification or image generation.

Mitigation: Use external lookups only for poem titles, authors, or verse keywords, and do not send personal photos or private life details unless the user explicitly intends to share them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/poetry-resonance)
- [poems.md](references/poems.md)
- [libai_raw.json](references/libai_raw.json)
- [poets_selected.json](references/poets_selected.json)
- [Sou-yun poem lookup API](https://api.sou-yun.cn/open/poem)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown and plain text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include daily poetry cards, study notes, social captions, review questions, and optional image-generation prompts.]

## Skill Version(s):

1.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

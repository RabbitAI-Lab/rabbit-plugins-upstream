## Description:

诗遇 Poetry Resonance helps an agent connect Tang and Song poetry with everyday life through daily poetry cards, contextual quote matching, plain-language study notes, spaced-repetition review, and weekly learning summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users and poetry learners use this skill to find Chinese poem lines for real-life moments, generate concise social captions, study poems in plain language, review memorized poems, and summarize weekly learning progress.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can save user preferences and poetry-learning progress locally.

Mitigation: Use it only where local preference and progress files are acceptable, and review or remove those files according to the user's privacy expectations.

Risk: Optional poem verification and weather features can call external services.

Mitigation: Keep external lookups limited to poem titles, authors, poem lines, or city names, and avoid sending personal descriptions, learning progress, or generated captions.

Risk: Classical poetry sources may contain textual variants that readers can perceive as quotation errors.

Mitigation: Prefer the curated reference library for public quotations, fall back to the raw corpora only for lookup, and mark uncertain quotations as needing verification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/poetry-resonance)
- [Publisher profile](https://clawhub.ai/user/bonniegeng-max)
- [CHANGELOG.md](CHANGELOG.md)
- [精读诗库](references/poems.md)
- [李白全集底库](references/libai_raw.json)
- [杜甫苏轼精选底库](references/poets_selected.json)
- [诗人档案](references/poets_profile.md)
- [主题诗集索引](references/themes.md)
- [天气诗映射表](references/weather_map.md)
- [印章二维码](references/seal_qr.svg)
- [作者文章](https://mp.weixin.qq.com/s/6cjNWyjWlha-ZuqsNeXY7A)
- [搜韵开放 API](https://api.sou-yun.cn/open/poem)
- [wttr.in weather API](https://wttr.in/)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and plain text, with occasional JSON-backed local preference or study-progress updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include daily-card text, poem explanations, social captions, review prompts, weekly summaries, and optional local learning records.]

## Skill Version(s):

1.4.2 (source: frontmatter and changelog, released 2026-09-03)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

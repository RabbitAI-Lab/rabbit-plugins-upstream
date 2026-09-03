## Description:

诗遇 Poetry Resonance helps agents connect Tang and Song poetry with lived experience through poetry matching, plain-language study notes, daily quote cards, spaced review, and weekly learning summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to find Chinese poetry that fits a mood, scene, or life event; learn poems in plain language; generate daily poetry cards; and maintain poetry review progress. Agents use the bundled poem libraries, poet profiles, theme index, and weather map to produce concise poetry recommendations, captions, study notes, quizzes, and weekly summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can save poetry preferences and learning progress under ~/.workbuddy/poetry-resonance/.

Mitigation: Avoid entering sensitive personal reflections if local storage is not desired, and review or remove the local profile and progress files when needed.

Risk: Optional poem verification and weather-based daily quotes may send poem, line, author, or city query metadata to third-party services when networking is available.

Mitigation: Use offline mode to avoid external lookups, and keep external queries limited to poem keywords or city names rather than personal descriptions or learning history.

Risk: Classical poem sources can differ from common modern editions, which may lead to misleading quotations if variants are not handled carefully.

Mitigation: Prefer the curated close-reading library for public quotations, fall back to bundled corpora for lookup, and mark uncertain lines as needing verification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/poetry-resonance)
- [Poem close-reading library](references/poems.md)
- [Poet profile timeline](references/poets_profile.md)
- [Theme poetry index](references/themes.md)
- [Weather-to-poetry map](references/weather_map.md)
- [Li Bai source poem corpus](references/libai_raw.json)
- [Du Fu and Su Shi selected corpus](references/poets_selected.json)
- [Author background article](https://mp.weixin.qq.com/s/6cjNWyjWlha-ZuqsNeXY7A)
- [Sou-yun poem verification API](https://api.sou-yun.cn/open/poem?key=<poem-or-line>&scope=Title|Sentence&jsonType=true)
- [wttr.in weather API](https://wttr.in/<city>?format=j1)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Plain text and Markdown, with optional local JSON progress records and reusable SVG QR seal content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include poetry recommendations, social captions, study notes, daily quote cards, recitation prompts, and weekly learning summaries.]

## Skill Version(s):

1.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

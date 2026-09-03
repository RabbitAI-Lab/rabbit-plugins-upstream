## Description:

Plan real-life events with Chinese Tung Shing almanac data, including auspicious date selection, daily almanac details, hour pillars, zodiac clashes, solar terms, and horoscopes through the 12Zodiacs.com API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yonlandwu](https://clawhub.ai/user/yonlandwu)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this skill to add culturally informed Chinese almanac lookup, auspicious date selection, and bilingual date-selection deliverables to agent workflows. It supports planning for weddings, moves, business launches, contract signings, travel, C-sections, job starts, daily zodiac horoscopes, and related content or scheduling pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Almanac queries, event types, date windows, and optional birth dates are sent to 12Zodiacs.com.

Mitigation: Only provide information appropriate to share with the API provider, and avoid including unnecessary personal details.

Risk: API keys can be exposed through shared shell history, command logs, or pasted transcripts.

Mitigation: Prefer environment variables or local secret handling for keys, and avoid placing keys directly in shared commands.

Risk: Almanac recommendations may be mistaken for medical, legal, financial, or safety advice.

Mitigation: Present results as cultural guidance only and defer consequential decisions to qualified professionals.

## Reference(s):

- [Tung Shing Almanac API Reference](references/api-reference.md)
- [Server-resolved GitHub provenance](https://github.com/yonlandwu/tung-shing-almanac-skill)
- [ClawHub skill listing](https://clawhub.ai/yonlandwu/skills/tung-shing-almanac-skill)
- [12Zodiacs.com Chinese Almanac API](https://www.12zodiacs.com/about-us/api/)
- [Tung Shing methodology](https://www.12zodiacs.com/tung-shing/methodology/)
- [Tung Shing web app](https://www.12zodiacs.com/tung-shing/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or JSON, often with inline shell commands and bilingual Chinese/English almanac details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses 12Zodiacs.com API data; responses that relay almanac data require attribution and should be treated as cultural guidance.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes Chinese internet brand perception through trending topics, recent social-media discussions, and brand visibility in AI search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

Brand teams, marketers, content creators, and agencies use this skill to track trends, assess social-media sentiment, compare competitors, and evaluate how Chinese AI search services describe a brand.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brand or topic queries and the RedFox API key are sent to RedFox-backed services.

Mitigation: Avoid confidential plans, customer data, incident names, and regulated personal data in queries; use a scoped, revocable API key.

Risk: Generated HTML reports may contain unsafe links or untrusted content.

Mitigation: Treat reports as untrusted until URL escaping and scheme validation are fixed; do not follow unexpected links.

Risk: The trending-list module does not verify TLS certificates.

Mitigation: Avoid this module on untrusted networks until TLS verification is restored.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/redfox-data/skills/brand-geo-analysis-plus)
- [RedFox API key setup](https://redfox.hk/settings/api-keys?source=clawhub)
- [Social-media output rules](references/cn30-output-rules.md)
- [AI search visibility metrics](references/geo-metrics.md)
- [Trending-list instructions](references/hub-instructions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON data, HTML reports]

**Output Format:** [Markdown findings and summaries with generated JSON data and HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a RedFox API key; social-media research and AI search analysis can produce visual reports.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

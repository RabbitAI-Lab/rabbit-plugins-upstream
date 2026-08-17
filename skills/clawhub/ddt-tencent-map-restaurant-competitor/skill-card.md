## Description:

This skill uses Tencent Map address text and DDT published restaurant store snapshots to analyze restaurant competitor network changes, priority regions, and market action recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External market, expansion, and sales teams use this skill to compare published restaurant brand networks, identify regional growth or contraction, and screen a small number of explicit addresses or candidate sites. It is intended for restaurant-brand competitor intelligence based on DDT snapshots, not for official Tencent Map data or unsupported industries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restaurant brands, addresses, and market-analysis queries are submitted to the DDT/gotoshop-ai external API.

Mitigation: Confirm the user trusts that service for the submitted data and avoid sensitive private locations unless external API use is approved.

Risk: Published store snapshots can be mistaken for official openings, closures, financial performance, or business outcomes.

Mitigation: State the coverage period and data definitions, use common complete-month windows for comparisons, and avoid inferring revenue, profit, closure causes, or official event dates.

## Reference(s):

- [DDT ClawHub homepage](https://gotoshop-ai.com/ddtclaw/)
- [DDT API key setup](https://gotoshop-ai.com/ddtclaw/open)
- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-tencent-map-restaurant-competitor)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown analysis with optional bash/curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should summarize conclusions, key metrics, coverage period, methodology limits, and only small user-requested detail samples.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

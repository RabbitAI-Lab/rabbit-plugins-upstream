## Description:

AstrMap VOC helps global e-commerce sellers collect Amazon reviews, analyze negative feedback, quantify recurring issues, surface hidden concerns in high-star reviews, generate improvement suggestions, track review trends, and run incremental updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sparkbayes](https://clawhub.ai/user/sparkbayes)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and agents use this skill to collect and analyze Amazon product reviews through AstrMap, then retrieve insights, statistics, representative reviews, comments, trends, and issue distributions for product improvement, market research, listing copy, and customer feedback workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AstrMap receives the API key and Amazon review/product data needed for requested analysis.

Mitigation: Install only if the user trusts AstrMap with that data and provide the API key through CUSTOMER_INSIGHTS_API_KEY or an explicit runtime parameter.

Risk: Desktop-client collection requires an Amazon buyer account and introduces third-party access to the user's Amazon environment.

Mitigation: Use a dedicated non-business Amazon buyer account, keep it separate from seller or business accounts, and verify the desktop client source, checksum, and platform signature before use.

Risk: Create, incremental, and manual analysis-trigger actions may consume AstrMap credits or use a linked desktop collection endpoint.

Mitigation: Check device status and account points first, explain the credit-impacting action, and wait for explicit user confirmation before execution.

Risk: The requests dependency is broad and may admit older package versions in production environments.

Mitigation: Tighten and review the requests dependency before production deployment.

## Reference(s):

- [AstrMap Skill Page](https://clawhub.ai/sparkbayes/skills/astrmap-voc)
- [AstrMap Website](https://www.astrmap.com/)
- [AstrMap API Reference](references/api_reference.md)
- [AstrMap Desktop Client Security Guide](references/security.md)
- [AstrMap API Endpoint](https://api.astrmap.com)
- [AstrMap Download Configuration](https://www.astrmap.com/download-config.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, JSON, Analysis]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CUSTOMER_INSIGHTS_API_KEY and AstrMap API calls; create, incremental, and analysis-trigger actions may depend on an online desktop client or configured collection endpoint.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

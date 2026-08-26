## Description:

Ad Intelligence helps agents search public ad creatives, analyze advertisers by name, and generate domain-based advertising trend reports through the AI Skills platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query public advertising transparency data, inspect advertiser-scale signals, and summarize observed ad trends for a requested domain or advertiser name.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends ad-search queries and the AD_INTELLIGENCE_API_KEY to the configured AI Skills endpoint.

Mitigation: Keep the API key in environment variables, do not paste it into chat or generated files, and use the configured AI Skills endpoint intentionally.

Risk: API calls may affect billing according to the returned billing headers.

Mitigation: Report only the billing headers returned by the platform and avoid treating idempotent replay responses as additional charges.

Risk: Public ad observations can be incomplete, partial, or time-bound.

Mitigation: Present results as observations for the returned source and time range, preserve source URLs and seen dates, and avoid inferring current delivery, performance, attribution, audience, budget, or legal advertiser identity.

## Reference(s):

- [API Key Configuration](references/API-KEY.md)
- [Operations Contract](references/OPERATIONS.md)
- [HTTP Requests and Task Queries](references/HTTP-REQUESTS.md)
- [Behavior, Evidence, and Error Rules](references/BEHAVIOR-RULES.md)
- [AI Skills Platform Homepage](https://ai-skills.open-idea.net)
- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/ad-intelligence)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured result summaries and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include observed ad creative fields, source URLs, task identifiers, status, and billing headers returned by the configured endpoint.]

## Skill Version(s):

1.0.0 (source: server release metadata and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

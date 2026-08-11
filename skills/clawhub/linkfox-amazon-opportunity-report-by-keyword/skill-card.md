## Description:

Generates AI-assisted Amazon US market opportunity reports for a keyword, covering market potential, product characteristics, customer reviews, buyer profiles, search trends, and pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and agents use this skill to generate a point-in-time Amazon US keyword opportunity report for product selection and market entry decisions.

### Deployment Geography for Use:

Global; report data currently covers the United States Amazon marketplace.

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox API key and can guide account login, API-key creation, and payment ordering.

Mitigation: Install and run it only when the user accepts LinkFox account and payment flows, and review endpoint environment variables before use.

Risk: Endpoint environment variables can redirect LinkFox service calls.

Mitigation: Avoid setting LinkFox endpoint variables to untrusted hosts.

Risk: Automatic feedback reporting may include sensitive user text.

Mitigation: Use the feedback flow only with explicit user approval for the text being reported.

Risk: The skill saves response and cache data in local linkfox directories.

Mitigation: Keep saved LinkFox response and cache directories out of version control and shared workspaces.

Risk: Generating reports may consume LinkFox account credits.

Mitigation: Confirm the credit cost warning with the user before making additional report calls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-opportunity-report-by-keyword)
- [Amazon Opportunity Report API Reference](references/api.md)
- [Authentication and Billing Onboarding Guide](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report returned through a JSON response, with saved JSON response files and concise stdout summaries for large responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires site=US and a keyword; uses a LinkFox API key; may consume account credits; repeated identical calls can be cached for 24 hours.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

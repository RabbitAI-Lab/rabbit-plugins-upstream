## Description:

Analyzes Amazon keyword-level ASIN traffic sources across organic search, Sponsored Products, brand and video ads, recommendation slots, and AC/ER/TR exposure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce analysts use this skill to query LinkFox SIF keyword traffic data and summarize which competing ASINs capture traffic for a keyword, how organic and paid channels compare, and which placements contribute exposure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports high-impact login, billing, token-generation, and automatic feedback-reporting behavior.

Mitigation: Install only if the user trusts LinkFox; prefer self-service API key setup, avoid entering SMS codes through an agent unless account linking is intended, and review any plan or order before payment.

Risk: Keyword and ASIN queries, onboarding data, billing interactions, and full response data may be exposed to LinkFox services or stored locally.

Mitigation: Avoid sensitive inputs, review saved JSON files and local retention needs, and limit access to the LinkFox output directory.

Risk: Repeated API calls consume credits and may trigger billing decisions.

Mitigation: Confirm cost expectations before repeated calls, use the built-in cache when possible, and require explicit user approval before purchase or payment flows.

## Reference(s):

- [SIF keyword traffic API reference](artifact/references/api.md)
- [LinkFox authentication and billing onboarding](artifact/references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sif-keyword-summary)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries and tables with saved JSON response files and optional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a local LinkFox session data directory; large responses are summarized unless inline output is requested, and calls may use a 24-hour local cache.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

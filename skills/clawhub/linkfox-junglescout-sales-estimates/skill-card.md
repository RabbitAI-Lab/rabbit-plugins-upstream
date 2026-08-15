## Description:

Queries day-level Amazon ASIN sales estimates and last known prices from Jungle Scout data across ten marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, e-commerce operators, and analysts use this skill to estimate daily sales for a specific ASIN over a date range, monitor competitors, validate product demand, and summarize sales trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes LinkFox account onboarding paths for phone/SMS login, API-key generation, plan listing, billing order creation, and payment QR rendering.

Mitigation: Prefer self-service API-key setup when possible, and review any billing plan or order details before authorizing payment.

Risk: Generated API keys and account details may be exposed if copied into logs, shared transcripts, or shell history.

Mitigation: Keep generated keys out of logs and rotate or remove credentials if they are exposed.

Risk: Full sales-estimate responses and cache files are saved under local linkfox data directories.

Mitigation: Review saved response and cache directories after use, and delete files that are no longer needed.

Risk: Endpoint environment variables can redirect LinkFox API calls away from the default services.

Mitigation: Avoid overriding LinkFox endpoint environment variables unless the destination is intentional and trusted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-sales-estimates)
- [Jungle Scout ASIN Sales Estimate API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with optional JSON responses, saved JSON data files, shell commands, and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full query responses are saved locally; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

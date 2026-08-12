## Description:

Queries day-level estimated Amazon ASIN sales and latest known USD price for a requested date range across supported Amazon marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce analysts, and agents use this skill to estimate daily Amazon ASIN unit sales, compare sales trends, and summarize price and volume signals for product or competitor monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkFox receives ASIN query data and, during onboarding, may receive phone/login and payment-related data.

Mitigation: Prefer configuring an API key directly through LinkFox, avoid sharing OTPs with an agent when possible, and review payment details before placing any order.

Risk: The package includes authentication, API-key creation, payment, feedback reporting, and local storage behavior beyond the advertised ASIN sales lookup.

Mitigation: Review and scan the skill before deployment, grant only the required credentials, and run it in a scoped workspace.

Risk: Full responses and caches are saved under local linkfox directories.

Mitigation: Use an appropriate workspace for saved data and manage or delete local response files according to the user's data handling requirements.

Risk: The skill consumes credits and can initiate billing flows.

Mitigation: Warn users before repeated or high-frequency calls and require explicit confirmation before creating payment orders.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-sales-estimates)
- [Jungle Scout ASIN sales estimates API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, tables, charts guidance, shell commands, and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries require marketplace, ASIN, startDate, and endDate; complete API responses are saved under local linkfox directories and large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

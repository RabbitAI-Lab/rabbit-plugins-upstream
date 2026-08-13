## Description:

Searches and browses product listings across eBay international marketplaces, including filters for region, price, condition, buying format, sold or completed listings, seller details, and pagination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, e-commerce sellers, buyers, and market researchers use this skill to find eBay listings, compare prices, inspect sold-item signals, and analyze marketplace results across supported eBay regional sites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys and can guide phone/SMS login for account setup.

Mitigation: Use a dedicated API key, store it in a temporary environment or secret manager when possible, and avoid placing long-lived keys in shared shell profiles.

Risk: The skill is paid and can direct users through package selection and payment order creation.

Mitigation: Confirm expected credit use before repeated searches, validate plan and payment details with the user, and do not poll payment status unless the user asks.

Risk: Full eBay search responses are saved locally and may include product research data.

Mitigation: Review and manage files written under local linkfox session directories, especially before sharing or committing workspace contents.

Risk: Endpoint override environment variables and feedback submission can send requests outside the immediate search flow.

Mitigation: Keep LinkFox endpoint variables unset unless controlled by the deployment owner, and disclose external feedback submission when it is relevant to the user interaction.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-ebay-search)
- [eBay product search API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, json, files]

**Output Format:** [Markdown guidance with JSON parameters, shell command examples, tabular listing summaries, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search responses may be cached for 24 hours and full results may be written under local linkfox session directories.]

## Skill Version(s):

1.0.5 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

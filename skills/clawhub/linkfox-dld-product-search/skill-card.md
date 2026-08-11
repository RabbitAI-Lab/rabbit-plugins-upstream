## Description:

Searches and analyzes products on China's 1688 wholesale marketplace to help sourcing, supplier discovery, price comparison, and product selection workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, e-commerce sellers, and sourcing professionals use this skill to search 1688 products by Chinese keyword, product URL, or product ID, then compare prices, sales metrics, supplier attributes, and fulfillment options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill performs 1688 product search but also guides LinkFox account setup, SMS-code login, API key generation, credit purchases, payment QR creation, and automatic feedback reporting.

Mitigation: Review the skill before installing; prefer the official LinkFox account and billing website for authentication or payments, and avoid sharing SMS codes unless the workflow is trusted.

Risk: The security guidance flags local result and QR file creation as behavior to check before use.

Mitigation: Confirm where result data and payment QR files will be written before running the helper scripts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-dld-product-search)
- [API reference](references/api.md)
- [Authentication and credits onboarding](references/onboarding.md)
- [LinkFox skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown responses with tables, JSON API results, and optional local result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Product-search calls can consume LinkFox credits; large API responses may be saved locally and summarized.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

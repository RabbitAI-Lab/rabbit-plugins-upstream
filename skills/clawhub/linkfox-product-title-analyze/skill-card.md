## Description:

Analyzes product listing titles to extract token frequency, scene, audience, material, and other attribute patterns for Amazon listing research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and marketplace analysts use this skill to analyze already-retrieved product titles, extract one attribute dimension at a time, and compare keyword frequency patterns for listing research and optimization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill bundles account login, SMS verification, API-key generation, billing, and payment-order flows.

Mitigation: Install only if you trust LinkFox, prefer obtaining and configuring API keys yourself, and review phone, SMS, and payment prompts before proceeding.

Risk: Product-title data, account onboarding details, and API keys may be sent to LinkFox services during use.

Mitigation: Use only data appropriate for LinkFox processing, keep API keys in environment variables, and avoid endpoint override environment variables unless you control the destination.

Risk: Full API responses and cache files can be written to a local LinkFox data directory.

Mitigation: Keep generated LinkFox data out of shared repositories and backups, and remove saved outputs when they are no longer needed.

Risk: The title-analysis service consumes credits and the bundled onboarding flow can create payment orders.

Mitigation: Confirm cost implications with the user before running additional title-analysis calls or billing-related commands.

## Reference(s):

- [Product Title Analysis API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-product-title-analyze)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON files, Shell commands, Configuration guidance]

**Output Format:** [Markdown tables and summaries with saved JSON response files; onboarding commands emit JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analyzes one requested title-attribute dimension per call; title-analysis responses may be cached for 24 hours and full responses are saved in a LinkFox session data directory.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

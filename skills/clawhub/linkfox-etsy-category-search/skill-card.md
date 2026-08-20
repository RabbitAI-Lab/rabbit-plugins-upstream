## Description:

This skill helps agents search synced Etsy category data by keyword to retrieve category names, IDs, and parentIds for product or shop filtering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find Etsy category IDs from a synced LinkFox category library before filtering product or shop searches. The skill can also guide users through LinkFox API-key setup, authentication recovery, or billing steps when access fails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts LinkFox services and uses a LinkFox API key.

Mitigation: Install only when LinkFox service access is acceptable, keep API keys private, and avoid endpoint override environment variables unless you control the target endpoint.

Risk: Authentication recovery can involve phone-based login, SMS codes, generated API keys, and payment-order flows.

Mitigation: Review onboarding actions before running them, treat SMS codes and returned API keys as sensitive, and confirm any selected plan and payment method before order creation.

Risk: Lookup, cache, and onboarding outputs may leave retained data in generated LinkFox session files.

Mitigation: Review generated LinkFox cache and session files for sensitive or unnecessary retained data before sharing or archiving the workspace.

## Reference(s):

- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-etsy-category-search)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lookup responses may be saved under LinkFox session data; large responses are summarized while full JSON is retained on disk.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Searches locally synchronized Temu category data by keyword and returns matching Chinese names, English names, and category IDs for product or shop filtering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators and developers use this skill to find Temu category IDs after category data has been synchronized locally, then pass those IDs into product, shop, or category-filtering workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a LinkFox-hosted workflow that requires an API key and may guide users through phone/SMS login.

Mitigation: Prefer the self-service API key path, avoid sharing SMS codes with an agent unless the publisher is trusted, and restart the session after environment changes.

Risk: The onboarding flow can create payment orders and display payment artifacts when resolving billing or quota issues.

Mitigation: Confirm the selected plan and payment method before order creation, avoid automatic payment polling, and review where response files and QR artifacts are stored.

## Reference(s):

- [Temu category search API reference](references/api.md)
- [Authentication and billing onboarding reference](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-category-search)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON responses and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large result sets may be summarized inline with the full JSON response saved to a local response file.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Guides agents in accessing Gumroad storefront data and managing products, sales, subscribers, licenses, and webhooks with user approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Storefront operators and developers use this skill to inspect Gumroad sales and subscribers, verify licenses, manage products, and set up approved webhook notifications or automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Gumroad grants Maton access to the authorized storefront and its data.

Mitigation: Get user approval before connecting, grant only needed access, and use secure credential storage.

Risk: Writes, webhooks, functions, triggers, or destinations can change storefront data or create ongoing data flows.

Mitigation: Review the exact action, handler, destination, and scope with the user before enabling or running automation.

## Reference(s):

- [Gumroad skill on ClawHub](https://clawhub.ai/byungkyu/skills/gumroad)
- [Maton](https://maton.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses may contain Gumroad storefront and customer data.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

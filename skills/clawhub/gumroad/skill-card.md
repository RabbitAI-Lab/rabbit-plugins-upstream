## Description:

Helps agents manage a connected Gumroad storefront, review sales and subscribers, verify licenses, and configure approved webhooks and automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Storefront owners and their agents use this skill to inspect Gumroad products, sales, and subscribers, verify licenses, and set up user-approved webhook notifications or automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to connected storefront data may expose sensitive business or customer information.

Mitigation: Prefer read-only, narrowly scoped access and return only the fields needed for the task.

Risk: Writes can change storefront records or create lasting webhooks and automation.

Mitigation: Confirm each write, target account, and persistent destination with the user before proceeding.

Risk: Raw API keys can be exposed when handled outside the login flow.

Mitigation: Use the CLI login flow when possible and avoid raw API keys unless the CLI cannot be used.

## Reference(s):

- [Gumroad skill release](https://clawhub.ai/byungkyu/skills/gumroad)
- [Gumroad API overview](https://gumroad.com/api)
- [Gumroad license keys help](https://help.gumroad.com/article/76-license-keys)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with command examples and selected API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the authorized Gumroad connection; writes and persistent automation require user approval.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

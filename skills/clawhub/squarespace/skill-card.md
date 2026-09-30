## Description:

Guides agents in managing Squarespace Commerce products, inventory, orders, customer profiles, and transactions through an authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Store operators and developers use this skill to inspect and, with explicit approval, update Squarespace Commerce data or configure related automations through their Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to live Squarespace commerce data may affect products, stock, orders, or customer records.

Mitigation: Start with read-only calls and confirm exact resource IDs, payloads, and effects before each write.

Risk: Exposing raw API keys or customer data could disclose sensitive information.

Mitigation: Prefer Maton login and credential storage; avoid printing or persisting keys and limit displayed customer data to what the task needs.

Risk: Triggers and destinations can continue running or forwarding events after setup.

Mitigation: Create them only for a specific approved workflow, and obtain separate approval for persistent event forwarding.

## Reference(s):

- [Squarespace skill on ClawHub](https://clawhub.ai/byungkyu/skills/squarespace)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Squarespace Commerce APIs overview](https://developers.squarespace.com/commerce-apis/overview)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command, API request, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and an authorized Maton connection.]

## Skill Version(s):

1.2.7 (source: ClawHub release metadata; skill frontmatter: 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

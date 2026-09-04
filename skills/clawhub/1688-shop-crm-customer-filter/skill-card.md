## Description:

Filters, sorts, paginates, and summarizes 1688 shop CRM customers by tags, purchase behavior, activity, purchase intent, and custom attributes, and can inspect or add custom customer fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1688aiinfra](https://clawhub.ai/user/1688aiinfra)

### License/Terms of Use:

MIT-0

## Use Case:

External 1688 shop operators and CRM users use this skill to find, sort, and review customer segments by business criteria such as tags, payment history, activity, purchase intent, inquiry conversion status, and custom attributes. It also supports controlled customer attribute management when the user explicitly confirms a write action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a 1688 account credential and can read CRM customer data.

Mitigation: Install and run it only in environments approved for that 1688 account, and avoid exposing credentials or raw customer records in user-visible responses.

Risk: The skill can create custom customer attributes.

Mitigation: Require explicit user confirmation of the field key, label, type, and optional value before executing attribute creation.

Risk: The skill automatically reports command usage metadata and may read local OpenClaw configuration or .env values.

Mitigation: Deploy it only where that reporting and local configuration access are acceptable, and review environment variables and local config file permissions before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/1688aiinfra/skills/1688-shop-crm-customer-filter)
- [Customer List Capability](artifact/references/capabilities/customer_list.md)
- [Customer Attribute Field Configuration Capability](artifact/references/capabilities/customer_attr_field_config.md)
- [Customer Attribute Add Capability](artifact/references/capabilities/customer_attr_add.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON-backed CLI results and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and a configured 1688 account credential; customer queries can return paginated summaries or raw JSON when requested.]

## Skill Version(s):

0.47.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

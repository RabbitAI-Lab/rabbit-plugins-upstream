## Description:

Hire humans for physical-world tasks via RentAHuman.ai, including searching available humans, posting bounties, starting conversations, and coordinating real-world work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to find, contact, and hire humans for physical-world tasks such as errands, package pickup, event attendance, photography, QA, and taste testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can initiate real-world tasks, public bounties, messages, payments, webhooks, and account-management actions.

Mitigation: Require user confirmation before every public bounty, message, payment, webhook, or account-management action.

Risk: Task descriptions may expose sensitive personal details such as home addresses, package identifiers, IDs, or schedules.

Mitigation: Share only the minimum details needed for the task and avoid sensitive personal information unless strictly necessary.

Risk: The skill gives agents broad access when an API key is available.

Mitigation: Use only an API key the user is comfortable delegating and prefer the narrow helper-script workflow over the full referenced API surface.

## Reference(s):

- [RentAHuman Homepage](https://rentahuman.ai)
- [RentAHuman MCP API Reference](references/API.md)
- [ClawHub Skill Page](https://clawhub.ai/alexanderliteplo/skills/rentahuman)
- [ClawHub Publisher Profile](https://clawhub.ai/user/alexanderliteplo)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public search can use direct HTTPS requests; authenticated actions require RENTAHUMAN_API_KEY.]

## Skill Version(s):

1.22.0 (source: server release metadata and API reference)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

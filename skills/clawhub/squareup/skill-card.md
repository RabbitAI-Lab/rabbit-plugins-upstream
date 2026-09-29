## Description:

Guides agents in using a connected Square account to read and administer business and payment data through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to inspect and, with explicit approval, manage Square locations, payments, customers, orders, and related workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes or financial actions can change business and payment data in the wrong account or location.

Mitigation: Use the least-privileged Square account and OAuth scopes, verify the connection and exact resource, and obtain explicit approval for each write or financial action.

Risk: Unused connections or persistent automations can retain access or continue forwarding events.

Mitigation: Approve automation and destinations separately, review where event data goes, and remove unused connections, functions, triggers, and destinations.

## Reference(s):

- [Square skill release](https://clawhub.ai/byungkyu/skills/squareup)
- [Square API reference](https://developer.squareup.com/reference/square)
- [Maton documentation](https://docs.maton.ai)
- [Maton homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Systeme.io API integration with managed OAuth for managing contacts, contact tags, custom fields, tags, course enrollments, community memberships, and subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Systeme.io business data through Maton-managed authentication, including contact management, tag and custom-field updates, course enrollments, community memberships, subscriptions, and approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton-mediated access can affect Systeme.io customer data, billing or subscription state, paid-content access, and ongoing event forwarding.

Mitigation: Install only when Maton mediation is acceptable, and review every write, deletion, webhook, function, trigger, and destination before approving it.

Risk: The skill depends on network access and valid Maton authentication to reach the user's authorized Systeme.io connection.

Mitigation: Use the documented OAuth flow when possible, keep credentials out of logs and shared files, and limit actions to the connection and fields required for the task.

## Reference(s):

- [Systeme.io API Reference](https://developer.systeme.io/reference)
- [Systeme.io API Overview](https://developer.systeme.io/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/systeme)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in authenticated API calls through Maton when the user approves the relevant action.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

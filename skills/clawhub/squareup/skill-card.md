## Description:

Square API integration with managed OAuth for Square administration through Maton, defaulting to read and list calls while requiring explicit approval for writes, new connections, triggers, destinations, and hosted functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an authorized Square account through Maton, inspect and administer Square resources, and create approved hosted automations for documented Square workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive Square business or payment records may be read or modified through the connected account.

Mitigation: Install only for Square administration, use OAuth with the least-privileged Square account and scopes, default to read/list actions, and confirm each write with the exact endpoint, account, resource ID, and consequence.

Risk: An ambiguous or stale Maton connection could target the wrong Square account.

Mitigation: List active connections, verify the intended connection ID before each action, pass the specific connection when needed, and revoke unused connections promptly.

Risk: Hosted functions and triggers can continue running after setup and may act with the deploying Maton account's available connections.

Mitigation: Use hosted automation only when requested, require a user-authored or user-reviewed handler, get separate approval for deploys and invocations, prefer a dedicated Maton account with only the needed Square connection, and keep function network policy at DENY_ALL unless the user approves specific hosts.

Risk: Raw API responses and trigger payloads can expose customer, business, or payment data.

Mitigation: Return only the fields needed for the task, avoid logging or writing full payloads, and do not forward event data to third-party destinations without explicit user approval for the exact host and data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/squareup)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Square API Overview](https://developer.squareup.com/docs)
- [Square API Reference](https://developer.squareup.com/reference/square)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash, JSON, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and a valid Square connection; responses may contain business, customer, or payment data.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

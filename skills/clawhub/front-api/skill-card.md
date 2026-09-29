## Description:

Connects an agent to Front to manage customer conversations, messages, contacts, inboxes, and team workflows through a user's Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Customer-support teams and developers use this skill to read and manage Front conversations, messages, contacts, and shared workspace records. With separate approval, they can set up hosted functions and triggers for recurring actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Updates and messages can affect shared workspace records or external recipients.

Mitigation: Prefer read-only calls; confirm the target, payload, and effect before every write.

Risk: Triggers and destinations can continuously forward future events from connected services.

Mitigation: Require separate, specific approval for each trigger and destination; review sources, event scope, and destination before enabling.

Risk: A long-lived API key used without the CLI can be exposed through logs or local files.

Mitigation: Prefer CLI login; if raw HTTP is necessary, keep the key in a managed session secret and never print or persist it.

## Reference(s):

- [Front API Reference](https://dev.frontapp.com/reference/introduction)
- [Front API Authentication](https://dev.frontapp.com/docs/authentication)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with commands and API response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions are limited by the user's authorized connection; writes and automations require approval.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

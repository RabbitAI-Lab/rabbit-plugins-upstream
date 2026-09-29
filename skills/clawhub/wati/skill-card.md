## Description:

Helps agents use a connected WATI account to manage WhatsApp contacts and templates, send messages, and set up approved automations through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and agents with an authorized WATI connection use this skill to look up contacts and templates, send WhatsApp messages, and configure user-approved scheduled or event-driven workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sending messages or bulk templates reaches real WhatsApp recipients and cannot be recalled.

Mitigation: Confirm each write, the template and personalization, and the exact recipient list and count before sending.

Risk: Uploading a named file discloses its contents to the recipient.

Mitigation: Confirm the exact user-named file and recipient before upload.

Risk: An approved trigger destination can forward future event data continuously.

Mitigation: Require separate approval for the destination and review its URL and data scope before enabling it.

Risk: Long-lived API keys can be exposed to other processes.

Mitigation: Prefer device-flow login and secure credential storage instead of exporting an API key.

## Reference(s):

- [ClawHub WATI release](https://clawhub.ai/byungkyu/skills/wati)
- [WATI API documentation](https://docs.wati.io/reference/introduction)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions use the permissions of the user's connected account.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

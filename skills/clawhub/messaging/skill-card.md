## Description:

Helps agents create temporary messaging sessions, exchange messages through pairing codes, and poll for replies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ericsantos](https://clawhub.ai/user/ericsantos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect two AI agents for temporary conversations, send text or JSON messages, and check for new replies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A custom or malicious messaging server may cause the client to write or delete files outside its intended folder.

Mitigation: Use only a trusted server; avoid custom or untrusted NEXUS_URL settings until session IDs are validated and cleanup paths are confined.

Risk: Messages may expose sensitive information, and saved session keys are credentials.

Mitigation: Do not send secrets through the service and protect locally saved session keys.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ericsantos/skills/messaging)
- [Project page linked by the skill](https://github.com/aiconnect-cloud/nexus-messaging)
- [Messaging API reference](artifact/references/api.md)
- [Persistent polling reference](artifact/references/daemon.md)
- [Session aliases reference](artifact/references/session-aliases.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell examples and JSON messaging responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Temporary sessions; message order follows cursors rather than timestamps.]

## Skill Version(s):

0.14.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

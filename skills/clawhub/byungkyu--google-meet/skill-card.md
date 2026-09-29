## Description:

Helps agents use a connected Google Meet account to manage meeting spaces and retrieve conference records and participant information through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using Google Meet can ask an agent to create meeting spaces, review conference records, and retrieve participant details from an authorized account. With separate approval, they can also set up scheduled actions through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an account or making changes can grant access or alter meeting data.

Mitigation: Confirm the connection and each write with the user; use only the access needed for the task.

Risk: Hosted functions, triggers, and destinations can persist and forward sensitive meeting or event data.

Mitigation: Review their scope and destination with the user before approval, and avoid forwarding data to unapproved hosts.

Risk: Using a raw API key can expose a long-lived credential.

Mitigation: Prefer the managed login; if raw access is necessary, keep the key secret and never print or store it in logs or files.

## Reference(s):

- [Google Meet API documentation](https://developers.google.com/meet/api/reference/rest)
- [Maton documentation](https://docs.maton.ai)
- [Maton homepage](https://maton.ai)
- [Google Meet skill on ClawHub](https://clawhub.ai/byungkyu/skills/google-meet)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include meeting or participant information from the authorized connection.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Give AI agents persistent semantic memory using the BlueColumn API for storing, recalling, and searching selected notes, conversations, documents, and audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect an agent to BlueColumn persistent memory, store selected text, documents, or audio, and recall previously stored context through API-backed queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist selected content to an external memory service, including conversations, documents, audio, credentials, regulated data, or third-party private information if the user permits it.

Mitigation: Use the platform secret store for the BlueColumn API key, avoid plaintext key storage when possible, and only store content the user deliberately wants retained and searchable later.

## Reference(s):

- [BlueColumn API Reference](references/api.md)
- [BlueColumn](https://bluecolumn.ai)
- [ClawHub Skill Page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/bluecolumn-memory)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include endpoint selection guidance, API payload examples, and reminders to use a platform secret store for the BlueColumn API key.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

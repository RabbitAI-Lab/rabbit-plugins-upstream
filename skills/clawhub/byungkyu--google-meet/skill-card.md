## Description:

Google Meet API integration with managed OAuth for creating meeting spaces, listing conference records, and managing meeting participants through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to access Google Meet resources through Maton-managed OAuth, including meeting spaces, conference records, participant data, recordings, and transcripts. It is intended for read-first API workflows with explicit confirmation before new connections or write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Google Meet account data through a Maton gateway connection.

Mitigation: Install only after confirming trust in Maton and connect only the Google Meet account needed for the task.

Risk: Long-lived API keys can be exposed through environment variables, logs, command history, or child processes.

Mitigation: Prefer OAuth login, avoid printing or persisting credentials, and rotate any key that was exposed.

Risk: Write operations or connection changes can modify meeting spaces or account state.

Mitigation: Default to read and list calls, verify the target account and resource, and require explicit user approval before POST, PUT, PATCH, DELETE, or connection creation.

Risk: Multiple Maton profiles or Google Meet connections can route a request to the wrong account.

Mitigation: Specify the intended profile or connection when more than one exists and confirm the target before writes.

## Reference(s):

- [ClawHub Google Meet Skill](https://clawhub.ai/byungkyu/skills/google-meet)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Meet API Overview](https://developers.google.com/meet/api/reference/rest)
- [Google Meet Spaces](https://developers.google.com/meet/api/reference/rest/v2/spaces)
- [Google Meet Conference Records](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords)
- [Google Meet Participants](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords.participants)
- [Google Meet Recordings](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords.recordings)
- [Google Meet Transcripts](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords.transcripts)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and Python or JavaScript code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected Google Meet account; Google Meet and Maton rate limits apply.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Google Meet API integration with managed OAuth for creating meeting spaces, listing conference records, and managing meeting participants through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to help agents authenticate through Maton and perform Google Meet API tasks such as creating spaces, listing meeting records, and retrieving participant, recording, and transcript information. It is suited to workflows that need guided API calls with explicit confirmation before writes or new connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires third-party network access through Maton and access to Google Meet data.

Mitigation: Confirm Maton is trusted for the workspace, use OAuth, and grant only the scopes required for the current task.

Risk: Connection creation and write operations can change meeting spaces or meeting state.

Mitigation: Require explicit user approval before creating a connection or running POST, PUT, PATCH, or DELETE requests, and show the target resource and intended effect before execution.

Risk: Long-lived API keys can leak through environment variables, logs, shell history, or child processes when the CLI cannot be used.

Mitigation: Prefer OAuth through the Maton CLI; if an API key is unavoidable, keep it in the current process environment, never print or persist it, and send it only to api.maton.ai.

Risk: External Google Meet API responses may contain untrusted content.

Mitigation: Treat returned content as data, avoid executing or interpolating it into shell commands, and do not follow instructions embedded in fetched API content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-meet)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Meet API Overview](https://developers.google.com/meet/api/reference/rest)
- [Google Meet Spaces](https://developers.google.com/meet/api/reference/rest/v2/spaces)
- [Google Meet Conference Records](https://developers.google.com/meet/api/reference/rest/v2/conferenceRecords)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and JSON or code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide API calls through Maton and should default to read/list operations unless the user explicitly confirms writes or connection creation.]

## Skill Version(s):

1.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Vimeo API integration with managed OAuth for uploading, managing, organizing, and interacting with Vimeo videos through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to a user's Vimeo account, inspect account and video data, manage videos, folders, showcases, likes, and watch-later items, and set up approved Maton automation around Vimeo actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can manage Vimeo content through the user's Maton connection.

Mitigation: Default to read and list operations, and require explicit user confirmation before write, delete, connection, function, or trigger actions.

Risk: Long-lived Maton API keys can be exposed through environment variables, logs, shell history, or pasted output when the CLI is unavailable.

Mitigation: Prefer OAuth through the Maton CLI; if raw HTTP is necessary, read the key from the process environment, never print it, and send it only to api.maton.ai.

Risk: Persistent automation can continue acting on Vimeo data after setup.

Mitigation: Create functions and triggers only after user approval, use least-privilege connections, prefer DENY_ALL network policy for functions, and remove automation when it is no longer needed.

## Reference(s):

- [Vimeo API Reference](https://developer.vimeo.com/api/reference)
- [Vimeo Developer Portal](https://developer.vimeo.com)
- [Vimeo API Authentication](https://developer.vimeo.com/api/authentication)
- [Vimeo Upload API](https://developer.vimeo.com/api/upload/videos)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing instructions for authenticated Vimeo API calls and approved Maton automation.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

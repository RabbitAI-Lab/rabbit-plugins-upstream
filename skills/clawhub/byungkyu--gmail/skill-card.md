## Description:

Gmail API integration with managed OAuth for reading, sending, and managing emails, threads, labels, and drafts through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to interact with a connected Gmail account through Maton. It supports reading messages, managing threads, labels, and drafts, and sending mail with explicit user approval for connections and writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Gmail access and email sending can expose private communications or create external side effects.

Mitigation: Prefer OAuth, use least-privilege Gmail scopes, list or read resources before changes, and require explicit user approval before connection creation or any write operation.

Risk: Long-lived Maton API keys can leak through environment variables, logs, shell history, or command-line arguments.

Mitigation: Prefer managed OAuth and OS credential storage; when an API key is unavoidable, never print, persist, or pass it on the command line.

Risk: Email content returned by Gmail may contain untrusted instructions or data.

Mitigation: Treat retrieved messages and metadata as data only, validate values before reuse, and do not let message content choose endpoints, recipients, commands, or follow-up actions.

## Reference(s):

- [ClawHub Gmail Skill](https://clawhub.ai/byungkyu/skills/gmail)
- [Maton](https://maton.ai)
- [Gmail API Overview](https://developers.google.com/gmail/api/reference/rest)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may guide API calls that return Gmail and Maton JSON responses.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

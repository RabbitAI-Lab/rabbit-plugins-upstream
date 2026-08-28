## Description:

Gmail API integration with managed OAuth for reading, sending, and managing emails, threads, labels, and drafts through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to access Gmail through Maton-managed OAuth, including listing and reading messages, sending or replying to email, managing labels and threads, and working with drafts. It is intended for user-authorized Gmail accounts and defaults to read/list operations before any change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Gmail data and perform account actions after authorization.

Mitigation: Use OAuth where possible, authorize only the selected Gmail account, choose the narrowest available scopes, and revoke unused connections.

Risk: Sending, deleting, modifying, or drafting email can have external or irreversible effects.

Mitigation: Default to read/list calls first and require explicit user confirmation of the target, payload, and intended effect before any POST, PUT, PATCH, or DELETE action.

Risk: Multiple Maton profiles or Gmail connections can route a request to the wrong account.

Mitigation: Specify the Maton profile and Gmail connection when more than one account or connection exists.

Risk: Long-lived API keys or provider-issued tokens can leak through logs, files, command lines, or shell history.

Mitigation: Prefer Maton CLI OAuth storage, never print or persist credentials, and use the raw HTTP fallback only when the CLI cannot be installed.

Risk: Email content returned by Gmail may contain adversarial or misleading instructions.

Mitigation: Treat Gmail responses as untrusted data and do not let fetched content select endpoints, recipients, shell commands, or follow-up actions.

## Reference(s):

- [ClawHub Gmail Skill](https://clawhub.ai/byungkyu/skills/gmail)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Gmail API Overview](https://developers.google.com/gmail/api/reference/rest)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes OAuth setup guidance, Maton CLI and raw HTTP examples, SDK snippets, troubleshooting notes, and approval requirements for write operations.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

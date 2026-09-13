## Description:

Dropbox API integration with managed OAuth for managing files and folders, searching content, retrieving metadata, and working with file revisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to authenticate through Maton and perform Dropbox file management, search, metadata, sharing, and revision workflows with explicit confirmation for account connections and write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dropbox authorization can expose files, folders, metadata, and sharing state available to the connected account.

Mitigation: Prefer OAuth, grant the narrowest Dropbox scopes possible, connect only the account needed for the task, and revoke unused connections.

Risk: Upload, delete, share, move, copy, restore, tag, and folder-creation actions can modify or expose user data.

Mitigation: Confirm the exact target resource, payload, and intended effect before every write, delete, share, or automation step.

Risk: Raw HTTP fallback with a Maton API key can increase credential exposure if the key is exported broadly or logged.

Mitigation: Use OAuth and the credential store when possible; if a raw API key is unavoidable, keep it confined to the current environment and never print or persist it.

Risk: Hosted functions and trigger destinations can turn Dropbox actions or event delivery into persistent automation.

Mitigation: Use hosted automation only after explicit user approval, keep destinations on approved Maton-controlled URLs unless the user approves a named third-party host and data flow, and remove automation when it is no longer needed.

## Reference(s):

- [ClawHub Dropbox Skill](https://clawhub.ai/byungkyu/skills/dropbox-api)
- [Maton](https://maton.ai)
- [Dropbox HTTP API Overview](https://www.dropbox.com/developers/documentation/http/overview)
- [Dropbox Developer Portal](https://www.dropbox.com/developers)
- [Dropbox API Explorer](https://dropbox.github.io/dropbox-api-v2-explorer/)
- [DBX File Access Guide](https://developers.dropbox.com/dbx-file-access-guide)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and Dropbox authorization; defaults to read and list actions and requires explicit user confirmation for connection creation, writes, deletion, sharing, hosted functions, and trigger automation.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

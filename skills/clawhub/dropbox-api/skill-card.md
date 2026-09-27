## Description:

Dropbox API integration with managed OAuth for managing files and folders, searching content, retrieving metadata, and working with file revisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to access Dropbox through a Maton-managed OAuth connection for file listing, search, metadata, upload, download, revisions, tags, and approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help an agent access or modify Dropbox content through the user's Maton-connected account.

Mitigation: Confirm the exact account, connection, path, payload, and intended effect before creating OAuth connections or running file write, delete, upload, restore, move, copy, tag, hosted function, trigger, or destination actions.

Risk: API keys, OAuth sessions, hosted functions, triggers, and persistent destinations can create durable access or data-flow paths.

Mitigation: Prefer OAuth through the Maton CLI, avoid exposing MATON_API_KEY, use least-privilege Dropbox scopes, require separate approval for automations and destinations, and remove stale connections, functions, triggers, or destinations when they are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/dropbox-api)
- [Maton Homepage](https://maton.ai)
- [Dropbox HTTP API Overview](https://www.dropbox.com/developers/documentation/http/overview)
- [Dropbox Developer Portal](https://www.dropbox.com/developers)
- [Dropbox API Explorer](https://dropbox.github.io/dropbox-api-v2-explorer/)
- [DBX File Access Guide](https://developers.dropbox.com/dbx-file-access-guide)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Catalog](references/calendly/triggers.md)
- [GitHub Trigger Catalog](references/github/triggers.md)
- [Google Mail Trigger Catalog](references/google-mail/triggers.md)
- [HubSpot Trigger Catalog](references/hubspot/triggers.md)
- [Linear Trigger Catalog](references/linear/triggers.md)
- [Notion Trigger Catalog](references/notion/triggers.md)
- [Slack Trigger Catalog](references/slack/triggers.md)
- [Stripe Trigger Catalog](references/stripe/triggers.md)
- [Time Trigger Catalog](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown with inline shell, JSON, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Dropbox paths, request payloads, connection identifiers, automation setup steps, and user-approval checkpoints.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

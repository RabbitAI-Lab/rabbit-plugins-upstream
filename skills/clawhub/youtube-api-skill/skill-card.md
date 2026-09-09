## Description:

YouTube Data API integration with managed OAuth for searching videos, managing playlists, accessing channel data, and interacting with comments through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to access YouTube Data API workflows from an agent, including video search, channel and playlist inspection, playlist management, subscriptions, and comment operations. The skill is suited for tasks that need managed OAuth through Maton and human approval before account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access a connected YouTube account through Maton.

Mitigation: Prefer OAuth, connect only the needed YouTube account and scopes, and revoke unused connections.

Risk: Playlist, comment, subscription, and rating operations can modify account state or public content.

Mitigation: Default to read and list calls first, then confirm the target resource, payload, and intended effect before any write operation.

Risk: The raw API-key fallback exposes a long-lived Maton credential if used carelessly.

Mitigation: Avoid the raw API-key path unless the CLI cannot be used; never print, log, persist, or send the key outside api.maton.ai.

## Reference(s):

- [ClawHub YouTube Skill Page](https://clawhub.ai/byungkyu/skills/youtube-api-skill)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [YouTube Data API Overview](https://developers.google.com/youtube/v3)
- [YouTube Data API Quota Calculator](https://developers.google.com/youtube/v3/determine_quota_cost)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration, Code]

**Output Format:** [Markdown with inline shell commands, API paths, JSON examples, and optional code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected YouTube account; API calls can return JSON.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

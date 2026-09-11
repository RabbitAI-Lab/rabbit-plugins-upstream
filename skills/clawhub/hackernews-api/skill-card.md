## Description:

Read-only Hacker News API for monitoring stories, searching discussions, and looking up public items and users through ReplyNodes prepaid credits with one long-lived Bearer fetcher key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch public Hacker News stories, items, users, and discussion search results through the ReplyNodes gateway. It is suited for read-only monitoring and lookup workflows that can use prepaid ReplyNodes credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send Hacker News item IDs, user handles, or search queries to ReplyNodes and consume prepaid credits.

Mitigation: Use the skill only for intended public Hacker News lookups and monitor prepaid credit usage.

Risk: The ReplyNodes API key could be exposed if pasted into chats, URLs, logs, or source files.

Mitigation: Store the key in the agent secret store and send it only as an Authorization Bearer header.

## Reference(s):

- [Operations reference](references/operations.json)
- [ReplyNodes developer console](https://app.replynodes.com/developers)
- [ReplyNodes API gateway](https://api.replynodes.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with API request guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves the gateway response envelope and request ID when reporting results.]

## Skill Version(s):

2.0.1 (source: frontmatter, manifest, server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Read Remind classes, chats, messages, and notification settings from a shell by capturing a signed-in browser session with fpx and querying Remind's GraphQL API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically inclined Remind users use this skill to inspect account, class, chat, message, and notification data from shell scripts without running the Remind MCP server. The skill is read-oriented, with mutation examples separated for deliberate account changes only.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reusable logged-in Remind session is stored locally and can expose account data if copied, logged, or shared.

Mitigation: Keep ~/.remind-fpx-session.json private, restrict file permissions, avoid pasting it into chats or logs, and delete or refresh it when it is no longer needed.

Risk: Mutation examples can change notification settings or send messages; writes can affect real recipients and cannot be unsent.

Mitigation: Use read queries by default, run mutation examples only when an account owner explicitly intends the change, check permissions such as canSend first, and re-read state after notification changes.

## Reference(s):

- [Remind GraphQL ready-to-run documents](references/graphql-queries.md)
- [Remind GraphQL endpoint](https://www.remind.com/graphql)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and GraphQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a locally captured Remind browser session and curl-compatible GraphQL requests.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps agents read Remind classes, chats, messages, and notification settings using a captured signed-in session and shell-based queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Remind users and developers can use this skill to retrieve their account's classes, conversations, messages, and notification settings from a shell without running the remind-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A saved Remind session grants access to a signed-in account if exposed.

Mitigation: Keep the session file private, do not sync or share it, and delete it when finished.

Risk: The included mutation examples can change notification settings or send messages from a live account.

Mitigation: Avoid mutation examples unless you intentionally want to make those changes or send messages.

## Reference(s):

- [Remind GraphQL query examples](artifact/references/graphql-queries.md)
- [ContextMint Bridge releases (browser extension)](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell and GraphQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account data is returned by Remind when the suggested commands are run.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Read Remind classes, chats, messages, and notification settings from a shell by capturing a signed-in browser session with fpx and querying Remind's GraphQL API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to inspect Remind account, class, chat, message, and notification data from command-line workflows without running the remind-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent captured Remind session credentials could expose sensitive student, family, classroom, or administrative communications if mishandled.

Mitigation: Use a least-privileged Remind account where possible, restrict permissions on the session file, and delete the captured session when it is no longer needed.

Risk: Write-capable GraphQL examples can change notification settings or send messages even though the skill is framed as read-oriented.

Mitigation: Avoid mutation examples unless the change is intentional, confirm account permissions first, and do not run message-sending examples against real recipients unless delivery is intended.

## Reference(s):

- [Ready-to-run Remind GraphQL documents](references/graphql-queries.md)
- [Remind GraphQL endpoint](https://www.remind.com/graphql)
- [Remind web app](https://www.remind.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, GraphQL, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential-capture setup, reusable curl call patterns, GraphQL query examples, and safety notes for read-oriented use.]

## Skill Version(s):

0.4.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

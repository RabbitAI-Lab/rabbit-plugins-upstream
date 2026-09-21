## Description:

Read Remind classes, chats, messages, and notification settings from a shell by capturing a signed-in browser session once and querying Remind's GraphQL API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to inspect Remind account data, including classes, chats, messages, and notification settings, through shell commands without running the remind-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores live Remind session credentials in a local file, so anyone or any process that can read that file may be able to act as the signed-in user until the session expires.

Mitigation: Keep the session file private, use restrictive file permissions such as 600, refresh or remove the file when access is no longer needed, and review the skill before installing if read-only behavior is required.

Risk: The references include mutation examples that can change notification settings or send messages from the live Remind account.

Mitigation: Use the read-oriented queries by default, check account permissions before any write, and run mutation examples only when intentionally changing settings or sending messages.

Risk: Writes to Remind can reach real recipients and cannot be unsent.

Mitigation: Review any generated mutation payload and recipient identifiers before execution, and avoid message-sending mutations unless the user explicitly requests that action.

## Reference(s):

- [Remind GraphQL endpoint](https://www.remind.com/graphql)
- [Remind web app](https://www.remind.com/)
- [Remind GraphQL ready-to-run documents](references/graphql-queries.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/remind-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline bash and GraphQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command patterns and query examples for local execution against a signed-in Remind account.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

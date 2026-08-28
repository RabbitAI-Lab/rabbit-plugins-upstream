## Description:

Read Remind classes, chats, messages, and notification settings from a shell by capturing a signed-in browser session once and querying Remind's GraphQL API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Remind account, class, chat, message, and notification data from scripts or one-shot shell commands without running the separate MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill captures and stores signed-in Remind session cookies that can expose any Remind data reachable by that session.

Mitigation: Keep the session file private, restrict file permissions, refresh only when needed, and install the skill only when the agent is allowed to access that account's Remind data.

Risk: The references include write-capable GraphQL mutation examples that can change account settings or send messages to real people.

Mitigation: Use the skill for read-oriented workflows by default, check account permissions before any action, and run mutation examples only after explicitly confirming the intended account change or message.

Risk: Remind may return HTTP 200 for unauthorized or failed GraphQL requests, which can make a failed or expired session look successful.

Mitigation: Inspect response bodies for GraphQL errors and rerun the session capture when authorization errors appear.

## Reference(s):

- [Remind GraphQL ready-to-run documents](references/graphql-queries.md)
- [Remind GraphQL endpoint](https://www.remind.com/graphql)
- [Remind web app](https://www.remind.com/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline bash, GraphQL, curl, node, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for local shell execution; query results depend on the user's signed-in Remind account permissions.]

## Skill Version(s):

0.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

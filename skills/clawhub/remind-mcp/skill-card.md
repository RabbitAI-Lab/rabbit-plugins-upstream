## Description:

Read Remind classes, chats, messages, and notification settings from a shell by capturing a signed-in browser session and querying Remind's GraphQL API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access Remind account data from shell workflows, scripts, or one-shot agent sessions without running the remind-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill captures reusable Remind cookie and CSRF headers that can grant account access from shell commands.

Mitigation: Store the session file with restrictive permissions, avoid administrator-level npm installs, and delete or rotate the session file when finished.

Risk: Reference mutations can change notification settings or send messages to real recipients.

Mitigation: Treat the skill as read-oriented and run mutation examples only after explicit user approval, permission checks, and confirmation that the account action is intended.

Risk: Remind may return HTTP 200 for unauthorized or invalid GraphQL operations, which can make a failed request look successful.

Mitigation: Inspect the response body for errors and re-run session capture or schema introspection before relying on query results.

## Reference(s):

- [Remind GraphQL Query Examples](references/graphql-queries.md)
- [Remind GraphQL endpoint](https://www.remind.com/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/remind-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, GraphQL queries, and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may guide creation of a local session file containing captured Remind request headers.]

## Skill Version(s):

0.4.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

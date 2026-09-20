## Description:

Read Remind classes, chats, messages, and notification settings from a shell by capturing an authorized web session with fpx and querying Remind's GraphQL API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators with authorized Remind accounts use this skill to inspect classes, chats, message history, and notification settings from shell workflows without running the remind-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The captured session file can provide reusable access to a Remind account.

Mitigation: Use only an account you are authorized to access, store the session file with restrictive permissions, and delete or rotate it when finished.

Risk: The artifact includes write-capable GraphQL mutation examples despite being read-oriented.

Mitigation: Avoid mutation examples unless you explicitly intend to change account settings or send real messages, and check account permissions before attempting writes.

Risk: Remind data can include private classes, chats, messages, account details, and notification settings.

Mitigation: Limit queries and shared outputs to the minimum data needed for the task and follow the account owner's authorization boundaries.

## Reference(s):

- [Remind GraphQL ready-to-run documents](references/graphql-queries.md)
- [Remind web application](https://www.remind.com/)
- [Remind GraphQL endpoint](https://www.remind.com/graphql)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline bash, curl, jq, and GraphQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes read-oriented query recipes and clearly marked mutation examples.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

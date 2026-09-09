## Description:

Read Remind classes, chats, messages, and notification settings from a shell by capturing a signed-in browser session and querying Remind's GraphQL API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Remind account data, classes, chats, messages, notification settings, and GraphQL schema details from shell workflows. It is intended for authenticated Remind users who need scripted or one-shot access without running the remind-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill captures reusable Remind session credentials that can read private messages and account data.

Mitigation: Keep the captured session file private, restrict file permissions, and delete or refresh the session when access is no longer needed.

Risk: Mutation examples can change account settings or send content to real recipients.

Mitigation: Do not run mutation examples unless the user explicitly intends the account change or message delivery, and check permissions before attempting writes.

Risk: Remind authorization errors may appear inside HTTP 200 responses, which can mislead automation.

Mitigation: Inspect GraphQL response bodies for errors and re-capture the session when the response indicates unauthorized access.

## Reference(s):

- [Remind GraphQL ready-to-run documents](references/graphql-queries.md)
- [Remind GraphQL endpoint](https://www.remind.com/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/remind-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with inline bash, GraphQL, curl, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that read private Remind data or perform account mutations when the user intentionally runs mutation examples.]

## Skill Version(s):

0.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

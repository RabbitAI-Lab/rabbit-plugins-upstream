## Description:

Read Remind classes, chats, messages, and notification settings from a shell by capturing a signed-in browser session with fpx and querying Remind's GraphQL API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Remind account data from shell scripts or one-shot commands without running the remind-mcp server. It is best suited for read-oriented GraphQL queries against an authenticated Remind session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill captures cookie and CSRF headers from a live Remind browser session, so the saved session file can grant account access.

Mitigation: Treat the session file like a password, keep it private, restrict file permissions, and avoid exposing it in logs or shared shells.

Risk: The reference material includes live mutation examples that can change notification settings or send real messages.

Mitigation: Use the skill for read-oriented queries by default, and run mutations only after confirming the target account, permissions, and intended effect.

Risk: Remind may return HTTP 200 for unauthorized requests, and field mistakes can appear as GraphQL validation failures.

Mitigation: Inspect the JSON response body for errors, check account permissions before acting, and use schema introspection before editing field selections.

## Reference(s):

- [Remind GraphQL query reference](artifact/references/graphql-queries.md)
- [Remind GraphQL endpoint](https://www.remind.com/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/remind-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API Calls]

**Output Format:** [Markdown guidance with bash, GraphQL, curl, jq, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented examples with cautionary mutation examples for intentional account changes.]

## Skill Version(s):

0.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Access Remind classes, chats, messages, and notification settings from a shell using an authenticated Remind session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Remind account holders can use shell commands to review classes, conversations, messages, and notification settings. Optional mutations should be used only when the account permits them and the intended recipients, message content, or setting changes are explicitly authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The saved session can expose private Remind data and may allow permitted account actions.

Mitigation: Protect the session file, approve only the intended Remind scope, explicitly authorize recipients, message content, or setting changes before mutation examples, and delete the captured file and invalidate the Remind session when access is no longer needed.

## Reference(s):

- [GraphQL query examples](artifact/references/graphql-queries.md)
- [Remind GraphQL API](https://www.remind.com/graphql)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Guidance]

**Output Format:** [Markdown with shell commands and GraphQL query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return account data as JSON for display or further processing.]

## Skill Version(s):

1.2.8 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

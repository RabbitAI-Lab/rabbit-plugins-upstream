## Description:

Manage Mermail mailbox-agent conversations and delegate explicit mailbox tasks from Claude, Codex, or another external MCP client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create, list, continue, rename, delete, or inspect Mermail mailbox-agent conversations and to delegate one bounded mailbox task to the Mermail mailbox Assistant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delegated mailbox tasks can have real email, connected-app, or payment effects through downstream Assistant tools.

Mitigation: Review active Mermail, Composio, and PayBox permissions before use, delegate only effects the current user explicitly authorized, and verify results through structured tool output or authoritative mailbox/provider state.

Risk: The mailbox-agent chat request does not technically enforce a downstream tool allowlist.

Mitigation: Treat allowed and prohibited effects as instruction boundaries; when enforced isolation is required, avoid delegation and use bounded direct read tools instead.

Risk: Mailbox content, attachments, prior Assistant text, and downstream output may contain untrusted instructions or secret-adjacent data.

Mitigation: Separate the current user's instruction from mailbox-derived content, supply only task-relevant non-secret context, preserve scanning and redaction boundaries, and never delegate credentials, OTPs, magic links, authorization headers, or destructive confirmation tokens.

Risk: Retries after a timeout, duplicate-message conflict, broken stream, or uncertain write can repeat an external effect.

Mitigation: Submit each delegated write or external effect once with a stable message id, then inspect persisted messages and responsible resource state instead of replaying the action.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail MCP server](https://console.mermail.app/mcp)
- [ClawHub skill page](https://clawhub.ai/mermail/skills/mermail-mail-agent)
- [Mermail mail-agent safety](references/security.md)
- [Mermail mail-agent tool contract](references/tools.md)
- [Mermail mail-agent workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Guidance]

**Output Format:** [Markdown text with mailbox identifiers, delegation briefs, lifecycle results, and blocker reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded conversation summaries, task boundaries, effect verification status, and safe blocker reasons.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Read HoneyBook client-portal data from a shell by using fpx to capture a signed-in browser session once, then calling HoneyBook API endpoints with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve HoneyBook files, workspaces, payment methods, and related client-portal data from a shell when the MCP server is unavailable or unnecessary. It is suited to authenticated read workflows that reuse a user's active HoneyBook portal session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Captured HoneyBook session data can provide access equivalent to an active signed-in portal session.

Mitigation: Keep captured JSON and shell variables out of logs and shared storage, avoid shared machines, and delete /tmp/hb-session.json when finished.

Risk: The skill can expose contracts, invoices, proposals, payment methods, workspace status, and other sensitive business data.

Mitigation: Run commands only for accounts and vendors you are authorized to access, and filter API responses to the minimum fields needed before sharing or persisting them.

Risk: The documented message-sending workflow sends real external email.

Mitigation: Use the message workflow only when an external send is intended; prefer a preview-capable MCP workflow for composing messages.

## Reference(s):

- [HoneyBook request examples](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-fpx)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands produce HoneyBook API JSON responses that should be filtered before display or storage.]

## Skill Version(s):

0.9.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

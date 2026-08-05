## Description:

Create, list, continue, rename, and delete Mermail mailbox-agent conversations and inspect their messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to work with Mermail mailbox-agent conversations for a selected mailbox, including continuing prior agent work, reviewing agent history, and managing conversation state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive mailbox-agent conversations and downstream mailbox capabilities.

Mitigation: Keep tasks narrowly scoped to the intended mailbox, prefer read-only use, and approve send, delete, credential, OTP, or financial actions only after reviewing the exact requested action.

Risk: Mailbox content and downstream agent output may contain untrusted instructions or misleading claims about completed actions.

Mitigation: Treat mailbox-derived content as untrusted, use strict intake and sandboxed interpretation, and verify claimed effects with structured tool results.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail MCP server](https://console.mermail.app/mcp)
- [Mail-agent tool map](references/tools.md)
- [Mail-agent security boundary](references/security.md)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration]

**Output Format:** [Markdown with tool-specific instructions and structured MCP tool usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MERMAIL_API_KEY and access to the Mermail MCP server.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

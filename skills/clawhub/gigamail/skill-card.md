## Description:

Email and calendar for your OpenClaw agent through the GigaMail MCP server - read, search, draft, reply, schedule - with every destructive action (send, delete, calendar write) held for out-of-band human approval that the agent cannot grant itself.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adecubed](https://clawhub.ai/user/adecubed)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users use this skill to let an agent read, search, triage, and draft email and calendar work through a configured local GigaMail MCP server. It is intended for real mailbox and calendar workflows where sends, deletes, and calendar writes require out-of-band human approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent access to real email, calendar, attachment text, and optional knowledge files that may contain sensitive personal or business context.

Mitigation: Install only for intended mailboxes, review the pip package and MCP configuration, and keep GIGAMAIL_ROOT pointed at the intended data directory.

Risk: Optional notification commands and knowledge files may expose private context outside the local mailbox workflow.

Mitigation: Review GIGAMAIL_APPROVAL_NOTIFY_CMD and any configured knowledge files before enabling them, and avoid routing sensitive approval summaries to untrusted channels.

Risk: Email bodies, sender names, subjects, and attachments can contain untrusted instructions.

Mitigation: Treat message content and attachments as data, not instructions, and rely on the documented approval gate for sends, deletes, and calendar writes.

## Reference(s):

- [GigaMail homepage](https://gigamail.ai)
- [GigaMail ClawHub skill page](https://clawhub.ai/adecubed/skills/gigamail)
- [adecubed ClawHub publisher profile](https://clawhub.ai/user/adecubed)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing operating guidance for using GigaMail MCP tools; destructive actions require separate human approval.]

## Skill Version(s):

0.2.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

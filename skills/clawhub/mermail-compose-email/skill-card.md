## Description:

Draft, revise, regenerate, send, reply to, forward, and schedule email through Mermail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to compose, revise, review, send, reply to, forward, or schedule Mermail messages while preserving recipients, thread context, approval boundaries, and delivery state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use MERMAIL_API_KEY-backed access to create drafts or approved email deliveries.

Mitigation: Confirm agent access to Mermail before installation and review exact recipients, body, attachments, and scheduled time before approving any send-like action.

Risk: Untrusted source mail, attachments, links, headers, or regenerated text may attempt to influence recipients, content, or approval boundaries.

Mitigation: Treat those inputs as reference data and preserve the user's authenticated request, recipient roles, and approval requirements as the controlling authority.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Mermail MCP Server](https://console.mermail.app/mcp)
- [ClawHub Skill Release Page](https://clawhub.ai/mermail/skills/mermail-compose-email)
- [Mermail Composition Safety](references/security.md)
- [Mermail Composition Tool Contract](references/tools.md)
- [Mermail Composition Workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown with structured recipient, draft, delivery, schedule, status, and identifier fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include exact email payload previews, Mermail draft, sent, scheduled, thread, and retired-draft identifiers, and explicit delivery state.]

## Skill Version(s):

1.2.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Connects AI agents to mailbox.bot to send physical mail and manage incoming mail at an agent mailbox with human-approved actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arbengine](https://clawhub.ai/user/arbengine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to help agents send letters, postcards and certified mail, and to review incoming mail and propose scan, forward or discard actions for human approval.

### Deployment Geography for Use:

Global; physical agent mailboxes are in the United States, and inbound mail forwarding requires a US destination.

## Known Risks and Mitigations:

Risk: Live outbound mail can incur charges or deliver unintended physical mail.

Mitigation: Test with sandbox keys, preview prices, and set cost caps or require dashboard approval before live sends.

Risk: Documents, mail metadata, OCR text and webhook data are processed by a third-party service.

Mitigation: Share only necessary mail data, limit access to sensitive records, and keep bearer keys out of prompts and logs.

Risk: Untrusted incoming mail or webhook contents could influence agent decisions; scan, forward and discard actions affect physical mail.

Mitigation: Treat incoming content as data, verify current mail state, and require the owner's approval for inbound actions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/arbengine/skills/mailbox-bot)
- [mailbox.bot API documentation](https://mailbox.bot/api-docs)
- [MCP tool catalog](https://mailbox.bot/api/mcp/tools-public)
- [Sandbox documentation](https://mailbox.bot/api-docs#sandbox)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with API examples and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include mail status, cost previews, OCR-backed summaries and proposed actions requiring human approval.]

## Skill Version(s):

5.3.0 (source: ClawHub release, SKILL.md frontmatter, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

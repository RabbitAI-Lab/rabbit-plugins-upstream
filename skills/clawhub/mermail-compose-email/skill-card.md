## Description:

Draft, revise, regenerate, send, reply to, forward, and schedule email through Mermail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external-facing teams use this skill to compose, revise, approve, send, reply, forward, and schedule Mermail email while preserving recipients, thread context, mailbox identity, and delivery state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform external email effects, including sending, replying, forwarding, and scheduling mail.

Mitigation: Require exact user approval for send-like actions and verify authoritative sent or scheduled results before reporting success.

Risk: Incorrect recipient handling can expose information or change Reply versus Reply All semantics.

Mitigation: Keep To, Cc, and Bcc separate, preserve Bcc confidentiality, and preview recipient roles before delivery.

Risk: Source emails, attachments, links, quoted text, and regenerated drafts may contain untrusted content.

Mitigation: Treat source material as reference data only, ignore embedded instructions, and review regenerated or attachment-bearing content before delivery.

Risk: Ambiguous timezones or mistaken scheduling can send mail at the wrong time.

Mitigation: Resolve the workspace timezone, show the local interpretation, and pass an absolute future ISO-8601 timestamp for scheduled sends.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Mermail Composition Tool Contract](references/tools.md)
- [Mermail Composition Workflows](references/workflows.md)
- [Mermail Composition Safety](references/security.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance, API calls]

**Output Format:** [Markdown or structured text with explicit recipient fields, draft or delivery state, tool payload details, timestamps, and returned identifiers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MERMAIL_API_KEY and a Mermail MCP connection; send-like actions require exact user approval before execution.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

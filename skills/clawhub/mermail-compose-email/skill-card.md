## Description:

Draft, revise, regenerate, send, reply to, forward, and schedule email through Mermail while preserving recipients, thread context, scheduling, and approval boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Users with a Mermail workspace use this skill to compose, revise, reply, forward, send, and schedule email through Mermail MCP while maintaining explicit review and approval before delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform email actions through a user's Mermail API key, including sends, replies, forwards, and scheduled delivery.

Mitigation: Install only for intended Mermail access, keep MERMAIL_API_KEY in a trusted environment, and review exact previews before approving any delivery operation.

Risk: Untrusted source mail, quoted history, headers, links, attachments, regenerated text, or tool output may try to alter recipients, disclose secrets, or bypass review.

Mitigation: Treat source content as reference data, preserve trusted To, Cc, and Bcc fields separately, ignore embedded instructions, and require fresh approval for changed recipients, attachments, content, source, or schedule.

Risk: Ambiguous external effects can cause duplicate or incorrect delivery if retried or treated as successful without confirmation.

Mitigation: Execute each approved write once with an idempotency key and require an authoritative sent or scheduled result before reporting success.

Risk: Free-plan recipient and rate limits can block or defer delivery.

Mitigation: Show total To+Cc+Bcc recipient units in previews, stop on recipient or rate-limit errors, surface Retry-After when provided, and do not split, drop, or reclassify recipients to evade limits.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail MCP endpoint](https://console.mermail.app/mcp)
- [Mermail composition safety](artifact/references/security.md)
- [Mermail composition tool contract](artifact/references/tools.md)
- [Mermail composition workflows](artifact/references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or structured text previews, with MCP API calls for approved draft, send, reply, forward, regeneration, and schedule operations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve To, Cc, and Bcc separately; show total recipient units; distinguish draft, regenerated_for_review, approved, sent, scheduled, rate_limited, deferred, validation_failed, and delivery_unknown states; and include authoritative identifiers when returned.]

## Skill Version(s):

1.2.4 (source: server release evidence, released 2026-08-14T06:36:17Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

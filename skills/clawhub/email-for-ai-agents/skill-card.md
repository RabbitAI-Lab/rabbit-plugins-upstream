## Description:

Guides agents through sending one human-approved email via Sendmux and reconciling uncertain outcomes without duplicate sends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

People using AI agents to send an individual status notification or delegated email can approve the exact message and use an authorized Sendmux connection to send it and check the outcome. Bulk and batch sends are outside this skill's scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent could send an unintended email without human approval of its recipients or content.

Mitigation: Require approval of the exact sender, recipients, subject, body and attachments before sending.

Risk: Overprivileged credentials or secrets shared in chat could expose sending access.

Mitigation: Use a least-privilege Sendmux connection or delegated token, never a root key, and keep secrets out of chat.

Risk: Retrying an uncertain send with a new key could send a duplicate message.

Mitigation: Reuse the same idempotency key and exact payload within the retry window; otherwise reconcile the original attempt before another send.

## Reference(s):

- [Sendmux skills homepage (listed in skill metadata)](https://github.com/Sendmux/skills)
- [Sendmux MCP integration](https://sendmux.ai/docs/ai-integrations/mcp)
- [Sendmux sending attachments](https://sendmux.ai/docs/sending/attachments)
- [Sendmux HTTP sending](https://sendmux.ai/docs/sending/http)
- [Sendmux idempotency](https://sendmux.ai/docs/sending/idempotency)
- [Sendmux delegated agent access](https://sendmux.ai/docs/ai-integrations/agent-access)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Markdown guidance with example JSON requests and shell commands; plain-text send status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single approved message per workflow; reports the returned status or an uncertain outcome.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter says 1.7.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

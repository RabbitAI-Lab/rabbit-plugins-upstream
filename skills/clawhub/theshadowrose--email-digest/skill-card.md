## Description:

Smart email categorizer and digest formatter for agents that turns already-fetched email objects into a prioritized daily brief with urgent, action-needed, and FYI sections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[theshadowrose](https://clawhub.ai/user/theshadowrose)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this skill to summarize email arrays fetched by their own connector, CLI, or pipeline into a concise daily digest. It helps agents prioritize messages, identify likely action items, and filter configured low-value senders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes email objects that may contain sensitive personal or business content.

Mitigation: Only pass email data that the agent is authorized to process, and keep connector and mailbox permissions scoped separately from this skill.

Risk: Email prioritization is keyword and sender based, so important messages may be misclassified or omitted from short FYI output.

Mitigation: Review the generated digest before relying on it for time-sensitive or high-impact decisions, and tune priority senders, urgency keywords, action keywords, and ignore senders for the mailbox.

Risk: Security evidence covers this package, not any separate email connector or pipeline used to fetch messages.

Mitigation: Review and scan the email connector, CLI, or platform integration independently before deployment.

## Reference(s):

- [Email Digest ClawHub Page](https://clawhub.ai/theshadowrose/skills/email-digest)
- [himalaya CLI](https://github.com/soywod/himalaya)
- [OpenClaw](https://github.com/openclaw/openclaw)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown digest text with JavaScript configuration and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes email objects with from, subject, body, or snippet fields; local processing only according to server security evidence.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

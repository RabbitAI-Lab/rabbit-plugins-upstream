## Description:

Guides an agent through bounded, read-only triage of an authorized Sendmux inbox and preparation of unsent reply drafts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw agents and their users can review a selected, authorized Sendmux mailbox, classify relevant messages, and prepare replies for human review without changing or sending mail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may read sensitive content from the selected mailbox.

Mitigation: Use read-only permissions, confirm the authorized mailbox, and limit reads to the requested scope.

Risk: An inaccurate or premature reply may be mistaken for approved outgoing mail.

Mitigation: Keep replies as unsent drafts and require human review before any separate sending task.

## Reference(s):

- [Sendmux skills homepage (publisher-listed)](https://github.com/Sendmux/skills)
- [Sendmux MCP connection guide](https://sendmux.ai/docs/ai-integrations/mcp)
- [Sendmux mailbox search and batch reads](https://sendmux.ai/docs/developer-tools/mailbox-api/search-and-batch)
- [Sendmux mailbox selection and capabilities](https://sendmux.ai/docs/developer-tools/mailbox-api/targeting-and-capabilities)

## Skill Output:

**Output Type(s):** [Analysis, Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Message IDs, classifications, evidence, scope and gaps, with unsent reply text when useful.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

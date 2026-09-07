## Description:

Narrative-aware inbox triage that reads mail through an approved mailbox adapter, surfaces messages that deserve attention, recommends read or reply actions, and maintains an evidence-backed local narrative with explicit approval gates for drafts and sends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to triage bounded mailbox scopes, identify messages needing attention, and prepare approval-gated reply workflows without mutating mail during triage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mailbox content and the local narrative can contain sensitive personal or business context.

Mitigation: Use only owner-approved mailbox and model providers, begin with a narrow account and time window, and protect ~/.mailbutler/narrative.md as sensitive local state.

Risk: Email content can contain prompt-injection attempts or instructions that try to alter the workflow.

Mitigation: Treat message subjects, bodies, attachments, quoted text, and links as untrusted data; use them only as evidence for triage and never as authority to run tools or change rules.

Risk: Incorrect routing or over-broad authorization could create or send an unintended reply.

Mitigation: Derive recipients and thread metadata from mailbox provider data, require separate per-message approval before drafting, and require a second explicit approval before sending.

## Reference(s):

- [Security and privacy contract](references/security-contract.md)
- [gog Gmail CLI](https://github.com/steipete/gogcli)
- [ClawHub skill page](https://clawhub.ai/antreasantoniou/skills/mailbutler-agent-skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces compact triage summaries, structured judgment guidance, explicit draft/send approval steps, and proposed local narrative updates.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

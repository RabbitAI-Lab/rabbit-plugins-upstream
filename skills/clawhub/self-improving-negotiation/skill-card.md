## Description:

Captures negotiation strategy failures, concession leaks, BATNA weakness, framing misses, objection handling gaps, escalation misalignment, anchor errors, and agreement quality risks for continuous improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to record negotiation learnings, issues, and feature requests so recurring bargaining patterns can be reviewed and promoted into reusable playbooks, objection libraries, concession guardrails, BATNA checklists, or deal review templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Negotiation notes may contain pricing strategy, BATNA details, customer-confidential terms, legal advice, approvals, or transcripts.

Mitigation: Keep .learnings local or access-controlled and redact sensitive negotiation, customer, legal, and approval details before logging.

Risk: Optional persistent hooks can surface negotiation reminders from prompt or Bash-output signals.

Mitigation: Review hook scope before enabling, prefer project-local hooks, and keep matchers narrow.

Risk: Manual clone installation can point users at a repository source outside server-resolved provenance.

Mitigation: Verify the repository source before using the manual clone path; server-resolved provenance for this release is unavailable.

## Reference(s):

- [Negotiation Entry Examples](references/examples.md)
- [Hook Setup Guide](references/hooks-setup.md)
- [OpenClaw Integration](references/openclaw-integration.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command snippets, configuration examples, and structured logging templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reminder-only guidance; optional hooks emit prompts and risk-signal reminders without approving concessions, committing pricing, or finalizing agreements.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

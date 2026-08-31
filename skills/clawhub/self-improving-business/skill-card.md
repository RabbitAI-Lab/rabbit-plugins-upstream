## Description:

Captures business administration issues, policy gaps, KPI misalignment, decision delays, handoff failures, and stakeholder misalignment to improve operational decision quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operations teams use this skill to capture structured local learnings, business issues, and feature requests for process governance, KPI alignment, SLA delays, budget variance, vendor handoffs, and policy drift. It supports reminder-only logging and recommendations while leaving approvals and high-impact business decisions with human owners.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional persistent hooks can create broad business-term reminders and PostToolUse can inspect command output transiently.

Mitigation: Enable hooks only in projects where automatic business reminders are useful, keep them project-scoped with narrow matchers, and avoid PostToolUse when command output may contain sensitive material.

Risk: Business findings or recommendations could be mistaken for approvals, commitments, payroll actions, legal actions, procurement commitments, or policy sign-offs.

Mitigation: Treat entries as documentation and reminders only; require explicit human approval for high-impact business decisions.

Risk: Local learning logs may capture sensitive operational context if users paste raw business data or command output.

Mitigation: Record concise summaries, source attribution, owners, and next actions instead of secrets, transcripts, or raw sensitive outputs.

## Reference(s):

- [Business Entry Examples](references/examples.md)
- [Business Hook Setup Guide](references/hooks-setup.md)
- [OpenClaw Business Integration](references/openclaw-integration.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, local Markdown log entries, shell commands, and optional hook configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reminder-only; may create or append local .learnings Markdown files and can scaffold business skill files when explicitly invoked.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

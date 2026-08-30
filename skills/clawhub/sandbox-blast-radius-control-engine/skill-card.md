## Description:

Provides OpenClaw agents with runtime safety guidance for classifying risk, limiting blast radius, applying least privilege, using isolation and dry-runs, backing up, rolling back, and verifying actions before they can cause wider system damage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill as a safety gate for medium, high, and critical actions. It helps agents scope target impact, require authorization, prefer isolation and dry-runs, verify actual state, and recover or stop safely when risk is unclear.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may intentionally pause risky work for previews, confirmations, backups, and verification.

Mitigation: Treat these pauses as intended safety gates, and plan time for explicit approval and post-action verification on medium, high, and critical tasks.

Risk: Audit, trace, or evaluation records could expose sensitive context if secrets are included.

Mitigation: Keep observability and evaluation integrations local or explicitly approved, and redact secrets from traces, logs, memory, and user-visible output.

Risk: A destructive, production, or irreversible task could be under-controlled if its risk or target scope is misclassified.

Mitigation: Require explicit risk and target classification, dry-run or preview where available, verified backups, and a written rollback plan for high and critical actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/sandbox-blast-radius-control-engine)
- [Publisher Profile](https://clawhub.ai/user/pmuhammadagus-byte)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown policy guidance with decision tables, checklists, and command recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance only; evidence reports no executable code or hidden install behavior.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

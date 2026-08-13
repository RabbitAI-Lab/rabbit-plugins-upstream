## Description:

Mandatory risk-driven verification workflow for maintained-code changes. Use when implementing, fixing, refactoring, deleting, migrating, or reviewing code to identify all materially affected behavior, map failure risks to sufficient tests, execute required evidence, and report unresolved test gaps and residual risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wujiaming88](https://clawhub.ai/user/wujiaming88)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to verify maintained-code changes with a risk-driven workflow that maps changed behavior to impact, test evidence, gaps, and residual risk. It is especially useful for implementation, refactoring, bug fixing, deletion, migration, and review tasks where the agent must report traceable verification evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification may involve longer-running, expensive, or side-effecting repository commands.

Mitigation: Review proposed commands before execution, prefer scoped evidence where sufficient, and require explicit handling for destructive or production-like test environments.

Risk: Local verification cannot reproduce every production browser, content, timing, scale, or environment condition.

Mitigation: Record omitted dimensions as residual uncertainty and use proportionate controls such as staged rollout, monitoring, and rollback when production diversity cannot be reproduced.

## Reference(s):

- [Change Test Evidence](references/evidence-report-template.md)
- [Frontend Change Verification](references/frontend-change-verification.md)
- [Change Impact and Risk Analysis](references/impact-analysis.md)
- [Scientific Test Method Selection](references/test-method-selection.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with traceability tables, command evidence, and residual-risk summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes eight gate statuses, change impact traceability, test portfolio traceability, executed evidence, unresolved test gaps, and residual risk.]

## Skill Version(s):

0.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

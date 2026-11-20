## Description:

处理已经推进的功能决定变更，以逐层验收、可恢复变更日志和独立关闭证据追平需求、设计、任务、代码与验证。支持分段继续及明确授权的撤销；普通遗漏沿原任务补齐。

This skill is ready for commercial/non-commercial use.

## Publisher:

[peterflow-zh](https://clawhub.ai/user/peterflow-zh)

### License/Terms of Use:

MIT

## Use Case:

Developers and product teams use this skill to bring project artifacts back into alignment after an approved feature decision changes, while tracking scope, validation evidence, and recovery information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Active-round restoration may overwrite or remove files without fresh confirmation.

Mitigation: Before installing or restoring, review the affected paths and saved prior state; restore only with explicit authorization, then verify the result against the baseline.

## Reference(s):

- [Assessment and authorization](references/assessment.md)
- [Stage gates](references/stage-gates.md)
- [Contract and recovery schema](references/contract-schema.md)
- [Closure evidence](references/closure-evidence.md)
- [ClawHub release](https://clawhub.ai/peterflow-zh/skills/feature-retcon)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Files, Code, Shell commands]

**Output Format:** [Markdown guidance and project files, with JSON evidence and shell or Python commands as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scope follows the authorized reconciliation round; may include a recoverable change log, closure evidence, and a recovery archive.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

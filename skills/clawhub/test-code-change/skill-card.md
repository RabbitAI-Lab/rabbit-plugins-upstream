## Description:

Risk-driven test design and verification for coding agents changing maintained code. Use when implementing, fixing, refactoring, deleting, migrating, or reviewing code to identify affected behavior, select sufficient scientific test methods, apply TDD where useful, execute affected regressions, evaluate changed-line and branch coverage, and report reproducible evidence and residual risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wujiaming88](https://clawhub.ai/user/wujiaming88)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to plan, execute, and report risk-driven verification for implementation, review, refactoring, migration, deletion, and bug-fix work. It helps map changed behavior to observable contracts, select targeted tests, run relevant checks, and communicate executed evidence and residual risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may inspect the active repository and run project test or build commands when relevant.

Mitigation: Review the proposed commands and repository context before deployment in sensitive environments.

Risk: Incorrect or overstated test evidence could mislead code review or release decisions.

Mitigation: The skill requires agents to distinguish executed command results from unexecuted recommendations and to record residual risk.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wujiaming88/skills/test-code-change)
- [Server-resolved GitHub provenance](https://github.com/wujiaming88/skills/tree/main/test-code-change)
- [Change Test Evidence](references/evidence-report-template.md)
- [Change Impact and Risk Analysis](references/impact-analysis.md)
- [Scientific Test Method Selection](references/test-method-selection.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Analysis]

**Output Format:** [Markdown with structured tables and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include test plans, executed command results, coverage observations, no-test rationales, and residual-risk notes.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

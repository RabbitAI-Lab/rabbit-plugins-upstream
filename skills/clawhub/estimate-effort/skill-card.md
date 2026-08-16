## Description:

Estimates development effort in hours from requirements and relevant project source code for frontend, backend, and full-stack work using a three-year developer baseline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlykan](https://clawhub.ai/user/wlykan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn feature, refactor, bug-fix, or integration requests into task-level hour estimates after inspecting relevant project code. It supports sprint planning and schedule discussions across frontend, backend, and full-stack work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect repository files to ground its effort estimates.

Mitigation: Use it only in repositories where relevant code context may be read, and keep the review scope limited to files needed for the estimate.

Risk: Effort estimates can be misleading when requirements, acceptance criteria, or code context are incomplete.

Mitigation: Clarify acceptance criteria, include test, documentation, and buffer time, and review assumptions before using the estimate for planning.

Risk: The baseline assumes a three-year developer and may not match every team's delivery speed.

Mitigation: Adjust complexity factors, technology multipliers, and buffers to local team experience and project constraints.

## Reference(s):

- [Complexity Factors](references/complexity-factors.md)
- [Tech Stack Baseline](references/tech-stack-baseline.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown effort-estimation report with tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes task breakdowns, hour estimates, buffer assumptions, risk and dependency notes, and optimization suggestions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Reviews Chinese-language requirement and PRD text across completeness, clarity, consistency, testability, and feasibility, returning scored findings and improvement guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, product teams, and agents use this skill to assess requirements before test design, identify unclear or untestable statements, and produce a structured review report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may encourage agents to perform requirement review before many test-related tasks.

Mitigation: Install and enable it only where a Chinese-language requirement-review workflow is desired, and scope activation to requirement or PRD review tasks.

Risk: The artifact recommends installing a broader QA skills package for the complete workflow.

Mitigation: Review the separately recommended QA skills package before installing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-requirement-review)
- [Requirement review report template](references/report-template.md)
- [Five-dimension review standards](references/review-standards.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown review report with scores, issue tables, and improvement recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses five review dimensions and P0/P1/P2 issue severity categories.]

## Skill Version(s):

1.7.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Judging Rubric Grader is a zero-dependency contest decision-support CLI that applies UIBC rubric weighting to scores and returns deterministic JSON IR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Contest organizers and reviewers use this skill to calculate weighted rubric scores, grade outcomes, pass/fail status, warnings, and review notes for UIBC-style judging workflows. Its results are decision support and require human review before any final contest decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated rubric scores could be mistaken for final contest adjudication.

Mitigation: Treat outputs as decision support only and require organizer or committee review before final decisions.

Risk: Rubric criteria, weights, or pass lines may not match the current contest rules.

Mitigation: Verify criteria, weights, scores, and pass_line against the current UIBC rules before relying on results.

Risk: Malformed or incomplete JSON inputs can produce errors or incomplete determinations.

Mitigation: Validate input JSON and inspect rc, errors, and warnings before using the result in a review workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/judging-rubric-grader)
- [LGD theory reference](https://medxpert.cn/theory)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [JSON IR]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes return codes, weighted per-dimension scoring, grade and pass status, warnings, notes, and AIGC metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

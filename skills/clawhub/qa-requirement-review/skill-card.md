## Description: <br>
Reviews requirement documents across completeness, clarity, consistency, testability, and feasibility before test design or implementation planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers, product reviewers, and developers use this skill to review PRDs or requirement descriptions before test case design. It produces a structured review that identifies missing, ambiguous, inconsistent, hard-to-test, or infeasible requirements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be invoked broadly before requirement-related test design, including when a user only wants execution support or bug triage. <br>
Mitigation: Invoke it when the task involves PRD or requirement quality review; skip it for execution-only or bug-triage requests. <br>
Risk: The skill can produce incorrect or incomplete requirement-review guidance if the source requirement description lacks context. <br>
Mitigation: Ask for missing business context, acceptance criteria, constraints, or historical defects before treating the review as final. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-requirement-review) <br>
- [Requirement review report template](references/report-template.md) <br>
- [Five-dimension review standards](references/review-standards.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, guidance] <br>
**Output Format:** [Markdown requirement review report with scored dimensions, issue lists, and improvement suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include traceability identifiers and classify issues by P0, P1, and P2 severity.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

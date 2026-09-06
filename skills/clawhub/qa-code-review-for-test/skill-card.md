## Description:

Helps QA reviewers analyze code diffs from a testing perspective, identify impacted areas and risk patterns, and recommend a minimal regression testing scope.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and test leads use this skill after code changes or pull requests to determine affected functionality, identify high-risk change patterns, and define focused regression testing. It is intended for testing impact analysis, not source-code modification or general code-quality review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad code-reading or code-review phrases.

Mitigation: Use it when the intended task is QA impact analysis or regression-scope planning, and confirm the review scope before relying on its recommendations.

Risk: The review output may miss dependency impacts or produce incomplete testing guidance.

Mitigation: Validate findings against the diff, affected dependencies, and developer context before changing test scope or acting on the recommendations.

Risk: The artifact recommends a separate full-suite npx install for the broader QA workflow.

Mitigation: Review and approve the additional skills in that suite before installing them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/qa-code-review-for-test)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report with tables and structured sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a CR identifier, a 9-column test case table, review findings, test gaps, impact analysis, high-risk patterns, and regression-scope recommendations.]

## Skill Version(s):

1.7.6 (source: server release metadata; artifact frontmatter lists 1.7.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

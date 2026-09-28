## Description:

Analyzes code changes from a testing perspective to identify affected areas, high-risk patterns, and a focused regression testing scope.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to review code diffs, identify change-related test gaps, and plan targeted regression testing rather than assess overall code quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad review requests can invoke testing-focused analysis when a full engineering code review is intended.

Mitigation: Specify whether the request calls for test-scope analysis or a full engineering review.

Risk: A mistaken impact assessment can omit dependencies or narrow regression coverage incorrectly.

Mitigation: Check affected callers and dependencies, disclose uncovered areas, and confirm the change scope and regression risks with developers before acting on recommendations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/kokxi/skills/qa-code-review-for-test)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown code-change impact analysis report with a nine-column test case table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes review findings, test gaps, high-risk patterns, regression scope, and a review ID; coverage claims must state their basis and identify uncovered modules.]

## Skill Version(s):

1.7.7 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

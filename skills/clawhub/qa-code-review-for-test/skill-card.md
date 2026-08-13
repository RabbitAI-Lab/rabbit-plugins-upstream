## Description:

Helps developers and QA engineers review code changes from a testing perspective, identify impact areas and high-risk patterns, and define a minimal regression test scope.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and test leads use this skill when a PR, diff, or described code change needs test-impact analysis. It focuses on changed files, affected interfaces, data or configuration changes, high-risk patterns, and practical regression scope recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads code changes and diffs to analyze test impact.

Mitigation: Use it only in workspaces where code and diff review for QA purposes is acceptable.

Risk: Broad trigger phrases may match ordinary developer conversations.

Mitigation: Invoke it explicitly for PR or diff test-impact analysis when that behavior is intended.

Risk: Test-impact recommendations may be incomplete or misleading if the provided diff or context omits dependencies.

Mitigation: Review the recommendations with developers and supplement with dependency or boundary analysis before relying on the regression scope.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown test-impact analysis report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs review findings, test gaps, impact analysis, high-risk patterns, and regression scope recommendations.]

## Skill Version(s):

1.6.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

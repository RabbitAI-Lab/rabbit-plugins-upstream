## Description:

Analyzes code changes from a testing perspective to identify affected areas, high-risk patterns, test gaps, and a minimal regression testing scope.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and test leads use this skill to review diffs or change descriptions, estimate test impact, identify risky change patterns, and plan focused regression coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may invoke the skill during ordinary code-review discussions or against unrelated repository content.

Mitigation: Limit use to intended diffs, change descriptions, requirements, and relevant test cases; keep sensitive repositories and unrelated files out of scope.

Risk: The impact analysis and regression recommendations may be incomplete or misleading if dependencies or change scope are missing.

Mitigation: Confirm the change scope and regression risk with developers before using the conclusions to guide testing or source changes.

## Reference(s):


## Skill Output:

**Output Type(s):** [analysis, markdown, guidance]

**Output Format:** [Markdown report with test case tables, review findings, test gaps, impact analysis, high-risk patterns, and regression scope recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a CR traceability identifier and risk-ranked test recommendations; no external provenance references are available for this release.]

## Skill Version(s):

1.7.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

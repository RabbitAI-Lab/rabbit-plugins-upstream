## Description:

Validates generated test cases against requirements for factual accuracy, consistency, executability, and traceability before final delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA teams and developers use this skill to check AI-generated test cases against requirements and report unsupported claims or cases needing revision before release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad natural-language triggers may invoke validation for a task that is not final test-case QA.

Mitigation: Confirm that test cases and requirements are available and that the task calls for final validation before applying the checks.

Risk: Suggestions to revise, mark, or remove cases may affect valid test coverage.

Mitigation: Verify the case against source requirements and back up the original data before changing or removing it.

## Reference(s):

- [QA Output Validation on ClawHub](https://clawhub.ai/kokxi/skills/qa-output-validation)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown validation report with test-case tables and pass/fail findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes fact, consistency, executability, and traceability checks; findings reference original test-case IDs.]

## Skill Version(s):

1.7.7 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

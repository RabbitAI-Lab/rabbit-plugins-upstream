## Description:

Validates generated test cases before final delivery by checking factual grounding, consistency, executability, and traceability, then returns a pass/fail validation report with issues that must be corrected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and agents use this skill as a final quality gate after generating test cases and before returning them to a user. It checks whether test cases are grounded in the provided requirements, internally consistent, executable, and traceable to source inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Validation findings may incorrectly flag valid test cases or suggest removing cases whose source was not immediately visible.

Mitigation: Review the validation report against the original requirements and back up source data before changing or deleting test cases.

Risk: The skill may trigger on broad requests to verify output quality and influence downstream test-case changes.

Mitigation: Treat the report as a QA gate requiring human or workflow confirmation before applying corrections.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-output-validation)
- [Publisher profile](https://clawhub.ai/user/kokxi)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown validation report with pass/fail status, check results, issue tables, traceability notes, and correction guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report should preserve source traceability for each test case and identify issues without directly deleting test cases.]

## Skill Version(s):

1.6.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Validates AI-generated test cases before final output by checking factual grounding, consistency, executability, and traceability to stated requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, developers, and testing teams use this skill as a final validation gate for generated test cases before delivery. It checks whether test cases are grounded in source requirements, internally consistent, practically executable, and traceable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad quality-check phrasing may activate the skill even when the user did not intend a final validation pass.

Mitigation: Confirm the input contains generated test cases and source requirements, then scope the response to final-output validation.

Risk: Validation may flag nonexistent or unsupported features and lead to deletion or changes in test cases.

Mitigation: Verify each finding against source requirements and preserve the original test data before removing or revising cases.

Risk: The full QA Test Skills bundle is referenced but was not part of the security inspection.

Mitigation: Review and scan the separate bundle before relying on the complete workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-output-validation)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown validation report with pass/fail result, check summaries, issue list, and traceability notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a problem list and correction guidance when validation fails.]

## Skill Version(s):

1.7.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

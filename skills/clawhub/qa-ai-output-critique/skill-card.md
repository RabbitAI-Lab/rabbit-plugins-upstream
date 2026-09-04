## Description:

Reviews AI-generated test cases across completeness, correctness, executability, risk coverage, formatting, consistency, traceability, and redundancy before those cases are accepted as QA artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, developers, and test reviewers use this skill after AI generates test cases to score quality, identify missing or weak cases, and produce improvement guidance before the cases enter a test suite.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad review requests and critique content outside formal QA artifacts.

Mitigation: Invoke it explicitly around AI-generated test cases when formal QA review is intended.

Risk: The skill can recommend deleting, merging, or changing test cases.

Mitigation: Review suggestions before applying them to real test data, and back up important QA artifacts first.

## Reference(s):

- [Review Dimensions](references/review-dimensions.md)
- [Report Templates](references/report-templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown critique report with scoring tables, issue lists, quality scores, coverage gaps, and improvement suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports an eight-dimensional review when scenario and risk evidence are available, and a simplified six-dimensional review when upstream context is missing.]

## Skill Version(s):

1.7.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

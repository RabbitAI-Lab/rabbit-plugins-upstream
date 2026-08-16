## Description:

Helps QA reviewers compensate for common AI-generated test-case blind spots by checking timing dependencies, concurrency conflicts, resource contention, state accumulation, data consistency, and third-party integration differences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and test reviewers use this skill after reviewing AI-generated test cases to identify missing scenarios and add compensating cases across six recurring blind-spot categories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad coverage-review phrases may activate the skill in workflows where a structured blind-spot checklist is not desired.

Mitigation: Use it for post-review QA coverage checks and confirm the generated compensating test cases before adding them to the final test suite.

## Reference(s):

- [Six Blind Spot Details](references/blindspot-details.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with checklist tables and generated compensating test cases]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs blind-spot IDs, related requirement IDs, original test-case IDs, blind-spot type, and new test cases.]

## Skill Version(s):

1.6.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

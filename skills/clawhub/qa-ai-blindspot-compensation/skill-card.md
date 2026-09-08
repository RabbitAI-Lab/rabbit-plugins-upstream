## Description:

AI 测试盲区补偿 helps QA reviewers identify missed test scenarios across sequencing, concurrency, resource contention, state accumulation, data consistency, and third-party integration blind spots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this skill after reviewing AI-generated test cases to find blind spots and propose additional executable scenarios tied to requirements and original case IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read provided requirements, review reports, and test case files to suggest missing scenarios.

Mitigation: Provide only test and requirement artifacts appropriate for review in the current environment.

Risk: The skill recommends installing the broader qa-test-skills package for the full workflow, which was not validated by this artifact scan.

Mitigation: Review and scan the separate full-suite package before installing or running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-ai-blindspot-compensation)
- [六大盲区详解](references/blindspot-details.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with coverage tables and supplemental test case lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs blind spot IDs, linked requirement IDs, original test case IDs, blind spot type, risk level, and suggested test depth.]

## Skill Version(s):

1.7.6 (source: server release metadata; artifact frontmatter says 1.7.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

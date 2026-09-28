## Description:

Provides Chinese-language guidance for generating bulk test data, masking sensitive data, and managing the test-data lifecycle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this skill to plan and generate repeatable test datasets, specify masking rules for sensitive data, and design cleanup and data-management workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive production data may remain identifiable in test datasets.

Mitigation: Prefer synthetic data; use only approved, properly de-identified production data under applicable data-governance controls.

Risk: Example data-generation or cleanup commands could affect unintended records.

Mitigation: Use isolated test environments and scoped credentials; review cleanup queries and preview affected rows before execution.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Code, SQL commands]

**Output Format:** [Markdown with Python and SQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Test-data plans use DATA-XXXX identifiers and address generation, masking, and management.]

## Skill Version(s):

1.7.7 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

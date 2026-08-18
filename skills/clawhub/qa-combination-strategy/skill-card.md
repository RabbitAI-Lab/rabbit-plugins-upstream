## Description:

Helps QA practitioners design efficient combination-testing coverage using pairwise testing, orthogonal arrays, decision tables, and risk-weighted combinations when exhaustive testing is impractical.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this skill to reduce combination explosion across input, environment, and state parameters while preserving meaningful pairwise, orthogonal, and high-risk coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: QA planning inputs may contain production identifiers, payment details, screenshots, ID numbers, phone numbers, or customer data.

Mitigation: Mask or anonymize sensitive production and customer data before using the skill.

Risk: Combination-reduction strategies can miss important interactions when parameter identification or risk assessment is incomplete.

Mitigation: Review generated matrices for high-risk business rules and add explicit full-coverage cases where needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-combination-strategy)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with structured combination matrices, coverage notes, and test-case guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include combination matrix IDs, scenario traceability, pairwise and n-way combination analysis, and coverage gaps.]

## Skill Version(s):

1.6.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

This skill helps QA practitioners reduce combination-test explosion by applying pairwise testing, orthogonal arrays, and risk-weighted selection to produce combination coverage matrices and coverage gap notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, test designers, and developers use this skill when requirements contain many parameter, environment, or state combinations and exhaustive testing is impractical. It guides them to choose pairwise, orthogonal-array, risk-weighted, or full-combination strategies and to document coverage gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive production QA data, such as order details, payment records, IDs, phone numbers, screenshots, or financial records, could be pasted into prompts while designing tests.

Mitigation: Mask or replace sensitive production data before using the skill, and use synthetic examples where possible.

Risk: Using this standalone skill without upstream scenario, requirement, or risk context can lead to incomplete parameter identification or missed high-risk combinations.

Mitigation: Provide a scenario tree, requirements decomposition, and risk assessment, or review the broader QA skill suite before relying on the generated matrix.

Risk: Combination-reduction strategies can omit important interactions if inputs are incomplete or if a high-risk area is treated as low risk.

Mitigation: Review coverage gaps, manually add high-risk combinations for full testing, and avoid claiming absolute 100% coverage unless the evidence supports it.

## Reference(s):

- [ClawHub skill page: qa-combination-strategy](https://clawhub.ai/kokxi/skills/qa-combination-strategy)
- [ClawHub publisher profile: kokxi](https://clawhub.ai/user/kokxi)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown tables and structured text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes test-case tables, combination coverage matrices, pairwise and N-way combination analysis, and coverage gap notes.]

## Skill Version(s):

1.7.6 (source: ClawHub release evidence; artifact frontmatter says 1.7.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

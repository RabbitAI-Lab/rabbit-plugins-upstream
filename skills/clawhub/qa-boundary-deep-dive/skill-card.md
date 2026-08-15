## Description:

Boundary Deep Dive helps QA practitioners systematically identify input, state, time, and resource boundary conditions, assign risk levels, and define expected results for test coverage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, developers, and test designers use this skill when they need deeper boundary-value coverage after scenario analysis or equivalence-class testing. It turns system behavior into structured boundary checks across inputs, state transitions, timing, and resource limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: QA prompts may include real customer, payment, identity, credential, or production data while exploring boundary cases.

Mitigation: Use anonymized or masked test data and avoid pasting sensitive production information into prompts.

Risk: Boundary-analysis guidance can miss domain-specific constraints or produce expected results that do not match product requirements.

Mitigation: Review generated boundary cases against current requirements, state models, timeout rules, and resource limits before using them as test authority.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-boundary-deep-dive)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown boundary-analysis report with tables and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Boundary items are expected to include IDs, linked scenario IDs, risk levels, and expected results when the provided system context supports them.]

## Skill Version(s):

1.6.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

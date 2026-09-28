## Description:

Turns decomposed requirements into traceable test scenarios covering main flows, alternative paths, exceptions, and data flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA testers and developers use this skill to turn decomposed requirements into prioritized, requirement-linked test scenarios for complex workflows, including branches and failure paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Test examples may expose customer, payment, identity, or other production information.

Mitigation: Use masked or synthetic test data; do not paste real customer records or production evidence into prompts.

Risk: Broad testing trigger phrases may invoke scenario-tree planning when it is not intended.

Mitigation: Invoke the skill explicitly for scenario-tree test design and review the resulting scenarios against the source requirements.

## Reference(s):

- [Scenario Tree skill release](https://clawhub.ai/kokxi/skills/qa-scenario-tree)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown scenario tree and nine-column test-case table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario IDs and requirement links; priority and risk labels; coverage qualified by the supplied requirements.]

## Skill Version(s):

1.7.7 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

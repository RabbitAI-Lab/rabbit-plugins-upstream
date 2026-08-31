## Description:

Builds QA domain models from complex requirements by mapping state transitions, data flows, and service dependencies so testers can reason about business logic and system boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and test designers use this skill to turn complex business requirements or scenario trees into state-machine, data-flow, and service-dependency models for test planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad modeling-related wording and steer general modeling tasks toward QA domain-modeling behavior.

Mitigation: Use explicit prompts for QA domain modeling or disable the skill where general modeling language should not trigger this behavior.

Risk: Generated domain models can omit subsystems, implicit rules, or exception paths when the input requirements are incomplete.

Mitigation: Review the state, data-flow, and service-dependency outputs against the source requirements and scenario IDs, then return to the scenario tree to fill gaps before using the models for test scope decisions.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown tables and text diagrams describing state transitions, data flows, service dependencies, traceability IDs, and coverage notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include model IDs, scenario IDs, domain-model views, and coverage qualifications based on the provided requirements.]

## Skill Version(s):

1.7.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

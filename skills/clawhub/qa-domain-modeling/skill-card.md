## Description:

Helps QA practitioners model complex business requirements with state machines, data-flow views, and service-dependency diagrams to expose implicit business rules and system boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this skill to turn complex requirements, scenario trees, or deconstructed requirements into domain models that clarify state transitions, data movement, service dependencies, and test scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger terms can cause the skill to be invoked during generic design conversations.

Mitigation: Invoke it deliberately for QA domain-modeling tasks that include requirements, scenarios, or system interaction evidence.

Risk: Incomplete or ambiguous requirements can lead to missing states, data paths, service dependencies, or unsupported coverage claims.

Mitigation: Review generated models against the source requirements and label missing modules or unsupported coverage assumptions before using the output for test planning.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-domain-modeling)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown tables and text diagrams]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes model IDs, scenario traceability, state-machine, data-flow, and service-dependency sections; coverage statements should avoid absolute 100% claims.]

## Skill Version(s):

1.7.6 (source: server release metadata; artifact frontmatter lists 1.7.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps QA practitioners model complex business requirements with state machines, data-flow views, and service-dependency views so they can clarify logic, boundaries, and implicit rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, requirements analysts, and developers use this skill to turn complex requirements or scenario trees into domain models for testing scope analysis. It is suited for workflows that need state-transition tables, data-flow tables, service-dependency tables, and traceability to scenario IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is optimized for Chinese-language QA and requirements-modeling prompts, which may affect routing or output quality in multilingual skill sets.

Mitigation: Review trigger wording and routing configuration before deployment in multilingual or crowded agent environments.

Risk: Domain models may omit states, data endpoints, service callbacks, or degradation paths when source requirements are incomplete.

Mitigation: Review generated state, data-flow, and service-dependency tables against the source requirements and fill gaps before using them for test planning.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-domain-modeling)
- [Publisher profile](https://clawhub.ai/user/kokxi)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with structured tables and text diagrams]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces model IDs, linked scenario IDs, state-machine views, data-flow views, service-dependency views, and QA-oriented checklists.]

## Skill Version(s):

1.6.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

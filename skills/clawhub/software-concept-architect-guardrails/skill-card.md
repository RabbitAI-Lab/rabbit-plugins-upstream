## Description:

Helps developers audit, create, compare, and map concept specifications so documented contracts stay aligned with implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review specification coverage and drift, draft concept and data-flow contracts, document coordination, and derive architecture maps from project evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional hooks may automatically read project specifications and place repository Markdown into the agent's working context during session and edit events.

Mitigation: Enable hooks only in repositories with trusted specification files; otherwise use the explicitly invoked skill modes without installing hooks.

## Reference(s):

- [Project homepage](https://github.com/ontology-of-everything/concept-skills)
- [wyx (adapted workflow)](https://github.com/jlifyio/wyx)

## Skill Output:

**Output Type(s):** [Markdown specifications, Text reports, Architecture maps, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audit and drift modes are read-only; specification changes require authorization.]

## Skill Version(s):

1.0.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Applies pipes-and-filters for sequential data transformations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and architects use this skill to decide when to apply a pipes-and-filters pipeline and to plan stages, pipes, schemas, observability, testing, scaling, and failure isolation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers such as architecture, pipeline, and streaming may activate the skill in conversations where pipeline architecture guidance is not relevant.

Mitigation: Review and narrow activation triggers before installing in constrained environments.

Risk: Architecture recommendations may be incomplete if applied without workload, schema, back-pressure, observability, and failure-mode validation.

Mitigation: Have developers or architects review generated ADRs, schema contracts, load tests, and stage-level observability plans before implementation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-pipeline)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown architecture guidance with checklists and risk mitigations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory content only; no executable commands, files, API calls, or tool invocations are produced by the skill.]

## Skill Version(s):

1.9.18 (source: release evidence; artifact frontmatter states 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Applies Functional Core, Imperative Shell to isolate logic from side effects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan and review migrations that separate pure business rules from I/O boundaries, improving testability and reducing coupling to frameworks or infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may influence architectural refactor proposals that are incorrect or unsuitable for a specific codebase.

Mitigation: Review proposed boundaries, ADRs, and tests with project maintainers before implementing changes.

Risk: The artifact references a separate Claude Code plugin that was not part of the inspected skill artifact.

Mitigation: Review and scan the separate plugin before installing or relying on it.

## Reference(s):

- [Claude Night Market archetypes](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes)
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-functional-core)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration]

**Output Format:** [Markdown guidance with optional code and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only architecture guidance; no executable code is included in the inspected artifact.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

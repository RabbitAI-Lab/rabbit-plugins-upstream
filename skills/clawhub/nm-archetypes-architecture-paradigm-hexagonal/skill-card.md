## Description:

Applies hexagonal architecture by isolating domain logic from infrastructure through ports and adapters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and software architects use this skill to decide when to apply hexagonal architecture and to plan port interfaces, adapters, contract tests, and dependency rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hexagonal architecture guidance can add unnecessary abstraction and maintenance overhead to small systems, scripts, utilities, or early prototypes.

Mitigation: Apply the pattern case by case; avoid port and adapter layers when the project has few external dependencies or the abstraction cost outweighs testability benefits.

Risk: Architecture proposals could introduce misleading boundaries, leaky ports, or adapter drift if adopted without review.

Mitigation: Review recommendations before implementation, keep port interfaces domain-centric, and validate adapters with contract tests or other architecture checks.

## Reference(s):

- [Project homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes)
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-hexagonal)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown guidance and structured architecture recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Architecture guidance only; no executable code, shell commands, hidden behavior, or sensitive access are included.]

## Skill Version(s):

1.9.19 (source: server release evidence; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

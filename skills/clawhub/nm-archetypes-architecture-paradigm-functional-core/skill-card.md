## Description:

Applies Functional Core, Imperative Shell to isolate logic from side effects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and software architects use this skill to decide when and how to isolate pure business logic from I/O and framework code using Functional Core, Imperative Shell. It guides adoption steps, deliverables, and pattern-specific risks for improving testability and managing side effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may appear during broad architecture or testability discussions where this pattern is not the right fit.

Mitigation: Confirm that business logic is materially entangled with I/O, framework calls, or brittle tests before applying the guidance.

Risk: Teams may duplicate decisions in the imperative shell instead of keeping business logic in the functional core.

Mitigation: Use code reviews and architecture tests to enforce that the core owns decisions while the shell handles orchestration and side effects.

Risk: The pattern can be a poor fit for performance-critical hot paths or framework lifecycles that resist a thin shell boundary.

Mitigation: Exclude hot paths when immutability overhead matters and validate framework integration with small adapters before broader refactoring.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-functional-core)
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown prose with architecture adoption steps, deliverables, and risk mitigations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code, credential use, persistence, or environment modification is identified in the release security evidence.]

## Skill Version(s):

1.9.18 (source: server release evidence; artifact frontmatter says 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

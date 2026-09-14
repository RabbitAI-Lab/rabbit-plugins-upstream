## Description:

Generates modular-monolith implementation guidance from a confirmed concept model when explicitly invoked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to map confirmed concept models into modular-monolith implementations, including concept modules, sync composition, interface placement, specification colocation, and validation checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated architecture or code changes may fail to preserve confirmed concept boundaries, sync behavior, or error contracts.

Mitigation: Review generated changes and require CI boundary checks plus behavior tests for sync binding, errors, retries, and concurrent request isolation.

Risk: Requested implementations may introduce dependencies or persistence choices that are inappropriate for the target application.

Mitigation: Review dependency choices and any persistence, outbox, retry, or idempotency storage before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/agenticweb4/skills/concept-implementation)
- [Project Homepage](https://github.com/ontology-of-everything/SemanticSkills/tree/main/skills/concept-implementation)
- [Composition Layer Implementation](references/composition-layer.md)
- [Scaling: Concept Grouping and Sync Packages](references/scaling.md)
- [Java / Spring Modulith](references/java-spring.md)
- [Rust Implementation](references/rust.md)
- [TypeScript Implementation](references/typescript.md)
- [Sources Used by This Skill](references/sources.md)
- [Beyond Objects](https://arxiv.org/abs/2606.27258)
- [WYSIWID Paper](https://arxiv.org/abs/2508.14511)
- [Spring Modulith](https://spring.io/projects/spring-modulith)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with code, shell command, and configuration snippets when implementation is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve confirmed concept boundaries, route cross-concept behavior through syncs, and include validation checks appropriate to the target language.]

## Skill Version(s):

0.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

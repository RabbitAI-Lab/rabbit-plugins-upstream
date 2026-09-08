## Description:

Maps a confirmed concept model using Daniel Jackson's concept design onto a modular monolith, with one module per concept and syncs implemented as mediators or a rule engine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to translate a confirmed concept model and concept PRD into a modular-monolith implementation plan, including module boundaries, sync composition, interface placement, guardrail tests, and colocated specifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated implementation guidance may lead to code changes or optional dependency choices such as framework modules, rule engines, or CI boundary-checking tools.

Mitigation: Review generated code changes and dependency selections before adoption, and run normal project tests and dependency review.

Risk: Architecture guidance may be misapplied if concept boundaries, sync failure paths, or colocated specifications are not checked against the confirmed model.

Mitigation: Use the skill's boundary guardrail tests and specification co-location checks to confirm concept modules do not directly reference each other and sync failure paths are explicit.

## Reference(s):

- [Composition Layer Guidance](references/composition-layer.md)
- [Scaling Guidance](references/scaling.md)
- [Rust Implementation Guidance](references/rust.md)
- [Java Spring Modulith Guidance](references/java-spring.md)
- [TypeScript Implementation Guidance](references/typescript.md)
- [Source Basis](references/sources.md)
- [Beyond Objects](https://arxiv.org/abs/2606.27258)
- [WYSIWID Paper](https://arxiv.org/abs/2508.14511)
- [Concept Design Overview](https://essenceofsoftware.com/posts/distillation/)
- [conceptbox](https://github.com/61040-fa25/conceptbox)
- [Spring Modulith](https://spring.io/projects/spring-modulith)
- [LegibleSync](https://github.com/mastepanoski/legiblesync)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code, shell command, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are implementation guidance and proposed artifacts for review; no hidden execution or persistence behavior was identified in security evidence.]

## Skill Version(s):

0.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Implements a confirmed concept model as a modular monolith only when the user explicitly invokes $concept-implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to turn confirmed concept models into modular monolith implementations with independent concept modules, explicit synchronization composition, colocated specifications, and behavior and dependency checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated implementation changes may alter module boundaries, persistence behavior, retry logic, dependency checks, or tests in a real repository.

Mitigation: Review proposed code, persistence and retry behavior, boundary-check CI, and test changes before deployment.

Risk: The skill depends on confirmed concept specifications; applying it to incomplete or ambiguous models can produce incorrect implementation guidance.

Mitigation: Route model gaps back to concept design and update specifications before implementing behavior-changing decisions.

## Reference(s):

- [OpenClaw homepage](https://github.com/ontology-of-everything/concept-skills/tree/main/skills/en/concept-implementation)
- [Concept and Synchronization Specification Contract](references/spec-format.md)
- [Composition Layer](references/composition-layer.md)
- [Rust Implementation](references/rust.md)
- [Java and Spring Modulith](references/java-spring.md)
- [TypeScript Implementation](references/typescript.md)
- [Scaling Groups and Packages](references/scaling.md)
- [Implementation Sources](references/sources.md)
- [Concept Purposes and Synchronization](https://essenceofsoftware.com/posts/distillation/)
- [Jackson 2015](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf)
- [Beyond Objects](https://arxiv.org/abs/2606.27258)
- [WYSIWID](https://arxiv.org/abs/2508.14511)
- [conceptbox](https://github.com/61040-fa25/conceptbox)
- [Cargo workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html)
- [cargo-deny bans](https://embarkstudios.github.io/cargo-deny/checks/bans/cfg.html)
- [LegibleSync](https://github.com/mastepanoski/legiblesync)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with implementation plans, code edits or snippets, shell commands, and configuration guidance as requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explicit invocation only; outputs should preserve confirmed specifications, concept boundaries, synchronization contracts, and verification steps.]

## Skill Version(s):

0.6.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

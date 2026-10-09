## Description:

Guides agents writing, reviewing, refactoring, and debugging modern C++ systems and libraries, including ownership, API and ABI design, concurrency, and CMake tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement and review C++ code while respecting project conventions, resource lifetimes, API compatibility, and build and test practices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested build, lint, sanitizer, or test commands may be inappropriate for a particular project.

Mitigation: Review commands against the project's configuration before running them.

Risk: C++ changes may violate lifetime assumptions or public API and ABI compatibility.

Mitigation: Check ownership and interface constraints, then build and run relevant tests and sanitizers.

## Reference(s):

- [Value and interface design](artifact/references/value-and-interface-design.md)
- [C++ API and ABI boundaries](artifact/references/api-and-abi.md)
- [Concurrency and verification](artifact/references/concurrency-and-verification.md)
- [CMake and C++ tooling](artifact/references/cmake-and-tooling.md)
- [C++ legibility standard](artifact/references/legibility-standard.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with C++ and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations should follow the project's C++ standard and repository conventions.]

## Skill Version(s):

5.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

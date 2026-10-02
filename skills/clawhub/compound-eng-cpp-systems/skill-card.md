## Description:

Guides agents writing and reviewing modern C++ code, including ownership, error handling, API and ABI compatibility, concurrency, and build tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to write, refactor, debug, and review C++ libraries and applications while checking ownership, interface stability, threading, and project-specific conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested local build, lint, formatting, or sanitizer commands may affect sensitive repositories.

Mitigation: Review proposed commands and their effects before running them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-cpp-systems)
- [C++ API and ABI boundaries](artifact/references/api-and-abi.md)
- [CMake and C++ tooling](artifact/references/cmake-and-tooling.md)
- [Concurrency and verification](artifact/references/concurrency-and-verification.md)
- [C++ legibility](artifact/references/legibility-standard.md)
- [Value and interface design](artifact/references/value-and-interface-design.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with C++ and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations should follow the repository's C++ standard, error model, formatting, and ABI requirements.]

## Skill Version(s):

5.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

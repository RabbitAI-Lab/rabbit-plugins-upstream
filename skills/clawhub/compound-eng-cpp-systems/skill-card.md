## Description:

Guides agents writing and reviewing modern C++ on ownership, error handling, API and ABI stability, concurrency, and CMake tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to guide an agent in writing, reviewing, refactoring, and debugging C++ code and library interfaces while respecting project conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Guidance may change C++ behavior or public interfaces if applied without checking local constraints.

Mitigation: Review proposed changes against project build settings, style files, and ABI requirements before adoption.

Risk: Suggested build, sanitizer, or formatting commands may affect the local project.

Mitigation: Inspect commands and project configuration before running them; verify results with the project's tests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-cpp-systems)
- [Value and interface design](artifact/references/value-and-interface-design.md)
- [API and ABI boundaries](artifact/references/api-and-abi.md)
- [Concurrency and verification](artifact/references/concurrency-and-verification.md)
- [CMake and C++ tooling](artifact/references/cmake-and-tooling.md)
- [C++ legibility standard](artifact/references/legibility-standard.md)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with C++ and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advice adapts to the project's C++ standard, build settings, and style conventions.]

## Skill Version(s):

5.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

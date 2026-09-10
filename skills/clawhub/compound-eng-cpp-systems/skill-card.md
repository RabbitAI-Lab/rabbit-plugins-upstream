## Description:

Modern C++ patterns: RAII and ownership, rule of zero/five, exceptions and error handling, API and ABI boundaries, templates, and CMake tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when writing, reviewing, refactoring, or debugging C++ systems and libraries, especially work involving ownership, move semantics, API and ABI boundaries, templates, gtest, clang-tidy, and CMake tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can steer an agent toward repository inspection and normal C++ verification commands such as builds, tests, formatting checks, clang-tidy, and sanitizer runs.

Mitigation: Review proposed commands, paths, and scope before execution, especially in sensitive or large repositories.

Risk: C++ ownership, ABI, concurrency, and build guidance can cause regressions if applied without local project constraints.

Mitigation: Check the repository's C++ standard, CMake configuration, formatting and linting rules, adjacent code patterns, tests, sanitizer results, and ABI requirements before accepting changes.

## Reference(s):

- [C++ API and ABI boundaries](references/api-and-abi.md)
- [CMake and C++ tooling](references/cmake-and-tooling.md)
- [Concurrency and verification](references/concurrency-and-verification.md)
- [C++ legibility: the deep rules and a worked refactor](references/legibility-standard.md)
- [Value and interface design](references/value-and-interface-design.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, C++ and CMake examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapts recommendations to the repository's C++ standard, build configuration, formatting, linting, tests, sanitizer setup, and ABI constraints.]

## Skill Version(s):

4.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

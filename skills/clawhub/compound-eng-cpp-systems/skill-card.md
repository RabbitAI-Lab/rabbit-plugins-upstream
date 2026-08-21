## Description:

Modern C++ guidance covering RAII and ownership, rule of zero/five, exceptions and error handling, API and ABI boundaries, templates, CMake tooling, smart pointers, move semantics, memory leaks, template errors, and gtest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when writing, reviewing, refactoring, or debugging modern C++ systems and libraries, especially around ownership, ABI-safe APIs, templates, tests, and CMake tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated build, sanitizer, or dependency commands may affect local build outputs when run in a user's repository.

Mitigation: Review commands before execution and adapt them to the repository's build directories, dependency policy, and CI conventions.

Risk: C++ API, ABI, or ownership guidance applied without checking project constraints can introduce compatibility or behavior regressions.

Mitigation: Check the project's C++ standard, exception policy, ABI requirements, formatting, linting, and adjacent code before applying recommendations.

## Reference(s):

- [C++ API and ABI boundaries](references/api-and-abi.md)
- [CMake and C++ tooling](references/cmake-and-tooling.md)
- [C++ legibility: the deep rules and a worked refactor](references/legibility-standard.md)
- [write-legible-c](https://github.com/7etsuo/write-legible-c)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with C++ code snippets, CMake examples, shell commands, and review checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May route the agent to bundled reference files for API/ABI, CMake/tooling, and legibility details.]

## Skill Version(s):

4.4.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

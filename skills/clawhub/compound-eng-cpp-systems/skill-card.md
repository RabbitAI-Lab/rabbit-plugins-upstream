## Description:

Modern C++ patterns: RAII and ownership, rule of zero/five, exceptions and error handling, API and ABI boundaries, templates, and CMake tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when writing, reviewing, refactoring, or debugging C++ systems and libraries, especially around ownership, API and ABI boundaries, templates, CMake tooling, tests, and static analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to propose or run build, lint, formatter, sanitizer, or test commands in a C++ repository.

Mitigation: Review commands before execution in sensitive or production workspaces and run them in an appropriate development environment.

Risk: C++ API, ABI, ownership, and error-handling recommendations can be wrong for a repository with stricter local constraints.

Mitigation: Check the repository's C++ standard, build flags, formatting and linting configuration, adjacent code, and compatibility requirements before applying generated changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-cpp-systems)
- [C++ API and ABI boundaries](artifact/references/api-and-abi.md)
- [CMake and C++ tooling](artifact/references/cmake-and-tooling.md)
- [C++ legibility: the deep rules and a worked refactor](artifact/references/legibility-standard.md)
- [write-legible-c](https://github.com/7etsuo/write-legible-c)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with C++, CMake, shell, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapts recommendations to the repository's existing C++ standard, formatting, linting, build, and API compatibility constraints.]

## Skill Version(s):

4.4.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

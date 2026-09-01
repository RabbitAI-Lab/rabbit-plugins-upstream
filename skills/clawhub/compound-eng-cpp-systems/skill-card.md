## Description:

Modern C++ patterns: RAII and ownership, rule of zero/five, exceptions and error handling, API and ABI boundaries, templates, and CMake tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when writing, reviewing, refactoring, or debugging C++ systems and library code. It provides guidance for ownership, API and ABI boundaries, templates, CMake tooling, tests, sanitizers, and code legibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: C++ edits made from this guidance can unintentionally change ownership, exception, threading, API, or ABI behavior.

Mitigation: Review public headers and ownership changes before merging, then run the project build, tests, compiler warnings, clang-tidy, and relevant sanitizers.

Risk: Tooling recommendations can conflict with local project constraints such as pinned C++ standards, exception-free builds, embedded targets, or existing formatter and linter settings.

Mitigation: Apply the repository's CMake, compiler, formatter, linter, and platform constraints before following general guidance from the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-cpp-systems)
- [C++ API and ABI boundaries](references/api-and-abi.md)
- [CMake and C++ tooling](references/cmake-and-tooling.md)
- [C++ legibility: the deep rules and a worked refactor](references/legibility-standard.md)
- [write-legible-c](https://github.com/7etsuo/write-legible-c)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code, shell command, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; does not add executable code or request special access by itself.]

## Skill Version(s):

4.5.0 (source: server release evidence; changelog v4.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

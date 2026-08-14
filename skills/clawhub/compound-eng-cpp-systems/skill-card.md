## Description:

Modern C++ patterns: RAII and ownership, rule of zero/five, exceptions and error handling, API and ABI boundaries, templates, and CMake tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when writing, reviewing, refactoring, or debugging modern C++ systems and libraries, including ownership, move semantics, API and ABI boundaries, templates, tests, and CMake tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can recommend local build, formatting, lint, and sanitizer commands that affect a user's repository or consume significant local resources.

Mitigation: Review suggested commands before running them, especially on sensitive or very large repositories.

Risk: The skill influences C++ coding and review behavior, so incorrect guidance could affect API compatibility, memory safety, or build configuration decisions.

Mitigation: Validate recommendations against repository conventions, tests, compiler warnings, clang-tidy, and sanitizer results before deployment.

## Reference(s):

- [C++ API and ABI boundaries](references/api-and-abi.md)
- [CMake and tooling](references/cmake-and-tooling.md)
- [Legibility standard](references/legibility-standard.md)
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-cpp-systems)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; no bundled executable tools or MCP integrations detected.]

## Skill Version(s):

4.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

KWDB Build helps agents configure, build, clean, install, and test KaiwuDB source checkouts using CMake and bundled C++ and Go test workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kwdb](https://clawhub.ai/user/kwdb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers working on KaiwuDB use this skill to confirm build settings, prepare CMake build or install commands, and run C++ or Go unit tests. The skill also guides agents to report compile or test failures without automatically fixing source code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cleanup and test workflows can delete broad project and GOPATH paths.

Mitigation: Use only on disposable or backed-up KaiwuDB checkouts, confirm the exact source root and GOPATH, and require the agent to show resolved cleanup targets before running destructive cleanup commands.

Risk: Build and test guidance may install dependencies or run project test scripts.

Mitigation: Review proposed apt-get, make clean, test script, and shell commands before execution, and run them in an isolated development environment when possible.

## Reference(s):

- [Build Questions](references/build-questions.md)
- [CMake Options](references/cmake-options.md)
- [C++ Unit Test](references/cpp-unittest.md)
- [Go Unit Test](references/golang-unittest.md)
- [Dependencies](references/dependencies.md)
- [Project Structure](references/project-structure.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and configuration checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-confirmed source root, GOPATH, build type, and allowed CMake options before commands are run.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

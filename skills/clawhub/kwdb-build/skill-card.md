## Description: <br>
KWDB Build helps agents configure, build, and run C++ or Go unit tests for KaiwuDB using the documented CMake workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kwdb](https://clawhub.ai/user/kwdb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to guide KaiwuDB source builds, CMake configuration, cleanup checks, and C++ or Go unit test runs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cleanup steps may delete broad workspace or GOPATH content, including wildcard build paths and GOPATH-native content. <br>
Mitigation: Require the agent to show the exact cleanup paths before execution, confirm they are inside the intended KaiwuDB source checkout, and manually approve any GOPATH or wildcard deletion. <br>
Risk: Build and test commands can run shell scripts and CMake or Make targets on a local source checkout. <br>
Mitigation: Run the skill only in a disposable or backed-up workspace with reviewed source paths and user-confirmed configuration values. <br>


## Reference(s): <br>
- [KWDB Build on ClawHub](https://clawhub.ai/kwdb/skills/kwdb-build) <br>
- [Build configuration questions](references/build-questions.md) <br>
- [CMake options reference](references/cmake-options.md) <br>
- [C++ unit test workflow](references/cpp-unittest.md) <br>
- [Go unit test workflow](references/golang-unittest.md) <br>
- [Dependency reference](references/dependencies.md) <br>
- [Project structure reference](references/project-structure.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and configuration choices] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation before build or test actions and should report failures without automatic fixes.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

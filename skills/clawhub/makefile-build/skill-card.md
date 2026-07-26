## Description: <br>
Write Makefiles for project automation across languages, including targets, dependencies, variables, pattern rules, phony targets, and alternatives such as Just and Task. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to create or improve project build automation, task runners, and repeatable build, test, lint, deploy, and cleanup workflows across Go, Python, Node.js, Docker, and multi-directory projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated or adapted build targets may install packages, delete directories, change permissions, or run privileged commands. <br>
Mitigation: Review Makefile, Justfile, and Taskfile commands before execution, especially commands that install dependencies, remove files, change permissions, or use sudo. <br>
Risk: Build automation examples can be copied into projects without matching local paths, tools, or deployment assumptions. <br>
Mitigation: Adjust paths, binaries, environment variables, and deployment commands for the target project, then test targets in a disposable or non-production environment first. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gitgoodordietrying/skills/makefile-build) <br>
- [Just project](https://github.com/casey/just) <br>
- [Task installation](https://taskfile.dev/installation/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with Makefile, Justfile, Taskfile, YAML, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Examples target Linux, macOS, and Windows workflows and may require make, just, or task depending on the chosen approach.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

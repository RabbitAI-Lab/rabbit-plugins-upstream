## Description: <br>
Scaffolds dev project files for Python, Node, Docker, Go, and Rust, returning toolchain commands for the calling agent while writing files only inside the agent workspace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use env-manager to scaffold starter project files for common language and toolchain environments and receive structured commands that the calling agent can review and run. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Workspace containment may not be reliably enforced before writing files. <br>
Mitigation: Use only supported environment types with an explicit validated name, inspect returned paths before running generated commands, and avoid sensitive repositories until workspace root handling and type/name validation are verified. <br>
Risk: Setup writes starter files and state during each successful setup call, with no preview step. <br>
Mitigation: Review the target environment name, generated path, and existing files before invoking setup; do not call setup when file writes are not intended. <br>
Risk: Returned shell commands could be run incorrectly by the calling agent. <br>
Mitigation: Inspect each command object's binary, arguments, working directory, status, and warnings before execution; do not run commands marked blocked or not_found. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/env-manager) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration] <br>
**Output Format:** [JSON objects, human-readable command text, and generated project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated files are written during setup; returned commands are not executed by the skill.] <br>

## Skill Version(s): <br>
3.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

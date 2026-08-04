## Description: <br>
Scaffolds dev project files for Python, Node, Docker, Go, and Rust, tracks environment, service, and port metadata, and returns toolchain commands for the calling agent to inspect and run. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to create starter project files, maintain workspace-local environment metadata, and receive structured setup commands that the calling agent may review and execute separately. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes and overwrites scaffold files and workspace state without a preview or dry-run step. <br>
Mitigation: Call setupEnvironment only when file creation is intended, use a project-specific environment name, and inspect existing workspace files before setup. <br>
Risk: Lower-level file generation can write to a caller-supplied target directory, which may exceed the documented workspace boundary. <br>
Mitigation: Use the validated setupEnvironment flow with known environment types; avoid direct generateScaffoldFiles calls unless the target directory is fully controlled. <br>
Risk: Returned toolchain commands are data for the calling agent and may still affect the workspace if executed later. <br>
Mitigation: Review commands and warnings before execution, and run only commands marked ready and expected for the selected toolchain. <br>


## Reference(s): <br>
- [ClawHub env-manager skill page](https://clawhub.ai/jlacroix82/skills/env-manager) <br>
- [README](artifact/README.md) <br>
- [Security Audit](artifact/SECURITY-AUDIT.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration] <br>
**Output Format:** [JSON objects, plain-text command summaries, and scaffold files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill writes starter files and JSON state in the workspace and returns commands as data for the calling agent to evaluate.] <br>

## Skill Version(s): <br>
3.0.5 (source: server release metadata and clawhub.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

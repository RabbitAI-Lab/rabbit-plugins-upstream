## Description: <br>
Scaffolds starter files for Python, Node, Docker, Go, and Rust projects and returns toolchain commands for a calling agent to inspect and run. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to create starter project files, track environment metadata, and receive structured setup commands for common development stacks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crafted project names may cause file writes outside the intended workspace. <br>
Mitigation: Use simple trusted project names and avoid path components such as ../ or absolute-looking names. <br>
Risk: Setup calls write files immediately and can overwrite starter files. <br>
Mitigation: Run the skill in a controlled workspace and inspect generated files before relying on them. <br>
Risk: Returned setup commands may not be appropriate for every environment. <br>
Mitigation: Review returned commands and run only entries that are expected and appropriate for the project. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/env-mgr) <br>
- [README](README.md) <br>
- [Security audit](SECURITY-AUDIT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Shell commands, Configuration] <br>
**Output Format:** [JSON objects with formatted command text and generated workspace files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes starter files and environment state; returned commands are data for the calling agent and are not executed by the skill.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

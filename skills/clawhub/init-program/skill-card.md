## Description: <br>
Create or update the correct agent instruction file for the active coding assistant, then initialize a software project according to that file. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dreamingphper](https://clawhub.ai/user/dreamingphper) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to create or update repository agent instructions, then scaffold or initialize a project according to those instructions. It is useful when bootstrapping a repository, choosing between AGENTS.md and Claude Code instruction files, or setting implementation and review expectations before coding. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify agent instruction files and create starter project files during initialization. <br>
Mitigation: Review proposed changes before accepting them, especially changes to AGENTS.md, CLAUDE.md, setup commands, and generated project files. <br>


## Reference(s): <br>
- [Init Program on ClawHub](https://clawhub.ai/dreamingphper/skills/init-program) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with proposed file changes and command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or create AGENTS.md, CLAUDE.md, starter project files, configuration files, environment examples, and validation commands.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

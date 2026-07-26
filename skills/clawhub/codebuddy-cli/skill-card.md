## Description: <br>
CodeBuddy Code CLI installation, configuration, and usage guidance for Tencent's AI-powered terminal programming assistant. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pmwalkercao](https://clawhub.ai/user/pmwalkercao) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to install, configure, and operate Tencent CodeBuddy CLI, including interactive sessions, single-task commands, slash commands, updates, and troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Permission-bypass modes can let an agent make broad file changes without normal safeguards. <br>
Mitigation: Use bypass or auto-approval flags only in disposable workspaces after reviewing the files the agent may read, write, or delete. <br>
Risk: A persistent global npm installation expands trust in the CodeBuddy CLI package across local projects. <br>
Mitigation: Install only when the package source is trusted and keep backups before using the tool on important workspaces. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and command tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes security cautions for permission-bypass flags and global npm installation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

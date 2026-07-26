## Description: <br>
CodeBuddy Code for OpenClaw provides installation, configuration, usage, and troubleshooting guidance for Tencent's CodeBuddy Code CLI programming assistant. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pmwalkercao](https://clawhub.ai/user/pmwalkercao) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to install, configure, run, update, and troubleshoot CodeBuddy Code CLI, including login modes, CLI flags, slash commands, and custom command files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Global installation of the CodeBuddy CLI can install software from an external npm package publisher. <br>
Mitigation: Verify the npm package and publisher before installing globally, and install only if Tencent CodeBuddy is intended for use. <br>
Risk: Permission-bypass flags such as -y, --dangerously-skip-permissions, and bypass modes can allow file changes without interactive confirmation. <br>
Mitigation: Use interactive permission prompts for real projects and reserve bypass modes for disposable sandboxes. <br>
Risk: Generated memory or custom command files can influence later agent sessions. <br>
Mitigation: Review generated memory and command files before relying on future sessions. <br>


## Reference(s): <br>
- [CodeBuddy Code for OpenClaw on ClawHub](https://clawhub.ai/pmwalkercao/skills/codebuddy-code) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and command tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes CLI installation, login, command, update, and security usage guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

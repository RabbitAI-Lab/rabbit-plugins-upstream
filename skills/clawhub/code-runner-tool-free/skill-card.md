## Description: <br>
Runs coding tasks in non-interactive environments through a PTY with automatic prompt responses, timeout control, output capture, and project file synchronization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to delegate code review, refactoring, feature development, and bug-fix tasks to an agent that can execute commands and synchronize resulting file changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can execute commands and synchronize file changes across a project directory. <br>
Mitigation: Run it in a disposable clone or container and review all diffs before applying changes to important repositories. <br>
Risk: Automatic prompt approval can accept actions the user did not explicitly review. <br>
Mitigation: Avoid using it on sensitive repositories unless confirmation handling and requested tasks are reviewed first. <br>
Risk: Callback URLs and API keys can expose execution results or credentials if configured unsafely. <br>
Mitigation: Use only trusted callback endpoints and protect credentials such as API keys. <br>
Risk: Running with sudo or root privileges increases the impact of command execution or file ownership changes. <br>
Mitigation: Avoid sudo/root runtime execution and prefer a dedicated low-privilege user. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/code-runner-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, code blocks, command output, and synchronized project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include execution logs, status values, and changed project files.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

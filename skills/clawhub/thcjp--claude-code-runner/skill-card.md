## Description: <br>
Claude Code Runner helps agents execute programming tasks through PTY-based Claude Code invocation, including code review, refactoring, debugging, testing, and deployment support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation workflow owners use this skill to delegate coding tasks such as code review, bug fixing, refactoring, testing, and deployment assistance to a command-capable agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can execute commands and write files, which may alter repositories or environments beyond the intended task. <br>
Mitigation: Install and run it only in trusted repositories or isolated workspaces, review proposed actions before execution, and keep backups or version control available for recovery. <br>
Risk: The documentation does not clearly scope or warn about the breadth of command execution and file-write capability. <br>
Mitigation: Require human review before installation and use, and document local permission boundaries before delegating tasks to the skill. <br>
Risk: The artifact mentions root or sudo use for user switching, which can increase impact if commands are incorrect or unsafe. <br>
Mitigation: Avoid sudo or root privileges unless a specific task requires them and a user explicitly approves that elevated execution. <br>
Risk: The artifact claims sandboxed command execution, but server security guidance says not to rely on that claim without separate containment. <br>
Mitigation: Use an external sandbox, container, disposable checkout, or least-privilege runtime when command execution or file writes are possible. <br>


## Reference(s): <br>
- [Claude Code Runner on ClawHub](https://clawhub.ai/thcjp/skills/claude-code-runner) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, code snippets, shell commands, and structured JSON-style status responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include command results, file changes, diagnostics, and task status metadata depending on the invoking agent.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

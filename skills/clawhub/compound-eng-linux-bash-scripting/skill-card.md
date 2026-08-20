## Description:

Defensive Bash scripting for Linux covering safe foundations, argument parsing, production patterns, and ShellCheck compliance for bash scripts, shell scripts, cron jobs, and CLI tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to draft and review Linux Bash scripts for automation, deployment, backup, cron, and CLI workflows with safer shell idioms and lint-oriented practices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated shell scripts can affect system paths or perform destructive operations if applied without review.

Mitigation: Review generated scripts before execution, especially commands that touch system paths or delete, overwrite, move, or chmod files.

Risk: Generated Bash examples may still require local validation for project-specific inputs, dependencies, and edge cases.

Mitigation: Run ShellCheck with all checks enabled and shfmt in diff mode, then test empty input, missing files, and paths containing spaces before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-linux-bash-scripting)
- [ClawHub publisher profile](https://clawhub.ai/user/iliaal)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with Bash code blocks and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets GNU Bash 4.4+ on Linux and expects ShellCheck and shfmt verification.]

## Skill Version(s):

4.4.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

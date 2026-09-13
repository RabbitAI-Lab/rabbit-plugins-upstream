## Description:

Defensive Bash scripting for Linux: safe foundations, argument parsing, production patterns, ShellCheck compliance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to draft and review GNU Bash 4.4+ scripts for Linux automation, CLI tools, cron jobs, and deployment tasks with safer argument parsing, process handling, file operations, and ShellCheck/shfmt validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended Bash script foundation includes an unsafe cleanup trap that can delete caller-controlled paths when sourced.

Mitigation: Review generated scripts before use; install cleanup traps only for direct execution, after a script-created temporary directory exists, and validate any path before deletion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-linux-bash-scripting)
- [Input and process safety](./references/input-and-process-safety.md)
- [Production patterns](./references/production-patterns.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with Bash code blocks and concise implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Linux Bash 4.4+ focus; advises ShellCheck and shfmt validation.]

## Skill Version(s):

4.5.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

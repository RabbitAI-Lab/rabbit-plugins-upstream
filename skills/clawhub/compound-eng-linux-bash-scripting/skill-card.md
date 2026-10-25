## Description:

Provides defensive Linux Bash scripting guidance for safe foundations, argument parsing, production patterns, and ShellCheck compliance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to write and review defensive Bash scripts, cron jobs, and CLI automation for Linux.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated scripts may replace files, change permissions, or run cleanup commands on production systems.

Mitigation: Review generated scripts and their targets before running them on real systems.

Risk: Locking or sudo-mediated copies may affect shared resources or privileged files.

Mitigation: Check lock scope and elevated file operations before execution.

## Reference(s):

- [Input and process safety](references/input-and-process-safety.md)
- [Production patterns](references/production-patterns.md)
- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-linux-bash-scripting)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Linux GNU Bash 4.4+; recommends ShellCheck and shfmt validation]

## Skill Version(s):

5.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

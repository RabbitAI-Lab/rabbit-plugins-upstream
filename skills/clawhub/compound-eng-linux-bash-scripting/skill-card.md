## Description:

Provides defensive Bash scripting guidance for Linux, including safe foundations, argument parsing, production patterns, and ShellCheck compliance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to write and review safer Linux Bash scripts for CLI tools, cron jobs, backups, and deployment automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated scripts may delete files or alter system configuration with elevated privileges.

Mitigation: Review commands, paths, and permissions before execution; use a dry run when possible.

Risk: Scripts that fetch URLs or automate releases may act on unintended inputs or publish changes.

Mitigation: Check external sources and release targets, and require operator review before running.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iliaal/skills/compound-eng-linux-bash-scripting)
- [Input and process safety](artifact/references/input-and-process-safety.md)
- [Production patterns](artifact/references/production-patterns.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets GNU Bash 4.4+ on Linux; recommends ShellCheck and shfmt validation.]

## Skill Version(s):

5.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

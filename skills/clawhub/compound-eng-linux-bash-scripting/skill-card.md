## Description:

Provides defensive Bash scripting guidance for Linux, including safe foundations, argument parsing, production patterns, and ShellCheck compliance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to write and review safer Linux Bash scripts for automation, cron jobs, and command-line tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated scripts may change or delete files, alter system configuration, or expose secrets when executed without review.

Mitigation: Review scripts before running them, especially commands involving rm, sudo, /etc, curl, locks, cron jobs, or secrets.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-linux-bash-scripting)
- [Input and process safety](artifact/references/input-and-process-safety.md)
- [Production patterns](artifact/references/production-patterns.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets GNU Bash 4.4+ on Linux; recommends ShellCheck and shfmt validation.]

## Skill Version(s):

5.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

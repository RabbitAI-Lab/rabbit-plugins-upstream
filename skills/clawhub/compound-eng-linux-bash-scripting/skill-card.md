## Description:

Defensive Bash scripting for Linux: safe foundations, argument parsing, production patterns, ShellCheck compliance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when asking an agent to write or review Linux Bash scripts, shell automation, cron jobs, deployment scripts, backups, or CLI tooling with defensive conventions and ShellCheck-oriented output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Bash may include destructive operations, privileged paths, cron-style automation, or sudo-adjacent workflows.

Mitigation: Review generated scripts before running them, especially in production or as root, and verify destructive paths, privileges, and scheduling behavior.

Risk: The skill can produce shell commands and scripts that depend on local environment assumptions or missing tooling.

Mitigation: Run ShellCheck, shfmt, and functional edge-case tests before deployment; if those tools are unavailable, report the skipped checks and at minimum run Bash syntax validation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-linux-bash-scripting)
- [Publisher profile](https://clawhub.ai/user/iliaal)
- [input-and-process-safety.md](artifact/references/input-and-process-safety.md)
- [production-patterns.md](artifact/references/production-patterns.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with Bash code blocks and concise implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets GNU Bash 4.4+ on Linux and emphasizes ShellCheck and shfmt verification.]

## Skill Version(s):

4.6.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

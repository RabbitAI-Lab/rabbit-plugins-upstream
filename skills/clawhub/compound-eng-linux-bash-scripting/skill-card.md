## Description:

Provides defensive Linux Bash scripting guidance for safe argument parsing, production automation, and ShellCheck-compliant scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to write and review defensive Bash scripts, cron jobs, and Linux CLI automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated scripts may delete files, use elevated privileges, or change production systems.

Mitigation: Review scripts and their targets before execution, particularly destructive commands and sudo usage.

Risk: Scripts handling secrets may expose credentials if run without care.

Mitigation: Review secret handling before running; keep secrets out of process arguments and shell tracing.

## Reference(s):

- [Input and process safety](references/input-and-process-safety.md)
- [Production patterns](references/production-patterns.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets GNU Bash 4.4+ on Linux; recommends ShellCheck and shfmt checks.]

## Skill Version(s):

5.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

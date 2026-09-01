## Description:

Defensive Bash scripting for Linux: safe foundations, argument parsing, production patterns, ShellCheck compliance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when writing, reviewing, or improving GNU Bash scripts, cron jobs, shell automation, and Linux CLI tooling. It focuses on safer Bash foundations, argument parsing, production patterns, and ShellCheck/shfmt compliance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Bash can include destructive file operations, privileged path writes, or commands with broad filesystem effects.

Mitigation: Review proposed scripts before running them, require explicit path validation, and use dry-run or staged execution for risky file operations.

Risk: Scripts that call networks or handle secrets can expose credentials or perform unintended requests.

Mitigation: Review network and secret-handling commands, keep secrets out of command arguments and logs, and prefer explicit environment or stdin handling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-linux-bash-scripting)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bash-focused guidance for Linux and GNU Bash 4.4+; generated scripts should be reviewed before execution.]

## Skill Version(s):

4.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

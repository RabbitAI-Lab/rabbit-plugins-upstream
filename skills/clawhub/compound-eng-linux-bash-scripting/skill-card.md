## Description:

Defensive Bash scripting guidance for Linux that covers safe foundations, argument parsing, production patterns, and ShellCheck-compliant scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to draft or review GNU Bash 4.4+ Linux automation, cron, deployment, and CLI scripts with safer input handling, process control, cleanup, and ShellCheck/shfmt validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated scripts may inherit an unsafe cleanup trap pattern that can delete an unintended path.

Mitigation: Register cleanup traps inside main only after creating and validating a private temporary directory; review generated cleanup logic before execution.

## Reference(s):

- [Input and process safety](references/input-and-process-safety.md)
- [Production patterns](references/production-patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Bash code blocks and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Designed for GNU Bash 4.4+ on Linux; generated scripts should be checked with ShellCheck and shfmt when available.]

## Skill Version(s):

4.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

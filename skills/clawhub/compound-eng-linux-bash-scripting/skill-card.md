## Description:

Guides developers in writing defensive Linux Bash scripts, including argument parsing, safe automation patterns, and ShellCheck compliance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to draft and review Linux Bash scripts for CLI tools, cron jobs, and production automation with safer input handling, file operations, and process management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated scripts may delete files or alter system paths.

Mitigation: Review destructive operations, target paths, and required permissions before running the script.

Risk: Network calls or unattended cron and production runs can have unintended effects.

Mitigation: Review external calls and test the script in a safe environment before scheduling or deploying it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-linux-bash-scripting)
- [Input and process safety](references/input-and-process-safety.md)
- [Production patterns](references/production-patterns.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Bash code and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets GNU Bash 4.4+ on Linux; review and lint generated scripts before execution.]

## Skill Version(s):

5.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

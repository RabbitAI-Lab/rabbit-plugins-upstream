## Description:

Provides defensive Linux Bash scripting guidance for safe foundations, argument parsing, production patterns, and ShellCheck-compliant scripts, cron jobs, and CLI tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to write or review GNU Bash 4.4+ scripts for Linux automation, including shell scripts, cron jobs, deployment scripts, backup rotation, and CLI tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated scripts may copy the cleanup trap pattern and recursively delete an inherited or unvalidated temporary-directory path.

Mitigation: Initialize temporary-directory variables with mktemp before registering deletion traps, validate the path, and remove only directories created by the script.

Risk: Bash guidance can produce scripts that perform destructive filesystem or deployment actions.

Mitigation: Review generated scripts before execution, run ShellCheck and shfmt, and test edge cases such as missing files, empty input, and paths containing spaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-linux-bash-scripting)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with Bash code blocks and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated or revised Bash scripts, validation commands, and review guidance.]

## Skill Version(s):

4.5.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

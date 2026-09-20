## Description:

Runs the rest of a /shell request as a literal shell command when the user explicitly invokes /shell and wants the following text executed directly in the terminal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when they explicitly want an agent to run a raw shell command exactly as written after /shell and report the exit status and important output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user-provided /shell command can perform destructive or unintended terminal actions because the skill is designed to execute the command literally.

Mitigation: Invoke the skill only with explicit /shell requests and review each command carefully before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eohmig/skills/shell)

## Skill Output:

**Output Type(s):** [Shell commands, Text]

**Output Format:** [Terminal execution followed by a concise text summary of exit status, stdout, and stderr]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Model invocation is disabled; behavior is based on explicit command execution output.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

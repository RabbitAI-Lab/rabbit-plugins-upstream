## Description:

Sanitizes log content by removing passwords, tokens, and other sensitive patterns before logs are shared or analyzed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operations teams, and automation users use this skill to sanitize log content in JSON, text, or Markdown by removing secrets such as passwords and tokens before analysis, monitoring, or sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad read, write, and command execution access could expose or modify files outside the intended log-sanitization task.

Mitigation: Use the skill only on logs or files intentionally provided, constrain paths and commands, and require confirmation before writes or monitoring workflows.

Risk: Sanitized output may still contain secrets if a sensitive pattern is missed.

Mitigation: Review sanitized output before sharing and update sensitive-pattern coverage for new password, token, and key formats.

Risk: Command execution in the workflow can be unsafe if unrestricted.

Mitigation: Run in a sandboxed agent environment, allowlist commands, and avoid passing untrusted input directly into shell commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/expanso-log-sanitize)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional JSON-like execution results and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read provided log content, write sanitized output when authorized, and execute commands in a constrained agent environment.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

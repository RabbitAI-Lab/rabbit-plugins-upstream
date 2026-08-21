## Description:

Provides agent workflow guidance for batch and concurrent code-execution tasks with audit logging, CI/CD integration, and configuration examples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to guide agents through code execution, batch task orchestration, audit logging, CI/CD workflows, and related troubleshooting. It is intended for technical development and automation workflows rather than general non-technical use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports broad code execution workflows that may modify files, run package installs, or affect credentials.

Mitigation: Use it only in disposable or tightly scoped repositories, require explicit approval for file-changing commands and package installs, and avoid root or sudo unless necessary.

Risk: The artifact describes generic auto-confirmation behavior and password entry through EXEC_PASSWORD, which can approve unsafe prompts or expose sensitive credentials.

Mitigation: Disable generic auto-confirmation, do not inject passwords automatically, and require explicit review for commands that request credentials or confirmation.

Risk: CI/CD execution can amplify mistakes across shared projects or deployment environments.

Mitigation: Require human approval before CI/CD use, scope environment variables narrowly, and review audit logs after each run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/code-runner-tool-pro)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with inline code blocks and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include executable command examples, CI/CD snippets, audit-log paths, and configuration guidance.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

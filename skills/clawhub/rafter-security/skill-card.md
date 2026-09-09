## Description:

Security toolkit for AI workflows that helps scan code and repositories for vulnerabilities, audit third-party skills, MCPs, and agent configs, evaluate shell commands before execution, and generate secure design questions for new features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafter](https://clawhub.ai/user/rafter)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to run Rafter-backed security checks for code, commands, agent extensions, and security-design review workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a locally installed Rafter CLI and can route commands through Rafter command execution workflows.

Mitigation: Install and use the Rafter CLI only from a trusted source, review enabled hooks from `rafter agent init --all`, and verify dry-run behavior before treating command classification as non-executing.

Risk: `/rafter-bash` and `rafter agent exec <command>` may execute commands unless a verified dry-run mode is used.

Mitigation: Use explicit dry-run or review modes for command-risk checks, inspect the command before approval, and avoid routing untrusted commands into execution workflows.

## Reference(s):

- [Rafter homepage](https://rafter.so)
- [Rafter Security on ClawHub](https://clawhub.ai/rafter/skills/rafter-security)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and structured security review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference RAFTER_API_KEY for remote scans; local secrets scanning can run without it.]

## Skill Version(s):

0.10.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

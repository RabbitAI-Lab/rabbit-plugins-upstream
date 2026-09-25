## Description:

This skill helps an agent manage macOS system functions, including system information, process management, volume and brightness control, network and power actions, screenshots, clipboard use, and Finder operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and engineers use this skill to ask an agent to inspect or change macOS system state during administration and workflow automation tasks. It is appropriate only where local command execution and system-setting changes are expected.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad local command, read, and write access for macOS system-control tasks.

Mitigation: Install and run it only in environments where the agent is expected to execute local commands and change system settings.

Risk: Screenshots, clipboard access, process termination, network changes, file writes, and power actions can expose data or disrupt the host system.

Mitigation: Require explicit user confirmation before those actions and avoid approving vague productivity requests.

Risk: The security evidence flags the release as suspicious because the scope and user-control details are not sufficiently constrained.

Mitigation: Review the skill carefully before installation and restrict use to deliberate macOS administration workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/mac-system-control)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured text, with command-oriented instructions and status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or execute macOS system-control actions through the host agent's local tools.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

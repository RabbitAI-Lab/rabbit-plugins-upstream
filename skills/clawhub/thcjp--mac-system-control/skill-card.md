## Description:

Controls macOS system functions, including system information, process management, volume and brightness, network and power settings, screenshots, clipboard, and Finder operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent users can use this skill to inspect and control local macOS settings and workflows through an AI agent. It is intended for deliberate system administration tasks such as checking status, managing processes, adjusting settings, and capturing local system context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can request broad local system-control actions, including process termination, network or power changes, screenshots, clipboard access, and file modification.

Mitigation: Use it only for explicit local administration requests and require confirmation before actions that alter system state, expose screen or clipboard contents, or modify files.

Risk: The security evidence warns that the skill's command boundaries are unclear and its sandbox claims should not be assumed.

Mitigation: Rely on host-enforced sandboxing, command approvals, and least-privilege permissions rather than the skill text alone.

Risk: The artifact presents macOS-specific behavior while also making contradictory platform claims.

Mitigation: Validate the target operating system before use and decline device-control requests that do not match the supported macOS behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/mac-system-control)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or JSON with command, status, and confirmation details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May involve local system-control actions when the host agent permits them.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Guides troubleshooting of vx installation, version, PATH, runtime, and configuration issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to diagnose vx failures and choose repair steps for installations, versions, command resolution, runtime dependencies, and configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands may run unreviewed code.

Mitigation: Require explicit approval; verify download sources and inspect scripts before execution.

Risk: Reset, forced sync, elevated commands, or PATH shim changes may delete state or replace executables.

Mitigation: Back up configuration, inspect affected files and ownership, and get explicit approval before destructive or privileged repairs.

Risk: Issue-tracker instructions go beyond vx troubleshooting and may publish unrelated information.

Mitigation: Keep tracker updates within the user's authorized task and require approval before posting comments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/loonghao/skills/vx-troubleshooting)
- [vx documentation](https://github.com/loonghao/vx#readme)
- [Managed command shim guide](https://github.com/loonghao/vx/blob/main/docs/guide/managed-command-shims.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diagnostic and repair guidance; commands require review before execution.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

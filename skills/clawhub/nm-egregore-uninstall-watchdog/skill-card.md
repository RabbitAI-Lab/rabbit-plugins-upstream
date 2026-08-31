## Description:

Removes the egregore watchdog daemon and its associated files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to remove an installed egregore watchdog service, clean up its local files, and disable automatic egregore session relaunching.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cleanup commands remove local watchdog service files, pid files, and logs.

Mitigation: Use the skill only when the egregore watchdog is installed and automatic relaunching should be disabled; review the listed paths first if the watchdog setup was customized.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-egregore-uninstall-watchdog)
- [Egregore homepage](https://github.com/athola/claude-night-market/tree/master/plugins/egregore)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance]

**Output Format:** [Markdown with bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target local launchd or systemd user service files, pid files, and watchdog logs.]

## Skill Version(s):

1.9.19 (source: server release evidence; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Launch and coordinate agent sessions inside the Orca IDE runtime, including sending prompts to existing terminals, launching new worktree sessions, and installing Orca skills into supported agent harnesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to coordinate Orca-managed coding-agent sessions, route prompts to the right terminal, start new agent worktrees, and install Orca skill bundles into compatible harnesses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent cross-harness installs and mutable symlinks can change which Orca skills a harness loads over time.

Mitigation: Review the source and destination before installing, and prefer project-scoped or copied installs unless live updates are intentional.

Risk: Command examples that include task names or prompt text can be unsafe if interpolated through a shell.

Mitigation: Treat user-supplied task names and prompts as argument values that must be escaped or passed without shell interpolation.

Risk: Sending a prompt to the wrong Orca terminal can cause an unrelated agent session to act on unrelated work.

Mitigation: Use the documented list, filter, disambiguate, and deliver flow, including self-exclusion and mandatory user disambiguation when multiple candidates match.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/orca)
- [Orca session management guide](SKILL.md)
- [Send topic guide](send.md)
- [Launch topic guide](launch.md)
- [Install topic guide](install.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts users to disambiguate terminal targets and installation choices before taking actions that could affect other sessions or harness configuration.]

## Skill Version(s):

0.2.1 (source: release metadata and changelog, released 2026-09-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

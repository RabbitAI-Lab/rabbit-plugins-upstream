## Description:

Launch and coordinate agent sessions inside the Orca IDE runtime by sending prompts to selected terminals, launching new agent worktrees, and installing Orca's bundled skills into supported harnesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to coordinate agent sessions in Orca IDE, including targeted prompt delivery, new agent session launch, and harness setup for Orca's bundled skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A prompt could be delivered to an unintended Orca terminal session.

Mitigation: Resolve candidates first, exclude the caller's own pane, require user disambiguation when multiple terminals match, and read the selected terminal before sending.

Risk: The helper can use a different Orca CLI executable if ORCA_CLI_COMMAND is changed.

Mitigation: Keep Orca-related environment variables under user control and stop on CLI resolution failures instead of falling through to another executable.

Risk: Install workflows may modify harness plugin or configuration locations.

Mitigation: Run install actions only after an explicit user choice and report what was actually verified after file or plugin changes.

## Reference(s):

- [Orca skill on ClawHub](https://clawhub.ai/drumrobot/skills/orca)
- [Publisher profile](https://clawhub.ai/user/drumrobot)
- [Send topic guide](send.md)
- [Launch topic guide](launch.md)
- [Install topic guide](install.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-directed instructions for Orca IDE session management; no independent binary artifact is generated.]

## Skill Version(s):

0.2.0 (source: release evidence and changelog, released 2026-09-01; SKILL.md frontmatter reports 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

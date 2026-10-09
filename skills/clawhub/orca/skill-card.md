## Description:

Helps agents find and message Orca IDE sessions, launch new sessions, and install Orca skills into supported agent tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers using Orca IDE can locate a live agent terminal, send it a confirmed prompt, launch another agent session, or install Orca's skill bundle into Claude Code, OpenClaw, or Antigravity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A prompt sent to the wrong terminal could trigger unintended work.

Mitigation: Confirm the live target and exact prompt with the user before sending.

Risk: New sessions and worktrees can consume resources or alter workspace state.

Mitigation: Request approval for new worktrees and close unused sessions.

Risk: Installing the bundled skills changes agent plugin and configuration directories.

Mitigation: Review proposed writes to Claude Code, OpenClaw, and Antigravity settings before installation.

## Reference(s):

- [Orca on ClawHub](https://clawhub.ai/drumrobot/skills/orca)
- [Send guide](send.md)
- [Launch guide](launch.md)
- [Install guide](install.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May send prompts to live sessions, start agent terminals, or modify plugin configuration after user confirmation.]

## Skill Version(s):

0.5.0 (source: ClawHub release and CHANGELOG; skill frontmatter still says 0.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

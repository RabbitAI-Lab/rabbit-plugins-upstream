## Description:

Coordinates Orca IDE agent sessions by finding and messaging running terminals, launching new sessions, and guiding installation of Orca skills into other agent harnesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers using Orca can identify and message a specific running agent session, launch an agent in a pane or worktree, and install Orca's bundled skills in supported harnesses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A prompt could reach the wrong agent session or carry an unapproved payload.

Mitigation: Confirm the exact recipient and prompt with the user before sending; do not rely solely on the included hooks.

Risk: Launching agents or registering repositories could create unintended sessions or tracked workspaces.

Mitigation: Obtain explicit approval for the target and launch, and review repository registration before execution.

Risk: Installation can modify harness plugin configuration and symlinks.

Mitigation: Review proposed configuration and symlink changes before applying them.

## Reference(s):

- [Orca on ClawHub](https://clawhub.ai/drumrobot/skills/orca)
- [Send guide](artifact/send.md)
- [Launch guide](artifact/launch.md)
- [Install guide](artifact/install.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can direct actions in other agent sessions and changes to local harness configuration.]

## Skill Version(s):

0.5.1 (source: release metadata and CHANGELOG; skill frontmatter still says 0.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

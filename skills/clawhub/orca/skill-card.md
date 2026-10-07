## Description:

Coordinates agent sessions in Orca IDE, including sending work to running terminals, launching sessions, and installing Orca skills into supported agent harnesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to find and coordinate Orca agent sessions, start agents in terminals or worktrees, and install Orca's bundled skills into other agent harnesses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sending a prompt to the wrong active agent or launching a new agent can cause unintended work.

Mitigation: Confirm the target session and exact prompt with the user before sending, and confirm the intended agent and workspace before launch.

Risk: Installing skills can change another harness's plugin configuration or remove stale symlinks.

Mitigation: Confirm the installation method and review configuration paths and symlink removals before applying changes.

## Reference(s):

- [Orca skill on ClawHub](https://clawhub.ai/drumrobot/skills/orca)
- [Send topic](send.md)
- [Launch topic](launch.md)
- [Install topic](install.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request user confirmation before sending prompts, launching sessions, or changing installation settings.]

## Skill Version(s):

0.4.1 (source: ClawHub release metadata and CHANGELOG, released 2026-09-30)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

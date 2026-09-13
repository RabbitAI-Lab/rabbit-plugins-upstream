## Description:

Tracks in-session work progress by registering multi-step tasks, updating status, and guiding resume or cleanup workflows across Claude Code and Antigravity environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to keep multi-step work visible, recover task state after compaction, and decide how to proceed with remaining items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hooks can influence edit tools and task-deletion behavior.

Mitigation: Review or disable hook scripts before installation, and require explicit confirmation before deleting task state.

Risk: The skill may inspect conversation logs or persist state outside the workspace.

Mitigation: Audit the documented home-directory paths and cache writes before enabling the skill in shared or sensitive environments.

Risk: External status checks may use gh, curl, or ssh.

Mitigation: Review proposed commands before execution and run them only with appropriate credentials and network access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/wip)
- [Claude Code WIP guide](artifact/claude.md)
- [Antigravity WIP tracking guide](artifact/antigravity.md)
- [Resume workflow guide](artifact/resume.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands and checklist updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose task-list updates, persistent checklist entries, WIP commit guidance, or hook configuration depending on the agent environment.]

## Skill Version(s):

0.7.1 (source: release metadata and CHANGELOG, released 2026-09-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

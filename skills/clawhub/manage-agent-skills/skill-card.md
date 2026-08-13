## Description:

Manage Agent Skills helps agents audit, search, enable, disable, set Claude Code visibility states, and apply presets for installed skills across Codex, Claude Code, GitHub Copilot CLI, OpenClaw, and Hermes without deleting skill files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yunze7373](https://clawhub.ai/user/yunze7373)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to audit and safely toggle installed agent skills across supported hosts, reduce idle context, keep rarely used skills manual, and apply host-specific presets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad selectors such as all or group-based presets can persistently change which skills an agent can use.

Mitigation: Use dry-run first, resolve exact skill names with search, and review the reported platform, affected skills, config path, and backup path before applying changes.

Risk: Local configuration changes can require a new agent session or gateway restart before behavior matches the reported state.

Mitigation: Report whether a new session or restart is required after each mutation and keep backups for recovery.

Risk: Host-specific overrides or allowlists can make a skill appear enabled in one configuration layer while remaining unavailable in the host.

Mitigation: Check platform-specific status and support boundaries, especially Claude Code project/local settings and OpenClaw agent allowlists.

## Reference(s):

- [Manage Agent Skills on ClawHub](https://clawhub.ai/yunze7373/skills/manage-agent-skills)
- [Platform support](references/platforms.md)
- [Preset file format](references/presets.md)
- [Agent Skills specification](https://agentskills.io/specification)
- [Codex app-server skill config methods](https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code settings](https://code.claude.com/docs/en/settings)
- [GitHub Copilot CLI skill commands](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference)
- [OpenClaw skills](https://docs.openclaw.ai/tools/skills)
- [Hermes Agent skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/)
- [Hermes Agent configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command examples and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run previews, affected skills, config path, backup path, and whether a new agent session or gateway restart is required.]

## Skill Version(s):

0.1.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

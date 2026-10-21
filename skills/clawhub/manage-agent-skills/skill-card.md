## Description:

Audit installed Agent Skills and manage their host-specific visibility across Codex, Claude Code, Copilot CLI, OpenClaw, Hermes, and Antigravity. Use for skill inventory, duplicate or malformed metadata diagnosis, exact enable/disable changes, Claude visibility states, and reusable presets. Does not install skills or measure actual model token usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yunze7373](https://clawhub.ai/user/yunze7373)

### License/Terms of Use:

MIT-0

## Use Case:

Developers can inventory, audit, and locate installed skills, then safely adjust skill visibility for a selected coding-agent host. The skill supports exact changes and reusable presets, while reporting configured state and recovery information without installing skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configuration backups may contain secrets.

Mitigation: Keep backup paths private and restrict access.

Risk: Interrupted or batched changes may leave state uncertain or partially updated.

Mitigation: Preview exact platforms and targets before applying changes; inspect current state and recovery paths after interruption.

Risk: Configured visibility may differ from what the host actually exposes because other configuration layers can affect it.

Mitigation: Verify the resulting visibility in the host after making changes.

## Reference(s):

- [Auditing and recovery](references/auditing.md)
- [Supported platforms](references/platforms.md)
- [Preset file format](references/presets.md)
- [Codex skills guide](https://learn.chatgpt.com/docs/build-skills)
- [Codex configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Claude Code skills documentation](https://code.claude.com/docs/en/skills)
- [ClawHub skill page](https://clawhub.ai/yunze7373/skills/manage-agent-skills)
- [Publisher profile](https://clawhub.ai/user/yunze7373)

## Skill Output:

**Output Type(s):** [text, JSON, configuration, guidance]

**Output Format:** [Text or JSON status, audit, and search reports; host-specific settings updates for requested changes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected host, its configuration layers, and the exact target; reports distinguish configured state from live host behavior.]

## Skill Version(s):

1.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

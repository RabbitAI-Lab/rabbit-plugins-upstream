## Description:

Restructures oversized SKILL.md files into an entry point and on-demand skill packs, and helps summarize and transfer long-conversation context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Developers using Codex, Claude Code, or Cursor use the skill to restructure oversized skills, create and validate routing indexes, and package conversation summaries for handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Multi-section extraction may lose content.

Mitigation: Keep the generated backup and review the extracted files and resulting skill before replacing the original.

Risk: Conversation-resume triggers may activate too broadly.

Mitigation: Use resume and import actions only for explicit user requests, and review the selected snapshot before continuing.

Risk: Conversation-derived exports may expose sensitive information.

Mitigation: Inspect snapshots and archives for private content, then confirm the intended recipients before sharing.

Risk: The security scan did not fully inspect one referenced script.

Mitigation: Review the uninspected script and its behavior before relying on the package.

## Reference(s):

- [ClawHub release](https://clawhub.ai/lisong2003-lgtm/skills/skill-architect)
- [Long conversation summary guidance](references/长对话归纳最佳实践.md)
- [Cross-user transfer guidance](references/跨用户传输最佳实践.md)
- [Trigger priority and troubleshooting](references/触发优先级与故障排查.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown, JSON, generated skill files, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create snapshots, routing indexes, skill-pack files, backups, and handoff archives.]

## Skill Version(s):

0.3.7 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

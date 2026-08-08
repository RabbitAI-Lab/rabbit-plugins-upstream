## Description:

Wdp Ctx helps an agent save, load, verify, export, list, and clear persistent project-context profiles and snapshots so work can resume across sessions or agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckystar513](https://clawhub.ai/user/luckystar513)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding-agent users use this skill to preserve project context across session resets, context compaction, and agent handoffs. It creates and reloads stable project profiles, timestamped work snapshots, drift checks, and compact exports for other agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved profiles, snapshots, or exports may summarize private project details.

Mitigation: Review generated context before sharing or exporting it, and record credential locations rather than secret values.

Risk: Clearing saved context can remove project memory that an agent may need later.

Mitigation: Review the deletion list and confirmation prompt carefully, and use retention options when only older snapshots should be removed.

Risk: Exporting context can add generated project-state material to AGENTS.md.

Mitigation: Review the generated section before relying on it or sharing the repository.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/luckystar513/wdp-ai-skills/tree/main/skills/wdp-ctx)
- [ClawHub skill page](https://clawhub.ai/luckystar513/skills/wdp-ctx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown context documents and concise text responses with command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local profile, snapshot, latest pointer, and optional AGENTS.md export files.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

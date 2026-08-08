## Description:

Save, load, verify, export, or clear a project's stable profile and incremental work snapshots to enable session-resilient context management in English.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckystar513](https://clawhub.ai/user/luckystar513)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to preserve and resume project context across session resets, context compaction, agent switching, and handoffs. It separates stable project profile information from volatile work snapshots and can export a compact AGENTS.md handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local context summaries may capture sensitive project details such as architecture, work status, file names, decisions, and credential locations.

Mitigation: Review generated profile, snapshot, and AGENTS.md content before sharing a repository or machine, and avoid recording secret values.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/luckystar513/wdp-ai-skills/tree/main/skills/wdp-ctx-en)
- [ClawHub skill page](https://clawhub.ai/luckystar513/skills/wdp-ctx-en)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown documents and concise terminal-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces or updates local profile, snapshot, latest pointer, and AGENTS.md context files when requested.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

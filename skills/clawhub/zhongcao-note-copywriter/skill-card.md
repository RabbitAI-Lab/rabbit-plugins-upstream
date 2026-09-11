## Description:

Create Xiaohongshu or REDnote copy from a product, experience, topic, or audience brief, including title options, a structured note body, cover wording, relevant hashtags, a natural comment starter, an optional matching vertical 3:4 cover, and optional Xiaohongshu research from platform notes, comments, and account activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to turn a product, experience, topic, or audience brief into Xiaohongshu or REDnote-ready copy, including titles, a structured note body, cover wording, hashtags, and a comment starter. When approved, it can also prepare and run a matching vertical cover generation and optionally use paid Xiaohongshu lookup for grounded research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device token with broad media, artifact, task, and wallet-spending authority.

Mitigation: Install only when those account powers are acceptable, review account scopes and spending controls before use, and revoke the device authorization when it is no longer needed.

Risk: Package files silently self-update by default.

Mitigation: Consider disabling automatic updates with the documented update command and review package changes before continuing sensitive work.

Risk: Optional Xiaohongshu lookup and cover generation can spend Beatra credits.

Mitigation: Require separate approval for each paid lookup or cover generation, show current pricing before execution, and report returned billing fields after completion.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/zhongcao-note-copywriter)
- [Package homepage](https://beatra.ai/skills/zhongcao-note-copywriter)
- [REDnote note copy workflow](references/workflow.md)
- [Reading Xiaohongshu](references/note-lookup.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands, files]

**Output Format:** [Markdown containing note copy, hashtags, review notes, approval prompts, and optional generated cover artifact links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The normal deliverable is text copy; optional Xiaohongshu lookup and cover generation are paid actions that require separate approval and billing reporting.]

## Skill Version(s):

0.1.6 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Structured memory architecture for hierarchical storage, daily logging, weekly compaction, and proactive memory hygiene.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to give an agent a repeatable memory practice based on daily logs, project and people files, decision records, an index, and periodic compaction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to create long-lived memory files and archives that may retain confidential, personal, legal, medical, financial, or credential-related information.

Mitigation: Require explicit memory rules for consent, redaction, sensitive-data exclusions, and retention limits before using it in workspaces that may contain sensitive information.

Risk: The skill broadly encourages recording user, project, and people details without clear user-control boundaries.

Mitigation: Review proposed memory entries before persistence and give users a clear way to exclude, revise, or remove stored details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/koompi-memory)
- [Publisher profile](https://clawhub.ai/user/zuoyunlai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown memory files and concise text status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and updates workspace memory files such as MEMORY.md and memory/daily/YYYY-MM-DD.md.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

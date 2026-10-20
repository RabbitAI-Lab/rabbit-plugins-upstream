## Description:

Reviews completed agent tasks, distills reusable experience into a skill or memory, and records the resulting capability update.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Agent operators and developers use this skill to review completed work, distinguish reusable procedures from factual memories, and update an agent's capability record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers could turn session content into persistent skills or memories without deliberate approval.

Mitigation: Restrict activation to a dedicated command and require explicit user or administrator confirmation before write-back.

Risk: Sensitive session details may be retained in long-lived capability records.

Mitigation: Redact sensitive session content before saving any skill, memory, or evolution record.

Risk: Declared permissions do not clearly match the described write and search behavior.

Mitigation: Reconcile actual write and search access with declared permissions before enabling automation.

## Reference(s):

- [Agent Evolution on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-evolution)
- [LGD governance theory reference linked by the skill](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [JSON evolution record and text confirmation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Classifies experience as Skill or Memory and may update a capability record.]

## Skill Version(s):

1.1.0 (source: ClawHub release; bundled skill frontmatter says 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Audits installed AI skills, classifies them, and recommends keep, archive, or uninstall actions to keep an agent skill set lean and focused.

This skill is ready for commercial/non-commercial use.

## Publisher:

[helloyxs](https://clawhub.ai/user/helloyxs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI assistant users use this skill to audit installed agent skills, classify their value, and decide which skills to keep, archive, or uninstall.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enumerates local installed skills and reports names, paths, descriptions, sizes, and modification times.

Mitigation: Review the report before sharing it and avoid exposing paths or skill descriptions that reveal sensitive workspace context.

Risk: Keep, archive, or uninstall recommendations may rely on inferred usage or business relevance.

Mitigation: Review recommendations yourself and approve only cleanup actions you actually want performed.

Risk: Archive or uninstall operations change the local skill set.

Mitigation: Proceed only after explicit confirmation and preserve key configuration content when archiving.

## Reference(s):

- [Evaluation Framework](references/evaluation_framework.md)
- [English Audit Report Example](examples/audit_report_en.md)
- [Chinese Audit Report Example](examples/audit_report_zh.md)
- [ClawHub Skill Page](https://clawhub.ai/helloyxs/skills/skill-subtraction)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown audit report with optional shell commands and JSON scan data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bilingual English or Chinese output; cleanup actions require explicit user confirmation.]

## Skill Version(s):

1.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Text to Infographic helps agents turn complex source material into a structured single-page infographic plan and draft SVG, whiteboard, and document adapters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users can use this skill to compress workflows, frameworks, analysis notes, plans, dashboards, or knowledge summaries into editable overview visuals. It is best suited for one-page explanation, summary, comparison, diagnosis, planning, persuasion, and dashboarding tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Lark, Feishu, or whiteboard tooling may access external accounts or mutate external documents when connected.

Mitigation: Review tool permissions and generated adapter drafts before connecting live accounts or applying changes.

Risk: Compressing complex material into one overview visual can omit nuance or imply precision that the source material does not support.

Mitigation: Review the generated plan for assumptions, omitted detail, labels, and metrics before publishing or using it for decisions.

## Reference(s):

- [README](README.md)
- [Infographic plan schema](schemas/infographic-plan.schema.json)
- [Plan validator](scripts/validate_infographic_plan.py)
- [Adapter draft builder](scripts/build_infographic_adapters.py)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON infographic plans and adapter draft files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans follow schemas/infographic-plan.schema.json; adapter drafts may target SVG, whiteboard, and companion document workflows.]

## Skill Version(s):

0.1.0 (source: SKILL.md frontmatter, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

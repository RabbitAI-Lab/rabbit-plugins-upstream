## Description:

帮助学生归档具体错题、定位通用错因并跟踪反复出现的薄弱知识点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students use the skill after homework or practice to review a specific wrong answer, identify its likely cause, and prepare targeted review materials. Elementary students should use it with a parent or teacher present.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wrong-answer records may contain sensitive student information, and sharing with parents or companion skills can broaden access.

Mitigation: Choose record, sharing, and reminder controls deliberately, confirm consent, and review the host platform's storage and companion-skill behavior; use the documented pause, delete, and export controls as needed.

Risk: A student may disclose a safety or crisis concern during an academic review.

Mitigation: Follow the crisis exception and referral protocol, stop the normal learning workflow, and direct the student to a trusted adult and the appropriate local help channel.

## Reference(s):

- [ClawHub release](https://clawhub.ai/qizhitang/skills/xiaozhi-correction-notebook)
- [Error Analysis Framework](references/error-analysis-framework.md)
- [Crisis Referral Protocol](shared/crisis-referral-protocol.md)
- [Handover Protocol Schema](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON]

**Output Format:** [Conversational text, Markdown reports, and consent-gated JSON handover proposals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Record writeback is proposed for confirmation; data storage and companion integrations depend on the host platform.]

## Skill Version(s):

2.12.5 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps math teachers design diagnostic assessment blueprints, two-way specification tables, item selection notes, item statistics, and teacher-confirmed writeback proposals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

External math teachers and education operators use this skill to plan middle-school math assessments, align items to curriculum levels, mark item provenance and copyright status, and summarize item-level statistics for teacher review. It is scoped to assessment design and measurement reporting, not individual diagnosis, remediation planning, or parent communication.

### Deployment Geography for Use:

China-focused by default; other regions require localization of curriculum alignment, minor-student data rules, and help-channel wording before direct student use.

## Known Risks and Mitigations:

Risk: Student item-score data may be handed to another skill without a clearly required cross-skill sharing-consent check.

Mitigation: Install only where the platform enforces cross-skill sharing consent, or update the skill to check crossSkillSharing before handing off itemScores and to define itemScores in the schema and read whitelist.

Risk: AI-generated candidate math items could be incorrect or unsuitable if used without review.

Mitigation: Keep AI-generated items as candidate drafts, label them for manual verification, and require teacher validation before they enter an assessment.

Risk: Unlicensed or restricted item text could be copied into a paper or resource library.

Mitigation: Use the documented copyrightStatus values and store only indexes for restricted teaching-aid or past-exam items.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-exam-designer)
- [ClawHub publisher profile](https://clawhub.ai/user/qizhitang)
- [Math assessment design process](references/exam-design-process.md)
- [Two-way specification table template](references/blueprint-template.md)
- [Item statistics rubric](references/result-analysis-rubric.md)
- [AI item check protocol](shared/ai-item-check.md)
- [Platform conventions and localization notes](shared/platform-conventions.md)
- [Shared vocabulary and consent fields](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured workspace-field proposals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher confirmation is required before writeback; student-specific reporting uses aliases and consent checks.]

## Skill Version(s):

2.1.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

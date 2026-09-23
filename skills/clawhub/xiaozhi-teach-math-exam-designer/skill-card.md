## Description:

Helps math teachers design diagnostic math assessments with two-way specification tables, item selection and copyright labeling, item statistics, and teacher-confirmed writeback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External math teachers use this skill to design classroom assessments, prepare specification tables, review item coverage and difficulty, compute item-level P/D and reliability statistics, and record only teacher-confirmed assessment outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles classroom assessment data and limited tier or weakness summaries.

Mitigation: Deploy only where the platform enforces the declared field whitelist and teacher-confirmation controls for writeback.

Risk: AI-generated candidate math items may be incorrect, ambiguous, or unsuitable for the class level.

Mitigation: Require teacher verification before any generated item is included in an assessment or marked as verified.

Risk: Active unified exam materials can be sensitive or confidential.

Mitigation: Use the skill for assessment methods, blueprints, and self-authored practice rather than entering unreleased exam papers, answers, or scoring standards.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-exam-designer)
- [Publisher Profile](https://clawhub.ai/user/qizhitang)
- [Blueprint Sample](artifact/references/blueprint-sample.md)
- [Blueprint Template](artifact/references/blueprint-template.md)
- [Exam Design Process](artifact/references/exam-design-process.md)
- [Result Analysis Rubric](artifact/references/result-analysis-rubric.md)
- [Class Teaching Workspace Schema](artifact/shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown guidance with structured assessment tables and teacher-confirmed writeback fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are scoped to math assessment design, item-level statistics, and approved workspace fields.]

## Skill Version(s):

2.2.0 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

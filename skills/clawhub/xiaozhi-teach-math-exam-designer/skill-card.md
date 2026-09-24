## Description:

Helps Chinese K12 math teachers design diagnostic assessment blueprints, two-way specification tables, item copyright labels, item-level P/D statistics, and teacher-confirmed workspace writebacks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External educators use this skill to turn math assessment requests into teacher-reviewable blueprints, item-selection guidance, item statistics, and handoff summaries. It is intended for Chinese K12 math-teacher workflows and keeps diagnosis, remediation, student grouping, and parent communication outside this skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Use outside the intended Chinese K12 math-teacher context could produce assessment guidance that does not match the skill's assumptions.

Mitigation: Install and activate it only for explicit math assessment-design tasks in the intended teacher workflow.

Risk: Workspace or student-file writeback without consent or review could expose or change learner records incorrectly.

Mitigation: Keep teacher confirmation and consent checks enabled before any writeback, and enforce the declared read/write field scope.

Risk: AI-generated candidate math items may contain errors or unsuitable conditions.

Mitigation: Require the built-in item self-check and teacher verification before any generated item enters a worksheet, exam, resource library, or workspace record.

Risk: Assessment materials may include copyrighted or sensitive pre-release exam content.

Mitigation: Use the declared copyright-status labels, avoid pre-release unified exam materials, and store restricted items as indexes rather than copied question text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-exam-designer)
- [blueprint-template.md](references/blueprint-template.md)
- [exam-design-process.md](references/exam-design-process.md)
- [result-analysis-rubric.md](references/result-analysis-rubric.md)
- [class-report-sample.md](references/class-report-sample.md)
- [student-report-sample.md](references/student-report-sample.md)
- [class-teaching-workspace.schema.json](shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown reports, tabular assessment blueprints, and JSON-compatible workspace entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft outputs require teacher confirmation before writeback; student-facing and parent-facing outputs are routed to other skills.]

## Skill Version(s):

2.3.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

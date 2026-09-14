## Description:

Helps independent teachers draft evidence-based student stage reports and renewal guidance from a named student's learning records, homework follow-ups, progress evidence, course package data, and consent fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to prepare parent-facing or teacher-only progress reports and renewal talking points based on recorded lessons, homework errors, progress evidence, and course package status. The skill is intended for a specific named student and includes consent checks before generating parent-visible content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill needs access to a named student's longitudinal learning history and consent fields.

Mitigation: Use it only where that access fits the teacher-workspace privacy model, confirm the student alias before reading records, and limit output to fields needed for the requested report.

Risk: Parent-visible reports or renewal messages could expose sensitive learning information without consent.

Mitigation: Generate parent-visible content only after checking parentCommunicationAllowed, and check emotionSharingWithParent before including classroom-state content.

Risk: A report could mislead families if it contains unsupported progress claims, invented percentages, or records from pending course confirmations.

Mitigation: Require every number and progress claim to trace to recorded evidence, omit unsupported items, and identify unconfirmed course entries separately.

Risk: Users may expect the skill to send messages or modify student records beyond its intended scope.

Mitigation: Keep sending manual, do not modify course balances or student cards, and route lifecycle or deletion requests to the appropriate student-intake workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-renewal-report)
- [Publisher Profile](https://clawhub.ai/user/qizhitang)
- [阶段报告模板（中期 / 续课 / 期末）](references/stage-report-templates.md)
- [续课沟通话术库](references/renewal-communication-scripts.md)
- [全库统一词表（单一事实源）](shared/vocab.md)
- [平台能力约定与降级路径（全库共享）](shared/platform-conventions.md)
- [危机例外（共享片段）](shared/crisis-exception.md)
- [Solo Teacher Workspace Schema](shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown reports, text talking points, and structured workspace-field guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should cite underlying records, avoid unsupported scores or claims, and require teacher review before any parent communication.]

## Skill Version(s):

2.1.12 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

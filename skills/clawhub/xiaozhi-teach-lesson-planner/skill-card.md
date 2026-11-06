## Description:

帮助教师用 UbD 逆向设计生成可观测目标、评估证据、课堂环节与分层任务的教案草稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向小学至高中教师，用于按 UbD 逆向设计备课，形成目标、评估证据、课堂时间安排、提问链和可选的 A/B/C 分层任务。输出供教师审阅的教案草稿。

### Deployment Geography for Use:

China (mainland); adapt crisis referral resources for other regions.

## Known Risks and Mitigations:

Risk: Classroom information or generated lesson content could expose student details or be shared before review.

Mitigation: Use student aliases and minimal classroom summaries, then review lessons before sharing.

Risk: Memory, deletion, or consent controls may not be supported by the host platform.

Mitigation: Confirm that the platform supports the documented memory, deletion, and consent controls before relying on them.

Risk: Companion skills and host platform data handling are outside this artifact review.

Mitigation: Assess the companion skills and host platform separately before using them with classroom data.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-planner)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Lesson plan template](artifact/references/lesson-plan-template.md)
- [Layered lesson example](artifact/references/layered-lesson-example.md)
- [AI-generated item checks](artifact/shared/ai-item-check.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Classroom workspace schema](artifact/shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese Markdown lesson-plan draft]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-reviewed draft that may include measurable learning goals, assessment evidence, timed activities, question prompts, and tiered tasks when class data is available.]

## Skill Version(s):

2.12.6 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Determines when elderly people living alone have no interaction or visitors for extended periods, and actively pushes care reminders to family members, suitable for remote care scenarios for elderly people living alone at home. | 无人陪伴监测技能，判定独居老人长时间无人互动来访，主动推送关怀提醒给家属，适用于居家独居老人远程关怀场景

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Family caregivers and care providers can use the skill to analyze submitted home monitoring images or videos for extended periods without interaction, review monitoring reports, and decide when a human follow-up is appropriate. Its results are a care aid and do not replace visits or professional care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private household footage may be uploaded for cloud analysis, and account enrollment may occur automatically.

Mitigation: Defer private footage until the no-analysis option and destination override are confirmed; obtain permission for external processing and clarify cloud enrollment, retention, and account ownership.

Risk: Monitoring results or reminders may be mistaken for continuous supervision of a person's safety.

Mitigation: Use results to prompt human follow-up, and do not rely on this package alone to continuously monitor someone or notify family members.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-unaccompanied-monitoring-analysis)
- [API interface reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured monitoring reports and results; Markdown tables for report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include care suggestions and report links. Results are for reference and do not replace human visits or professional care.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

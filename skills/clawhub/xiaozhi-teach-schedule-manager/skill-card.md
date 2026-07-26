## Description: <br>
帮助独立教师系统化生成周课表、检测排课冲突、管理课时包台账，并处理补课、请假、调课和续费预警流程。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
独立教师使用该技能把学员可上课时间、老师可用时段、课时包余额和调课记录整理为可检查的排课建议与台账。它适合需要在共享教学工作空间内保持课表清晰、冲突可见、课时消耗可追溯的日常教学运营场景。 <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Student schedules and lesson-unit balances may expose sensitive learner information when kept in a shared workspace. <br>
Mitigation: Use aliases, avoid real names, contact details, addresses, payment records, and other high-sensitivity fields, and honor view, correction, deletion, pause-recording, and sharing-control requests. <br>
Risk: Incorrect schedule or lesson-unit changes could disrupt classes or ledger accuracy. <br>
Mitigation: Treat generated schedules and ledger updates as proposals and require explicit teacher confirmation before writing changes. <br>
Risk: Cross-skill sharing can broaden access to student records beyond the intended teaching workflow. <br>
Mitigation: Confirm profile and cross-skill-sharing consent before creating records or sharing student data with related teaching skills. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-schedule-manager) <br>
- [周课表与课时台账模板](references/weekly-schedule-template.md) <br>
- [请假/补课/调课登记模板](references/leave-makeup-reschedule-forms.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown with structured schedules, ledgers, conflict reports, and plain-text registration templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires teacher confirmation before schedule changes, cross-skill sharing, or deletion of student records.] <br>

## Skill Version(s): <br>
2.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

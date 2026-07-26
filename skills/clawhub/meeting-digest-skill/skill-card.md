## Description: <br>
基于腾讯会议（tmeet）智能纪要与转写，把多场会议聚合为结构化周报与复盘报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golgys0621](https://clawhub.ai/user/golgys0621) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external teams, and developers use this skill to turn Tencent Meeting notes, transcripts, or local meeting-note files into weekly digests, retrospectives, and action-item summaries for review and sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meeting notes and Tencent Meeting records may contain sensitive project details, decisions, or personal information. <br>
Mitigation: Limit the requested date range, meeting set, or local notes directory, and review generated reports before sharing or backfilling them. <br>
Risk: Generated summaries can misstate conclusions, owners, deadlines, or source support when meeting material is incomplete. <br>
Mitigation: Keep unsupported items marked for confirmation and verify names, conclusions, and action items against the original meeting notes before use. <br>
Risk: Optional write-back or participant sharing could distribute an unreviewed digest. <br>
Mitigation: Require explicit user authorization before any backfill, sharing, or push to meeting participants. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/golgys0621/skills/meeting-digest-skill) <br>
- [周报模板（weekly）](references/weekly_template.md) <br>
- [复盘模板（retrospective）](references/retrospective_template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports and tables with optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated reports mark missing sources or confirmations for human review.] <br>

## Skill Version(s): <br>
2.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

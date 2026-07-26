## Description: <br>
基于腾讯会议(tmeet)会议报告和智能纪要，量化会议健康度，包括发言均衡度、议题覆盖率、决策产出率和沉默成员识别，并给出改进建议。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golgys0621](https://clawhub.ai/user/golgys0621) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and team facilitators use this skill to assess meeting participation and outcome quality from Tencent Meeting reports, intelligent minutes, or a local CSV roster plus minutes file. It produces meeting health metrics and practical suggestions for improving future meetings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meeting reports and generated analyses may include participant names, speaking patterns, and meeting decisions. <br>
Mitigation: Install and run the skill only where tmeet access is authorized, and store or share reports according to the organization's meeting-data policy. <br>
Risk: Heuristic metrics such as speaking time and silent-member detection can be mistaken for absolute measures of contribution or performance. <br>
Mitigation: Use the report as an improvement signal and interpret results with participant roles, meeting context, and qualitative judgment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/golgys0621/skills/meeting-health-skill) <br>
- [README](artifact/README.md) <br>
- [Health report template](artifact/references/health_template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown report with optional local Python command usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use authorized tmeet meeting reports and minutes, or local CSV and Markdown files, to produce heuristic meeting-health metrics.] <br>

## Skill Version(s): <br>
2.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

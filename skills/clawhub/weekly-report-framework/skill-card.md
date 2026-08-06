## Description: <br>
A weekly project report framework for Smart Equipment Institute research-room managers that initializes project knowledge bases, gathers approved project chat updates, detects reporting anomalies, and generates weekly report materials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Research-room managers use this skill to maintain a structured project knowledge base and produce weekly Excel or Markdown project status reports for institute leadership. It is intended for authorized workplace reporting workflows where group chats, project lists, member ownership, risks, and next-week plans need to be consolidated. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can collect and summarize workplace group chat history and attachments. <br>
Mitigation: Use it only where the operator is authorized to process those chats, define which groups may be accessed, and require explicit confirmation before first-time group capture. <br>
Risk: Chat-derived records may be retained permanently in the project knowledge base. <br>
Mitigation: Set a retention and deletion policy before deployment, including rules for report drafts, archived workbooks, chat summaries, and project records after completion. <br>
Risk: Incorrect group-to-project associations could put unrelated chat content into a report. <br>
Mitigation: Require the research-room manager to confirm candidate group matches before storing session IDs or generating report content. <br>
Risk: Scheduled report generation or sending may run before a reviewer approves the latest content. <br>
Mitigation: Require approval for scheduled runs and sending, and review generated weekly reports before they are shared. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/weekly-report-framework) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Project weekly report framework V2.5](artifact/references/项目周报管理框架V2.5.md) <br>
- [Knowledge base template README](artifact/references/知识库模板/README.md) <br>
- [Weekly report template generator](artifact/scripts/generate_weekly_report_template.py) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance, structured knowledge-base files, shell commands, and Python-generated Excel workbook templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create project knowledge-base records, weekly report drafts, archived workbooks, anomaly notes, and chat-derived summaries in the workspace.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
生产现场隐患排查与整改跟踪；用于日常安全检查、隐患录入、统计分析、整改任务管理及合规性评估；帮助企业建立隐患闭环管理机制 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Safety, operations, and compliance teams use this skill to record production-site hazards, apply checklist-based inspections, analyze hazard trends, and track remediation tasks through closure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates and updates local inspection and remediation records in ./inspection_data/. <br>
Mitigation: Use it only in a workspace where those records belong, and review file changes before relying on them. <br>
Risk: Operational or compliance reporting based on the generated records can be incomplete or misleading if the underlying inspection data is inaccurate. <br>
Mitigation: Validate records against actual site inspections and internal safety review processes before using them for decisions or reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-hazard-inspection) <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-hazard-inspection) <br>
- [Production-site hazard inspection checklist](references/inspection_checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON script outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and updates local JSON inspection and remediation records under ./inspection_data/ when the bundled scripts are run.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

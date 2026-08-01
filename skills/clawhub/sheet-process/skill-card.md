## Description: <br>
Filters Tencent Docs SmartSheet tables by column and keyword conditions, then returns structured JSON for workflow use or guided JSON/HTML outputs for interactive use. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liuyi-arch](https://clawhub.ai/user/liuyi-arch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and developers use this skill in WorkBuddy to filter Tencent Docs SmartSheet records by selected columns, keywords, and union/intersection rules. It is suited for turning referenced spreadsheet data into structured downstream agent input or a human-readable filtered table. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Tencent Docs sheets referenced by the user. <br>
Mitigation: Use it only with documents the operator is authorized to access and review connector permissions before deployment. <br>
Risk: The filtering script depends on a local WorkBuddy Tencent Docs path and can load code from that installation. <br>
Mitigation: Review or update the local dependency path before use, and deploy only in a controlled WorkBuddy environment. <br>
Risk: Filtered spreadsheet rows may be written to local JSON or HTML files. <br>
Mitigation: Send exports to a controlled folder, avoid shared temporary locations, and handle the output according to the data sensitivity of the source sheet. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, JSON, HTML, Files] <br>
**Output Format:** [Conversational guidance plus JSON or HTML files containing filtered records and match metadata.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Workflow mode writes JSON with meta and records; atomic mode can produce JSON or HTML based on user choice.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

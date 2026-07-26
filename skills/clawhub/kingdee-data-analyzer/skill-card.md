## Description: <br>
金蝶云星空经营数据分析技能，可在用户明确请求时分析 Kingdee/K3 Cloud 库存、采购、销售、开票和结算数据，并生成 HTML 报告、全量明细 Excel 和结构化 JSON。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yk-niu](https://clawhub.ai/user/yk-niu) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Employees and external users who manage authorized Kingdee Cloud business data use this skill to turn Excel exports, or optional live exports, into inventory, purchase, and sales operating reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML, Excel, and JSON outputs can contain sensitive Kingdee operational details. <br>
Mitigation: Store and share outputs as sensitive business records, and restrict access to users authorized for the source data. <br>
Risk: Live export depends on a separate kingdee-data-exporter installation and its Kingdee credentials/configuration. <br>
Mitigation: Review and configure the exporter separately before using real-time data collection against real Kingdee systems. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yk-niu/skills/kingdee-data-analyzer) <br>
- [Publisher profile](https://clawhub.ai/user/yk-niu) <br>
- [KingdeeDataAnalyzer GitHub repository](https://github.com/LittleBeaverStudio/KingdeeDataAnalyzer) <br>
- [KingdeeDataExporter GitHub repository](https://github.com/LittleBeaverStudio/KingdeeDataExporter) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell commands; generated artifacts are HTML reports, Excel workbooks, and JSON analysis files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local analysis outputs may contain full operational details from the source Kingdee data.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
金蝶云星空经营数据导出技能。仅当用户明确要求从金蝶云星空或 K3 Cloud 查询、导出经营数据时使用；支持配置账号、查询组织和可用单据/报表，按期间、组织及单据或报表类型导出多工作表 Excel，也支持追加官方字段、全组织导出和结果二次筛选。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yk-niu](https://clawhub.ai/user/yk-niu) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Authorized Kingdee Cloud Galaxy or K3 Cloud users use this skill to configure local credentials, list organizations and supported forms, export business and financial records into multi-sheet Excel workbooks, and filter exported workbooks by organization or document type. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive Kingdee business and financial exports. <br>
Mitigation: Use it only with authorized tenant access, restrict the output directory, and treat generated Excel files as sensitive records. <br>
Risk: Overbroad export options can retrieve more organizational data than needed. <br>
Mitigation: Use --org and --only to scope exports to the requested organization, document, or report. <br>
Risk: Local credentials may be exposed if config.py is shared or committed. <br>
Mitigation: Create config.py locally, keep it out of source control, and avoid showing credentials in conversations, logs, or public repositories. <br>
Risk: The pinned requests dependency may require review for environment-specific advisories. <br>
Mitigation: Update the pinned requests dependency if the deployment environment confirms the reported advisory applies. <br>


## Reference(s): <br>
- [Skill Instructions](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Configuration Example](artifact/config.example.py) <br>
- [Official Field Reference Directory](artifact/官方字段说明/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated Excel workbook files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Exports may contain sensitive business and financial records and should be written to an access-controlled output directory.] <br>

## Skill Version(s): <br>
1.2.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

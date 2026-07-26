## Description: <br>
通用模版。用户上传问句文档（xlsx），自动提取指标、维度和过滤条件，生成完整的问句模型.xlsx（包含01-问句、11-指标、12-维度、13-业务模型、00-业务规则等多个Sheet）。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hht1ng](https://clawhub.ai/user/hht1ng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
BI analysts, data product teams, and implementation engineers use this skill to turn uploaded question workbooks and optional reference documents into a structured BI question model workbook. It supports early requirements analysis by extracting metrics, dimensions, filters, business rules, source-system notes, and metric-dimension relationships. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded BI workbooks and reference documents are fully readable by the agent during processing, including auxiliary or hidden-looking sheets. <br>
Mitigation: Use copies of business spreadsheets where possible and remove unrelated sensitive tabs before processing. <br>
Risk: The generated workbook may carry forward derived business rules, metrics, dimensions, and source details from sensitive input documents. <br>
Mitigation: Review the generated workbook before sharing it outside the intended audience. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hht1ng/skills/question) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [skill-指标维度说明书.md](artifact/skill-指标维度说明书.md) <br>
- [skill-业务知识说明书.md](artifact/skill-业务知识说明书.md) <br>
- [skill-数据字典.md](artifact/skill-数据字典.md) <br>
- [skill-表结构数据.md](artifact/skill-表结构数据.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Guidance] <br>
**Output Format:** [Excel workbook (.xlsx) with multiple worksheets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a question model workbook with question analysis, metrics, dimensions, business model matrix, business rules, optional knowledge entries, and optional source-system information.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

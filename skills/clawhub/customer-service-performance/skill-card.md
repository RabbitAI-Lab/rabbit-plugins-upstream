## Description: <br>
通过Python脚本读取Excel数据和规则文件，转换为文本后由大模型解析字段、阶梯规则与权重，自动完成逐行核算与排名输出。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zenobiazizi](https://clawhub.ai/user/zenobiazizi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer service operations managers and analysts use this skill to calculate agent performance scores and rankings from supplied data and scoring rules, then produce a concise management report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Performance spreadsheets and rule files may contain real names, employee IDs, or other sensitive employee data. <br>
Mitigation: Remove or mask sensitive fields where possible before giving files to the agent. <br>
Risk: Scores and rankings may affect management, pay, or evaluation decisions if used without review. <br>
Mitigation: Independently verify calculations, rule interpretation, and rankings before using results for personnel decisions. <br>
Risk: Large or unsupported input files can fail during local file conversion. <br>
Mitigation: Keep individual files within the documented 10 MB limit and use the supported .xlsx, .xls, .md, .txt, or .csv formats. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zenobiazizi/skills/customer-service-performance) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown table and narrative report, with shell command guidance for reading supported files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads user-provided .xlsx, .xls, .md, .txt, and .csv files up to the documented 10 MB limit.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter declares 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

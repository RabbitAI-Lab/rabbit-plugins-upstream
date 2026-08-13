## Description:

Searches for current-month IT and informatization bidding announcements for Zhangye City, extracts key procurement fields, and appends new results to a predefined Excel template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xizhima](https://clawhub.ai/user/xizhima)

### License/Terms of Use:

MIT-0

## Use Case:

Employees or procurement analysts use this skill to find Zhangye City IT, digital, and informatization bidding notices, extract structured announcement details, avoid duplicate entries, and update an Excel tracking workbook.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill appends and saves rows to a disclosed Excel workbook, so an incorrect target path or unreviewed records could update the wrong file.

Mitigation: Confirm the workbook path before use, keep a backup for important spreadsheets, or ask the agent to show proposed rows before writing.

## Reference(s):

- [张掖市信息化项目标讯搜索参考资料](references/bidding_sources.md)
- [张掖信息化标讯搜索 on ClawHub](https://clawhub.ai/xizhima/skills/zhangye-it-bidding)
- [甘肃省公共资源交易网](https://ggzyjy.gansu.gov.cn)
- [张掖市公共资源交易中心](https://ggzy.zhangye.gov.cn)
- [甘肃政府采购网](https://www.ccgp-gansu.gov.cn)
- [中国政府采购网](https://www.ccgp.gov.cn)
- [全国公共资源交易平台](https://www.ggzy.gov.cn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with extracted procurement records and optional Python/openpyxl workbook update steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May append rows to the configured Excel workbook and report search statistics.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

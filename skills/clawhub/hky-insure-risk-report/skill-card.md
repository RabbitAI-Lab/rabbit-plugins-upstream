## Description:

读取结构化养老与传承面谈纪要，生成标准化风险评估报告，包括家庭架构图、基本信息与资产盘点、人权财主线或特殊需要子女家庭防火墙分析、P0-P3 风险排序、法律释义出处、工具方向矩阵、风险盘点总表和二次沟通议程。

This skill is ready for commercial/non-commercial use.

## Publisher:

[hukaiyi777](https://clawhub.ai/user/hukaiyi777)

### License/Terms of Use:

MIT

## Use Case:

External insurance, retirement, and inheritance-planning advisors use this skill to turn structured client interview notes into a client-facing risk assessment report. The generated report focuses on risk logic, missing information, and follow-up discussion priorities rather than recommending specific products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated DOCX and PNG files may contain sensitive family, health, financial, insurance, property, and inheritance details.

Mitigation: Use a private working folder, avoid synced or shared directories, redact source notes where possible, and delete or protect generated reports after delivery.

Risk: The report discusses legal, trust, insurance, health, and regulatory topics that may require current professional review.

Mitigation: Have qualified professionals verify legal, underwriting, trust, and regulatory statements before relying on the report with a client.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hukaiyi777/skills/hky-insure-risk-report)
- [README](artifact/README.md)
- [Report template generator](artifact/assets/report_template.py)
- [Example generated report](artifact/demo/示例-养老与传承风险分析报告.docx)
- [Report preview image](artifact/images/report-preview.png)

## Skill Output:

**Output Type(s):** [markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional Python DOCX/PNG generation commands and generated local report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local DOCX and PNG files when the bundled report template generator is used.]

## Skill Version(s):

0.1.2 (source: ClawHub server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

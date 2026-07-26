## Description: <br>
员工持股平台（有限合伙/公司型/资管型）财税合规专项助手，面向股权激励递延纳税、持股平台税负、股份支付、股权代持、上市审核、减持退出和合规报告等场景提供政策依据、风险指标、测算和实操模板。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, legal, and company operations teams use this skill to analyze PRC employee shareholding platform structures, compare company-form and partnership-form tax outcomes, identify compliance risks, and draft guidance or reports for planning, self-check, listing-review, and exit scenarios. <br>

### Deployment Geography for Use: <br>
China-focused; deployment may be global where users need PRC employee shareholding platform tax and compliance guidance. <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and scenarios may be sent to mcp.aitaxs.top for online policy answers, risk checks, calculations, and web workflows. <br>
Mitigation: Avoid entering sensitive company, payroll, cap-table, listing-preparation, or personal details unless that cloud data flow is acceptable; use offline workflows for local reference where suitable. <br>
Risk: The skill includes MCP client helpers and optional setup code that can write client configuration when explicitly enabled. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run setup helpers unless MCP configuration changes are intended; review configuration changes before use. <br>
Risk: The related-skill matrix installer can add packages under the user's skills directory. <br>
Mitigation: Review install_matrix.py and use the matrix install trigger only when bulk installation of related tax skills is desired. <br>
Risk: Tax, legal, accounting, and listing-review conclusions may vary by facts, timing, jurisdictional practice, and regulator or court interpretation. <br>
Mitigation: Verify material advice against current official policy and qualified professional review before filing, restructuring, listing, litigation, or transaction execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-esop-platform) <br>
- [Web tax-burden and compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_esop.html) <br>
- [Cloud MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, structured reports, tax calculations, local workflow output, and configuration or shell-command suggestions when installation or MCP setup is requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a cloud MCP service for policy answers, risk checks, calculations, and knowledge-base metadata; offline workflows provide local reference and report generation.] <br>

## Skill Version(s): <br>
3.14.38 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

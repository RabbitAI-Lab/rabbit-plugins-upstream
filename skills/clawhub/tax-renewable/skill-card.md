## Description: <br>
再生资源/资源回收/废旧物资企业财税政策、反向开票、资源综合利用即征即退、简易计税、风险指标、案例、报告模板与实操指引专题助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax, finance, and compliance users use this skill to ask renewable-resource industry tax questions, check reverse invoicing and resource-recycling VAT treatment, identify compliance risks, and draft self-check or remediation reports. It is focused on Chinese renewable-resource and waste-material recovery tax scenarios and should not be treated as legal, audit, or tax filing advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill may send tax questions or self-check metrics to mcp.aitaxs.top. <br>
Mitigation: Avoid entering sensitive client, taxpayer, or confidential business details unless those remote-service data flows are acceptable. <br>
Risk: The skill can create and store service credentials and logs locally. <br>
Mitigation: Review and protect the local client data directory, and remove stored credentials or logs when they are no longer needed. <br>
Risk: The skill may alter MCP client configuration when setup is explicitly run or enabled. <br>
Mitigation: Run setup in dry-run mode first where available, inspect proposed MCP configuration changes, and keep backups before enabling automatic setup. <br>
Risk: Tax calculations, risk scores, and policy guidance may be incomplete, outdated, or unsuitable for a specific taxpayer. <br>
Mitigation: Confirm material conclusions with official tax authority guidance or a qualified tax professional before filing, remediating, or relying on the output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-renewable) <br>
- [Renewable-resource compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_renewable.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [State Taxation Administration](https://www.chinatax.gov.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown and structured text, with optional configuration guidance and report-style outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May provide links to an interactive self-check page, policy Q&A prompts, risk findings, remediation steps, and report templates.] <br>

## Skill Version(s): <br>
3.15.4 (source: server release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

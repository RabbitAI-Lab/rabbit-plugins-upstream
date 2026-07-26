## Description: <br>
减资撤资（未实缴减资）个人所得税专项助手，聚焦公司减资、股东撤资退股、未实缴减资免除出资义务、定向减资（公司回购股权）、减资弥补亏损、新公司法下减资程序与税务衔接，提供不征税论证、个税测算、核定风险预警、合规方案与报告模板。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax/compliance practitioners use this skill to assess capital reduction and shareholder withdrawal scenarios, including unpaid subscribed capital reductions, individual income tax calculations, procedural checks, risk warnings, and draft compliance reports. It also offers a structured self-check workflow and can route related tax questions to adjacent matrix skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, scenarios, and self-check data may be sent to mcp.aitaxs.top. <br>
Mitigation: Install and use the skill only when that data transfer is acceptable, and avoid entering sensitive taxpayer or company details unless the user has approved the remote service use. <br>
Risk: The skill can create local API credentials, cache, and logs. <br>
Mitigation: Review local credential and log handling before use, and remove generated local data if the skill is uninstalled or no longer trusted. <br>
Risk: Client configuration may be modified if config/init_agent.py is run with setup enabled or TAX_ENABLE_AUTOSETUP is set. <br>
Mitigation: Do not run setup-enabled configuration paths unless MCP client changes are intended; inspect the generated MCP entry before enabling it. <br>
Risk: The full matrix installation workflow can add many related tax skills. <br>
Mitigation: Treat matrix installation as a separate approval step and review the target skill list before installing additional packages. <br>
Risk: Capital reduction tax guidance can be jurisdiction-specific, time-sensitive, and dependent on facts. <br>
Mitigation: Use the skill output as decision support and confirm material filing, tax, and legal positions with current official sources or qualified professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-capital-reduction) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Capital reduction self-check page](https://mcp.aitaxs.top/web/topic_workflow_capital_reduction.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>
- [Related tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with structured self-check results, calculation summaries, report templates, and optional configuration or installation commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP service and may produce local client configuration or matrix installation steps when the user requests those workflows.] <br>

## Skill Version(s): <br>
3.14.38 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

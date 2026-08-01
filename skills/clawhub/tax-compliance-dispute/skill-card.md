## Description: <br>
财税合规与争议解决专业助手，覆盖财税内审、企业清算注销、税务争议、合同涉税条款审核、发票合规正负面清单、稽查应对、涉税刑事风险和争议救济路径。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, business operators, finance teams, and tax professionals use this skill to self-check tax compliance disputes, liquidation and cancellation issues, invoice risks, audit response, contract tax clauses, and available dispute-resolution paths. It produces practical guidance, risk checklists, and report-style outputs that should be reviewed against current authority or professional advice for material matters. <br>

### Deployment Geography for Use: <br>
Global; the substantive tax guidance is focused on mainland China tax compliance topics. <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax, invoice, dispute, litigation, or account details may be sent to the remote mcp.aitaxs.top service during online use. <br>
Mitigation: Avoid entering confidential taxpayer or case-specific data unless the provider's data-handling terms have been reviewed and accepted. <br>
Risk: The package can store API credentials and stable identifiers locally. <br>
Mitigation: Review local config, cache, and log locations before deployment, restrict file access, and remove stored credentials when they are no longer needed. <br>
Risk: Setup code can modify MCP client configuration when run directly or when TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Do not run config/init_agent.py directly or enable TAX_ENABLE_AUTOSETUP unless configuration changes are intended and have been reviewed. <br>
Risk: Tax policies and dispute outcomes are time-sensitive and fact-specific. <br>
Mitigation: Treat outputs as self-check guidance and confirm material decisions with current official sources, a qualified tax advisor, or legal counsel. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/zxj2devs/skills/tax-compliance-dispute) <br>
- [Embedded compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_dispute.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown text with structured checklists, links, and optional tool-result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route questions to a remote MCP tax-policy service and may provide offline fallback guidance when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
国有企业经济责任审计涉税风险与合规专项助手，帮助识别虚开发票、偷逃税款、账外账小金库、国有资本收益上交、财政专项资金、重大经济决策涉税、境外国有资产税务监管、审计整改闭环和三公经费审计隐形违规等风险。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax, audit, compliance, and enterprise-risk users use this skill to structure state-owned enterprise economic-responsibility audit questions, identify tax and expense-control risks, and draft self-check, evidence, remediation, and reporting guidance. It is especially focused on China tax compliance scenarios for SOE audits, related-party pricing, fiscal funds, overseas assets, invoices, and audit rectification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security verdict is suspicious because the skill under-discloses cloud routing for sensitive audit, taxpayer, invoice, personnel, or enterprise-risk data. <br>
Mitigation: Review and approve use of mcp.aitaxs.top cloud processing before installation; avoid submitting confidential data unless that routing is acceptable. <br>
Risk: The security summary identifies local credential persistence and local logging. <br>
Mitigation: Install only in environments where local credential and log storage is permitted, and apply local data-retention and access-control procedures. <br>
Risk: The security guidance notes possible fallback queries to public search engines. <br>
Mitigation: Disable or avoid fallback workflows for confidential scenarios, or redact sensitive details before any fallback query is generated. <br>
Risk: The security guidance notes optional MCP client configuration changes when setup is explicitly enabled. <br>
Mitigation: Keep setup in dry-run mode until the proposed client configuration changes have been reviewed and approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-soe-audit) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [SOE audit self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_soe_audit.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge related skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Tax compliance dispute related skill](https://skillhub.cn/skills/tax-compliance-dispute) <br>
- [Tax equity governance related skill](https://skillhub.cn/skills/tax-equity-governance) <br>
- [Tax restructuring related skill](https://skillhub.cn/skills/tax-restructuring) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown and plain text guidance, with optional copied report prompts, local CLI output, and MCP configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route requests to cloud MCP services, store local credentials and logs, use fallback public search queries, and optionally modify MCP client configuration when setup is explicitly enabled.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

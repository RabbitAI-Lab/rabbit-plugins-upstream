## Description: <br>
国有企业经济责任审计涉税风险与合规专项助手，聚焦虚开发票、偷逃税款、账外账小金库、国有资本收益上交、财政专项资金挤占挪用、重大经济决策涉税、境外国有资产税务监管、审计整改闭环，以及三公经费审计隐形违规识别。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, audit teams, tax compliance staff, and SOE governance reviewers use this skill to structure SOE economic-responsibility audit tax-risk checks, policy questions, evidence preparation, risk self-assessment, and整改闭环 guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive SOE audit, tax, supplier, investigation, or personal data may be shared with cloud services or fallback search when the skill is used. <br>
Mitigation: Do not enter confidential details unless the deployment owner has approved those cloud and search data flows; redact or summarize sensitive facts before use. <br>
Risk: The skill can persist API credentials for the tax-policy MCP client. <br>
Mitigation: Review local credential storage expectations before installation and rotate or remove credentials when the skill is no longer needed. <br>
Risk: Setup code can modify local MCP client configuration when explicitly invoked or when TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Run setup in dry-run or review mode first, keep backups, and enable TAX_ENABLE_AUTOSETUP only when configuration changes are intended. <br>
Risk: Tax, audit, and regulatory guidance can become outdated or may not fit a specific jurisdiction or fact pattern. <br>
Mitigation: Verify conclusions against current official tax and audit authority guidance before relying on them for filings, audit conclusions, or enforcement responses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-soe-audit) <br>
- [SOE audit tax self-check web workflow](https://mcp.aitaxs.top/web/topic_workflow_soe_audit.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge MCP endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Tax compliance dispute skill](https://skillhub.cn/skills/tax-compliance-dispute) <br>
- [Tax equity governance skill](https://skillhub.cn/skills/tax-equity-governance) <br>
- [Tax restructuring skill](https://skillhub.cn/skills/tax-restructuring) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured responses with optional inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call cloud MCP tools for policy Q&A, risk checks, tax calculation, and knowledge-base listing; offline scripts provide local process guidance and keyword reference.] <br>

## Skill Version(s): <br>
3.15.6 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

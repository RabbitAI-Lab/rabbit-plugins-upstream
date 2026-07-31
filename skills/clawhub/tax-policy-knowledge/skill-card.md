## Description: <br>
Tax Policy Knowledge is a China-focused tax policy, calculation, risk self-check, invoice compliance, contract review, and compliance-reporting assistant. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Businesses, finance teams, tax advisers, and compliance reviewers use this skill to answer China tax-policy questions, estimate common taxes, triage invoice and contract risks, perform tax-risk self-checks, and draft compliance guidance or reports. <br>

### Deployment Geography for Use: <br>
Global use; content focuses on China tax policy and compliance scenarios. <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax facts, client scenarios, invoice details, contract text, payroll facts, or account information may be sent to the operator's cloud service. <br>
Mitigation: Do not enter confidential client, payroll, invoice, contract, or account details unless the organization has approved that data flow and reviewed the operator. <br>
Risk: When the remote service is unavailable, fallback behavior can use public search engines, which may expose query text outside the primary service. <br>
Mitigation: Avoid putting confidential facts in fallback queries; disable or block fallback search where external search is not approved. <br>
Risk: The local client stores configuration, credentials, cache, and logs under ~/.tax-policy-client. <br>
Mitigation: Treat that directory as sensitive, restrict filesystem access, rotate credentials when needed, and avoid sharing logs without review. <br>
Risk: Optional setup behavior can write or merge MCP configuration when TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Review or disable TAX_ENABLE_AUTOSETUP before installation, and inspect generated MCP configuration before use. <br>
Risk: Tax calculations, risk scores, and compliance suggestions are advisory and may be incomplete or time-sensitive. <br>
Mitigation: Confirm material tax positions against official sources and qualified tax or legal professionals before filing, audit, dispute, or transaction decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-policy-knowledge) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Public MCP endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>
- [Related tax skill matrix](https://skillhub.cn/skills/tax-restructuring) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text, structured guidance, Python helper code, MCP configuration snippets, and JSON-like tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a cloud MCP service, local stdio proxy, or fallback public search path depending on configuration and service availability.] <br>

## Skill Version(s): <br>
3.15.4 (source: server evidence release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

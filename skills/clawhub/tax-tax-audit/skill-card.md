## Description: <br>
Tax Tax Audit helps agents provide China-focused enterprise tax audit and tax compliance audit guidance, including audit procedures, internal control testing, tax fraud indicators, key audit matter disclosure, self-check workflows, and remediation report drafting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax and audit practitioners, business users, and agent operators use this skill to structure China tax audit questions, screen compliance risks, prepare self-check reports, and identify when professional review is needed. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax or audit prompts and scenarios may be sent to the remote mcp.aitaxs.top service. <br>
Mitigation: Use only with organization-approved data sharing, and avoid entering client-identifying or confidential financial details unless the service is approved for that use. <br>
Risk: The skill may store local API credentials for the remote service. <br>
Mitigation: Review local credential storage before deployment, restrict file access, and rotate or remove credentials if the skill is no longer trusted. <br>
Risk: Opt-in client setup can add the remote MCP service to local agent configuration. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run config/init_agent.py directly unless you intentionally want the remote service registered in local agent clients. <br>
Risk: Tax audit outputs can be mistaken for filing, audit, legal, or professional advice. <br>
Mitigation: Treat outputs as reference guidance and require qualified tax, audit, or legal review before making filing, disclosure, or engagement decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-tax-audit) <br>
- [Tax audit self-check page](https://mcp.aitaxs.top/web/topic_workflow_tax_audit.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance, text reports, JSON tool results, Python code, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP tax-policy service and includes offline reference workflows for degraded operation.] <br>

## Skill Version(s): <br>
3.15.7 (source: SKILL.md frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

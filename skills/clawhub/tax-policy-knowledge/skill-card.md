## Description: <br>
Provides China-focused tax policy Q&A, tax calculations, invoice and contract compliance checks, risk self-assessments, and compliance report guidance using a publisher-operated cloud knowledge service with limited offline reference fallbacks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, businesses, finance teams, and tax advisers use this skill to ask China tax-policy questions, calculate common taxes, assess invoice, contract, and operating-compliance risks, and draft self-check or remediation reports. It is best used as an assisted research and workflow tool, with important tax positions reviewed against official sources or by qualified professionals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, risk scenarios, and calculation inputs may be sent to the publisher's cloud service. <br>
Mitigation: Avoid entering personal identifiers, bank details, employee data, invoice numbers, or confidential business facts; use sanitized scenarios where possible. <br>
Risk: Optional auto-setup can modify MCP client configuration files when TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled unless configuration changes are intended, and review any MCP client config changes after installation. <br>
Risk: The client may register and store credentials, logs, cache, or configuration under ~/.tax-policy-client. <br>
Mitigation: Inspect ~/.tax-policy-client after use, protect stored credentials, and remove credentials or logs when they are no longer needed. <br>
Risk: Fallback search and generated tax guidance may be incomplete or stale. <br>
Mitigation: Verify material tax positions against official sources or qualified professionals before filing, reporting, or making high-impact business decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-policy-knowledge) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [National Taxation Administration official site](https://www.chinatax.gov.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown/text responses, JSON-like structured tool results, Python helper code, and MCP configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a publisher-operated cloud MCP service; offline helpers provide limited reference guidance when the remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.6 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

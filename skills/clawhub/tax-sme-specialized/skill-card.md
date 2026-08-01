## Description: <br>
A Chinese tax-compliance assistant for specialized and innovative SMEs that supports recognition-data consistency checks, R&D and high-tech tax treatment, fiscal subsidy tax analysis, pre-listing tax planning, qualification maintenance, related-party pricing, and structured self-check reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business tax teams use this skill to ask Chinese SME tax-compliance questions, run structured risk self-checks, review supporting policy considerations, and prepare remediation-oriented compliance reports. The skill is advisory and does not replace licensed tax representation or official filing decisions. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, scenarios, and selected self-check metrics may be sent to the remote mcp.aitaxs.top service. <br>
Mitigation: Use the skill only when that data sharing is acceptable; avoid entering sensitive taxpayer details unless the deployment has approved the remote service. <br>
Risk: Local API keys and logs may persist under ~/.tax-policy-client. <br>
Mitigation: Review local storage policies before use and clear or protect the directory according to organizational credential and logging requirements. <br>
Risk: Auto-setup can change local MCP client configuration when enabled. <br>
Mitigation: Review config/init_agent.py first and leave TAX_ENABLE_AUTOSETUP disabled unless the user intentionally wants MCP configuration changes. <br>
Risk: Tax guidance can become outdated or may not fit a specific taxpayer's facts. <br>
Mitigation: Verify cited policy positions with official tax authorities or qualified professionals before filing, claiming incentives, or completing transactions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-sme-specialized) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Interactive SME tax-compliance self-check](https://mcp.aitaxs.top/web/topic_workflow_sme_specialized.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Comprehensive tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [High-tech enterprise and R&D additional deduction skill](https://skillhub.cn/skills/tax-high-tech-rd) <br>
- [IPO tax compliance skill](https://skillhub.cn/skills/tax-ipo-compliance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, API Calls, configuration] <br>
**Output Format:** [Markdown-style advisory responses, structured self-check results, compliance report guidance, and optional web workflow links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP services for policy Q&A, risk checks, calculations, and knowledge-base listing; includes offline workflow guidance when the remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.6 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

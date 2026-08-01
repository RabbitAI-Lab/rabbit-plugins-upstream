## Description: <br>
行业涉税风险图谱指引 helps users identify tax-risk patterns in fuel retail, online freight, logistics, bulk commodities, related-party trading, and tax-preferential zones, then produces self-check and remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business, finance, and tax-compliance users use this skill to screen industry-specific tax risks, ask policy questions, and prepare structured self-check or remediation reports. It is advisory and does not replace licensed tax, audit, or legal review. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and self-checks can be sent to the mcp.aitaxs.top cloud service. <br>
Mitigation: Use the skill only when that service is acceptable for the data involved, and avoid entering highly sensitive financial, employee, transaction, or dispute details unless the service is trusted. <br>
Risk: The client may persist local client IDs, API keys, caches, or logs. <br>
Mitigation: Review stored data under ~/.tax-policy-client and browser localStorage, and clear those locations when persistent identifiers or local logs are not desired. <br>
Risk: Optional auto-setup can modify supported MCP client configuration files. <br>
Mitigation: Review or disable TAX_ENABLE_AUTOSETUP before running setup scripts, and inspect generated MCP configuration before use. <br>
Risk: Tax-risk guidance can be time-sensitive and fact-specific. <br>
Mitigation: Treat outputs as advisory self-check material and confirm significant filing, dispute, audit, or planning decisions with official sources or qualified professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-industry-tax-risk) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Industry tax-risk self-check page](https://mcp.aitaxs.top/web/topic_workflow_industry_tax_risk.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, plain text, JSON tool results, Python snippets, shell commands, and browser-copyable report text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include risk levels, checklists, policy-source summaries, tax calculations, remediation steps, MCP configuration snippets, and locally generated offline fallback guidance.] <br>

## Skill Version(s): <br>
3.15.6 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

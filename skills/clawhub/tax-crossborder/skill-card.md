## Description: <br>
Provides cross-border ecommerce and trade tax compliance guidance, risk self-check workflows, export refund support, and China-focused cross-border tax analysis for scenarios such as 9610/1210 customs modes, withholding tax, CRS, beneficial ownership, offshore income credits, VIE/red-chip structures, and Hainan Free Trade Port incentives. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and compliance teams use this skill to ask China-focused cross-border ecommerce and trade tax questions, run structured risk self-checks, generate practical compliance guidance, and route deeper policy, risk, calculation, or report workflows through the included MCP and offline fallback assets. <br>

### Deployment Geography for Use: <br>
Global, with content focused on China cross-border tax and trade compliance. <br>

## Known Risks and Mitigations: <br>
Risk: Questions, scenarios, and self-check inputs may be sent to remote cloud MCP services or fallback search services. <br>
Mitigation: Avoid entering confidential taxpayer, customer, ownership, or transaction details unless cloud processing is acceptable for the environment. <br>
Risk: The client can store API keys, health state, cache, and logs locally, and the web asset can store an API key in browser localStorage. <br>
Mitigation: Review and remove stored API keys, logs, and browser localStorage entries after use on shared or regulated systems. <br>
Risk: Optional auto-setup can persist MCP/editor configuration changes when explicitly enabled or run in setup mode. <br>
Mitigation: Keep the default dry-run posture unless setup is intended; review configuration changes and backups before enabling TAX_ENABLE_AUTOSETUP or running config/init_agent.py. <br>
Risk: Tax calculations and compliance conclusions may be incomplete or stale for a specific jurisdiction, filing period, or business structure. <br>
Mitigation: Use outputs as decision support only and confirm material tax positions with official sources, tax authorities, or qualified professionals. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/zxj2devs/skills/tax-crossborder) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Cross-border compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_crossborder.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>
- [State Taxation Administration website](https://www.chinatax.gov.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, JSON-compatible MCP responses, Python helper code, shell commands, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include remote MCP-backed policy answers, risk checks, tax calculations, generated compliance report text, local offline fallback guidance, and web self-check prompts.] <br>

## Skill Version(s): <br>
3.15.6 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

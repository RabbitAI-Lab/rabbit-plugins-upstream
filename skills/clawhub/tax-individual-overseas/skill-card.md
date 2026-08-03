## Description: <br>
帮助居民个人和财税顾问规划境外证券、存款、房产相关的涉税申报、税收抵免、合规投资通道和CRS一致性自查。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External individuals with overseas assets and their tax advisers use this skill to assess China-facing reporting, foreign tax credit, permitted investment-channel, SPV registration, tax-residence, and CRS consistency questions. It provides planning guidance, risk self-checks, calculations, and report-ready checklists rather than filing or legal representation. <br>

### Deployment Geography for Use: <br>
China-focused <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive personal tax and investment questions may be sent to the remote mcp.aitaxs.top service. <br>
Mitigation: Use only with trusted data, minimize personal identifiers, and avoid entering real names, account numbers, exact balances, or other unnecessary sensitive details. <br>
Risk: The Python client stores API tokens, logs, and configuration under ~/.tax-policy-client. <br>
Mitigation: Review and clear local logs/config after use when working with sensitive scenarios, and protect any locally stored API key. <br>
Risk: Setup code can modify local MCP client configuration when explicitly enabled. <br>
Mitigation: Leave TAX_ENABLE_AUTOSETUP disabled and avoid running config/init_agent.py directly unless local MCP configuration changes are intended and reviewed. <br>
Risk: Tax calculations and compliance conclusions may be incomplete, outdated, or unsuitable for a specific case. <br>
Mitigation: Treat outputs as planning support and confirm high-impact positions with official sources, the competent tax authority, or qualified tax/legal professionals before filing or restructuring. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-individual-overseas) <br>
- [个人境外投资自检页](https://mcp.aitaxs.top/web/topic_workflow_individual_overseas.html) <br>
- [财税合规自检门户](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown guidance, structured checklists, JSON-like tool results, copied report text, and local configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP service for policy answers, risk checks, tax calculations, and knowledge-base listing; includes offline workflow guidance when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.8 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
个人（居民个人/境内个人）直持境外证券、存款、房产的涉税申报、税收抵免与合规投资通道一站式筹划。覆盖837号令对外投资监管、居民个人境外所得申报与抵免（2020年3号）、港股通/QDII/跨境理财通免税通道、37号文登记与6年规则、CRS一致性自查。适合有港美股、境外资产或出海身份规划需求的自然人及为其服务的财税顾问。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individuals with overseas securities, deposits, real estate, or outbound identity planning needs, and tax advisers supporting them, use this skill to assess Chinese tax reporting, foreign tax credit, foreign exchange registration, compliant investment channels, and CRS consistency. It provides Q&A, structured self-checks, risk prompts, calculations, reports, and offline fallback guidance; it does not replace professional tax, audit, or legal advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is a cloud-connected MCP integration and can forward tax, financial, company, account, or offshore asset details to remote services; fallback behavior may use public search engines. <br>
Mitigation: Use non-identifying scenarios where possible, avoid sensitive account or asset details unless remote processing is acceptable, and review remote-service use before installation. <br>
Risk: The package includes API registration, local config, cache, health, and log persistence. <br>
Mitigation: Review local storage behavior before use, rotate or remove generated API keys when retiring the skill, and avoid sharing generated local config or logs. <br>
Risk: Initialization code can modify MCP client configuration when explicitly run or enabled. <br>
Mitigation: Do not run config/init_agent.py directly and do not enable TAX_ENABLE_AUTOSETUP unless client configuration changes are intended. <br>
Risk: Tax calculations, risk scores, and policy guidance are advisory and may be time-sensitive or jurisdiction-dependent. <br>
Mitigation: Confirm material conclusions against official sources and qualified tax or legal professionals before filing, restructuring, or dispute response. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-individual-overseas) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [财税合规自检门户](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured responses, with optional shell commands, client configuration snippets, copied prompts, CSV exports, and plain-text reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP service for policy Q&A, risk checks, tax calculations, and knowledge-base metadata; offline scripts provide local reference output when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.4 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

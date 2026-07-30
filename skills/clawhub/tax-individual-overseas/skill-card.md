## Description: <br>
个人（居民个人/境内个人）直持境外证券、存款、房产的涉税申报、税收抵免与合规投资通道一站式筹划。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax or compliance advisors use this skill to assess Chinese individual overseas investment tax reporting, foreign tax credit, foreign exchange registration, CRS consistency, and compliant investment-channel options. It supports policy Q&A, scenario risk checks, tax calculations, offline reference workflows, and interactive self-check reports. <br>

### Deployment Geography for Use: <br>
China-focused <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax, residency, account, asset, or identity details may be processed by the cloud service at mcp.aitaxs.top or by public search engines during fallback. <br>
Mitigation: Avoid real identifiers unless necessary, minimize scenario detail, review the service terms before use, and prefer anonymized examples for exploratory questions. <br>
Risk: Optional setup code can add MCP client configuration when TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Check the TAX_ENABLE_AUTOSETUP environment variable before running setup, review generated client configuration changes, and keep the automatic backup files until configuration is verified. <br>
Risk: The client can auto-register and store API credentials in local user data or browser storage. <br>
Mitigation: Review local credential storage after installation, remove stored API keys when no longer needed, and avoid sharing logs or config directories that may reveal account linkage. <br>
Risk: Tax calculations and compliance conclusions may be incomplete, outdated, or unsuitable for a specific filing position. <br>
Mitigation: Treat outputs as preliminary self-check guidance, verify against official tax authority materials, and consult a qualified tax or legal professional for filing, dispute, or material investment decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-individual-overseas) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [财税合规自检门户](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>
- [Tax policy API base](https://mcp.aitaxs.top/api/services/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Chinese-language Markdown guidance, structured JSON-like tool results, configuration snippets, local HTML self-check output, and downloadable text or CSV reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Cloud MCP calls can return policy answers, risk checks, calculations, and knowledge-base metadata; fallback paths provide local search summaries and offline checklist guidance.] <br>

## Skill Version(s): <br>
3.15.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

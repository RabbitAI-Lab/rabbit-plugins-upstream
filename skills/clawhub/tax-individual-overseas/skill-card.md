## Description: <br>
个人（居民个人/境内个人）直持境外证券、存款、房产的涉税申报、税收抵免与合规投资通道一站式筹划。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, individual investors, and tax advisors use this skill to assess China tax, foreign-exchange, CRS, and reporting considerations for personally held overseas securities, deposits, real estate, and related offshore structures. It supports policy Q&A, risk self-checks, tax calculations, remediation checklists, and compliance report drafting. <br>

### Deployment Geography for Use: <br>
Global, with substantive focus on China tax and foreign-exchange compliance. <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and user scenarios may be sent to mcp.aitaxs.top for remote policy answers, risk checks, tax calculations, and knowledge-base listings. <br>
Mitigation: Use anonymized or minimized scenarios, avoid names, account details, asset identifiers, and other sensitive tax data, and install only if this remote data flow is acceptable. <br>
Risk: The skill can persist an API key and raw query logs under a local user data directory. <br>
Mitigation: Review local storage practices before use, protect the host account, avoid shared machines for sensitive cases, and periodically inspect or remove stored logs and configuration. <br>
Risk: Optional autosetup behavior can write MCP configuration entries when explicitly enabled or run. <br>
Mitigation: Keep autosetup disabled unless needed, review proposed configuration changes before enabling writes, and confirm backups are available. <br>
Risk: Tax calculations, policy interpretation, and risk scoring are decision-support outputs and may be incomplete or stale for a specific taxpayer or jurisdiction. <br>
Mitigation: Verify material conclusions against official sources and consult a qualified tax advisor or relevant authority before filing, restructuring, or remediating. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-individual-overseas) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Personal overseas investment self-check page](https://mcp.aitaxs.top/web/topic_workflow_individual_overseas.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured checklists, JSON-like tool results, local command examples, and generated compliance report text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP tools for policy answers, risk checks, tax calculations, and knowledge-base listings; offline scripts provide local reference guidance when remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

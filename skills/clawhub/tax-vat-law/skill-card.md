## Description: <br>
增值税法及实施条例2026施行落地专项助手，面向应税交易识别、税目适用、进项抵扣、混合销售与兼营核算、留抵退税风控、登记起征点与优惠衔接提供结构化合规自检和实操指引。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax practitioners, finance teams, and developers use this skill to ask China VAT-law implementation questions, run structured VAT compliance self-checks, identify invoice and refund risks, and produce practical remediation guidance. It is scoped to guidance and self-check workflows, not tax filing, invoicing-system operation, legal representation, or guaranteed tax authority outcomes. <br>

### Deployment Geography for Use: <br>
Global (content focuses on China VAT compliance) <br>

## Known Risks and Mitigations: <br>
Risk: Cloud-connected tax queries and web self-check inputs may be transmitted to mcp.aitaxs.top and may involve sensitive taxpayer, contract, invoice, or investigation details. <br>
Mitigation: Use only data you are willing to send to that service, redact sensitive identifiers where possible, and avoid entering highly sensitive matters unless the organization accepts the transmission and logging posture. <br>
Risk: The client stores API credentials, cache, and logs under ~/.tax-policy-client, and the web workflow stores an API key and client identifier in browser localStorage. <br>
Mitigation: Review and clear ~/.tax-policy-client and relevant browser localStorage after use on shared or managed machines, and treat stored API keys as credentials. <br>
Risk: Running config/init_agent.py directly or enabling TAX_ENABLE_AUTOSETUP can write MCP entries into local agent or editor configuration. <br>
Mitigation: Keep auto-setup disabled unless intentional, review proposed MCP configuration changes first, and back up or inspect affected client configuration files after setup. <br>
Risk: Tax guidance can be time-sensitive and jurisdiction-specific, and the skill itself states that final treatment depends on current official rules and competent tax authority or judicial determinations. <br>
Mitigation: Validate conclusions against current official policy documents and qualified tax or legal professionals before filing, claiming refunds, or making material compliance decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-vat-law) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [VAT law self-check web workflow](https://mcp.aitaxs.top/web/topic_workflow_vat_law.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge MCP endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>
- [Comprehensive tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Digital invoice compliance skill](https://skillhub.cn/skills/tax-invoice-compliance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, JSON-style tool responses, MCP tool calls, web self-check results, and Python command-line output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP tools for policy Q&A, risk checks, tax calculations, and knowledge-base metadata; offline scripts provide local reference and workflow guidance when the cloud service is unavailable.] <br>

## Skill Version(s): <br>
3.15.6 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

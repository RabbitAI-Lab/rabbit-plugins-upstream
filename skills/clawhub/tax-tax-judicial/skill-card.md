## Description: <br>
涉税司法案例与税务争议裁判规则专项助手。聚焦最高法危害税收征管犯罪典型案例、虚开专票罪三档量刑与出罪规则、下游受票方复议诉权、机械征税被撤销等裁判规则；提供涉税刑事与争议风险自检与全链路闭环实操，覆盖交易真实性—证据链—程序合法性—复议诉讼—内控整改全流程。（聚焦涉税司法、虚开量刑、虚开出罪、下游诉权、机械征税、阴阳合同逃税、税务争议。） <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax teams, and advisors use this skill to explore Chinese tax judicial cases, tax dispute paths, invoice-related criminal risk, downstream invoice recipient rights, and practical self-check steps. It provides guidance and structured risk review prompts, not legal representation or guaranteed outcomes. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax dispute facts, taxpayer identities, litigation strategy, invoices, or business-sensitive details may be sent to remote services or public search engines during fallback. <br>
Mitigation: Use sanitized prompts, avoid entering confidential or identifiable details, and confirm organizational approval before using remote MCP or fallback search behavior. <br>
Risk: The skill stores local identifiers, API keys, cache, and logs in local browser storage and ~/.tax-policy-client. <br>
Mitigation: Review and clear browser localStorage and ~/.tax-policy-client when persistent identifiers, API keys, or local logs should not remain on the device. <br>
Risk: Auto-setup can alter MCP client configuration when TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Leave TAX_ENABLE_AUTOSETUP disabled unless configuration changes are intentional, and review generated MCP client settings before use. <br>
Risk: Tax and judicial guidance can be incomplete, outdated, or unsuitable for a specific dispute or criminal-risk scenario. <br>
Mitigation: Treat outputs as decision support only and verify important conclusions against official sources and qualified tax or legal professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-tax-judicial) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Interactive tax judicial workflow](https://mcp.aitaxs.top/web/topic_workflow_tax_judicial.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>
- [Tax policy API service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge) <br>
- [Related tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Related tax invoice compliance skill](https://skillhub.cn/skills/tax-invoice-compliance) <br>
- [Related tax compliance dispute skill](https://skillhub.cn/skills/tax-compliance-dispute) <br>
- [Related VAT law skill](https://skillhub.cn/skills/tax-vat-law) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown and structured text with links, checklists, risk summaries, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP tools and web workflow pages; offline fallback provides limited self-check guidance when remote services are unavailable.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

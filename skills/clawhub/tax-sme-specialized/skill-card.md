## Description: <br>
A Chinese-language tax compliance assistant for specialized and innovative SMEs, covering certification data consistency, R&D expense treatment, fiscal subsidy tax treatment, Beijing Stock Exchange listing tax planning, qualification renewal, related-party pricing, and structured self-check reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, tax professionals, and enterprise compliance teams use this skill to ask tax-policy questions, run SME compliance self-checks, scan risk scenarios, calculate tax impacts, and generate actionable remediation guidance. It is focused on China tax compliance workflows for specialized and innovative SMEs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax and compliance questions may be processed by mcp.aitaxs.top. <br>
Mitigation: Use only with approval for the relevant data, avoid entering confidential client data unless authorized, and verify privacy and data-handling expectations before deployment. <br>
Risk: API keys and logs may be stored locally by the skill's client tooling. <br>
Mitigation: Protect the local user profile where the client stores configuration and logs, and review or remove local credentials and logs according to organizational policy. <br>
Risk: Optional setup behavior can modify local MCP or editor configuration when explicitly enabled. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run setup routines directly unless configuration changes are intended, and review resulting MCP/editor configuration before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-sme-specialized) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [SME tax compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_sme_specialized.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [High-tech and R&D deduction skill](https://skillhub.cn/skills/tax-high-tech-rd) <br>
- [IPO tax compliance skill](https://skillhub.cn/skills/tax-ipo-compliance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, JSON tool responses, Python helper code, shell/configuration snippets, and browser-generated text reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route tax-policy questions, risk checks, tax calculations, and knowledge-base listings through a cloud MCP service, with offline fallback guidance when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

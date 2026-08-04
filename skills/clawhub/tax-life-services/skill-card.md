## Description: <br>
Tax Life Services helps users assess Chinese tax compliance risks and practical handling steps for life-service businesses, especially medical beauty providers and gold or jewelry retailers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business operators use this skill to ask tax-policy questions, run light compliance self-checks, identify invoice, revenue-recognition, private-account collection, and prepaid-card risks, and draft practical remediation or self-check report content. Developers or agent operators may also use the bundled MCP client and offline workflows to connect the agent to cloud tax-policy tools or local fallback guidance. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send tax questions, scenarios, and self-check metrics to mcp.aitaxs.top. <br>
Mitigation: Avoid entering names, taxpayer IDs, bank details, invoice numbers, or other regulated data unless the provider's privacy practices have been reviewed. <br>
Risk: The client may store local API credentials and diagnostic logs. <br>
Mitigation: Use the skill only on trusted devices, restrict access to local user data, and review or remove local configuration and log files when handling sensitive matters. <br>
Risk: Automatic setup can modify MCP client configuration files when explicitly enabled or when init_agent.py is run directly. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run config/init_agent.py directly unless configuration changes are intended; inspect backups and resulting MCP entries after setup. <br>
Risk: Tax calculations, risk scores, and policy guidance are time-sensitive and may be incomplete for a specific case. <br>
Mitigation: Verify material conclusions against official tax authority sources and consult a qualified tax or legal professional before filing, remediation, or dispute action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-life-services) <br>
- [Life services compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_life_services.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown answers, structured risk results, generated report text, Python helper code, MCP configuration snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may rely on cloud MCP tools for current tax-policy answers and local offline workflows when the remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.10 (source: frontmatter and server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

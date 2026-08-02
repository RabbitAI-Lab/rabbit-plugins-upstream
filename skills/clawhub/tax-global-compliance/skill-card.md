## Description: <br>
Provides conversational guidance for Chinese companies assessing overseas employment, payroll, tax, transfer pricing, data-transfer, and related compliance risks across major investment destinations using public authoritative sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, business teams, and compliance practitioners use this skill to triage cross-border operating questions, identify likely employment, tax, data-transfer, and overseas risk issues, and assemble next-step checklists before seeking qualified local professional advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive compliance questions and risk scenarios may be sent to mcp.aitaxs.top and, during fallback behavior, public search engines. <br>
Mitigation: Do not submit confidential, personal, or regulated data unless the destination services are approved for that data; use sanitized scenarios where possible. <br>
Risk: Local API keys, anonymous identifiers, cache entries, and raw query logs may be written on the host. <br>
Mitigation: Restrict filesystem access, review and clear local client data as needed, and manage API keys according to the deploying organization's secrets policy. <br>
Risk: Auto-setup behavior can modify MCP client configuration files when explicitly enabled. <br>
Mitigation: Leave TAX_ENABLE_AUTOSETUP disabled unless automatic client configuration is intended; review generated configuration changes and backups before use. <br>
Risk: The packaged backend and offline tools may not fully match the advertised global-compliance scope. <br>
Mitigation: Treat responses as triage rather than legal or tax advice, verify source citations, and route material decisions to qualified local professionals. <br>
Risk: Server evidence marks the release verdict as suspicious because of under-disclosed cloud forwarding, local persistence, host-client probing, and mismatched tax-policy tooling. <br>
Mitigation: Perform an installation review focused on data flows, local persistence, client probing, and whether the available tools meet the intended compliance use case. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-global-compliance) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Global compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_global_compliance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Cross-border tax architecture skill](https://skillhub.cn/skills/tax-crossborder) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown or plain-text guidance, JSON-like tool results, and local HTML workflow output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are compliance triage and workflow guidance; tax and legal conclusions should be verified against authoritative sources and qualified local professional advice.] <br>

## Skill Version(s): <br>
3.15.7 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

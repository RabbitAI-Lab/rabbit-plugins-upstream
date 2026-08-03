## Description: <br>
tax-global-compliance helps agents provide structured global compliance guidance for Chinese companies evaluating overseas employment, payroll, tax, transfer-pricing, data-transfer, and market-entry risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business users and agents use this skill to triage outbound-investment compliance questions, identify country-specific employment and tax issues, and produce structured checklists or guidance before engaging qualified local professionals. It is especially focused on Chinese companies entering or operating in overseas markets. <br>

### Deployment Geography for Use: <br>
Global, with content focused on Chinese outbound investment and named destination markets including the United States, Saudi Arabia, Indonesia, Mexico, and Brunei. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send tax, payroll, employment, or cross-border business questions and risk scenarios to mcp.aitaxs.top when online. <br>
Mitigation: Review intended use before installation in sensitive environments and avoid entering confidential business, payroll, or personal data unless the deployment has approved that service. <br>
Risk: The skill stores identifiers, API keys, and local logs under ~/.tax-policy-client, and the web self-check flow can persist identifiers or keys in browser localStorage. <br>
Mitigation: Clear ~/.tax-policy-client and relevant browser localStorage when removing the skill or when persisted identifiers, keys, or logs should not remain on the device. <br>
Risk: The setup path can alter local MCP client configuration when TAX_ENABLE_AUTOSETUP is enabled or auto_setup is run with dry_run disabled. <br>
Mitigation: Leave TAX_ENABLE_AUTOSETUP unset unless configuration changes are intended, and review client MCP configuration before and after any setup run. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-global-compliance) <br>
- [Global compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_global_compliance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Cross-border tax architecture skill](https://skillhub.cn/skills/tax-crossborder) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with checklists, structured risk summaries, and optional code or shell-command snippets for local tools.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use online MCP-backed responses when configured, with offline workflow guidance available when the remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

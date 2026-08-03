## Description: <br>
A Chinese tax compliance assistant for transfer-pricing and contemporaneous-documentation workflows, including related-party reporting, method selection, APA preparation, thin-capitalization checks, CFC considerations, self-checklists, risk scans, and remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, enterprise tax teams, and tax advisors use this skill to structure transfer-pricing questions, generate compliance self-checks and contemporaneous-documentation checklists, scan related-party transaction risks, and prepare follow-up remediation guidance. Outputs are decision-support material and should be reviewed against official tax authority requirements before filing or formal tax action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Company tax, transfer-pricing, audit, APA, CFC, or related-party data may be sent to the remote MCP service and possibly to public search engines during fallback. <br>
Mitigation: Use synthetic or minimized data unless the deployment has approved the remote service and fallback behavior for the relevant confidentiality requirements. <br>
Risk: API keys and logs may persist under ~/.tax-policy-client. <br>
Mitigation: Inspect that directory before and after installation, restrict local file permissions, and remove or rotate stored keys when the skill is no longer needed. <br>
Risk: Optional auto-setup can modify MCP client configuration. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled by default and review config/init_agent.py behavior, generated config changes, and backups before enabling automatic setup. <br>
Risk: Tax compliance guidance can be incomplete, outdated, or jurisdiction-specific. <br>
Mitigation: Validate outputs against official tax authority materials and qualified tax professionals before filing, APA negotiation, audit response, or other formal action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-transfer-pricing) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Transfer pricing workflow page](https://mcp.aitaxs.top/web/topic_workflow_transfer_pricing.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration, Shell commands] <br>
**Output Format:** [Markdown text with structured checklists, links, and configuration or shell-command snippets when setup guidance is needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use online MCP-backed tax tools or local offline reference scripts; outputs require professional review before use for real tax compliance decisions.] <br>

## Skill Version(s): <br>
3.15.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
This skill helps Chinese companies assess global expansion compliance across employment, payroll and individual tax, transfer pricing and cross-border tax, data transfers, and overseas operational risk topics using public authoritative sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business, tax, legal, and operations teams use this skill to ask scenario-based questions and receive structured compliance checklists, source-oriented guidance, and risk triage for overseas market entry and operations. <br>

### Deployment Geography for Use: <br>
Global, with content focused on Chinese outbound investment and selected destination countries. <br>

## Known Risks and Mitigations: <br>
Risk: Questions, risk scenarios, and self-check indicators may be submitted to a third-party cloud tax/compliance service. <br>
Mitigation: Do not enter confidential payroll, tax exposure, employee, customer, or data-transfer details unless the vendor and retention model are approved by your organization. <br>
Risk: The package may store local logs, cached data, or API key configuration for MCP client use. <br>
Mitigation: Review or disable local logs and stored API keys where possible, and clear local client data according to organizational policy. <br>
Risk: Optional setup behavior can modify local MCP settings for supported AI clients. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run setup scripts directly unless you intentionally want the skill to update local MCP configuration. <br>
Risk: Compliance guidance can become outdated or require jurisdiction-specific professional judgment. <br>
Mitigation: Verify important employment, tax, data-transfer, and market-entry conclusions against current official sources and qualified local professionals before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-global-compliance) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Shell commands, Guidance] <br>
**Output Format:** [Markdown or plain text guidance with optional configuration snippets and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include structured compliance steps, risk levels, source-oriented notes, offline fallback references, and MCP setup guidance.] <br>

## Skill Version(s): <br>
3.15.4 (source: evidence release version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Assists with China-focused IPO tax compliance review, including tax incentive reliance, disclosure requirements, red-chip tax documentation, exchange review concerns, structured self-checks, and compliance report guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax, finance, legal, and compliance teams use this skill to assess IPO tax compliance questions, organize self-check findings, identify review risks, and prepare practical remediation or disclosure guidance for China-related listing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive IPO, ownership, transaction, or personal tax details may be sent to a cloud-backed Chinese tax-policy service. <br>
Mitigation: Minimize or anonymize sensitive inputs, and use the skill only when remote processing is acceptable for the data involved. <br>
Risk: Local credentials, configuration, cache, or logs may remain under the user's tax-policy client data directory after use. <br>
Mitigation: Review and clear local tax-policy client logs and configuration after sensitive sessions. <br>
Risk: Optional setup behavior can modify MCP client configuration when explicitly enabled or run directly. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run setup modules unless configuration changes are intended; inspect any changes and backups afterward. <br>
Risk: The security verdict is suspicious because the skill combines tax-compliance assistance with remote routing, local credential handling, logging, and configuration changes that are not fully disclosed. <br>
Mitigation: Review the skill before installation and deploy it only when those behaviors match the intended trust and operating model. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-ipo-tax) <br>
- [IPO tax compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_ipo_tax.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown and structured text; JSON may be returned through MCP tool calls.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include compliance checklists, risk rankings, tax calculation results, policy references, and remediation or disclosure guidance.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

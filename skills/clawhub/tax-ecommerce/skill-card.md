## Description: <br>
Tax Ecommerce helps users assess tax and invoicing compliance for Chinese ecommerce stores, livestream sales, MCNs, platform reporting, private-account payments, and related audit scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business compliance teams use this skill to ask tax-policy questions, run lightweight ecommerce and livestream compliance self-checks, identify risk indicators, and generate practical remediation guidance for Chinese platform-commerce scenarios. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, self-check metrics, and tax/compliance questions may be sent to mcp.aitaxs.top for remote MCP processing. <br>
Mitigation: Use the skill only if that service is trusted, avoid entering unnecessary business identifiers or personal data, and prefer the offline fallback for low-sensitivity preliminary review. <br>
Risk: The package stores local credentials and logs for MCP access. <br>
Mitigation: Review local configuration and log files after installation, protect the workspace account, and remove stored credentials if the skill is no longer needed. <br>
Risk: Optional setup code can modify local MCP client configuration when explicitly enabled or run directly. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run config/init_agent.py directly unless the user intentionally wants the skill to change local agent configuration. <br>
Risk: Tax-policy answers and self-check results are advisory and may not reflect every local or time-sensitive requirement. <br>
Mitigation: Treat outputs as preliminary guidance and confirm material filing, audit, legal, or dispute decisions with official sources or qualified tax professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-ecommerce) <br>
- [Ecommerce compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_ecommerce.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [State Taxation Administration of China](https://www.chinatax.gov.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown and structured text with optional self-check reports and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a remote MCP service for policy answers, risk checks, tax calculations, and knowledge-base listings; local offline fallback provides limited reference guidance.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

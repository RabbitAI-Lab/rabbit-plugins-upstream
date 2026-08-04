## Description: <br>
Provides specialized tax-compliance guidance for "specialized and sophisticated little giant" SMEs, including certification data consistency, R&D expense treatment, high-tech 15% tax status maintenance, fiscal subsidy tax treatment, Beijing Stock Exchange listing tax planning, qualification renewal, related-party pricing, self-checks, measurement, and remediation planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax/compliance practitioners use this skill to structure SME tax-compliance checks, compare reported R&D and financial data across regimes, plan subsidy and listing-related tax treatment, and produce practical remediation guidance. It is focused on China-oriented tax scenarios for specialized SME and high-tech enterprise workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax and compliance prompts may be processed by the remote mcp.aitaxs.top service. <br>
Mitigation: Use only when the user accepts cloud processing; avoid entering confidential client, employee, financial, or transaction details unless the service and its retention claims are trusted. <br>
Risk: The skill may store an API key, device identifier, cache data, and logs locally. <br>
Mitigation: Review local storage expectations before installation and rotate or remove locally stored credentials and logs according to the user's data-handling policy. <br>
Risk: Fallback behavior may send queries to public search engines. <br>
Mitigation: Disable or avoid fallback mode for sensitive tax matters, or sanitize prompts before allowing fallback search. <br>
Risk: Optional setup can modify local MCP client configuration. <br>
Mitigation: Do not run config/init_agent.py or enable TAX_ENABLE_AUTOSETUP unless the user intentionally wants the skill to write MCP client configuration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-sme-specialized) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Interactive SME tax-compliance self-check](https://mcp.aitaxs.top/web/topic_workflow_sme_specialized.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Remote MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text, Configuration, Shell commands] <br>
**Output Format:** [Markdown and plain text guidance, with optional configuration snippets and command-line workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route tax prompts to a remote MCP service or use local offline reference workflows depending on availability and configuration.] <br>

## Skill Version(s): <br>
3.15.10 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

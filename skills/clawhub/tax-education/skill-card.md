## Description: <br>
Provides education and training-sector China tax compliance guidance, including VAT exemption checks, non-degree education tax handling, childcare and private-school issues, teacher payroll tax, invoice compliance, risk self-checks, and compliance report support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, tax advisors, and agent operators use this skill to ask education-sector tax questions, run lightweight compliance self-checks, and draft risk-oriented tax guidance for training providers, private schools, childcare providers, and related education businesses. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax questions, scenarios, and self-check metrics may be sent to a cloud service. <br>
Mitigation: Review the provider's privacy and retention terms before use, avoid entering confidential taxpayer, payroll, invoice, bank, or audit details, and prefer anonymized or generalized scenarios. <br>
Risk: The skill can persist local API credentials and logs. <br>
Mitigation: Inspect and manage the local credential and log directories before production use, rotate or delete stored API credentials when no longer needed, and avoid shared-machine deployments without access controls. <br>
Risk: Optional setup behavior may register MCP configuration in other agent clients. <br>
Mitigation: Keep auto-setup disabled unless intentionally enabling it, review generated MCP configuration before use, and remove unwanted MCP entries from affected clients. <br>
Risk: Tax guidance may be incomplete, outdated, or unsuitable for a specific taxpayer's facts. <br>
Mitigation: Treat outputs as educational support, verify policy positions against official sources, and involve qualified tax or legal professionals for filing, audit, dispute, or high-value decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-education) <br>
- [Education compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_education.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown and structured text with optional MCP tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call cloud MCP tools for policy answers, risk checks, tax calculations, and knowledge-base metadata; includes local fallback guidance when remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.6 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Tax Renewable helps renewable-resource and scrap-recycling businesses handle Chinese tax compliance questions, reverse-invoicing workflows, resource-comprehensive-use VAT refund checks, risk self-assessments, and practical report templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, tax teams, and compliance professionals use this skill to ask scenario-specific questions about China's renewable-resource recycling tax rules, run lightweight compliance self-checks, and draft checklists or reports for reverse invoicing, VAT treatment, and common audit risks. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill may send tax questions, risk scenarios, and web self-check metrics to mcp.aitaxs.top. <br>
Mitigation: Review data-sharing expectations before use and avoid entering real enterprise identifiers or sensitive tax facts unless they are necessary. <br>
Risk: The skill can store a local API key and logs under ~/.tax-policy-client. <br>
Mitigation: Use it only on trusted hosts, restrict access to the local user profile, and inspect or remove the local credential and log directory when decommissioning the skill. <br>
Risk: Setup behavior may modify MCP client configuration when autosetup is enabled or setup scripts are run. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run setup scripts unless configuration changes are intended; review client configuration and backups afterward. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-renewable) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Renewable-resource compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_renewable.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown-style answers, JSON-like tool responses, and copied report text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include policy source notes, risk levels, checklists, calculations, setup guidance, and self-check report drafts.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

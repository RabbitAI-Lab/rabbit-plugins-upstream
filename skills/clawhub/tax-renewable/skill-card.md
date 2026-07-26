## Description: <br>
Tax Renewable Resources helps agents answer renewable-resource and waste-material tax compliance questions, run self-check workflows, and draft practical guidance for reverse invoicing, VAT refund, simplified tax, invoice-flow, and audit-risk scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax, finance, and compliance users use this skill to explore China-focused renewable-resource tax policy, reverse invoicing, resource-utilization VAT refund, simplified tax, risk indicators, cases, templates, and self-check reports. The outputs are advisory support for review by qualified tax or legal professionals, not a substitute for filing, audit, or legal representation. <br>

### Deployment Geography for Use: <br>
China-focused <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and self-check metrics may be sent to mcp.aitaxs.top. <br>
Mitigation: Use the skill only when remote processing is acceptable, avoid unnecessary sensitive business data, and review the service endpoint before deployment. <br>
Risk: The skill can store service credentials and logs locally. <br>
Mitigation: Protect local configuration files, remove stored credentials when uninstalling, and rotate keys if the local environment may be exposed. <br>
Risk: Client MCP configuration files can be modified when TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Leave auto-setup disabled unless the user intends configuration changes, and inspect any proposed MCP client changes before use. <br>
Risk: The one-click matrix installer may download and install related tax skills. <br>
Mitigation: Avoid the matrix installer until each package source and download URL has been verified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-renewable) <br>
- [Renewable-resource self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_renewable.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown and structured text with optional configuration or command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP service, launch a web self-check workflow, store local service credentials, or propose related skill installation; review outputs before operational tax use.] <br>

## Skill Version(s): <br>
3.14.38 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

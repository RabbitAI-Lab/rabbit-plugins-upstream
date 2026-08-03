## Description: <br>
tax-govsubsidy helps agents provide China tax-compliance guidance for government subsidies and fiscal funds, including non-taxable income qualification, dedicated accounting, expense treatment, five-year tracking, input VAT treatment, self-check templates, and remediation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external tax practitioners, and developers use this skill to triage government subsidy tax treatment, generate structured self-check guidance, prepare dedicated-accounting and five-year tracking templates, and route questions to online or offline tax-compliance workflows. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax or compliance questions and self-check metrics may be sent to mcp.aitaxs.top. <br>
Mitigation: Use the skill only when the organization approves this remote service, and avoid submitting confidential business tax facts unless that use is authorized. <br>
Risk: The skill can persist local API credentials for MCP access. <br>
Mitigation: Review where credentials are stored, restrict local file permissions, and remove stored credentials when access is no longer needed. <br>
Risk: Setup flows may change local MCP client configuration. <br>
Mitigation: Review configuration changes before enabling auto-setup, keep backups, and confirm that the configured MCP endpoint is expected. <br>
Risk: Tax guidance can be time-sensitive and may not replace official tax authority or professional determinations. <br>
Mitigation: Confirm final positions against current official rules and qualified tax advice before filing, deducting expenses, or treating subsidy funds as non-taxable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-govsubsidy) <br>
- [Government subsidy workflow page](https://mcp.aitaxs.top/web/topic_workflow_govsubsidy.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Comprehensive tax policy knowledge skill](https://skillhub.cn/skills/user_11064e10/tax-policy-knowledge) <br>
- [High-tech and R&D deduction skill](https://skillhub.cn/skills/user_11064e10/tax-high-tech-deduction) <br>
- [Tax incentives skill](https://skillhub.cn/skills/user_11064e10/tax-incentives) <br>
- [Green and energy-saving tax skill](https://skillhub.cn/skills/user_11064e10/tax-renewable) <br>
- [Environmental tax and carbon skill](https://skillhub.cn/skills/user_11064e10/tax-environmental) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, plain text, JSON-style tool responses, Python code, MCP configuration snippets, and interactive web workflow outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include tax-compliance checklists, risk levels, policy-source prompts, self-check reports, dedicated-accounting templates, five-year tracking guidance, local setup guidance, and offline fallback references.] <br>

## Skill Version(s): <br>
3.15.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

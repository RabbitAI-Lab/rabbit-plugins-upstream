## Description: <br>
Battery consumption-tax compliance assistant focused on staged tax rates, exemption lists, CMA testing reports, entrusted-processing deductions, self-produced self-use treatment, compliance self-checks, and practical risk guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax teams, and compliance practitioners use this skill to answer battery consumption-tax questions, run self-checks and risk scans, and prepare practical guidance for tax-rate timing, exemptions, CMA report requirements, deductions, and self-use declarations. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags broad cloud-backed tax tooling and under-disclosed remote data flows involving mcp.aitaxs.top. <br>
Mitigation: Review the skill before installation, avoid entering confidential company, tax, or compliance facts unless the remote service is approved, and validate important tax conclusions against official sources or qualified advisers. <br>
Risk: The skill can persist API credentials locally and stores browser credentials in localStorage for the web workflow. <br>
Mitigation: Use trusted devices and profiles, restrict local file and browser access, and clear local configuration or browser storage when the skill is no longer needed. <br>
Risk: Optional MCP client auto-setup can modify local AI-client configuration when TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled unless configuration changes are intentional; inspect client configuration and backups after enabling it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-consumption-tax) <br>
- [Battery consumption-tax self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_consumption_tax.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Related tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Related manufacturing tax risk skill](https://skillhub.cn/skills/tax-mfg-lifecycle-risk) <br>
- [Related industry tax risk skill](https://skillhub.cn/skills/tax-industry-tax-risk) <br>
- [Related VAT law skill](https://skillhub.cn/skills/tax-vat-law) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown text with structured checklists, policy references, self-check links, and concise risk or remediation guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include links to web self-check flows and offline fallback guidance when cloud tools are unavailable.] <br>

## Skill Version(s): <br>
3.15.8 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

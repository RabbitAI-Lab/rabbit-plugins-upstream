## Description: <br>
A Chinese-language tax judicial case and tax dispute assistant focused on invoice crime sentencing and non-criminalization rules, downstream invoice recipient rights, mechanical tax assessment challenges, and practical risk self-checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax, finance, compliance, and legal-support users can use this skill to ask about Chinese tax-related judicial cases, invoice-crime risk, administrative reconsideration or litigation paths, and structured tax dispute self-checks. It produces practical guidance and checklists, but final tax, litigation, or criminal-defense decisions should be reviewed by qualified professionals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax questions or case facts may be sent to the cloud-backed MCP endpoint. <br>
Mitigation: Do not enter confidential case facts, taxpayer identifiers, or legal strategy until endpoint trust and data handling have been reviewed. <br>
Risk: The skill stores a local API key and logs during use. <br>
Mitigation: Review local storage and logging behavior before deployment, and rotate or remove stored credentials if the skill is no longer trusted. <br>
Risk: The skill may fall back to public search engines when the main service is unavailable. <br>
Mitigation: Avoid sending confidential or identifying information in fallback queries, and verify search-derived guidance against authoritative tax and legal sources. <br>
Risk: Optional setup code can modify MCP client configuration files when explicitly enabled. <br>
Mitigation: Keep setup in dry-run mode unless configuration changes are intended, and review backups and merged MCP entries before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-tax-judicial) <br>
- [Tax judicial workflow page](https://mcp.aitaxs.top/web/topic_workflow_tax_judicial.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Related tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Related tax invoice compliance skill](https://skillhub.cn/skills/tax-invoice-compliance) <br>
- [Related tax compliance dispute skill](https://skillhub.cn/skills/tax-compliance-dispute) <br>
- [Related VAT law skill](https://skillhub.cn/skills/tax-vat-law) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with structured checklists, risk summaries, report-style guidance, optional code snippets, and configuration or shell command instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route questions to a cloud-backed MCP endpoint, use offline fallback guidance when unavailable, and provide links to web self-check workflows.] <br>

## Skill Version(s): <br>
3.15.10 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

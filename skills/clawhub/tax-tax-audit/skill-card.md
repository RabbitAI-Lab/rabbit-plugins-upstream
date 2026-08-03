## Description: <br>
Tax Tax Audit helps users reason through enterprise tax compliance audit and tax-audit workflows, including financial statement audit tax procedures, tax internal-control testing, tax-fraud indicators, key audit matter disclosure, and structured self-check reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax practitioners, auditors, and compliance teams use this skill to obtain structured tax-audit guidance, risk self-checks, audit procedure checklists, and report-ready remediation suggestions. The content is reference guidance and should be reviewed by qualified tax, audit, or legal professionals before use in formal filings, audit opinions, or client advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax and audit prompts may be sent to the mcp.aitaxs.top cloud service and, during fallback, to public search providers. <br>
Mitigation: Do not enter confidential client, company, financial, or personal data unless the organization has approved that processing path; use synthetic or redacted facts for exploratory use. <br>
Risk: The skill can create and store API credentials, cache data, health state, and logs in local user directories. <br>
Mitigation: Review the local credential and log locations before enterprise deployment, apply workstation access controls, and rotate or delete generated credentials when the skill is removed. <br>
Risk: Auto-setup behavior can modify local MCP client configuration when explicitly enabled. <br>
Mitigation: Keep auto-setup disabled until configuration changes are reviewed; prefer dry-run output and manually approve any MCP client edits. <br>
Risk: Tax calculations, audit risk ratings, and compliance suggestions may be inaccurate or incomplete for a specific jurisdiction, date, or client fact pattern. <br>
Mitigation: Treat outputs as reference material only and require review by qualified tax, audit, or legal professionals before relying on them for filings, audit opinions, or client advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-tax-audit) <br>
- [Tax audit self-check page](https://mcp.aitaxs.top/web/topic_workflow_tax_audit.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown and structured text with checklists, risk ratings, policy references, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a cloud MCP service for policy Q&A, risk checks, calculations, and knowledge-base listings; local fallback can provide limited offline guidance or public-search summaries.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

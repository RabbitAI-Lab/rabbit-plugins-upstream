## Description: <br>
Tax Equity Governance helps users assess China-focused tax and governance questions for equity transfers, family ownership structures, state-owned enterprise mixed-ownership reform, VIE/red-chip structures, and equity-structure tax burden comparisons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax, finance, governance, or corporate advisers use this skill to ask equity-governance tax questions, run structured self-checks, compare transaction or ownership structures, identify risks, and draft compliance reports or remediation checklists. <br>

### Deployment Geography for Use: <br>
Global; content is focused on China tax and corporate-governance scenarios. <br>

## Known Risks and Mitigations: <br>
Risk: Cloud-backed tax assistance may send questions, self-check metrics, or related usage data to mcp.aitaxs.top. <br>
Mitigation: Review the provider's privacy and retention terms before entering confidential transaction, shareholder, or tax facts; use only non-sensitive or redacted scenarios until approved. <br>
Risk: The skill may persist local API credentials, client IDs, logs, or cache data for its MCP client. <br>
Mitigation: Inspect local client storage and credential handling before deployment, rotate generated credentials when needed, and avoid shared-machine use without a local data policy. <br>
Risk: Setup code can alter MCP client configuration when explicitly run or when autosetup is enabled. <br>
Mitigation: Run setup in dry-run or reviewed mode first, keep configuration backups, and enable automatic setup only for approved agent clients. <br>
Risk: Tax guidance may be incomplete or jurisdiction-dependent for high-stakes equity transactions. <br>
Mitigation: Require review by qualified tax professionals or the competent tax authority before filing, restructuring, or relying on calculations for material transactions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-equity-governance) <br>
- [Equity governance self-check page](https://mcp.aitaxs.top/web/topic_workflow_equity_governance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown guidance, structured checklist/report text, web self-check results, and optional local configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use cloud-backed MCP services when available and local offline reference tools when remote services are unavailable.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

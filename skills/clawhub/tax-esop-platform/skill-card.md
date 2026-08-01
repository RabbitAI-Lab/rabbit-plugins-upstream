## Description: <br>
A Chinese-language ESOP tax compliance assistant for employee shareholding platforms, covering deferred taxation, partnership and company platform tax treatment, dividend and exit scenarios, share-based payment, nominee holding, listing review, calculations, risk checks, and compliance report drafting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, legal, HR, and advisory users use this skill to evaluate employee shareholding platform structures, tax treatments, risk indicators, filing considerations, and exit scenarios under Chinese tax and listing-review practice. It can produce policy-grounded answers, structured risk checks, tax burden comparisons, implementation checklists, and draft compliance reports. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax and business prompts may be sent to the remote service at mcp.aitaxs.top and, during fallback, to public search providers. <br>
Mitigation: Use anonymized or synthetic facts unless the remote service and its retention practices are acceptable for the data being entered. <br>
Risk: Credentials and logs may be stored locally by the skill client. <br>
Mitigation: Review local configuration and log storage before deployment, restrict file access, and remove stored credentials or logs when they are no longer needed. <br>
Risk: Optional setup paths can modify MCP client configuration when autosetup is enabled or setup scripts are run directly. <br>
Mitigation: Run setup in dry-run mode first, review planned configuration changes and backups, and enable autosetup only in environments where the MCP endpoint is approved. <br>
Risk: The authoritative security summary flags under-disclosure around remote data sharing, local logging, credential storage, and optional configuration changes. <br>
Mitigation: Treat installation as requiring explicit review and user disclosure before use with taxpayer, employee, or company-identifying information. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-esop-platform) <br>
- [zxj2devs publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [ESOP self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_esop.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text, with optional generated files, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-language tax guidance may include calculations, checklists, policy references, risk summaries, and draft compliance reports.] <br>

## Skill Version(s): <br>
3.15.6 (source: release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

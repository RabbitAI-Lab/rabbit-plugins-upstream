## Description: <br>
A tax compliance assistant for employee shareholding platforms and ESOP-related scenarios, covering deferred taxation, holding-platform tax treatment, dividends, share transfers, equity holding proxies, listing review considerations, calculations, risk checks, and compliance report drafting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business, finance, tax, and legal-support users use this skill to ask ESOP and employee holding-platform tax questions, compare platform structures, run tax-burden calculations, identify compliance risks, and draft structured guidance or reports. It is most relevant to Chinese tax, equity-incentive, and listing-review workflows. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and scenario details may be sent to mcp.aitaxs.top for remote MCP processing. <br>
Mitigation: Avoid entering confidential payroll, cap-table, client, or listing-preparation details unless the remote service and retention terms meet organizational requirements. <br>
Risk: API credentials, cache files, health state, and logs may be persisted locally under the user's tax-policy client data directory or browser localStorage. <br>
Mitigation: Review local storage locations, restrict access to the user profile, and clear stored credentials or logs when handling sensitive matters. <br>
Risk: When automatic setup is explicitly enabled, the artifact can merge MCP server entries into supported agent configuration files. <br>
Mitigation: Leave TAX_ENABLE_AUTOSETUP unset unless the MCP configuration changes have been reviewed and approved; inspect generated backups and config diffs after enabling setup. <br>
Risk: Fallback searches against public search engines may occur when the remote service is unavailable. <br>
Mitigation: Treat fallback answers as lower assurance, avoid sensitive query text, and verify policy conclusions against authoritative sources before relying on them. <br>
Risk: The security verdict is suspicious because sensitive tax workflows depend on remote processing and local persistence. <br>
Mitigation: Run security review and deployment approval before using the skill in regulated, client-facing, payroll, cap-table, or IPO/listing-preparation workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-esop-platform) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [ESOP self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_esop.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, plain text, JSON-like tool results, generated Markdown/HTML reports, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP service for tax-policy questions, risk checks, calculations, and knowledge-base metadata; offline scripts provide local reference output and report generation.] <br>

## Skill Version(s): <br>
3.15.4 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

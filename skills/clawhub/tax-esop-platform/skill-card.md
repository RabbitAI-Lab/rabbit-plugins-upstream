## Description: <br>
Provides tax and compliance guidance for employee stock ownership platforms, including deferred taxation, partnership and company platform tax treatment, dividends, share-based payment, nominee shareholding, listing-review issues, risk checks, calculations, and report drafting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, legal, and listing-advisory users use this skill to assess employee stock ownership platform structures, calculate tax outcomes, run compliance self-checks, and draft risk or compliance reports. It should not be treated as a substitute for qualified tax, legal, securities, or filing advice. <br>

### Deployment Geography for Use: <br>
Global, with PRC tax-law subject matter <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax, company, compensation, ownership, or filing details may be sent to remote services or fallback public search engines. <br>
Mitigation: Use anonymized scenarios unless the user accepts that data sharing, and review the service endpoints before installation. <br>
Risk: The skill can persist API keys, health data, and logs under ~/.tax-policy-client. <br>
Mitigation: Inspect and manage ~/.tax-policy-client after use, and remove stored credentials or logs when they are no longer needed. <br>
Risk: Automatic MCP client setup may edit local client configuration when TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Leave TAX_ENABLE_AUTOSETUP unset for dry-run behavior, or review configuration changes and backups before enabling it. <br>
Risk: Tax and listing guidance may be incomplete or outdated for a specific transaction or filing. <br>
Mitigation: Verify conclusions against current official rules and qualified tax, legal, or securities advisers before filing or transaction decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-esop-platform) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [ESOP compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_esop.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Natural-language guidance, Markdown reports, structured calculation results, optional HTML report files, and setup snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP services for policy, risk, and calculation workflows; offline workflows can generate local reports from user-supplied metrics.] <br>

## Skill Version(s): <br>
3.15.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Tax Life Services helps agents answer Chinese tax-compliance questions for life-services businesses, with emphasis on medical beauty, gold and jewelry retail, invoice compliance, private-account payment risk, structured self-checks, templates, and practical remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business operators, finance teams, and tax advisors use this skill to triage life-services tax scenarios, generate compliance self-check guidance, identify invoice and revenue-recognition risks, and prepare report-style remediation outputs. It is most relevant to Chinese medical beauty, jewelry, precious-metals, private-payment, and membership-prepayment compliance workflows. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, risk scenarios, and tool inputs may be sent to the cloud-backed service at mcp.aitaxs.top. <br>
Mitigation: Do not enter confidential client data, personal identifiers, invoice details, account data, or other private records unless the service and data-handling behavior have been reviewed. <br>
Risk: The skill may persist API credentials and operational logs locally. <br>
Mitigation: Review local storage under the configured tax-policy client directory, restrict file permissions, remove credentials when no longer needed, and avoid submitting sensitive details in prompts. <br>
Risk: Optional MCP client configuration can modify local client settings when automatic setup is explicitly enabled. <br>
Mitigation: Keep setup in dry-run mode by default, enable automatic configuration only intentionally, and review generated MCP client entries before use. <br>
Risk: Tax outputs can be incomplete or stale for high-stakes filing, audit, or legal decisions. <br>
Mitigation: Treat outputs as assistance only and confirm material conclusions with official tax authority sources or qualified tax/legal professionals before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-life-services) <br>
- [Life-services compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_life_services.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, structured text, JSON-like tool responses, and occasional command or configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can call cloud-backed MCP tools for policy Q&A, risk checks, tax calculations, and knowledge-base listings, with offline reference workflows when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.4 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
A Chinese-language construction tax compliance assistant for identifying tax risks, running self-checks and calculations, and producing practical remediation guidance for construction-sector scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, construction businesses, tax teams, and professional advisors use this skill to ask China-focused construction tax questions, screen compliance risks, calculate project-related tax items, and draft self-check or remediation reports. It is intended as decision-support guidance and should not replace filing, audit, legal, or licensed tax advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive construction, payroll, bidding, tax, or accounting details may be sent to remote services or fallback search engines. <br>
Mitigation: Use redacted business summaries, avoid submitting confidential identifiers or raw records, and confirm organizational approval before use. <br>
Risk: Persistent API credentials may be stored locally by the Python client or browser self-check page. <br>
Mitigation: Administrators should review credential and localStorage handling, restrict access to local profiles, and clear or rotate keys when access changes. <br>
Risk: Optional setup behavior can alter MCP client configuration when explicitly enabled or when setup scripts are run directly. <br>
Mitigation: Review init_agent.py behavior before enabling TAX_ENABLE_AUTOSETUP or direct setup execution, and keep backups of existing MCP configuration. <br>
Risk: Tax and legal compliance guidance may be incomplete, outdated, or unsuitable for a specific filing or dispute. <br>
Mitigation: Validate outputs against current official sources and have licensed tax or legal professionals review high-impact decisions before filing or acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-construction) <br>
- [Construction compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_construction.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text responses, JSON-like tool results, copied reports, Python configuration/scripts, and command guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP services and a web self-check endpoint; includes local fallback reference outputs.] <br>

## Skill Version(s): <br>
3.15.6 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Provides Chinese tax restructuring guidance, self-check workflows, risk alerts, and report-oriented outputs for bankruptcy restructuring, listed-company restructuring, mergers, divisions, debt restructuring, and cross-border restructuring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance, tax, legal, and compliance users use this skill to ask restructuring tax questions, run structured self-checks, identify likely compliance risks, and prepare remediation-oriented tax analysis or self-inspection reports. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Confidential restructuring, bankruptcy, transaction, or tax facts may be sent to remote services. <br>
Mitigation: Use the skill only after approving the mcp.aitaxs.top data flow, and avoid entering client-identifying or confidential facts unless the publisher's retention and access controls are separately trusted. <br>
Risk: The skill may persist API credentials, logs, cache data, or browser identifiers locally. <br>
Mitigation: Run it in a controlled profile or workspace, review local skill/browser storage after use, and remove or rotate stored credentials when access is no longer needed. <br>
Risk: Optional installer and setup behavior can modify local skill directories or MCP client configuration. <br>
Mitigation: Review any setup or matrix-install action before enabling it, keep dry-run behavior where possible, and avoid enabling automatic configuration in sensitive environments. <br>
Risk: The server evidence marks the release as suspicious due to under-disclosed remote processing, local persistence, configuration changes, and matrix installation powers. <br>
Mitigation: Treat the skill as requiring review before installation, especially in environments that handle regulated tax, legal, or transaction data. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/zxj2devs/skills/tax-restructuring) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Restructuring compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_restructuring.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance, structured JSON tool responses, web self-check results, copyable prompts, reports, shell commands, and MCP configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP tools for tax policy questions, risk checks, calculations, and knowledge-base metadata; includes offline fallback guidance when remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

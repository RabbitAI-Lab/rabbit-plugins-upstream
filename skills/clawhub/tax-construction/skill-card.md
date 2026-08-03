## Description: <br>
Tax Construction is a construction-industry tax compliance assistant for identifying tax risks, checking common construction tax scenarios, calculating self-check metrics, and producing practical remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax teams, compliance staff, and developers use this skill to ask construction tax questions, run lightweight compliance self-checks, identify invoice, prepayment, subcontracting, labor, and bidding-related risks, and draft tax compliance reports or remediation checklists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security summary identifies under-disclosed remote data flows to mcp.aitaxs.top. <br>
Mitigation: Use the skill only with data that can be sent to that service, and redact payroll, tax IDs, bank data, contracts, and suspected misconduct details before use. <br>
Risk: The security guidance notes local or browser credential persistence. <br>
Mitigation: Review stored credentials and local configuration before deployment, rotate credentials if exposure is suspected, and limit use to trusted workstations. <br>
Risk: The security guidance warns that setup code can modify local agent configuration. <br>
Mitigation: Avoid running config/init_agent.py directly unless MCP client configuration changes are intended; review proposed config changes before enabling automatic setup. <br>
Risk: The skill provides tax and compliance guidance that may be incomplete, outdated, or jurisdiction-sensitive. <br>
Mitigation: Treat results as decision support, validate important conclusions against official tax authorities or qualified professionals, and avoid using generated outputs as final filings or legal advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-construction) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Construction compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_construction.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown answers, structured JSON tool results, local HTML workflow output, and Python or shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP service for tax policy, risk checks, calculations, and knowledge-base listing; includes local fallback scripts and a browser-based self-check workflow.] <br>

## Skill Version(s): <br>
3.15.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

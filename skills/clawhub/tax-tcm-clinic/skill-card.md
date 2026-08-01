## Description: <br>
Provides Chinese tax-compliance guidance, risk self-checks, policy Q&A, case references, and report-oriented remediation guidance for TCM clinics and medical institutions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax professionals, and clinic operators use this skill to ask China-focused tax compliance questions, run medical-institution risk self-checks, and draft practical remediation or compliance-report guidance. It is intended for decision support, not as a substitute for licensed tax, audit, or legal advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax, revenue, payroll, patient-adjacent, or business-operation details may be sent to the remote MCP service during policy Q&A, risk checks, calculations, or web self-check flows. <br>
Mitigation: Use sanitized or minimal scenarios, avoid entering personal or patient-identifying details, and confirm that remote processing is acceptable before using online workflows. <br>
Risk: Optional setup code can persist MCP client configuration when run directly or when TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Do not run config/init_agent.py directly or enable TAX_ENABLE_AUTOSETUP unless configuration changes are intended; review any client config backup and merged MCP entries afterward. <br>
Risk: Credentials, client identifiers, cache files, logs, or browser localStorage entries may remain after testing. <br>
Mitigation: After evaluation, inspect and clear browser localStorage keys used by the web page and the ~/.tax-policy-client directory if sensitive test data or credentials were used. <br>
Risk: Tax and compliance outputs may be incomplete, outdated, or unsuitable for a specific institution. <br>
Mitigation: Treat outputs as decision support and verify material conclusions with official tax authorities or licensed tax, audit, or legal professionals before filing or remediation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-tcm-clinic) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [TCM clinic compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_tcm_clinic.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with structured lists, JSON-like tool results, optional shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can use a remote MCP service for policy Q&A, risk checks, calculations, and knowledge-base listings; offline helpers provide limited local reference output.] <br>

## Skill Version(s): <br>
3.15.6 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

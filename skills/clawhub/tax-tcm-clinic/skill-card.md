## Description: <br>
Tax TCM Clinic helps users assess Chinese tax-compliance risks for TCM clinics and medical institutions, including VAT exemptions, separate accounting for taxable and exempt services, clinic filing, doctor individual income tax, Chinese herbal medicine invoicing, medical insurance settlement, cash revenue, and compliance self-check reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External clinic operators, finance teams, tax staff, and advisors use this skill to ask China-focused clinic tax questions, identify compliance risks, produce self-check guidance, and draft practical remediation or reporting materials. It is intended for informational compliance support and does not replace licensed tax, audit, medical, or legal advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Clinic and tax questions may be processed by the remote mcp.aitaxs.top service. <br>
Mitigation: Install only if remote processing is acceptable, and avoid entering patient-identifying, employee, bank, or highly confidential business details. <br>
Risk: The skill can use local files under ~/.tax-policy-client for client configuration, cache, health state, and logs. <br>
Mitigation: Review local data handling expectations before installation and periodically clear local cache or logs when they are no longer needed. <br>
Risk: Agent MCP configuration may be changed when config/init_agent.py is run directly or TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Review proposed MCP configuration changes before execution and keep auto-setup disabled unless the user intentionally wants configuration updates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-tcm-clinic) <br>
- [Publisher profile: zxj2devs](https://clawhub.ai/user/zxj2devs) <br>
- [TCM clinic compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_tcm_clinic.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with structured checklists, reports, code snippets, shell commands, and optional JSON-like tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route questions to a remote MCP service and may provide offline reference workflows when the remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
tax-steel helps metallurgy businesses assess Chinese tax compliance risks for steel, nonferrous, rare earth, and precious-metal operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, compliance, and operations teams use this skill to ask metallurgy-specific tax questions, run compliance self-checks, and draft risk findings or remediation guidance. It covers resource tax, recycled-material VAT incentives, precious-metal VAT treatment, transfer pricing, energy-cost tax topics, and trade-compliance red flags. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send tax questions and risk scenarios to a remote service. <br>
Mitigation: Avoid entering secrets, unnecessary identifiers, confidential pricing, audit details, or sensitive tax records unless the deployment has approved that data flow. <br>
Risk: Local logs or persisted identifiers/API keys may expose sensitive context. <br>
Mitigation: Review local storage and logging behavior before use in confidential environments, and rotate or remove stored credentials that are no longer needed. <br>
Risk: Setup code can modify local agent client configuration when explicitly enabled. <br>
Mitigation: Do not run config/init_agent.py or set TAX_ENABLE_AUTOSETUP unless configuration changes have been reviewed and approved. <br>
Risk: Tax guidance may be incomplete, outdated, or unsuitable for a specific filing position. <br>
Mitigation: Treat outputs as review support, verify policy citations against authoritative sources, and consult qualified tax professionals for filing, audit, dispute, or legal decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-steel) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Metallurgy compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_steel.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown or plain text with optional links, checklists, report outlines, and setup commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote tax-policy MCP service and may fall back to local workflow guidance when remote service access is unavailable.] <br>

## Skill Version(s): <br>
3.15.4 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

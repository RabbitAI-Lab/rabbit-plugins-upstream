## Description: <br>
A China social-insurance and tax compliance assistant for contribution basis checks, individual income tax alignment, flexible employment boundaries, risk grading, audit response, and remediation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and compliance professionals use this skill to assess China social-insurance contribution basis risks, compare payroll, tax, and social-insurance data, estimate gaps or late fees, and draft remediation checklists or reports. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive payroll, employee, tax, or compliance inputs may be routed to mcp.aitaxs.top services. <br>
Mitigation: Install only in approved environments where cloud routing of this data is permitted, and review data handling expectations before use. <br>
Risk: The artifact can persist local API keys, client IDs, and logs. <br>
Mitigation: Use managed workstations or profiles where local credential and log persistence is acceptable, and rotate or remove stored credentials when decommissioning the skill. <br>
Risk: The artifact can change MCP client configuration when automatic setup is enabled. <br>
Mitigation: Keep automatic setup disabled unless an administrator has reviewed the proposed MCP server entry and approved the configuration change. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-social-insurance) <br>
- [Social-insurance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_social_insurance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown and structured text with links, checklists, risk classifications, calculations, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call cloud MCP services or use offline workflow guidance depending on client configuration and service availability.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

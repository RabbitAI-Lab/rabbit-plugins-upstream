## Description: <br>
Helps agents provide tax audit and corporate tax compliance audit guidance across planning, internal controls, substantive procedures, fraud identification, disclosure, and reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, audit, and compliance practitioners use this skill to structure China-focused enterprise tax-audit self-checks, internal-control tests, fraud red-flag reviews, and tax-risk disclosure drafts. <br>

### Deployment Geography for Use: <br>
China-focused tax and audit contexts <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports remote service calls to mcp.aitaxs.top for tax-policy workflows. <br>
Mitigation: Review the remote-service behavior before installation and avoid entering privileged or highly sensitive audit details unless that service use is approved. <br>
Risk: The security evidence reports persistent local API-key, configuration, and log files. <br>
Mitigation: Store the skill only in trusted environments, protect local credentials and logs, and rotate keys if exposure is suspected. <br>
Risk: The security evidence notes optional local MCP client configuration changes. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP unless client configuration changes are intentional and reviewed. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/zxj2devs/skills/tax-tax-audit) <br>
- [Tax audit self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_tax_audit.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Related tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration, shell commands] <br>
**Output Format:** [Markdown or structured text with checklist, risk summary, and report-style sections.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce reference-oriented tax audit guidance and configuration instructions for MCP-backed workflows.] <br>

## Skill Version(s): <br>
3.15.10 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

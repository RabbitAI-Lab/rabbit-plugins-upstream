## Description: <br>
Provides education-sector tax compliance guidance for Chinese education and training providers, including VAT exemptions, simplified taxation, nonprofit qualification, tuition revenue recognition, teacher tax and social insurance, invoicing, risk self-checks, cases, and compliance reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators, finance teams, tax staff, and advisors for education and training organizations use this skill to ask tax compliance questions, perform scenario self-checks, identify filing and invoicing risks, and draft compliance action reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and scenarios may be sent to the provider's cloud MCP service. <br>
Mitigation: Avoid entering taxpayer identifiers, bank details, confidential business records, or other sensitive data unless the provider's data handling terms have been reviewed and accepted. <br>
Risk: The skill can create a local API key, device ID, and raw logs under ~/.tax-policy-client. <br>
Mitigation: Restrict local file access, periodically review or remove stored credentials and logs, and rotate credentials if the workstation is shared or compromised. <br>
Risk: Optional setup behavior can modify MCP client configuration. <br>
Mitigation: Leave TAX_ENABLE_AUTOSETUP disabled and do not run config/init_agent.py directly unless configuration changes are intended; review any generated backups and client config entries. <br>
Risk: Tax guidance can be time-sensitive and may not substitute for professional advice. <br>
Mitigation: Confirm material conclusions against official tax authority sources or qualified tax professionals before filing, paying, claiming exemptions, or responding to audits. <br>


## Reference(s): <br>
- [ClawHub tax-education skill page](https://clawhub.ai/zxj2devs/skills/tax-education) <br>
- [Education tax compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_education.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with structured checklists, links, calculations, and report-style guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may rely on remote MCP tools for current policy answers and should be reviewed against official tax sources before filing or making legal decisions.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

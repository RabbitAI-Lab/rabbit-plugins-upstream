## Description: <br>
Provides tax-compliance guidance, risk self-checks, and practical reporting support for traditional Chinese medicine clinics and other medical institutions, including VAT exemption, enterprise income tax, physician income tax, medical insurance invoicing, pharmacy sales, cash-revenue controls, and tax audit risk scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, clinic operators, finance staff, and compliance reviewers use this skill to ask scenario-specific tax questions, perform structured self-checks, and draft practical compliance guidance for TCM clinics, private hospitals, community medical services, pharmacy sales, insurance settlement invoicing, and physician income tax handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on mcp.aitaxs.top for cloud-backed answers and self-checks. <br>
Mitigation: Review the cloud data flow before use and avoid entering sensitive clinic, payroll, doctor-income, patient-adjacent, or tax dispute details unless that data flow is acceptable. <br>
Risk: The skill may store an API key and local logs under ~/.tax-policy-client. <br>
Mitigation: Check local retention expectations, protect the user profile directory, and remove stored credentials or logs when they are no longer needed. <br>
Risk: The package includes code that can modify MCP client configuration when explicitly enabled or run. <br>
Mitigation: Keep automatic setup disabled unless needed, review proposed MCP configuration changes, and back up client configuration before enabling writes. <br>
Risk: Tax guidance can be time-sensitive and fact-specific. <br>
Mitigation: Treat outputs as compliance support, verify conclusions against authoritative tax sources, and involve qualified professionals for filings, disputes, audits, or high-value decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-tcm-clinic) <br>
- [TCM clinic compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_tcm_clinic.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown guidance with structured checklists, links, and optional risk self-check results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud-backed answers, local offline fallback guidance, and client configuration suggestions.] <br>

## Skill Version(s): <br>
3.15.10 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

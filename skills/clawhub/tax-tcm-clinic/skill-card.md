## Description: <br>
Provides tax-compliance self-check guidance for TCM clinics and medical institutions, including VAT exemption boundaries, clinic filing, doctor income tax, medicine sales, medical insurance invoicing, and cash-revenue risk scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinic operators, finance teams, accountants, and compliance reviewers use this skill to ask Chinese tax-compliance questions, run structured self-checks, and produce practical remediation guidance for TCM clinics, private hospitals, and related medical institutions. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: User questions and self-check values may be sent to mcp.aitaxs.top or logged locally. <br>
Mitigation: Do not enter patient-identifying details or sensitive business records; use representative, minimized facts unless the deployment has approved the data flow. <br>
Risk: The skill can install related tax skills and may alter MCP client configuration. <br>
Mitigation: Use the matrix installer or automatic setup only when intentional, and review any skill-directory or MCP client configuration changes before relying on them. <br>
Risk: The security scan summarized the release as suspicious because remote services, credential storage, local logging, and configuration changes are not clearly scoped for all users. <br>
Mitigation: Review the security summary before installation in clinic, accounting, or compliance environments and restrict use to approved agents and workspaces. <br>
Risk: Generated tax guidance can be incomplete or unsuitable for a specific filing, audit, or legal dispute. <br>
Mitigation: Treat outputs as self-check support and confirm material tax positions with qualified tax or legal professionals and the relevant authorities. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/zxj2devs/skills/tax-tcm-clinic) <br>
- [TCM clinic compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_tcm_clinic.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown or plain text guidance with optional links, checklists, reports, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote tax-policy tools or use offline workflow guidance when remote services are unavailable.] <br>

## Skill Version(s): <br>
3.15.3 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

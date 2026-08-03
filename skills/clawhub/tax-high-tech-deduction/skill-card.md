## Description: <br>
A Chinese-language tax compliance assistant for high-tech enterprise qualification and R&D expense super-deduction workflows, including indicator checks, expense categorization, multi-basis reports, and audit-preparation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, compliance, and advisory users can use this skill to assess high-tech enterprise qualification, R&D expense super-deduction eligibility, evidence-chain readiness, and reporting differences across tax, accounting, and R&D statistics views. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports under-disclosed remote processing and warns that prompts or tool inputs may be sent to mcp.aitaxs.top. <br>
Mitigation: Avoid entering raw payroll, employee timekeeping, tax audit, or confidential R&D records unless approved, and redact sensitive identifiers before use. <br>
Risk: The security review reports local API credential and log persistence. <br>
Mitigation: Review local configuration and log locations after installation, limit credential scope, and remove stored credentials or logs that are no longer needed. <br>
Risk: The security review reports optional host configuration changes for MCP client setup. <br>
Mitigation: Review requested configuration changes before applying them and install only in environments where those changes are allowed. <br>
Risk: Tax guidance may be incomplete, outdated, or unsuitable for a specific taxpayer's facts. <br>
Mitigation: Have qualified tax or legal professionals review outputs before relying on them for filings, audits, or business decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-high-tech-deduction) <br>
- [High-tech tax workflow page](https://mcp.aitaxs.top/web/topic_workflow_high_tech.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional generated code, commands, configuration steps, reports, tables, and links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May provide tax compliance assessments, self-check summaries, remediation guidance, and workflow links; outputs should be reviewed by qualified tax or legal professionals before use.] <br>

## Skill Version(s): <br>
3.15.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

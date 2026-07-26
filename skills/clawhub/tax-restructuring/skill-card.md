## Description: <br>
企业重组资本运作涉税专业助手，覆盖破产重整、上市公司重组、企业分立、企业合并、债务重组、跨境重组等场景，并提供税务设计与风险预警。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, restructuring, and compliance users can use this skill to ask restructuring tax questions, run lightweight compliance self-checks, and receive practical risk guidance. It is intended as decision support and does not replace licensed tax, legal, filing, or government-facing work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax, restructuring, debt, or company identity information may be sent to cloud-backed services. <br>
Mitigation: Use sanitized or non-confidential inputs unless the service and data-handling terms have been approved for the environment. <br>
Risk: The skill may store local credentials or logs. <br>
Mitigation: Review local storage paths and retention behavior before use, and avoid installation on shared or unmanaged machines. <br>
Risk: Matrix installation and automatic MCP setup may add related packages or modify agent configuration. <br>
Mitigation: Disable or avoid automatic setup unless an administrator has approved the remote endpoints, package provenance, and configuration changes. <br>
Risk: Tax guidance may be incomplete or stale for a specific transaction, jurisdiction, or filing date. <br>
Mitigation: Treat outputs as decision support and verify material restructuring positions with qualified tax professionals or the relevant tax authority. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zxj2devs/skills/tax-restructuring) <br>
- [Tax Restructuring Self-Check Workflow](https://mcp.aitaxs.top/web/topic_workflow_restructuring.html) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown responses with tax guidance, risk checks, workflow links, and occasional setup instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route questions to external services and may suggest optional related skill installation.] <br>

## Skill Version(s): <br>
3.14.38 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

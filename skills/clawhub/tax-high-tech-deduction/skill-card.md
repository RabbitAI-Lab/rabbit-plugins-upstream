## Description: <br>
This skill helps users assess Chinese high-tech enterprise qualification and R&D expense super-deduction compliance, including indicator checks, expense allocation, self-check workflows, evidence-chain outputs, and audit-response guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance, tax, and compliance teams use this skill to evaluate Chinese high-tech enterprise qualification, R&D super-deduction eligibility, four-basis R&D reporting, and audit preparation. It supports structured self-checks, policy-grounded Q&A, calculation guidance, and report-oriented compliance outputs. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill is cloud-backed and may send tax scenarios or company facts to remote services. <br>
Mitigation: Avoid entering trade secrets, employee personal data, payroll details, audit-sensitive facts, or unreduced company identifiers unless the organization has approved the remote service. <br>
Risk: The client may persist credentials and logs locally. <br>
Mitigation: Review local credential and log storage before deployment, restrict filesystem access, and remove stored credentials or logs when they are no longer needed. <br>
Risk: Client configuration setup behavior can modify local MCP client configuration when enabled. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled unless automatic configuration is intentional, and review configuration changes before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-high-tech-deduction) <br>
- [High-tech enterprise and R&D compliance workflow](https://mcp.aitaxs.top/web/topic_workflow_high_tech.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with structured checklists, calculations, report drafts, code snippets, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use cloud-backed MCP tools for policy Q&A, risk checks, calculations, and knowledge-base metadata; offline scripts provide limited local reference workflows.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Tax Education helps education and training organizations assess Chinese tax compliance for VAT exemptions, tuition revenue recognition, teacher payroll taxes, invoicing, private-account payments, refund handling, and related self-check reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External education and training operators, finance teams, and tax advisors use this skill to ask tax-compliance questions, run education-industry self-checks, identify risk indicators, and draft practical remediation guidance. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Cloud-backed use may send tax, payroll, invoice, student, or business identity data to mcp.aitaxs.top. <br>
Mitigation: Review the data sent before use, avoid entering sensitive identity or business data unless approved, and use offline workflows when cloud transmission is not acceptable. <br>
Risk: Local API keys, client identifiers, caches, and logs may be stored on the user's machine or in browser localStorage. <br>
Mitigation: Inspect and protect local client storage according to organizational policy, and clear stored keys or logs when the skill is no longer needed. <br>
Risk: Optional automatic MCP setup can modify supported agent or client configuration files. <br>
Mitigation: Leave automatic setup disabled unless the user intentionally wants configuration changes, and review proposed config entries and backups before enabling it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zxj2devs/skills/tax-education) <br>
- [Publisher Profile](https://clawhub.ai/user/zxj2devs) <br>
- [Education Compliance Self-Check](https://mcp.aitaxs.top/web/topic_workflow_education.html) <br>
- [Tax Compliance Self-Check Portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown and structured text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include tax self-check findings, risk labels, policy-source notes, remediation steps, and MCP setup guidance.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

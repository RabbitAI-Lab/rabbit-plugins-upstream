## Description: <br>
国有企业经济责任审计涉税风险与合规专项助手，帮助识别虚开发票、账外账、国有资本收益、财政专项资金、重大涉税决策、境外资产税务、审计整改和三公经费隐形违规风险。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Audit, tax, finance, and compliance teams use this skill to structure state-owned enterprise economic responsibility audit questions, screen tax risk scenarios, prepare evidence checklists, and produce practical remediation guidance. It is most relevant to Chinese tax and state-owned enterprise audit workflows. <br>

### Deployment Geography for Use: <br>
Global, with subject-matter focus on Chinese tax and state-owned enterprise audit scenarios. <br>

## Known Risks and Mitigations: <br>
Risk: Audit questions and risk scenarios may be sent to a cloud-backed tax service. <br>
Mitigation: Do not enter confidential taxpayer, state-owned enterprise investigation, supplier, reimbursement, personnel, or other sensitive details unless the organization has approved the remote endpoint and data handling. <br>
Risk: The skill can create local plaintext credentials, client identifiers, and usage logs. <br>
Mitigation: Review local storage locations before use, restrict access on shared machines, and clear saved API keys or logs according to organizational policy. <br>
Risk: Optional setup and matrix installation behavior can modify MCP client configuration or install related skills. <br>
Mitigation: Treat setup and matrix installation as privileged actions; use dry-run or manual review first, and install only from trusted ClawHub or SkillHub download sources. <br>
Risk: Tax and audit guidance can be time-sensitive or incomplete for a specific matter. <br>
Mitigation: Verify conclusions against current official tax and audit authority guidance and obtain qualified professional review before relying on the output for filings, investigations, or final audit positions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-soe-audit) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [SOE audit tax self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_soe_audit.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge matrix](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown responses, JSON-compatible MCP tool results, web self-check reports, and plaintext CLI output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include risk levels, policy-source summaries, evidence checklists, remediation steps, copied report text, local fallback guidance, and setup or installer actions for related tax skills.] <br>

## Skill Version(s): <br>
3.15.3 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Tax Policy Knowledge 财税政策知识库与风险合规助手 provides Chinese tax-policy Q&A, common tax calculations, invoice and contract compliance review, risk self-checks, remediation guidance, and compliance report or template generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, finance teams, tax professionals, and developers use this skill to ask tax-policy questions, calculate common taxes, check invoice, contract, and transaction risks, and draft compliance reports, remediation checklists, and contract or consulting templates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and risk scenarios may be transmitted to the cloud-backed service at mcp.aitaxs.top. <br>
Mitigation: Avoid entering highly sensitive taxpayer, payroll, invoice, or client data unless the organization has approved that cloud service; minimize or anonymize scenario details where possible. <br>
Risk: The artifact may store a local API key and logs and probe local agent configuration. <br>
Mitigation: Review local storage, logging, and agent configuration behavior before deployment, and keep automatic setup disabled unless configuration changes are intended. <br>
Risk: The matrix installer can install related skills into ~/.skills when triggered. <br>
Mitigation: Run matrix installation only after reviewing the skill list and source channel, and avoid triggering bulk installation in restricted or unmanaged environments. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/zxj2devs/skills/tax-policy-knowledge) <br>
- [Tax topic workflow portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [National Taxation Administration](https://www.chinatax.gov.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown or plain text responses with structured checklists, reports, templates, and occasional code or configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a cloud-backed MCP service for tax-policy answers and risk checks, with local offline fallback guidance when the remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

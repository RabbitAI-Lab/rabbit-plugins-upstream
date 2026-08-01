## Description: <br>
医疗美容（医美）、黄金珠宝（贵金属/钻石）等生活服务业财税政策、收入确认、发票合规、私户收款与刷单风险、五流合一合规经营（业务/合同/票据/资金/财务交叉核对、税负率与成本费用率异常排查）、真实案例、报告模板与实操指引专题助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business operators, finance teams, and compliance reviewers use this skill to self-check tax compliance scenarios in medical beauty, gold jewelry, prepaid membership, private-account collection, invoicing, and related life-services operations. It provides policy-oriented guidance, risk triage, calculation prompts, self-check reports, and remediation checklists for review before action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The authoritative security review says the skill under-discloses remote data transmission and may process sensitive tax, invoice, revenue, customer, or business details through cloud services or fallback search providers. <br>
Mitigation: Avoid entering unnecessary personal, customer, invoice, bank, revenue, or confidential business data; use redacted or aggregated facts when possible and obtain approval before cloud processing. <br>
Risk: The authoritative security review identifies local prompt logs, persistent API keys, and persistent client identifiers as risks. <br>
Mitigation: Review and clear local tax-policy client data after sensitive sessions, avoid use on shared machines, and rotate or remove stored credentials when they are no longer needed. <br>
Risk: The authoritative security review identifies optional MCP configuration changes when setup is enabled. <br>
Mitigation: Keep setup in dry-run mode until the configuration change is reviewed, inspect generated MCP entries before enabling them, and preserve backups of existing client configuration. <br>
Risk: The artifact states that tax calculations, benefit judgments, and risk scores are only references and are not tax filing, audit, legal, or dispute-resolution opinions. <br>
Mitigation: Have qualified tax or legal professionals verify conclusions before filings, payments, refund claims, administrative disputes, litigation, or high-impact compliance decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-life-services) <br>
- [Life-services compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_life_services.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown and plain text responses, with optional structured risk summaries, calculation guidance, copied prompts, and generated self-check report text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are advisory and should be reviewed against official policy and professional tax advice before filing, payment, dispute handling, or other formal action.] <br>

## Skill Version(s): <br>
3.15.6 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
医疗美容（医美）、黄金珠宝（贵金属/钻石）等生活服务业财税政策、收入确认、发票合规、私户收款与刷单风险、五流合一合规经营（业务/合同/票据/资金/财务交叉核对、税负率与成本费用率异常排查）、真实案例、报告模板与实操指引专题助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, business operators, and tax compliance practitioners use this skill to self-check Chinese tax compliance issues for medical beauty and jewelry retail scenarios, including invoicing, revenue recognition, private-account collections, risk indicators, and remediation planning. Outputs are advisory and should be reviewed by qualified tax or legal professionals before filing, audit, or dispute use. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends tax questions, risk scenarios, and calculation inputs to external tax-service endpoints. <br>
Mitigation: Do not enter confidential tax, customer, or business data unless the user trusts the remote service and has authorization to share that data. <br>
Risk: The skill registers and stores local service credentials for API access. <br>
Mitigation: Review local credential storage before deployment, restrict file access, and rotate or remove credentials when the skill is no longer used. <br>
Risk: The skill can install related skills and can modify MCP or agent configuration when setup behavior is intentionally enabled. <br>
Mitigation: Run the matrix installer or initialization setup only when configuration changes are intended; review the target directory and configuration backup behavior first. <br>
Risk: The skill provides tax compliance guidance that may be incomplete or unsuitable for a specific filing, audit, or dispute. <br>
Mitigation: Treat outputs as advisory self-check material and obtain qualified professional review before taking legal, tax filing, or audit-response action. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zxj2devs/skills/tax-life-services) <br>
- [Publisher Profile](https://clawhub.ai/user/zxj2devs) <br>
- [Life Services Self-Check Workflow](https://mcp.aitaxs.top/web/topic_workflow_life_services.html) <br>
- [Tax Compliance Self-Check Portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text responses, with optional JSON tool results, configuration snippets, shell commands, and downloadable self-check reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include links to a web self-check workflow, policy prompts, risk summaries, remediation checklists, and installer or MCP configuration guidance.] <br>

## Skill Version(s): <br>
3.15.3 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

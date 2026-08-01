## Description: <br>
宠物连锁行业（供应链、商贸、美容、医疗、寄养、行为训练全链路）财税政策知识、风险指标、案例、报告模板与实操指引专题助手，覆盖动物诊疗免税、宠物食品与饲料税率、美容寄养生活服务、加盟费无形资产、兼营分别核算、活体买卖与私户隐匿收入风险等合规要点。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business operators, finance and tax staff, and advisors use this skill to ask China-focused pet-chain tax compliance questions, run lightweight risk self-checks, and draft remediation checklists or self-inspection reports. It is intended for preliminary compliance guidance and should be verified against current rules and professional advice for filing, audit, dispute, or high-impact decisions. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill may send business, tax, revenue, audit, or scenario details to remote services during policy questions, risk checks, tax calculations, or web self-check flows. <br>
Mitigation: Review the data flow before use, submit only the minimum necessary scenario or indicator values, and avoid confidential details unless that remote processing is acceptable. <br>
Risk: The skill can persist local identifiers, API keys, logs, and browser localStorage credentials. <br>
Mitigation: Protect the local user profile, inspect or clear ~/.tax-policy-client and browser localStorage when rotating credentials or uninstalling, and avoid shared-machine use for sensitive matters. <br>
Risk: Optional automatic setup can change MCP client configuration. <br>
Mitigation: Leave automatic setup disabled unless reviewed, inspect the target client configuration before enabling it, and keep backups of MCP configuration files. <br>
Risk: Public search fallback and generated tax guidance may be incomplete, stale, or unsuitable for filing, audit, dispute, or legal decisions. <br>
Mitigation: Treat fallback and generated guidance as preliminary, verify current policy sources, and consult a qualified tax or legal professional before acting on high-impact conclusions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-pet-chain) <br>
- [Interactive pet-chain compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_pet_chain.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [SkillHub tax-pet-chain page](https://skillhub.cn/skills/tax-pet-chain) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown-style natural language answers with structured checklists, risk findings, remediation steps, report text, and MCP configuration guidance when applicable] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include policy references, risk levels, indicator results, suggested follow-up questions, copied prompts for deeper analysis, and offline fallback guidance.] <br>

## Skill Version(s): <br>
3.15.6 (source: frontmatter, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

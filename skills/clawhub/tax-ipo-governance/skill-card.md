## Description: <br>
拟上市企业上市前三年财税规范与内部控制建设框架专项助手，覆盖上市前三年倒排时间轴、股份制改造净资产折股涉税、内部控制建设、高发内控缺陷整改、关联交易清理、新收入准则收入确认与会计基础。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
拟IPO企业实控人、CFO、财务负责人，以及券商、会计师、税务师等外部服务人员，可用该技能梳理上市前三年财税规范路径、股改涉税事项、内控建设、常见缺陷整改、关联交易清理和收入确认风险。输出应作为初步合规辅助材料，并由具备资质的税务、审计或法律专业人员复核。 <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses cloud services and may send IPO, tax, internal-control, and business-scenario details to mcp.aitaxs.top. <br>
Mitigation: Confirm organizational approval before use, avoid submitting unnecessary sensitive data, and review outputs with qualified tax, audit, or legal professionals. <br>
Risk: Fallback behavior may use public search engines for policy lookup when the primary service is unavailable. <br>
Mitigation: Treat fallback results as preliminary and verify policy citations against authoritative sources before acting. <br>
Risk: The client can persist API keys, local logs, cache data, and a random anonymous identifier under ~/.tax-policy-client. <br>
Mitigation: Inspect and manage that directory during testing, and remove persisted credentials or logs according to local data-handling policy. <br>
Risk: Optional autosetup can modify MCP client configuration files when explicitly enabled. <br>
Mitigation: Leave autosetup in dry-run mode unless configuration edits are intended, and review generated MCP entries before enabling them in production. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-ipo-governance) <br>
- [IPO governance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_ipo_governance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Related skill: tax-policy-knowledge](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Related skill: tax-ipo-tax](https://skillhub.cn/skills/tax-ipo-tax) <br>
- [Related skill: tax-esop-platform](https://skillhub.cn/skills/tax-esop-platform) <br>
- [Related skill: tax-listed-advisory](https://skillhub.cn/skills/tax-listed-advisory) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown guidance, structured checklists, risk summaries, compliance-report text, JSON-style tool results, and optional MCP configuration instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route to cloud MCP services, an interactive web self-check page, or offline fallback scripts depending on agent configuration and network availability.] <br>

## Skill Version(s): <br>
3.15.10 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

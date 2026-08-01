## Description: <br>
拟上市企业上市前三年财税规范与内部控制建设框架专项助手，覆盖倒排时间轴、股改涉税、内控建设、高发缺陷整改、关联交易清理、收入确认与合规报告场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
拟IPO企业实控人、CFO、财务负责人及外部券商、会计师、税务师使用该技能梳理上市前三年财税规范、股改涉税、内部控制建设、关联交易清理和收入跨期风险，并生成自查、整改与合规报告思路。 <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may transmit user questions or scenario details to mcp.aitaxs.top for cloud MCP processing. <br>
Mitigation: Review and approve cloud processing before use, and avoid submitting confidential pre-IPO, shareholder, payroll, revenue, or internal-control data unless that processing is acceptable. <br>
Risk: The skill may store local API-key material and logs. <br>
Mitigation: Install only in environments where local credential persistence and local logging are permitted, and review local storage handling before production use. <br>
Risk: Enabling automatic setup can modify local agent MCP configuration files. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled unless configuration changes are intentional; review proposed MCP settings before enabling automatic setup. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-ipo-governance) <br>
- [上市前规范与内控自检页面](https://mcp.aitaxs.top/web/topic_workflow_ipo_governance.html) <br>
- [财税合规自检门户](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or structured text with optional JSON-style tool results, Python workflow output, and MCP configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use cloud MCP tools for policy Q&A, risk checks, calculations, and knowledge-base listings; includes offline fallback guidance when cloud access is unavailable.] <br>

## Skill Version(s): <br>
3.15.6 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

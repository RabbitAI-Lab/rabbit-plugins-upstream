## Description: <br>
数据资源（数据资产）入表税务专项助手，帮助用户围绕税会差异、数据资产估值、数据产品交易涉税、研发加计、权属合规和上市问询开展合规自检与风险防控。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
财税、合规、上市审核和企业数据资产管理人员可用该技能梳理数据资源入表、税会差异、交易涉税、研发支出归集、估值监测和问询应对流程。它适合生成结构化自检清单、风险提示、政策核验路径和整改方案草案，最终判断仍需结合最新主管机关口径和专业复核。 <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax, financial, listing, or client data may be sent to remote tax-service endpoints or public-search fallback paths. <br>
Mitigation: Use only authorized and minimized data, avoid confidential details unless the environment is approved for remote processing, and verify conclusions against official policy sources or qualified advisers. <br>
Risk: The skill stores local credentials, cache data, health state, and logs. <br>
Mitigation: Review the local data directory before use, restrict file permissions, avoid logging secrets, and rotate or remove API keys and logs when access is no longer needed. <br>
Risk: Optional MCP setup can modify local agent or client configuration. <br>
Mitigation: Review proposed configuration changes and backups before enabling writes, use least-privilege credentials, and keep a rollback copy of existing client settings. <br>
Risk: The matrix installer can fetch and install additional related skills from remote package URLs. <br>
Mitigation: Install only from trusted ClawHub or SkillHub sources, review the matrix entries before installation, and scan each installed skill before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-data-asset) <br>
- [Data asset tax compliance web workflow](https://mcp.aitaxs.top/web/topic_workflow_data_asset.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured checklists, risk summaries, links, and optional code or command snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include web self-check links, offline workflow output, MCP configuration guidance, and related skill installation guidance.] <br>

## Skill Version(s): <br>
3.14.38 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
元典法条与案例检索。本技能应在需要查询中国法律法规条文、检索相关案例、为法律分析提供数据支撑时使用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cat-xierluo](https://clawhub.ai/user/cat-xierluo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Legal researchers, lawyers, and agents use this skill to retrieve Chinese statutes, regulations, cases, and enterprise background data from Yuandian, then preserve results for legal analysis and review. It supports legal search planning, API-backed retrieval, hallucination checks for cited legal material, and consolidated legal research reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Legal queries, text, case identifiers, and enterprise identifiers may be sent to Yuandian. <br>
Mitigation: Confirm the user is comfortable sharing the matter data with Yuandian before API-backed retrieval. <br>
Risk: Full legal or business search results are stored locally by default. <br>
Mitigation: Use report suppression flags where appropriate and periodically clean archive/ when it may contain confidential matter data. <br>
Risk: The release asks users to run Codex with broad runtime authority for some network scenarios. <br>
Mitigation: Prefer isolated workspaces and balanced or economical modes for routine work; avoid unrestricted permissions unless the environment and data are appropriate. <br>
Risk: Raw and aggressive modes can increase data exposure and API spend. <br>
Mitigation: Use balanced or economical mode for normal work, and reserve aggressive mode for explicitly approved high-coverage searches. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cat-xierluo/skills/yuandian-law-search) <br>
- [Publisher profile](https://clawhub.ai/user/cat-xierluo) <br>
- [Source homepage](https://github.com/cat-xierluo/legal-skills) <br>
- [Yuandian Open Platform](https://open.chineselaw.com) <br>
- [关键词扩展与分阶段检索](references/01-keyword-expansion.md) <br>
- [典型工作流与用户引导](references/02-typical-workflows.md) <br>
- [法律检索报告与目标目录归档](references/03-report-consolidation.md) <br>
- [法律检索报告 7 节设计原理](references/04-report-design-notes.md) <br>
- [MCP 协同工作流](references/05-mcp-workflow.md) <br>
- [企业全息画像](references/06-enterprise-portrait.md) <br>
- [检索机制感知型中间层执行合同](references/07-research-middleware.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, terminal guidance, shell commands, and archived API result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call paid Yuandian APIs and archive retrieved legal, case, and enterprise results locally.] <br>

## Skill Version(s): <br>
1.8.6 (source: frontmatter, changelog, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

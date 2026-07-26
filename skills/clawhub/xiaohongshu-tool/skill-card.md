## Description: <br>
小红书运营数据工具，用于关键词搜索、笔记详情和评论查询、博主作品监控、爆款挖掘、竞品分析、KOL筛选和趋势洞察。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[um-why](https://clawhub.ai/user/um-why) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External content creators, brand marketers, market analysts, MCN teams, and operators use this skill to query public Xiaohongshu data, compare competing accounts, identify high-engagement notes, screen KOLs, and prepare content or marketing analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Xiaohongshu keywords, note links, profile links, and the required GUAIKEI_API_TOKEN to the Guaikei third-party API. <br>
Mitigation: Use a dedicated token, avoid sensitive Xiaohongshu inputs on shared systems, and install only if the third-party API use is acceptable for the deployment. <br>
Risk: Query results are saved locally as JSON files in the logs directory. <br>
Mitigation: Manage file permissions and delete generated logs when they are no longer needed. <br>
Risk: The tool is documented for public Xiaohongshu data and internal personal or team use only. <br>
Mitigation: Do not use it for private or hidden content, and review outputs before redistribution or business use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/um-why/skills/xiaohongshu-tool) <br>
- [Publisher profile](https://clawhub.ai/user/um-why) <br>
- [Skill options](references/options.md) <br>
- [Skill changelog](references/changelog.md) <br>
- [Guaikei API token and support site](https://www.guaikei.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Analysis, Files, Configuration] <br>
**Output Format:** [JSON or Markdown command output, with JSON result files saved under logs/] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command options control keyword, URL, content type, sort order, time range, result limit, and output format.] <br>

## Skill Version(s): <br>
1.0.6 (source: SKILL.md frontmatter, package.json, evidence release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

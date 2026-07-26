## Description: <br>
基于FastMCP框架开发的专业文献搜索工具，支持多源文献搜索、文献详情获取、参考文献管理、文献关系分析、期刊质量评估和批量结果导出等功能，适用于学术研究和AI助手集成。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, researchers, and AI assistants use this skill to search scholarly literature, retrieve article full text by PMCID, collect references, analyze citation relationships, and evaluate journal quality through XiaoBenYang's API service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends literature queries and the XBY_APIKEY to XiaoBenYang's API service. <br>
Mitigation: Use the skill only when that data sharing is acceptable for the intended workflow. <br>
Risk: The skill can store the API key in a local .env file. <br>
Mitigation: Treat the .env file as sensitive, keep it out of version control and shared folders, and rotate the key if exposure is suspected. <br>
Risk: Some artifact documentation appears to contain stray gaokao or search_schools references unrelated to the literature-search tools. <br>
Mitigation: Prefer the declared literature tool functions and review generated actions before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/xby-article) <br>
- [XiaoBenYang API service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Configuration Guidance] <br>
**Output Format:** [Markdown or structured JSON summaries derived from API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY and may persist it in a local .env file.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence; artifact frontmatter is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

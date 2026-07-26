## Description: <br>
用于抖音数据分析、抖音热榜、抖音作品搜索、图文搜索、关键词检索、内容调研、竞品分析和趋势研究。覆盖 Douyin hot search and work search，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External analysts, marketers, researchers, and developers use this skill to fetch Douyin hot-search and keyword-search data for content research, competitor analysis, and trend scanning. It helps agents summarize visible ranking signals and search results while preserving traceable IDs, URLs, authors, counts, and publish times when useful. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Douyin search terms and requests are sent to SocialDataX under the user's API key. <br>
Mitigation: Use this skill only when the user is comfortable sharing those search terms with SocialDataX, and keep SOCIALDATAX_API_KEY in the runtime environment rather than embedding it in skill files. <br>
Risk: Using socialdatax-skills@latest can change CLI behavior or supply-chain exposure over time. <br>
Mitigation: Pin or review the npm package version before installation in stricter environments. <br>
Risk: Search results are bounded by pagination and filters and may not represent complete Douyin platform coverage. <br>
Mitigation: State query bounds in summaries and preserve returned IDs, URLs, counts, publish times, content types, and next-page markers when traceability matters. <br>


## Reference(s): <br>
- [SocialDataX AI API access](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown summaries with inline shell commands and JSON result excerpts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY at runtime and may include Douyin content IDs, URLs, titles, authors, metrics, publish times, content type, and pagination markers.] <br>

## Skill Version(s): <br>
0.1.15 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

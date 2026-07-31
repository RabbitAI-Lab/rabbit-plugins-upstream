## Description: <br>
轻量级联网搜索工具，支持 Bing 与 DuckDuckGo 双引擎自动路由，中文环境优化，适合个人日常信息检索。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, personal developers, students, and researchers use this skill to run lightweight web searches, retrieve Chinese-optimized search results, and optionally fetch limited page text for everyday information lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries, public IP-detection requests, and optional page fetching are external network requests that can expose sensitive terms or visited targets. <br>
Mitigation: Do not use secrets, private internal URLs, tokens, or confidential research terms as queries, and keep full-text fetching disabled unless visiting target pages is intended. <br>
Risk: Fetched page content may be incomplete, truncated, or unavailable when sites use heavy JavaScript, non-HTML content, rate limits, or blocking. <br>
Mitigation: Treat fetched text as convenience context, verify important claims against the original sources, and reduce full-text fetching when failures occur. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/free-web-search-tool-free) <br>
- [Artifact SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with search-result summaries, links, command examples, and optional fetched page excerpts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single-query search output; up to 10 results per query and optional full-text fetching for up to 5 results with page text truncation.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

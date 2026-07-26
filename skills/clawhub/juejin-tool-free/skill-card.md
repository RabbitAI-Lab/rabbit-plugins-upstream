## Description: <br>
掘金工具 helps agents query Juejin hot article rankings, download Juejin articles as Markdown, and create Markdown-based Juejin drafts with login-cookie handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill for personal Juejin workflows: browsing hot articles, saving selected articles as Markdown, and preparing draft posts without public publishing by default. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security summary reports unrelated database triggers and vague CRUD-style authority that could activate the skill outside its stated Juejin purpose. <br>
Mitigation: Use the skill only for explicit Juejin tasks and reject database, SQL, or unrelated storage requests. <br>
Risk: Juejin login stores a local cookie file and draft publishing uses the user's account session. <br>
Mitigation: Avoid logging in on shared or CI environments, keep cookie access restricted, and remove the cookie when finished. <br>
Risk: Draft creation can affect a real Juejin account session. <br>
Mitigation: Keep draft-only behavior as the default and require explicit confirmation before any public publishing action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/juejin-tool-free) <br>
- [Juejin category briefs API](https://api.juejin.cn/tag_api/v1/query_category_briefs) <br>
- [Juejin category recommendation feed API](https://api.juejin.cn/recommend_api/v1/article/recommend_cate_feed) <br>
- [Juejin all recommendation feed API](https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown responses with JSON-like status data and saved Markdown files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create files under ./output/ and use a local Juejin cookie for authenticated draft creation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

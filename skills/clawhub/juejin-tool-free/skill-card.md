## Description: <br>
Juejin Tool helps individual users browse Juejin rankings and categories, download Juejin articles as Markdown, and create Markdown-based Juejin drafts with browser login support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External individual users and developers use this skill to work with the Juejin technical community: reading hot article feeds, saving Juejin articles locally as Markdown, and preparing Markdown content as Juejin drafts. Logged-in write actions should be treated as account-affecting operations and kept to explicit Juejin requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Activation wording is broad and contradictory, including database, SQL, storage, and generic CRUD language outside the stated Juejin use case. <br>
Mitigation: Before installation, narrow triggers to explicit Juejin requests and remove unrelated database, SQL, storage, and generic CRUD instructions. <br>
Risk: Browser login can create and retain a local Juejin session cookie. <br>
Mitigation: Avoid use on shared or CI systems, keep cookie permissions restricted, and remove the session cookie after the task is complete. <br>
Risk: Draft creation and optional public publishing can affect the user's Juejin account content. <br>
Mitigation: Keep draft-only behavior as the default and require explicit double confirmation before any public publish action. <br>
Risk: Article download behavior writes files to the local filesystem. <br>
Mitigation: Restrict downloads to the documented ./output directory and require explicit Juejin URLs or author identifiers before writing files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/juejin-tool-free) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Juejin category API](https://api.juejin.cn/tag_api/v1/query_category_briefs) <br>
- [Juejin category recommendation API](https://api.juejin.cn/recommend_api/v1/article/recommend_cate_feed) <br>
- [Juejin all-feed recommendation API](https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API examples and JSON-style status responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write downloaded articles to ./output and use a local Juejin session cookie when browser login is required.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

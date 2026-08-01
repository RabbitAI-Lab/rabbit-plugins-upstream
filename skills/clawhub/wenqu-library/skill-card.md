## Description: <br>
文曲·文库 helps agents plan, search, download, index, and maintain reusable source libraries for Chinese content writing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, technical writers, and agents use this skill to collect similar articles and factual source material before drafting Chinese articles, reports, tutorials, project introductions, or explanatory documents. It supports a four-step workflow for planning, searching, downloading, and organizing reusable source libraries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can search the web, download pages, and store collected material under both project directories and $HOME/.gogoingai/wenqu-skills/library/. <br>
Mitigation: Confirm the collection scope before use, keep source URLs in the material index, and remove content that should not be retained. <br>
Risk: Optional CLI and browser installation can add search and crawling tools to the user's environment. <br>
Mitigation: Approve optional installation only when enhanced collection is needed; otherwise use the built-in search and download fallback paths. <br>
Risk: Logged-in or restricted content could be captured if the user intentionally authorizes that source. <br>
Mitigation: Prefer public sources and record access limitations when restricted material is intentionally handled. <br>


## Reference(s): <br>
- [文曲·文库 source homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-library) <br>
- [素材收集执行手册](references/collection-playbook.md) <br>
- [open-websearch：搜索补充模块](references/open-websearch/README.md) <br>
- [open-websearch CLI 与结果协议](references/open-websearch/cli.md) <br>
- [open-websearch 引擎选择](references/open-websearch/engines.md) <br>
- [open-websearch 安装、验证与降级](references/open-websearch/setup.md) <br>
- [Crawl4AI / crwl：浏览器检索恢复与下载增强模块](references/crawl4ai/README.md) <br>
- [crwl CLI、配置与使用边界](references/crawl4ai/cli.md) <br>
- [crwl 浏览器检索恢复](references/crawl4ai/search-recovery.md) <br>
- [crwl 站点食谱与失败分流](references/crawl4ai/site-recipes.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown plans, source indexes, captured material files, and optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write project material indexes and captured source files, and may update a user-level reusable source library.] <br>

## Skill Version(s): <br>
0.1.15 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

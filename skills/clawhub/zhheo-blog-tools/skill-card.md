## Description: <br>
通过 HTTP API 访问张洪Heo博客，支持全文搜索、热门文章、归档浏览、标签分类、页面发现、友链查询和读文摘要。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhheo](https://clawhub.ai/user/zhheo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to answer questions about 张洪Heo's blog by searching posts, browsing archives, listing popular posts, resolving tags and categories, checking friend links, and fetching article content through public HTTP endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generic trigger words may activate the skill in unrelated blog conversations. <br>
Mitigation: Use narrower trigger matching or confirm the user is asking about 张洪Heo's blog before calling its APIs. <br>
Risk: The hot-post endpoint returns 403 when the required Referer header is missing. <br>
Mitigation: Send Referer: https://blog.zhheo.com/ for /api/umami/hot.php requests and report access failures clearly. <br>
Risk: Article links can be wrong if an agent invents slugs instead of using API results. <br>
Mitigation: Use the original path or url returned by the blog APIs rather than constructing article URLs manually. <br>


## Reference(s): <br>
- [张洪Heo Blog](https://blog.zhheo.com) <br>
- [ClawHub skill page](https://clawhub.ai/zhheo/skills/zhheo-blog-tools) <br>
- [Search API example](https://blog.zhheo.com/api/search/search.php?q=OpenClaw&limit=5) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown guidance with HTTP endpoint examples, JSON response examples, and curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No credentials or local file access; hot-post requests require a Referer header; long article extracts should be truncated with a note.] <br>

## Skill Version(s): <br>
1.2.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

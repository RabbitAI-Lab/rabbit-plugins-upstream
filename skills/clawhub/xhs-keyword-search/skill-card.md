## Description:

xhs关键词搜索｜按关键词检索小红书公开笔记，支持图文/视频类型筛选、综合/最新/点赞/评论/收藏五种排序、一天/一周/半年/全部四档时间范围，一次最多返回1万条结果，包含笔记标题、作者、互动数据与跳转链接

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content creators, marketers, and analysts use this skill to retrieve public Xiaohongshu notes, note details, comments, and creator post lists for trend research, competitor monitoring, and follow-on reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords, Xiaohongshu links, public comments, profile or note URLs, and xsec_token query parameters may be sent to the Guaikei API and saved in local logs.

Mitigation: Use the skill only when that data sharing is acceptable, protect the GUAIKEI_API_TOKEN, and periodically review or delete the logs directory.

Risk: The skill is limited to public Xiaohongshu data and may return empty or unavailable results when a link is private, hidden, malformed, or otherwise unsupported.

Mitigation: Confirm the input is a public Xiaohongshu keyword, note URL, or creator profile URL before running the related CLI script.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-keyword-search)
- [Guaikei API service](https://www.guaikei.com)
- [Options and invocation reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON results from the called CLI scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI saves returned Xiaohongshu research results under a local logs directory.]

## Skill Version(s):

1.0.0 (source: server release metadata, artifact metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

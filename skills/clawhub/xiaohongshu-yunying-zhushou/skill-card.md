## Description:

查询小红书公开笔记与博主数据，支持关键词搜索、笔记详情、评论和作品分析，服务于选题、竞品监控、KOL筛选与舆情分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

小红书创作者、运营团队和品牌分析人员可用它检索公开笔记、查看博主作品与互动数据、分析笔记详情和评论，为选题研究、竞品跟踪、KOL筛选及舆情分析提供数据。查询需要 GUAIKEI_API_TOKEN，关键词和链接会发送到 Guaikei 服务。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious because its tool scope is undeclared and 13 of 42 components were only partly inspected, leaving evidence incomplete.

Mitigation: Review the skill's behavior and tool scope before installing, and weigh the privacy concerns as advised by the security review.

Risk: Queries require sending search keywords or Xiaohongshu links to the Guaikei service, along with the API token.

Mitigation: Use only public, non-sensitive queries and links, and consider the third-party data handling before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/xiaohongshu-yunying-zhushou)
- [Guaikei service and API access](https://www.guaikei.com)
- [小红书 search, detail, comment, and creator options](references/options.md)
- [JSON output contract](references/contract.md)
- [Error handling guidance](references/errors.md)

## Skill Output:

**Output Type(s):** [JSON data, Analysis]

**Output Format:** [Structured JSON results with concise natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One search, detail, comment, or creator query per command; result counts depend on the selected request and service plan.]

## Skill Version(s):

1.2.2 (source: frontmatter, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

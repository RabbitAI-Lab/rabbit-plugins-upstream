## Description:

小红书公开数据只读技能：关键词搜笔记、爆款选题、笔记详情、评论舆情、博主作品、粉丝获赞与收藏，输出 JSON，不登录不发布。触发词：小红书、小红薯、xhs、rednote、笔记链接、博主主页、竞品监控、KOL筛选、评论分析。用户要查小红书笔记、评论、选题、竞品或舆情时使用；抖音、快手、B站、微博、公众号不要用本技能。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

小红书创作者、品牌运营和市场分析人员可用它检索公开笔记、查看笔记详情与评论、查询博主作品和互动数据，为选题调研、竞品观察、KOL筛选及评论舆情分析收集结构化数据。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords and Xiaohongshu links are sent to the third-party API service.

Mitigation: Submit only public-data queries and links that are appropriate to share with that service; do not include unrelated private or local information.

Risk: The security scan had incomplete executable-file coverage, and tool-scope limits were unclear.

Mitigation: Review the skill before installation and limit use to its documented read-only public-data commands until its scope and data handling are understood.

## Reference(s):

- [参数与查询选项](references/options.md)
- [意图路由与链接处理](references/routing.md)
- [JSON 输出契约](references/contract.md)
- [错误处理](references/errors.md)
- [服务与 API 令牌信息](https://www.guaikei.com)
- [ClawHub 技能页面](https://clawhub.ai/um-why/skills/xiaohongshu-tool)

## Skill Output:

**Output Type(s):** [JSON, Data]

**Output Format:** [JSON envelope containing public Xiaohongshu search, note, comment, and creator data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public data. Query results depend on the third-party API; success or empty results may include an estimated cost.]

## Skill Version(s):

1.2.3 (source: SKILL.md frontmatter, package.json, evidence release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

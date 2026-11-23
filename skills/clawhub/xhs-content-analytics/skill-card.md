## Description:

小红书公开数据只读技能：关键词搜笔记、爆款选题、笔记详情、评论舆情、博主作品、粉丝获赞与收藏，输出 JSON，不登录不发布。触发词：小红书、小红薯、xhs、rednote、笔记链接、博主主页、竞品监控、KOL筛选、评论分析。用户要查小红书笔记、评论、选题、竞品或舆情时使用；抖音、快手、B站、微博、公众号不要用本技能。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

Creators, marketers, and analysts use this skill to retrieve public Xiaohongshu notes, comments, and creator metrics for topic research, competitor monitoring, influencer screening, and audience analysis. It returns structured data for an agent to summarize or compare.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords and note or profile links are sent to a third-party API.

Mitigation: Use only public content and avoid submitting sensitive keywords or links; account for this data sharing before use.

Risk: The security review reports medium confidence and partial component analysis, so some executable files were not fully inspected.

Mitigation: Review and scan the skill before installation, paying particular attention to components not covered by the existing analysis.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/um-why/skills/xhs-content-analytics)
- [GuaiKei API access](https://www.guaikei.com)
- [Output contract](references/contract.md)
- [Command options](references/options.md)
- [Intent routing](references/routing.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON response envelope with command-line usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns public note, comment, creator, and engagement data; success, empty, and error results share a documented envelope.]

## Skill Version(s):

1.2.3 (source: SKILL.md frontmatter, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

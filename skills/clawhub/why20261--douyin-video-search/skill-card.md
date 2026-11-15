## Description:

按关键词检索抖音视频和图文，并查询热榜、博主公开作品、作品详情及评论互动数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

内容创作者、运营人员和分析团队可用它发现热门内容与趋势、跟踪公开账号作品，并查看作品互动和评论，以支持选题、竞品观察、舆情与需求分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan has medium confidence and partial coverage; it could not fully interpret 18 of 42 components, including several command files.

Mitigation: Review the source before installation and treat the benign verdict as limited evidence, not a guarantee.

Risk: User-provided search terms and Douyin links are sent to the third-party API at guaikei.com.

Mitigation: Use public, non-sensitive inputs and confirm that sending them to the service is permitted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/douyin-video-search)
- [GuaiKei API and token support](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Demand-mining guide](references/demand-mining.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured JSON data, with concise text or Markdown summaries when analysis is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search and creator-post requests return up to 10,000 items with usage-based tokens; monthly plans allow up to 30 search or post items and 50 comments.]

## Skill Version(s):

1.4.2 (source: release evidence, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

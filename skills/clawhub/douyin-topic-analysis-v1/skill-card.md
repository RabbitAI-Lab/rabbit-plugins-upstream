## Description:

抖音选题分析帮助内容运营人员、品牌调研者和创作者检索抖音公开内容、追踪热榜，并分析博主作品与视频评论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

内容运营人员、品牌调研者和创作者可用此技能搜索抖音视频与图文、查看实时热榜、整理博主公开作品，并分析视频评论，以支持选题策划、竞品观察和舆情追踪。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and Douyin links are sent to the third-party GuaiKei service.

Mitigation: Use only inputs you are authorized to share, and review the provider's data-handling and pricing terms before use.

Risk: The API token and locally saved result files could be exposed if mishandled.

Mitigation: Keep GUAIKEI_API_TOKEN private, restrict access to saved results, and delete files from logs/ when they are no longer needed.

## Reference(s):

- [ClawHub release](https://clawhub.ai/why20261/skills/douyin-topic-analysis-v1)
- [GuaiKei data service](https://www.guaikei.com)
- [Options reference](references/options.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands]

**Output Format:** [Structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are also saved under logs/ for review; formatted timestamps use Beijing time.]

## Skill Version(s):

1.4.0 (source: SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

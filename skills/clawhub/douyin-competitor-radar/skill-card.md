## Description:

帮助品牌和创作者分析抖音公开内容、热榜、作者作品与视频评论，比较竞品表现并识别内容机会。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

品牌团队、营销人员和内容创作者可检索抖音公开内容、热榜、作者作品与评论，形成竞品对比、趋势判断和选题建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, profile or video links, limits, and the API token are sent to a third-party service.

Mitigation: Use only approved public-data queries and a scoped API token; confirm that sharing these inputs with the service is acceptable.

Risk: Search, post, and comment results are saved as full JSON in local logs, potentially exposing sensitive research data.

Mitigation: Avoid shared or synced folders and restrict access to, and retention of, locally saved results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/douyin-competitor-radar)
- [Usage options](references/options.md)
- [Release changelog](references/changelog.md)
- [Data API and usage help](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON data, Analysis, Guidance]

**Output Format:** [Structured JSON results with optional text summary and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes public content, engagement metrics, source links, and comments where available.]

## Skill Version(s):

1.3.0 (source: server release, frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

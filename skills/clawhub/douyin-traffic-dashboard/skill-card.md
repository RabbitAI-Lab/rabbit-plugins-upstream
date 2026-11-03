## Description:

用于查看抖音平台整体流量和热点在各内容分类间的分布。当用户问“抖音流量现在集中在哪些赛道”、“抖音各类内容流量占比”、“哪些内容分类更热门”、“抖音平台流量大盘/分类热度排行”，或需要做平台级赛道观察时使用。返回分类名称、热点数量、热度占比和更新时间，帮助进行内容方向与赛道布局的初步判断。本技能提供平台整体分类数据；不分析单个账号的流量、单条视频表现或粉丝画像，不用于查询具体热搜词、追踪单个话题或直接生成内容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[allinherog-star](https://clawhub.ai/user/allinherog-star)

### License/Terms of Use:

MIT-0

## Use Case:

内容创作者、运营人员、电商和营销从业者可用此技能查看抖音平台各内容分类的热点数量与热度占比，为赛道观察、内容方向初筛和运营复盘提供参考。结果反映平台分类层面的整体数据，不代表某个账号或视频的表现。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The configured API endpoint receives the API key and request parameters.

Mitigation: Keep the default HTTPS endpoint unless a replacement is trusted, and protect the API key.

Risk: The remote data service was not audited, and its pricing and privacy terms may affect use.

Mitigation: Review the provider's pricing and privacy terms before use; this skill needs only empty parameters, so do not provide private account data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/allinherog-star/skills/douyin-traffic-dashboard)
- [AI Skills service](https://ai-skills.ai)
- [Quick start instructions](https://github.com/allinherog-star/ai-skills/tree/main#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [JSON category data with names, hot-topic counts, percentages, and update time; may be summarized as concise text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Platform-level category distribution for Douyin; does not provide account or video analytics, specific hot-search terms, or generated content.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

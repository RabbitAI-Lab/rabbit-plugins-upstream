## Description:

当用户需要做社媒创作者研究、小红书博主画像、抖音达人画像、快手达人画像、账号资料、近期内容复盘、合作对象初筛或对标账号观察时使用。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users doing creator research can use this skill to find and review public creator profiles and recent content on Xiaohongshu, Douyin, and Kuaishou. It supports collaboration shortlists, account comparisons, and content reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and account details supplied to the service are shared with SocialDataX.

Mitigation: Remove unrelated private text from queries and submit only the information needed for creator research.

Risk: The read-only workflow does not sandbox downloaded package code, and the CLI uses an API key.

Mitigation: Use a reviewed, fixed helper version where possible and protect SOCIALDATAX_API_KEY.

Risk: Paginated queries can consume credits.

Mitigation: Set page limits to control usage costs.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Markdown creator research summaries based on structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include candidate accounts, profile details, recent content, timestamps, and engagement signals.]

## Skill Version(s):

1.0.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

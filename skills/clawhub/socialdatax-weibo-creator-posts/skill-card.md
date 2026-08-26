## Description:

用于微博创作者数据、微博创作者内容列表、近期发布、内容调研和创作者内容分析。覆盖 Weibo creator posts，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and summarize Weibo creator post lists through SocialDataX for recent publishing review, content research, creator benchmarking, and account tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses SOCIALDATAX_API_KEY at runtime to access SocialDataX data.

Mitigation: Use an API key limited to this service and avoid embedding credentials in generated skill files or shared outputs.

Risk: The direct CLI path runs an npm package through npx.

Mitigation: Verify the npm package source and version you are comfortable running before deployment.

Risk: Fetching many pages for large Weibo accounts can increase API usage and cost.

Mitigation: Use --pages or --max-items to bound collection unless full pagination is intentional.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-creator-posts)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY at runtime and returns read-only Weibo creator post data, including pagination metadata when available.]

## Skill Version(s):

0.1.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

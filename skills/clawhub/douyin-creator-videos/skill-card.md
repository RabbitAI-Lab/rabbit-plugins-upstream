## Description:

用于抖音达人数据、达人作品、KOL作品列表、博主作品列表、近期发布、内容调研和创作者内容分析，支持关键词搜索、实时热榜查询、公开博主作品抓取和视频评论分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, marketers, content operators, and analysts use this skill to retrieve public Douyin search results, trending topics, creator posts, and comment data for content research, competitor monitoring, social listening, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fetched social-media datasets are saved locally as plaintext JSON without retention controls.

Mitigation: Treat saved files as exported datasets, delete them when no longer needed, and avoid collecting or redistributing personal data without proper authorization.

Risk: The skill sends requests to the third-party guaikei.com API using GUAIKEI_API_TOKEN.

Mitigation: Review third-party API use in shared or sensitive workspaces, keep the token in environment variables, and confirm the data transfer is authorized.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-creator-videos)
- [Server-resolved source repository](https://github.com/why20261/douyin-creator-videos)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [Guaikei API service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [JSON responses from Node.js CLI tools, with brief guidance when required inputs or credentials are missing.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful search, creator-post, and comment results are also saved locally as plaintext JSON logs.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact package metadata reports 1.0.0 and changelog top entry reports 1.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

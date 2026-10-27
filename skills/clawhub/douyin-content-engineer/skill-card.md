## Description:

帮助用户搜索抖音内容、抓取博主作品与评论、查看实时热榜，并分析内容趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营人员、创作者及市场分析人员可用此技能检索抖音公开视频、查看博主作品和评论、跟踪热榜，并开展选题、竞品与舆情分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and target links are sent to www.guaikei.com using its service token.

Mitigation: Only submit queries and links approved for this provider, and protect the service token.

Risk: Provider charges may apply, and larger collection limits can increase usage.

Mitigation: Check provider charges and use the smallest collection limit that meets the task.

Risk: Full results and original inputs remain in local logs until deleted; logging cannot be disabled.

Mitigation: Treat logs as sensitive, restrict access to the logs/ directory, and delete retained data when no longer needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/why20261/skills/douyin-content-engineer)
- [Command options](artifact/references/options.md)
- [Release changelog](artifact/references/changelog.md)
- [Guaikei service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [Structured JSON envelope containing status, request metadata, and command-specific Douyin results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results vary by search, creator posts, comments, or hot list; records include available author, engagement, tags, and links.]

## Skill Version(s):

1.4.0 (source: server-resolved release and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

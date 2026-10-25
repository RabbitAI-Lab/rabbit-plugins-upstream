## Description:

该技能帮助代理检索小红书公开笔记、查看详情和评论、获取博主作品及互动数据，并以 JSON 返回结果，不登录或发布内容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT-0

## Use Case:

小红书创作者与运营团队、品牌市场人员及 MCN/KOL 经纪人可查询公开笔记、评论和博主数据，用于选题研究、竞品监控、KOL 筛选和评论舆情分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and supplied links are sent to Guaikei, and results may be retained in temporary files.

Mitigation: Keep the paid API token private, use appropriate query limits, and set XHS_GUAIKEI_DISABLE_LOG=1 to disable temporary-file logging.

## Reference(s):

- [Guaikei public-data API service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [JSON response envelope containing request details, metadata, and search results, note details, comments, or public creator metrics.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public data; results depend on the external service and the selected query limits.]

## Skill Version(s):

1.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

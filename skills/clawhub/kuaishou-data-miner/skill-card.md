## Description:

快手公开数据只读技能：关键词搜视频、博主作品与粉丝数据、视频评论，输出 JSON，不登录不发布。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

快手内容创作者、品牌营销人员和分析师可用它查询公开视频、博主作品与评论，支持内容选题、竞品观察、KOL 筛选和评论舆情分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and Kuaishou links or identifiers are sent to the third-party GuaiKei service; its retention practices and live responses were not verified.

Mitigation: Only submit terms and links you are comfortable sharing with that service.

Risk: The API token grants access to the third-party service and may be exposed if mishandled.

Mitigation: Keep GUAIKEI_API_TOKEN private and configure it through the environment rather than including it in prompts or output.

Risk: Optional logging saves local copies of query inputs and results, and large requests may exceed plan limits.

Mitigation: Leave logging disabled unless local copies are needed, and check plan limits before requesting large result sets.

## Reference(s):

- [ClawHub release](https://clawhub.ai/um-why/skills/kuaishou-data-miner)
- [GuaiKei API provider](https://www.guaikei.com)
- [Command options](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [JSON result envelopes containing video search results, creator posts and profile metrics, or video comments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public Kuaishou data retrieved through GuaiKei; requires an API token. Monthly plan limits apply, and optional local logging can save query results.]

## Skill Version(s):

1.1.1 (source: frontmatter, changelog; released 2026-11-04)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

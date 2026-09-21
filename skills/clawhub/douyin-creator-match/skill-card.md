## Description:

按关键词、点赞、类目和市场筛选抖音带货达人，结合达人互动数据、作品表现数据和带货效果给出合作优先级，找到真正和品类、受众及目标匹配的抖音达人候选。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, marketing analysts, and short-video operators use this skill to query public Douyin search, creator posts, comments, and hot-list data for creator matching, content research, competitive monitoring, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-provided Douyin keywords or links and the GUAIKEI_API_TOKEN to www.guaikei.com.

Mitigation: Use the skill only when that third-party API disclosure is acceptable, provide only intended public Douyin identifiers, and manage the token as a credential.

Risk: Fetched creator, comment, and content data can be retained in the skill's local logs directory.

Mitigation: Treat outputs and logs as retained social-media data, avoid unnecessary sharing, follow platform terms and privacy obligations, and delete logs when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-creator-match)
- [Publisher profile](https://clawhub.ai/user/why20261)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [GUAIKEI API token and help](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON envelopes and concise Markdown guidance with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; search, post, and comment commands can request up to 10000 public records.]

## Skill Version(s):

1.3.0 (source: frontmatter, package.json, changelog released 2026-09-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

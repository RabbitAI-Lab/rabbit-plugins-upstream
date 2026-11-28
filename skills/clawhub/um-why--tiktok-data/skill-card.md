## Description:

TikTok 公开数据只读技能：关键词搜视频、博主作品、视频评论，输出 JSON，不登录不发布。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketing teams, and agent developers use this skill to retrieve public TikTok search results, creator posts, and video comments for content research, competitor monitoring, KOL discovery, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The benign security verdict has medium confidence because only 22 of 35 components were fully inspected.

Mitigation: Review the skill and its behavior before installation, and use it only in an environment where its external API access is appropriate.

Risk: Queries are sent to the Guaikei service and require a GUAIKEI_API_TOKEN.

Mitigation: Use a token issued for this service and keep it in the environment rather than sharing it in prompts or command output.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/um-why/skills/tiktok-data)
- [Publisher profile](https://clawhub.ai/user/um-why)
- [Guaikei service and token setup](https://www.guaikei.com)
- [Options reference](references/options.md)
- [FAQ](references/faq.md)
- [Output contract](references/contract.md)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [Structured JSON envelope containing TikTok search results, creator posts, or video comments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful results are returned as arrays; empty or error responses use the documented JSON envelope.]

## Skill Version(s):

1.1.4 (source: SKILL.md frontmatter, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

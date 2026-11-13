## Description:

小红书公开数据只读技能：关键词搜笔记、爆款选题、笔记详情、评论舆情、博主作品、粉丝获赞与收藏，输出 JSON，不登录不发布。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

Content creators, brand teams, and analysts use it to research publicly visible Xiaohongshu notes, creator activity, engagement, and comment sentiment for topic selection, competitor tracking, KOL screening, and public-opinion analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and Xiaohongshu links are sent to the third-party Guaikei API to retrieve public data.

Mitigation: Use only queries and links appropriate to share with that service, and avoid including private or sensitive information.

Risk: The security review has medium confidence and partial component coverage.

Mitigation: Review the skill files before deployment and limit use to the documented read-only public-data functions.

## Reference(s):

- [Skill instructions and command routing](SKILL.md)
- [Options and query limits](references/options.md)
- [Output contract](references/contract.md)
- [Error codes and retry guidance](references/errors.md)
- [Guaikei API access](https://www.guaikei.com)
- [Project support](https://github.com/um-why/xiaohongshu-openclaw-skill/issues)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [Structured JSON results for searches, note details, comments, or creator profiles and posts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public content; available fields and result counts depend on the query and API access.]

## Skill Version(s):

1.2.2 (source: frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

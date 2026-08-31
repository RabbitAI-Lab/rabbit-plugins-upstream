## Description:

小红书公开数据检索工具，覆盖关键词搜笔记、笔记详情、评论、博主作品、博主粉丝量等互动数据；当用户提到小红书并需要查/分析公开内容时调用，可用于爆款选题、竞品监控、KOL 筛选、评论舆情分析，无需登录账号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

External content creators, brand marketers, market analysts, and operators use this skill to collect structured public Xiaohongshu notes, comments, creator posts, and interaction metrics for topic research, competitor monitoring, KOL screening, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, note URLs, and profile URLs to the third-party guaikei.com API.

Mitigation: Use the skill only when that data transfer is acceptable for the user's task and authorization scope.

Risk: A third-party GUAIKEI_API_TOKEN is required and may grant access to a paid or rate-limited data service.

Mitigation: Store the token in the environment, avoid sharing it in prompts or logs, and rotate or revoke it if exposed.

Risk: Fetched public comments and profile metrics may still be sensitive when collected in bulk.

Mitigation: Limit collection to the minimum needed, avoid unlawful profiling or redistribution, and apply internal privacy review for sensitive analyses.

Risk: Successful command runs may write JSON result logs to the system temporary directory.

Mitigation: Periodically clear local temporary logs, especially on shared machines or after handling sensitive research topics.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/um-why/skills/xiaohongshu-tool)
- [Project homepage](https://github.com/um-why/xiaohongshu-openclaw-skill)
- [Guaikei API token and support portal](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Node.js shell commands and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return status, error_code, request metadata, skill metadata, and public Xiaohongshu result records; successful runs may also write local JSON logs under the system temporary directory.]

## Skill Version(s):

1.1.3 (source: frontmatter, package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

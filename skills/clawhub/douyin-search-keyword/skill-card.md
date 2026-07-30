## Description: <br>
抖音公开数据智能获取工具。支持抖音关键词搜索、抖人作品抓取、获取作品评论、实时热榜跟踪，适用于短视频营销、竞品分析、舆情分析和热点监控，助力爆款内容策划与流量追踪。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[um-why](https://clawhub.ai/user/um-why) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and content-analysis teams use this skill to search public Douyin videos, inspect creator posts, retrieve comments, and monitor hot lists for marketing, competitor analysis, sentiment review, and trend tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can collect public Douyin user, video, and comment data at scale. <br>
Mitigation: Use it only for lawful, platform-compliant analysis and avoid collecting more data than needed for the task. <br>
Risk: Search, post, and comment outputs are saved locally by default and may contain user comments, identifiers, or sensitive topics. <br>
Mitigation: Store logs in protected locations, delete them when no longer needed, and avoid running the skill in synced, shared, CI, or regulated-data workspaces without review. <br>
Risk: The configured GUAIKEI_API_TOKEN is sent to guaikei.com for API requests. <br>
Mitigation: Keep the token out of shared environments, rotate it if exposed, and review installation before use on shared machines. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/um-why/skills/douyin-search-keyword) <br>
- [Guaikei token and support site](https://www.guaikei.com) <br>
- [Options reference](references/options.md) <br>
- [Changelog](references/changelog.md) <br>
- [Search request schema](assets/search_cli_req.schema.json) <br>
- [Search response schema](assets/search_cli_resp.schema.json) <br>
- [Post response schema](assets/post_cli_resp.schema.json) <br>
- [Comment response schema](assets/comment_cli_resp.schema.json) <br>
- [Hot list response schema](assets/hot_cli_resp.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, JSON, files, configuration, guidance] <br>
**Output Format:** [CLI commands with JSON stdout and JSON log files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; search, post, and comment commands save JSON logs locally by default.] <br>

## Skill Version(s): <br>
1.1.6 (source: server release evidence, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

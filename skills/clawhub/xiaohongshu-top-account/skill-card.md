## Description: <br>
小红书账号榜单追踪分析工具，支持查询日榜周榜月榜TOP50排名和热门账号 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuanyi-github](https://clawhub.ai/user/yuanyi-github) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketers, MCN operators, Xiaohongshu creators, and content researchers use this skill to query daily, weekly, or monthly top-account rankings by category, inspect growth metrics, export HTML reports, and optionally set up recurring ranking updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user queries and API key-authenticated requests to the RedFox API. <br>
Mitigation: Install only if you trust RedFoxHub with your REDFOX_API_KEY and queries; keep the key scoped, revocable, and out of code, prompts, logs, and shared outputs. <br>
Risk: The skill writes HTML ranking reports into the workspace. <br>
Mitigation: Review generated report files before sharing or opening them in sensitive contexts, and keep workspace permissions limited to intended users. <br>
Risk: Optional subscription behavior may create recurring ranking delivery automation or calendar entries. <br>
Mitigation: Create recurring delivery only after explicit user confirmation, and review the schedule, prompt, and cancellation path. <br>
Risk: Ranking data can be delayed, unavailable for some categories, or limited by the documented lookback windows. <br>
Mitigation: Show the data date and update window, use documented fallback behavior, and tell users when a requested category or date range has no available data. <br>


## Reference(s): <br>
- [Xiaohongshu Top Account Skill on ClawHub](https://clawhub.ai/yuanyi-github/skills/xiaohongshu-top-account) <br>
- [API documentation](references/api_docs.md) <br>
- [Score rules](references/score_rules.md) <br>
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown ranking tables, generated HTML report files, and optional JSON from helper scripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Live API calls require REDFOX_API_KEY; generated HTML reports are written to the workspace.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

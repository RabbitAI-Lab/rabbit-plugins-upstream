## Description: <br>
小红书账号榜单追踪分析工具，支持查询日榜、周榜、月榜 TOP50 排名和热门账号。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
品牌、MCN 运营者、小红书创作者和内容研究者可用此 skill 查询小红书日榜、周榜、月榜账号排名，按赛道筛选热门账号，生成 HTML 报告，并按需订阅定期推送。 <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a RedFox API key and sends ranking requests to RedFox APIs. <br>
Mitigation: Use a dedicated API key where possible, confirm its scope and revocation path, and avoid exposing it in prompts, logs, output files, or source files. <br>
Risk: Report generation can create local HTML files. <br>
Mitigation: Review generated report files before sharing them and store them only in locations appropriate for the account ranking data they contain. <br>
Risk: Subscription behavior is under-specified and could create persistent scheduled tasks. <br>
Mitigation: Confirm the exact cadence before creating a subscription and document how to review, pause, or delete the resulting automation or calendar entry. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/xiaohongshu-rank-tracker) <br>
- [API docs](references/api_docs.md) <br>
- [Score rules](references/score_rules.md) <br>
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown tables and status text, with optional HTML report files and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY and may contact RedFox ranking APIs; report generation can create local HTML files.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

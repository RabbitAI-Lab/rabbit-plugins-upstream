## Description: <br>
一款通过自然语言交互追踪每日卡路里摄入量的 MCP 服务器，提供餐食记录、每日总结、周报生成和食物搜索功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to log meals, search food calorie information, and generate daily or weekly calorie summaries through the XiaoBenYang MCP API after configuring an API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends meal and calorie-tracking data plus an API key to an external XiaoBenYang service. <br>
Mitigation: Install only if the user trusts the XiaoBenYang API provider and is comfortable sharing this data; treat the API key as sensitive. <br>
Risk: The API key is persisted in a plaintext .env file, which can expose credentials in shared workspaces. <br>
Mitigation: Avoid shared workspaces for this skill and keep the .env file out of logs, prompts, and source control. <br>
Risk: Server security evidence reports mismatched Gaokao and school-search remnants in a calorie-tracking release. <br>
Mitigation: Review the skill before deployment and ask the publisher to remove stale remnants, document backend data handling, sanitize upstream responses, and lock dependencies. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/xby-ccxt) <br>
- [XiaoBenYang API key page](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown summaries of JSON API responses with API-key configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY value; upstream responses are returned as raw JSON for the agent to summarize.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

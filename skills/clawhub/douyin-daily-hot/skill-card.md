## Description: <br>
抖音每日最热作品榜查询工具。日度收录全平台抖音作品，输出单日点赞TOP50榜单，支持按赛道分类查询、历史日期回溯（最多30天）、个性化订阅推送。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operations teams, creators, brands, MCNs, and data analysts use this skill to retrieve Douyin daily likes rankings, filter by category, review up to 30 days of history, and receive Markdown tables with clickable work links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires REDFOX_API_KEY and sends ranking queries to a fixed RedFox endpoint. <br>
Mitigation: Confirm you trust RedFox with the API key and query contents before installation or use. <br>
Risk: Subscription claims are documented by the skill but may depend on host support outside the skill files. <br>
Mitigation: Treat subscription behavior as documentation unless the host provides a separate subscription mechanism. <br>
Risk: Broad or ambiguous prompts could trigger the Douyin ranking workflow unexpectedly. <br>
Mitigation: Use explicit Douyin-ranking prompts and review outputs before relying on them for content or business decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/redfox-data/skills/douyin-daily-hot) <br>
- [API Configuration](references/api-config.md) <br>
- [Interaction Guide](references/interaction-guide.md) <br>
- [RedFox API Key Settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, API Calls, Guidance] <br>
**Output Format:** [Markdown tables with clickable links, concise status messages, and optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defaults to TOP20 results; can produce up to TOP50 results and includes category/date context.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

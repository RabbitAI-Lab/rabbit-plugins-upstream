## Description: <br>
Searches WeChat Official Account hot articles by keyword and returns ranked popular article results, recommendations, and trend context for content ideation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuanyi-github](https://clawhub.ai/user/yuanyi-github) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content creators, WeChat operators, brand teams, and self-media teams use this skill to search recent high-read WeChat articles, compare topic trends, and gather content inspiration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports a credential-like API key exposure. <br>
Mitigation: Rotate or remove the exposed key before deployment and require users to provide REDFOX_API_KEY through their environment instead of plaintext files, prompts, logs, or generated output. <br>
Risk: Search terms are sent to redfox.hk for article lookup. <br>
Mitigation: Use the skill only when users trust RedFoxHub with the submitted keywords and understand that queries leave the local agent environment. <br>
Risk: The subscription flow can create recurring scheduled tasks from searches. <br>
Mitigation: Enable subscription/calendar behavior only after explicit user confirmation of the keyword, schedule, and desired recurrence. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yuanyi-github/skills/wechat-search-redfox) <br>
- [gzh_trend_data_format.md](references/gzh_trend_data_format.md) <br>
- [RedFoxHub API Key Settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFox WeChat Hot Article API](https://redfox.hk/story/api/gzh/search/hotArticle) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown tables and guidance based on JSON API results, with optional HTML report files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY and may create scheduled subscription reminders when enabled by the user.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

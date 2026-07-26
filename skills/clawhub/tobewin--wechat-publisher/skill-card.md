## Description: <br>
A WeChat official-account publishing skill that helps agents prepare, upload, publish, inspect, and manage articles, media, statistics, and comments through the WeChat public API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobewin](https://clawhub.ai/user/tobewin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operators and developers use this skill to automate WeChat official-account article workflows, including draft creation, media upload, publishing, published-article lookup, statistics retrieval, and comment management. It is intended for accounts with valid WeChat publishing API access and configured WECHAT_APP_ID and WECHAT_APP_SECRET credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Article content, media files, account identifiers, and API credentials may be sent to WeChat API servers during normal publishing workflows. <br>
Mitigation: Use the skill only with content approved for WeChat publication, avoid sensitive or confidential material in automated runs, and keep WECHAT_APP_ID and WECHAT_APP_SECRET in the environment rather than in prompts or files. <br>
Risk: Publish and delete operations for drafts, published articles, materials, comments, and replies can be irreversible. <br>
Mitigation: Review generated commands and payloads before execution and require the documented --confirm flag for high-impact publish or delete actions. <br>
Risk: Misconfigured accounts or accounts without current WeChat publishing API permissions may fail or produce incomplete workflows. <br>
Mitigation: Run the connection test and confirm the account's WeChat API permissions before relying on the workflow for production publishing. <br>


## Reference(s): <br>
- [WeChat Publisher on ClawHub](https://clawhub.ai/tobewin/skills/wechat-publisher) <br>
- [WeChat Official Account API Documentation](https://developers.weixin.qq.com/doc/subscription/api/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON payload examples, and generated HTML for WeChat articles] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require outbound HTTPS requests to api.weixin.qq.com and datacube endpoints when commands are executed.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata, SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
查询智慧芽（PatSnap）专利家族信息，帮助用户按单个专利 ID 或公开号查看 Simple Family、INPADOC Family 和 PatSnap Family 成员。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve factual patent family and equivalent-patent data for a known single patent. It supports comparison of Simple Family, INPADOC Family, and PatSnap Family membership without providing legal opinions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent research data may be sensitive and full API responses are saved locally. <br>
Mitigation: Review the local output path before use and avoid running the skill in workspaces where saved patent data should not persist. <br>
Risk: The configured LinkFox gateway receives patent lookup requests and API credentials. <br>
Mitigation: Confirm the configured gateway is trusted and use the documented LinkFox API key environment variables. <br>
Risk: The skill can automatically submit feedback containing user intent and result-quality details to a separate feedback service. <br>
Mitigation: Review feedback submission behavior before installation and avoid automatic feedback submission when that information should not leave the workspace. <br>
Risk: The API consumes credits and each request supports only one patent. <br>
Mitigation: Confirm user consent before additional lookups, especially when checking multiple patents. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-patent-family) <br>
- [智慧芽专利家族查询 API 参考](references/api.md) <br>
- [LinkFox API Key Guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Markdown, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with JSON responses and saved JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts one patentId or patentNumber per request; full responses are saved locally and large responses are summarized.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

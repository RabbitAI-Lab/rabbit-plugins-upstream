## Description: <br>
用于小红书博主数据、小红书博主笔记、账号内容列表、近期发布、内容调研和创作者内容分析。覆盖 Xiaohongshu / XHS / RedNote creator notes，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and content analysts use this skill to retrieve Xiaohongshu / XHS / RedNote creator note lists for recent publishing review, content research, creator benchmarking, and account tracking. It supports direct CLI and MCP-tool workflows using a SocialDataX API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Network calls may consume SocialDataX credits when the agent retrieves creator note data. <br>
Mitigation: Use bounded options such as --max-items or --since-days for large accounts, and avoid repeated retries after insufficient-balance errors. <br>
Risk: The skill requires SOCIALDATAX_API_KEY at runtime. <br>
Mitigation: Keep the API key in the environment, use only the official SocialDataX AI access page for key management, and do not embed keys in generated files. <br>
Risk: Changing an opaque pagination token can corrupt or redirect a paginated retrieval chain. <br>
Mitigation: Pass returned next_page_token values back unchanged for the same creator note-list request. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-creator-notes) <br>
- [SocialDataX AI Access Page](https://socialdatax.com/ai?from=clawhub) <br>
- [Publisher Profile](https://clawhub.ai/user/devinchen2014) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only SocialDataX requests return creator note-list data, including platform, tool, arguments, data items, counts, and pagination tokens when available.] <br>

## Skill Version(s): <br>
0.1.15 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

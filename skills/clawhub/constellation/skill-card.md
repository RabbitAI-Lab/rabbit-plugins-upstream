## Description: <br>
一个功能完整的星座 MCP (Model Context Protocol) 服务，提供星座信息查询、运势分析、配对测试等功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to query zodiac information, daily horoscopes, compatibility analysis, zodiac lookup by birth date, and rising-sign calculations through the Xiaobenyang API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores the Xiaobenyang API key in a local .env file. <br>
Mitigation: Use only an API key that is acceptable for local plaintext storage, avoid running the skill in directories with unrelated secrets in .env, and rotate the key if it is exposed. <br>
Risk: Rising-sign calculations can send birth time and location coordinates to the external Xiaobenyang API. <br>
Mitigation: Provide exact birth time or coordinates only when the user accepts sharing that data with the third-party API. <br>
Risk: Server security evidence notes confusing copied Gaokao service identifiers. <br>
Mitigation: Review the tool and API mapping before deployment and verify that the configured MCP identifiers match the intended constellation service. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/constellation) <br>
- [Publisher profile](https://clawhub.ai/user/alinklab) <br>
- [Xiaobenyang API key provider](https://xiaobenyang.com) <br>
- [Xiaobenyang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Text, Markdown, Configuration] <br>
**Output Format:** [Markdown summaries of JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Xiaobenyang API key and may persist it in a local .env file.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

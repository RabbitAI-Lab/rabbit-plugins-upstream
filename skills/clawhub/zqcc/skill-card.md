## Description: <br>
企查查中转站 Skill。用于通过 zqcc 统一中转的企查查 MCP 和 Chat API 查询企业工商、股东、联系方式、风险、知识产权、经营、董监高和历史记录，也用于注册 zqcc AppKey 或配置企查查中转站 MCP。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shijingyu](https://clawhub.ai/user/shijingyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query Chinese company registry, shareholder, contact, risk, intellectual property, operating, executive, and historical records through the zqcc MCP endpoint or Chat API. It also helps configure the required AppKey and MCP client settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends business queries and the ZQCC_APP_KEY credential to a remote zqcc service. <br>
Mitigation: Install only when that remote service is intended, keep the AppKey out of chats, logs, screenshots, and repositories, and send it only to trusted zqcc endpoints. <br>
Risk: The skill can retrieve sensitive company, contact, legal, tax, executive, and risk records. <br>
Mitigation: Query and share only the data needed for the task, and confirm there is a legitimate basis before handling personal or sensitive business records. <br>
Risk: Changing ZQCC_BASE_URL can redirect authenticated requests away from the default service. <br>
Mitigation: Do not override ZQCC_BASE_URL unless the user controls and trusts the replacement endpoint. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/shijingyu/skills/zqcc) <br>
- [企查查中转站 Homepage](https://zqcc.mkstone.club) <br>
- [API Reference](references/api.md) <br>
- [Tool Catalog](references/tools.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration, and remote API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for authenticated MCP and Chat API calls; tool-call responses may include structured JSON inside text content.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

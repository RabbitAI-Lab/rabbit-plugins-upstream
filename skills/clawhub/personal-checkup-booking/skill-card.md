## Description:

好啦体检（haola-pe）个人体检预约与体检方案推荐。用户说帮我安排个体检、体检项目怎么选、体检多少钱、几百块能查什么、入职体检要做什么项目、附近哪有体检中心、体检报告在哪看、要改期或取消时使用。可按年龄、性别、婚否与健康关注点生成个性化体检方案，覆盖全国 240+ 城市，支持在线预约、改期、取消与报告查询。后端为好啦体检 MCP 服务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[ryanbihai](https://clawhub.ai/user/ryanbihai)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals use the skill to find checkup information and locations, request a personalized checkup plan, and manage their own or a family member’s appointment and report through Haola’s service.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The local login token is stored in ~/.haola/token.json, and restrictive file permissions are not enforced.

Mitigation: Keep the token file private and log out on shared machines.

Risk: Health information is sent to Haola when requesting personalized services, and the remote service’s data handling was not verified.

Mitigation: Explain the recipient and information being submitted, obtain the user’s consent, and submit only the information needed for the requested task.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/ryanbihai/skills/personal-checkup-booking)
- [Haola MCP service endpoint](https://ai.ihaola.com.cn/api/mcp/haola-pe)
- [Project homepage listed in release metadata](https://github.com/Beijing-Haola-Tech/haola-checkup-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, API Calls, Shell commands, Configuration instructions]

**Output Format:** [Conversational text and structured tool-call arguments; Markdown with inline shell examples when setup guidance is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on connected service results for specific plans, prices, locations, bookings, and reports.]

## Skill Version(s):

1.1.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

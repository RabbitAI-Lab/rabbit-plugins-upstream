## Description:

好啦体检（haola-pe）个人体检定制与预约。用户说帮我安排个体检、体检项目怎么选、体检多少钱、几百块能查什么、入职体检要做什么项目、附近哪有体检中心、体检报告在哪看、要改期或取消时使用。可按年龄、性别、婚否与健康关注点生成个性化体检方案，覆盖全国 240+ 城市，支持在线预约、改期、取消与报告查询。后端为好啦体检 MCP 服务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[haola](https://clawhub.ai/user/haola)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals use this skill to get a service-backed checkup plan based on their circumstances and budget, find clinics, and book or manage appointments and reports.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Health and identity information is sent to Haola, and login credentials remain on the local device until expiry or logout. The Windows PowerShell fallback may not keep sensitive requests within the declared service origin.

Mitigation: Prefer the Python client, protect the local credentials file, and log out on shared computers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haola/skills/personal-checkup-booking)
- [Project homepage listed in Clawdis metadata](https://github.com/Beijing-Haola-Tech/haola-checkup-mcp)
- [Haola checkup MCP service](https://ai.ihaola.com.cn/api/mcp/haola-pe)

## Skill Output:

**Output Type(s):** [Text, Guidance, API Calls]

**Output Format:** [Natural-language responses based on checkup service results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Specific plans, prices, clinics, and appointment availability are based on service results.]

## Skill Version(s):

1.1.11 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

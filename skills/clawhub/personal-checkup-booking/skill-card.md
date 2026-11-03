## Description:

帮助个人按健康关注点和预算了解体检方案，并查询门店、预约、改期、取消和报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[haola](https://clawhub.ai/user/haola)

### License/Terms of Use:

MIT-0

## Use Case:

个人用户可借助该 skill 了解体检方案和门店信息，并办理个人或家属的预约、改期、取消及报告查询。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill uses health and booking information; the assessment does not verify Haola's server-side privacy practices.

Mitigation: Use it only if you intend to share relevant health and booking details with Haola.

Risk: A booking request may commit the user to a proposed appointment and price.

Mitigation: Review the proposed appointment and price before requesting the booking.

Risk: Login credentials remain saved locally until removed.

Mitigation: Use the logout command to remove saved credentials when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haola/skills/personal-checkup-booking)
- [Haola MCP service](https://ai.ihaola.com.cn/api/mcp/haola-pe)
- [Project homepage](https://github.com/Beijing-Haola-Tech/haola-checkup-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Appointment and booking information]

**Output Format:** [Conversational Chinese text based on service results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Specific checkup details, prices, and availability require a successful service response.]

## Skill Version(s):

1.1.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

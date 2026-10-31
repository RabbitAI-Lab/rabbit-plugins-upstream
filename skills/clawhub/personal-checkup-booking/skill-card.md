## Description:

Helps users choose personal health checkup plans, find centers, and manage bookings, changes, cancellations, and report inquiries through the Haola service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ryanbihai](https://clawhub.ai/user/ryanbihai)

### License/Terms of Use:

MIT

## Use Case:

External users can ask for personalized checkup guidance, center availability, booking assistance, or help with existing appointments and reports. Personal plans and account actions require authenticated access; the included fallback supports anonymous lookups only.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Personal checkup plans, bookings, and reports involve sensitive health and personal information and require authenticated service access.

Mitigation: Keep passwords and login codes on the official website, share only necessary health information, and use authenticated access for personal actions.

Risk: The remote service's data practices have not been verified.

Mitigation: Submit only information needed for the requested service and verify the final package and price before payment.

Risk: The security guidance identifies a broken quotation example in the fallback client.

Mitigation: Do not rely on the fallback quotation example; confirm any quotation through a supported service flow before presenting it as a result.

## Reference(s):

- [Haola checkup MCP service](https://ai.ihaola.com.cn/api/mcp/haola-pe)
- [Haola personal checkup account portal](https://pe.ihaola.com.cn/auth/)
- [ClawHub skill release](https://clawhub.ai/ryanbihai/skills/personal-checkup-booking)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language responses with checkup guidance, service results, and booking details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Specific plans, prices, centers, and availability must come from service results; the skill must not invent them.]

## Skill Version(s):

1.0.9 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

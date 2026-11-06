## Description:

Helps users in mainland China plan, schedule, book, check, and cancel Amap rides, with confirmation before bookings and cancellations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lbs-amap](https://clawhub.ai/user/lbs-amap)

### License/Terms of Use:

MIT

## Use Case:

External users use the skill to arrange Amap rides in mainland China, check order status, and cancel rides. It also guides users through setup and ride preferences.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Route and timing details are sent to Amap during planning, before the user confirms a booking.

Mitigation: Explain this data sharing before planning and send only the route details needed for the requested ride.

Risk: The skill may save home or work addresses and other long-term ride preferences.

Mitigation: Tell users when preferences are saved and honor requests to review or forget them.

Risk: The Amap key is tied to the user's account and payment identity, and ride booking requires in-car recording authorization and password-free payment setup.

Mitigation: Use only the user's own key, protect the key and MCP configuration from logs or disclosure, and explain the Amap authorization requirements before booking.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lbs-amap/skills/amap-ride-hailing-skill)
- [MCP authentication and key setup](references/auth.md)
- [Ride tool contracts](references/tool-contracts.md)
- [Scheduled ride guidance](references/scheduling.md)

## Skill Output:

**Output Type(s):** [Text, API calls, Guidance, Configuration]

**Output Format:** [Natural-language ride guidance and order details, plus Amap ride-service requests.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save address aliases, a default city, and vehicle preferences in local files.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

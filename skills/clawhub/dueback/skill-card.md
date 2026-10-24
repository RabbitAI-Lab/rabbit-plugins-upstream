## Description:

Dueback: outcome-based bill negotiation. Detect negotiable bills, fees, and purchases; Dueback's backend negotiates and verifies savings against bank data. Free to try — pay only on verified savings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunrossmai-rgb](https://clawhub.ai/user/dunrossmai-rgb)

### License/Terms of Use:

MIT

## Use Case:

External users use this agent skill to identify negotiable bills, fees, subscriptions, or purchases, then—with their agreement—start a Dueback case and track bank-verified savings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Dueback involves bank permissions and may incur outcome-based fees when savings are verified.

Mitigation: Review Dueback’s privacy terms, requested bank permissions, fees, and cancellation options before connecting.

Risk: The README and SKILL.md differ on alpha eligibility and whether a redemption code is needed.

Mitigation: Confirm the current alpha code and eligibility with Dueback before describing a case as free.

Risk: Publisher identity and live service behavior were not independently verified.

Mitigation: Independently confirm the service identity and connection destination before sharing financial or bank information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunrossmai-rgb/skills/dueback)
- [Publisher profile](https://clawhub.ai/user/dunrossmai-rgb)
- [Dueback connection guide](https://dueback.co/connect.html)
- [Dueback MCP server](https://api.dueback.co/mcp/)
- [Dueback API](https://api.dueback.co)
- [Dueback service](https://dueback.co)

## Skill Output:

**Output Type(s):** [Guidance, Text, API Calls, Configuration instructions]

**Output Format:** [User-facing conversational guidance with structured API request payloads and connection instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user agreement before opening cases and explicit confirmation before publishing reviews.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

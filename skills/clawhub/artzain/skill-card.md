## Description:

Put this OpenClaw instance under ArtzAIn governance — every host tool call is checked against your own CogNEXUS Decision API before it runs, failing closed on deny, review, or any engine error.

This skill is ready for commercial/non-commercial use.

## Publisher:

[quantumskipper](https://clawhub.ai/user/quantumskipper)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw administrators and developers use this skill to install and configure the ArtzAIn integration, which sends host tool calls to a CogNEXUS Decision API for governance decisions and audit recording.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tool names, arguments, and the agent ID are sent to the configured Decision API and recorded in its audit trail.

Mitigation: Use an endpoint and account you trust, and keep secrets out of tool arguments.

Risk: A service outage or configuration error can block host tool calls because the gate fails closed.

Mitigation: Verify the pinned package, API key, and endpoint before enabling the gate, and plan for Decision API outages.

Risk: Using another account's API key records decisions in that account's audit trail.

Mitigation: Keep the Decision API key in the Gateway configuration and confirm it belongs to the intended account.

## Reference(s):

- [ArtzAIn plugin package on npm](https://www.npmjs.com/package/@cognexuslabs/openclaw-artzain)
- [ArtzAIn Tool Gate ClawHub listing](https://clawhub.ai/quantumskipper/skills/artzain)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Governance guidance]

**Output Format:** [Markdown with inline shell commands and JSONC configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup guidance pins the external plugin to version 0.2.8.]

## Skill Version(s):

0.2.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Guides OpenClaw operators through installing a tool gate that checks host tool calls with a CogNEXUS Decision API before execution and blocks denied, pending, or failed decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[quantumskipper](https://clawhub.ai/user/quantumskipper)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw operators and developers use this listing to verify, install, and configure the pinned ArtzAIn plugin so an external policy service reviews host tool calls before they run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tool names, arguments, and agent identity are sent to the configured CogNEXUS Decision API and recorded in its audit trail.

Mitigation: Use your intended deployment URL and keep secrets out of tool arguments you do not want recorded.

Risk: Denied or pending decisions, service errors, or a misconfigured key can block tool execution.

Mitigation: Confirm the policy service and key are configured and reachable before enabling the gate.

Risk: Installing an unverified plugin package could introduce unexpected code.

Mitigation: Verify the pinned npm version, registry signature, attestation, and integrity before installing.

## Reference(s):

- [ArtzAIn Tool Gate ClawHub listing](https://clawhub.ai/quantumskipper/skills/artzain)
- [ArtzAIn npm package](https://www.npmjs.com/package/@cognexuslabs/openclaw-artzain)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and configuration example]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pins plugin version 0.2.6 and describes signature and integrity checks before installation.]

## Skill Version(s):

0.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

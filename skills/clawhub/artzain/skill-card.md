## Description:

Put this OpenClaw instance under ArtzAIn governance: every host tool call is checked against the user's own CogNEXUS Decision API before it runs, failing closed on deny, review, or engine error.

This skill is ready for commercial/non-commercial use.

## Publisher:

[quantumskipper](https://clawhub.ai/user/quantumskipper)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and operators use this skill to configure an OpenClaw instance so host tool calls are governed by their own CogNEXUS decision service. It is intended for environments that need allow, deny, review, and fail-closed policy checks before tools run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A misconfigured API key or CogNEXUS base URL can block all host tool calls because the gate fails closed.

Mitigation: Configure baseUrl to a CogNEXUS deployment you control, use the correct Decision API key, and test the gateway before relying on it for normal work.

Risk: Tool-call metadata may enter the CogNEXUS audit trail.

Mitigation: Install only when CogNEXUS governance is intended and review audit-trail data handling for the target deployment.

Risk: Installing an unexpected package would place host tool calls under the wrong gate.

Mitigation: Verify the npm package provenance and install @cognexuslabs/openclaw-artzain from the expected package source.

## Reference(s):

- [ClawHub ArtzAIn Tool Gate listing](https://clawhub.ai/quantumskipper/skills/artzain)
- [npm package @cognexuslabs/openclaw-artzain](https://www.npmjs.com/package/@cognexuslabs/openclaw-artzain)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command and JSON5 configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance describes installation and configuration for a fail-closed tool gate connected to a user-controlled CogNEXUS deployment.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

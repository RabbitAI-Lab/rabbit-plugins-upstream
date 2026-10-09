## Description:

Guides OpenClaw operators in installing a governance plugin that checks each host tool call with a CogNEXUS Decision API and blocks calls on denial, review, or error.

This skill is ready for commercial/non-commercial use.

## Publisher:

[quantumskipper](https://clawhub.ai/user/quantumskipper)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw operators use this listing to verify and install a pinned governance plugin, configure their Decision API connection, and understand how tool calls are reviewed and blocked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Every host tool call's arguments may be sent to the Decision API and recorded in its audit trail.

Mitigation: Keep secrets out of tool arguments and point the API at a trusted deployment.

Risk: A missing or invalid key or an unavailable decision service can block host tools.

Mitigation: Configure and test the Decision API connection before relying on the gate for normal operations.

Risk: Installing an unverified or unpinned package could change the code that governs tool calls.

Mitigation: Install only the pinned version after verifying its registry signature and attestation.

## Reference(s):

- [ClawHub ArtzAIn Tool Gate listing](https://clawhub.ai/quantumskipper/skills/artzain)
- [CogNEXUS OpenClaw plugin package](https://www.npmjs.com/package/@cognexuslabs/openclaw-artzain)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and a configuration example]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pins plugin version 0.2.7; provides installation, verification, and setup guidance rather than a plugin bundle.]

## Skill Version(s):

0.2.7 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

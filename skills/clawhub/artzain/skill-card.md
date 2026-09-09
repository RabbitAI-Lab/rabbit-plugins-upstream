## Description:

Put this OpenClaw instance under ArtzAIn governance by checking host tool calls against the user's CogNEXUS Decision API before they run, failing closed on deny, review, or engine errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[quantumskipper](https://clawhub.ai/user/quantumskipper)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to install and configure the ArtzAIn/CogNEXUS OpenClaw governance plugin so host tool calls are checked by their own decision service before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill points users to an external npm package rather than bundling plugin code.

Mitigation: Verify the npm package provenance and linked source before installing.

Risk: A missing, invalid, or unavailable CogNEXUS Decision API configuration blocks host tool calls because the gate fails closed.

Mitigation: Use a Decision API key scoped for this gateway and validate service availability before relying on the gate in operations.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/quantumskipper/skills/artzain)
- [npm package: @cognexuslabs/openclaw-artzain](https://www.npmjs.com/package/@cognexuslabs/openclaw-artzain)
- [CogNEXUS tools source repository](https://github.com/CogNEXUSlabs/cognexus-tools)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON-style configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces installation and gateway configuration guidance; it does not bundle executable plugin code.]

## Skill Version(s):

0.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

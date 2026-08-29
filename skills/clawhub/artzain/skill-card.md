## Description:

Put this OpenClaw instance under ArtzAIn governance: every host tool call is checked against your own CogNEXUS Decision API before it runs, failing closed on deny, review, or engine error.

This skill is ready for commercial/non-commercial use.

## Publisher:

[quantumskipper](https://clawhub.ai/user/quantumskipper)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to place OpenClaw host tool execution behind an ArtzAIn/CogNEXUS Decision API gate. It helps enforce allow, deny, review, and fail-closed decisions before tools run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tool names, arguments, request IDs, and agent identity may be sent to the configured CogNEXUS Decision API and stored in its audit or registry systems.

Mitigation: Review before installing, configure baseUrl explicitly to the intended CogNEXUS deployment, and confirm the organization is comfortable with the disclosed tool-call data.

Risk: The security verdict is suspicious because the listing under-discloses that the referenced plugin can send every tool-call payload to a hosted CogNEXUS endpoint by default.

Mitigation: Treat evidence.security as authoritative during review and verify the referenced package behavior and endpoint configuration before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/quantumskipper/skills/artzain)
- [@cognexuslabs/openclaw-artzain npm package](https://www.npmjs.com/package/@cognexuslabs/openclaw-artzain)
- [CogNEXUS tools repository](https://github.com/CogNEXUSlabs/cognexus-tools)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with shell command and JSON5 configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [References an external npm package and a required CogNEXUS Decision API key.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

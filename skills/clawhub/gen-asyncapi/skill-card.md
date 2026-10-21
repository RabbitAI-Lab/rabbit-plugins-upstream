## Description:

Helps developers generate typed Go or TypeScript models, validators, message dispatch, and WebSocket clients from AsyncAPI 3 specifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to configure and run an AsyncAPI 3 code generator for Go services or TypeScript clients, producing typed messages, validation, dispatch, and a WebSocket client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an unpinned upstream Go module can introduce unexpected changes.

Mitigation: Trust the upstream module before installation and pin a reviewed version instead of using @latest.

Risk: Generated code may need review before use or commit.

Mitigation: Review the generated Go or TypeScript source before committing it.

Risk: Credentials included in the specification or generator configuration may be exposed.

Mitigation: Keep secrets out of AsyncAPI specifications and generator configuration.

## Reference(s):

- [Setup and configuration reference](artifact/references/setup.md)
- [Gen Asyncapi on ClawHub](https://clawhub.ai/psyb0t/skills/gen-asyncapi)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Go, TypeScript, YAML, and shell examples; generated Go or TypeScript source file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generator writes one output file selected by the configuration or command line.]

## Skill Version(s):

0.2.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

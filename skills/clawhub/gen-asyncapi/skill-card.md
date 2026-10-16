## Description:

Generates Go or TypeScript models, validators, message dispatch, and WebSocket clients from an AsyncAPI 3 specification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to generate typed Go or TypeScript code for message APIs described by AsyncAPI 3 specifications, including validation, dispatch, and WebSocket clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using an unpinned generator version can make builds difficult to reproduce.

Mitigation: Pin the generator version instead of using @latest.

Risk: Generated source can include errors or unintended behavior.

Mitigation: Review generated code before committing it.

Risk: Secrets placed in specifications or generator configuration may be exposed.

Mitigation: Keep tokens and other secrets out of AsyncAPI specifications and generator configuration.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/gen-asyncapi)
- [Generator homepage](https://github.com/psyb0t/gen-asyncapi)
- [Setup and configuration reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown guidance and examples; generated Go or TypeScript source file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generator writes a single configured output file; generated code should be reviewed before committing.]

## Skill Version(s):

0.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

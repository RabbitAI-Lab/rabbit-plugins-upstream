## Description:

Generates high-fidelity vector image assets with Recraft V4 Pro Vector for production-grade SVGs and detailed illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content teams use this skill to invoke the dLazy CLI for Recraft V4 Pro Vector image generation from prompts, with optional aspect-ratio controls and local saving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and any supplied local media files to the dLazy hosted API and media storage endpoints.

Mitigation: Only pass files intended for upload, review the linked dLazy CLI source or package when high assurance is required, and prefer isolated execution such as npx when appropriate.

Risk: The skill requires a dLazy API key stored in local configuration or supplied through the environment.

Mitigation: Treat the API key as a secret and rotate or revoke it if it is exposed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)

## Skill Output:

**Output Type(s):** [Shell commands, Files, API calls, Guidance]

**Output Format:** [JSON result metadata with hosted asset URLs or saved vector image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports dry-run, async generation, timeout control, aspect ratio selection, and local save paths.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Text-to-vector generation that produces SVG results for logos, icons, and scalable design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use the dLazy CLI to generate scalable visual assets such as logos and icons from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI requires a dLazy API key, which may be stored in the user's local CLI configuration.

Mitigation: Keep the key private, use a trusted environment, and rotate or revoke it from the dLazy dashboard if needed.

Risk: Prompts and supplied local media are sent to dLazy hosted services, and generated assets are hosted there.

Mitigation: Submit only prompts and files appropriate to share with the service, and review its terms before use.

Risk: The security review was partial because several references could not be resolved.

Mitigation: Review the CLI repository and linked service documentation before installation or use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [CLI repository link declared in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [JSON response containing generated image asset URLs; optionally saved as an image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-based generation with an optional aspect ratio; asynchronous jobs can return a generation ID.]

## Skill Version(s):

1.3.40 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

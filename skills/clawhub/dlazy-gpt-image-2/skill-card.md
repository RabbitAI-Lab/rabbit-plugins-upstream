## Description:

Generates images from text prompts and edits or combines images using reference inputs through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts or edit images with up to five reference inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running the pinned third-party CLI executes external package code.

Mitigation: Review the linked CLI source and pinned package before installation if supply-chain provenance matters.

Risk: Prompts and selected local input files are sent to dLazy's cloud service.

Mitigation: Only submit prompts and reference files that are appropriate to share with dLazy.

Risk: CLI login can save a dLazy API key in local configuration.

Mitigation: Use the per-invocation DLAZY_API_KEY option instead if a saved key is not desired.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI source (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [JSON result with image URLs; optional downloaded JPEG, PNG, or WebP files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID for later polling.]

## Skill Version(s):

1.3.24 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Automatically selects a suitable dlazy CLI image model for image generation from a prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can use the skill to select and run dlazy image-generation or image-processing commands from a prompt and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports image generation alongside video and speech features not disclosed in the stated purpose, and scan coverage is incomplete because some references could not be resolved.

Mitigation: Review the described capabilities and pinned CLI installation before use; inspect the commands you intend to run and confirm any unresolved references.

Risk: Prompts and local media files passed to the CLI are sent to dLazy's hosted API or media storage.

Mitigation: Avoid sending sensitive prompts or files unless approved for that service, and use only media you are authorized to upload.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Image URLs, SVG graphics]

**Output Format:** [JSON result envelopes with generated image or SVG URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media format and resolution depend on the selected model; generated media is hosted by dLazy.]

## Skill Version(s):

1.3.40 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

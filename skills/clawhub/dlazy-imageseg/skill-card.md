## Description:

Image matting tool: separates foreground from background and returns a transparent-background URL, suitable for product image processing, character cutout, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and image editors can submit an image for foreground/background separation and use the returned transparent image URL in product imagery, character cutouts, or compositing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial and flags CLI login and API-key setup as outside the stated image-separation purpose.

Mitigation: Review the CLI and its authentication flow before installation, and grant credentials only after confirming the account and service are appropriate for this use.

Risk: The skill sends prompts and supplied image files to dLazy-hosted services for processing and hosts returned image URLs.

Mitigation: Submit only images and prompts that are approved for processing by the third-party service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [CLI source declared by the skill](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, JSON, URLs]

**Output Format:** [JSON result metadata containing a transparent image URL; an image file can optionally be saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill returns a hosted result URL and can save the image to a requested local path.]

## Skill Version(s):

1.3.43 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

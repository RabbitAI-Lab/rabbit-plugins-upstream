## Description:

Turns a product image into a short, motion-guided product video for an online listing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to turn an existing product image into a 3–5 second listing video with controlled camera and material motion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and brand reference assets are sent to the selected cloud provider.

Mitigation: Use an approved provider and avoid confidential or rights-sensitive assets unless their upload is authorized.

Risk: Generation may incur charges or produce footage unsuitable for a listing.

Mitigation: Preview with dry-run, specify the intended provider and model, test one short clip, and review the video against platform requirements before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video backend setup](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with generation commands and prompt guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing the commands can create a local MP4; dry-run previews the request without generation.]

## Skill Version(s):

1.0.20 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

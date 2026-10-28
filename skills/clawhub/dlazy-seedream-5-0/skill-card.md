## Description:

Generates 2K, 3K, or 4K images from text prompts and reference images for key visuals, posters, and large-format print.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creative users and developers use this skill to create high-resolution images from prompts and optional reference images for key visuals, posters, and print work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to dLazy, and local image files may be uploaded to its media storage.

Mitigation: Only submit prompts and images you intend to share with the service.

Risk: Installing the third-party npm CLI runs its code in the user's environment.

Mitigation: Review the CLI package before installation and use the version-pinned install command documented by the skill.

Risk: The dLazy organization API key is saved in local CLI configuration when logging in or setting a key.

Mitigation: Protect the local configuration and rotate or revoke the key when it is no longer needed.

Risk: Image generation uses paid service credits.

Mitigation: Check the expected cost and available credits before generating; use the documented dry-run option to inspect a cost estimate.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI project information](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image assets with JSON result metadata and hosted image URLs.]

**Output Parameters:** [Text prompt, optional reference images (up to 10), resolution (2K, 3K, or 4K), and aspect ratio.]

**Other Properties Related to Output:** [Image results are hosted on files.dlazy.com; asynchronous requests can return a task identifier before results are ready.]

## Skill Version(s):

1.2.31 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

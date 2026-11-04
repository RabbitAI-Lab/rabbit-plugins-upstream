## Description:

Generates and edits images with GPT Image 2.5 Sunburst through dLazy, with support for reference images, wide aspect ratios, and high image quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and design teams can use the skill to generate or edit images from prompts and reference images, including compositions where fine detail, in-image text, or aspect ratio matters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference files are sent to dLazy, and local files supplied as inputs are uploaded to its media storage.

Mitigation: Check that prompts and reference files are appropriate to share with the service; avoid submitting sensitive material unless its use is approved.

Risk: The workflow uses paid dLazy credits and stores an API key in local CLI configuration when logged in or when a key is saved.

Mitigation: Protect the local configuration and key, review the pinned CLI before installing it, and rotate or revoke the key if needed.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image files with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports reference images and configurable aspect ratios and quality; asynchronous requests can return a task identifier for later polling.]

## Skill Version(s):

1.2.26 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

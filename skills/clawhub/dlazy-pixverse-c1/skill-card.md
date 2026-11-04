## Description:

PixVerse C1 video generation for text prompts, reference images, and first and last frame inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can create short PixVerse C1 videos from a text prompt, optional reference images, or first and last frames, with controls for duration, resolution, aspect ratio, and optional generated audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill requires trusting the external dLazy CLI package.

Mitigation: Review the pinned @dlazy/cli version and its project materials before installation.

Risk: Prompts and selected media are sent to dLazy, and local media files are uploaded for processing.

Mitigation: Submit only prompts and media intended for processing by the hosted service.

Risk: Login saves an API key in the local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key through the account console if it is exposed.

Risk: Video generation can consume account credits.

Mitigation: Use the documented --dry-run option to preview the request and estimated cost before generation.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Video files, Audio files, JSON status metadata]

**Output Format:** [Hosted media URLs or saved media files, with JSON generation or task status]

**Output Parameters:** [Prompt; optional reference images or first and last frames; generation mode; resolution; aspect ratio; duration; optional audio]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID for later polling. Results can be saved to local files.]

## Skill Version(s):

1.2.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

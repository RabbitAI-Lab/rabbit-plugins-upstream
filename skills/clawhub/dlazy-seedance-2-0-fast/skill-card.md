## Description:

Fast version of ByteDance's Seedance 2.0. Generates videos faster with support for multi-modal references, first/last frame, and text-to-video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating short videos use this skill to generate clips from text prompts, multimodal references, or first and last frame images through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy for cloud processing, and local media files may be uploaded to its media storage.

Mitigation: Only provide prompts and media you are comfortable uploading to dLazy.

Risk: Video generation may incur account charges.

Mitigation: Review the generation cost estimate and account credits before running a generation.

Risk: Installing the skill's CLI dependency executes third-party code.

Mitigation: Review the CLI package before installation and use the documented pinned version; device login or an environment-provided key is preferred, and stored keys should be revoked when no longer needed.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Generated video hosted at a URL, with a JSON result containing output details or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation can be asynchronous; a task identifier may be returned before the video is ready.]

## Skill Version(s):

1.3.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
